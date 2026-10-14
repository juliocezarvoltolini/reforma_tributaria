#!/usr/bin/env bash
# Verificação única da base. Fonte de verdade das checagens.
#
# Chamado pelo hook de pre-commit (.githooks/pre-commit) e pela CI
# (.github/workflows/validar.yml), para que os dois nunca divirjam.
#
# Uso:
#   pipeline/verificar.sh
#   pipeline/verificar.sh --corrigir-indices   # regrava indices/ e segue

set -uo pipefail
cd "$(git rev-parse --show-toplevel)"

CORRIGIR=0
[[ "${1:-}" == "--corrigir-indices" ]] && CORRIGIR=1

falhas=0
titulo() { printf '\n\033[1m%s\033[0m\n' "$1"; }
ok()     { printf '  \033[32mok\033[0m    %s\n' "$1"; }
falha()  { printf '  \033[31mFALHA\033[0m %s\n' "$1"; falhas=$((falhas + 1)); }

# ------------------------------------------------------- interpretador Python
# No Windows não existe `python3`: o nome é `python` ou o launcher `py`. E o
# `python3` que o Windows oferece costuma ser o atalho da Microsoft Store, que
# não executa nada — por isso cada candidato é testado de fato, não apenas
# localizado no PATH.
PY=""
for candidato in python3 python py; do
  if command -v "$candidato" >/dev/null 2>&1 &&
     "$candidato" -c "import sys; sys.exit(0 if sys.version_info[:2] >= (3, 9) else 1)" \
       >/dev/null 2>&1; then
    PY="$candidato"
    break
  fi
done

if [[ -z "$PY" ]]; then
  printf '\033[31mPython 3.9+ não encontrado.\033[0m Tentei: python3, python, py.\n'
  exit 2
fi

if ! "$PY" -c "import yaml" >/dev/null 2>&1; then
  printf '\033[31mpyyaml ausente.\033[0m Instale com: %s -m pip install pyyaml requests\n' "$PY"
  exit 2
fi

# ---------------------------------------------------------------- 1. testes
titulo "Testes do pipeline"
if saida=$("$PY" tests/test_pipeline.py 2>&1); then
  ok "parser, URNs, remissões, modelo temporal"
else
  falha "testes do pipeline"
  echo "$saida" | grep -E "FALHA" | sed 's/^/        /'
fi

# ---------------------------------------------------------------- 2. premissas
titulo "Premissas (PREMISSAS.md §7)"
if saida=$("$PY" pipeline/validar.py 2>&1); then
  ok "procedência, remissões, vigência, camadas"
  echo "$saida" | grep -E "^AVISO" | sed 's/^/        /' || true
else
  falha "validação da base"
  echo "$saida" | grep -E "^ERRO" | sed 's/^/        /'
fi

# ---------------------------------------------------------------- 3. índices
titulo "Índices derivados em dia (PREMISSAS.md §6.3)"
"$PY" pipeline/indexar.py >/dev/null 2>&1
# O índice REGENERADO tem de coincidir com o que está no índice do Git (staged).
# Exigir também que o staged coincida com o HEAD (`git diff --cached`) reprovaria
# todo commit que muda os índices de forma legítima, e a correção sugerida abaixo
# (`git add indices/`) nunca passaria. Arquivo novo ainda não rastreado também conta.
novos=$(git ls-files --others --exclude-standard -- indices/)
if git diff --quiet -- indices/ && [[ -z "$novos" ]]; then
  ok "indices/ é função pura de normas/"
elif [[ $CORRIGIR -eq 1 ]]; then
  git add indices/
  ok "indices/ regenerado e adicionado ao commit"
else
  falha "indices/ desatualizado ou editado à mão"
  git diff --stat -- indices/ | sed 's/^/        /'
  printf '        corrija com: %s pipeline/indexar.py && git add indices/\n' "$PY"
fi

# ---------------------------------------------------------------- 4. vazamento
titulo "Conteúdo sintético fora da base"
if grep -rl "FICT\|SINTETICO\|SINTÉTICO" normas/ fontes/ 2>/dev/null | grep -q .; then
  falha "fixture de teste vazou para normas/ ou fontes/ (PREMISSAS.md §1.3)"
  grep -rl "FICT\|SINTETICO\|SINTÉTICO" normas/ fontes/ 2>/dev/null | sed 's/^/        /'
else
  ok "nenhum texto de teste na camada 1"
fi

# ---------------------------------------------------------------- resultado
if [[ $falhas -gt 0 ]]; then
  printf '\n\033[31m%d verificação(ões) falharam.\033[0m\n' "$falhas"
  exit 1
fi
printf '\n\033[32mTudo verificado.\033[0m (%s)\n' "$("$PY" --version 2>&1)"
