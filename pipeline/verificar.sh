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

# ---------------------------------------------------------------- dependências
if ! python3 -c "import yaml" 2>/dev/null; then
  printf '\033[31mpyyaml ausente.\033[0m Instale com: pip install pyyaml requests\n'
  exit 2
fi

# ---------------------------------------------------------------- 1. testes
titulo "Testes do pipeline"
if saida=$(python3 tests/test_pipeline.py 2>&1); then
  ok "parser, URNs, remissões, modelo temporal"
else
  falha "testes do pipeline"
  echo "$saida" | grep -E "FALHA" | sed 's/^/        /'
fi

# ---------------------------------------------------------------- 2. premissas
titulo "Premissas (PREMISSAS.md §7)"
if saida=$(python3 pipeline/validar.py 2>&1); then
  ok "procedência, remissões, vigência, camadas"
  echo "$saida" | grep -E "^AVISO" | sed 's/^/        /' || true
else
  falha "validação da base"
  echo "$saida" | grep -E "^ERRO" | sed 's/^/        /'
fi

# ---------------------------------------------------------------- 3. índices
titulo "Índices derivados em dia (PREMISSAS.md §6.3)"
python3 pipeline/indexar.py >/dev/null 2>&1
if git diff --quiet -- indices/ && git diff --cached --quiet -- indices/; then
  ok "indices/ é função pura de normas/"
elif [[ $CORRIGIR -eq 1 ]]; then
  git add indices/
  ok "indices/ regenerado e adicionado ao commit"
else
  falha "indices/ desatualizado ou editado à mão"
  git diff --stat -- indices/ | sed 's/^/        /'
  printf '        corrija com: python3 pipeline/indexar.py && git add indices/\n'
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
printf '\n\033[32mTudo verificado.\033[0m\n'
