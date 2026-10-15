# /normas/ — dispositivos fatiados (camadas 1 e 2)

Um arquivo por artigo: `<slug-da-norma>/art-NNNN.md`.

- Gerado por `pipeline/fatiar.py` a partir de `/fontes/`. **Não escrever à mão.**
- Corpo = texto verbatim. Sem resumo, sem paráfrase, sem comentário.
- Para corrigir texto: reingira a fonte. Nunca edite o arquivo.
- Análise e opinião vão em `/interpretacoes/`, nunca aqui.

## Como ler o corpo

**`~~texto~~` é texto RISCADO no original.** O portal do Planalto mantém no
compilado a redação superada ou revogada, marcada com tachado. O corpo preserva
esse texto, entre `~~ ~~`, para que nada do que o portal mostra se perca e para
que a anotação `(Revogado pela ...)` continue colada ao trecho que ela revoga.

- Texto entre `~~ ~~` **não está em vigor** nesta consolidação. Não o cite como
  se estivesse.
- Quando um artigo tem redação anterior, ela vem **antes** da redação vigente,
  no mesmo arquivo (`Art. 28` riscado, depois `Art. 28` com
  `(Redação dada pela ...)`).
- `remete_a`, `subdivisoes`, `conceitos_definidos`, `anotacoes_oficiais` e
  `remete_a_externo` são extraídos **só do texto que não está riscado**.
- A anotação `(Revogado ...)` isolada no corpo refere-se ao dispositivo riscado
  imediatamente antes dela, não ao artigo inteiro.

O texto de **outra norma** que este artigo altera (entre aspas no original) fica
no corpo do artigo que promove a alteração e está listado em
`dispositivos_citados`. Não é dispositivo desta norma.

**Não está aqui:** assinatura, rodapé e anexos que seguem o último artigo. Eles
permanecem em `/fontes/` (o `fatiar.py --relatorio` informa quantas linhas e
quantos anexos ficaram de fora).
