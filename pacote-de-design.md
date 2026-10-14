# Pacote de design: Michely Modas

Documento único do projeto. Escrito antes de gerar qualquer imagem, e é a entrada da construção do site.

**Idioma:** este documento está em português, porque é para o dono da loja. **Toda a cópia do site está em espanhol**, verbatim, porque quem lê mora na Bolívia. Os prompts de geração ficam em inglês. Essa separação é proposital.

**Regra:** toda linha de cópia marcada como verbatim entra no site exatamente como está escrita aqui. A construção liga os fios, não reescreve o texto.

---

## 0. Ficha do negócio

| | |
|---|---|
| Nome | Michely Modas |
| Cidade | Guayaramerín, Beni, Bolívia |
| Endereço | Av. Federico Román, entre Av. 25 de Mayo y C. Sucre |
| Horário | Segunda a sábado, 8:30 às 19:30. Domingo e feriado, 9:00 às 13:00 |
| Produto | Roupa importada do Brasil: feminino adulto, masculino, jeans e básico |
| Público | Metade boliviano de Guayaramerín, metade brasileiro de Guajará-Mirim |
| Idioma do site | Espanhol, com **voseo** (guardá, preguntá, tenés, entrás), como se fala no Beni |
| WhatsApp | `[CONFIRMAR: número com código do país]` |
| Instagram | `[CONFIRMAR: existe? qual?]` |
| Logo | Não existe. Será desenhado neste projeto |

### Pendências que só o dono responde

1. Número do WhatsApp com código do país. Sem ele o botão principal não existe.
2. ~~Tratamento~~ **decidido: vos.**
3. Política de troca: se a peça não serve, o que acontece? Prazo? Precisa de etiqueta?
4. Formas de pagamento aceitas: dinheiro, QR, Tigo Money, cartão?
5. Tem dia fixo de chegada de mercadoria? Se tiver, vira o motor da página.
6. Faz entrega ou envio? Para onde?
7. Fotos das peças.

Nada disso é inventado no site. Enquanto não chegar, fica marcado `[CONFIRMAR: ...]` e visível.

---

## 1. A premissa da marca

**Acaba de cruzar el río.**

Toda peça da Michely Modas atravessou o Mamoré, vinda do Brasil, e chegou na Federico Román. Isso é verdade literal, é exclusivo dessa loja e nenhuma concorrente conta. Resolve de uma vez as duas coisas que a loja quer dizer, que a peça é nova e que ela é brasileira, e traz de brinde uma unidade de tempo que vende sozinha: o que cruzou esta semana some na semana que vem.

Toda seção serve essa ideia. A que não servir, sai da página.

---

## 2. A paleta, como tokens CSS

Direção tirada do mundo da filmagem escolhida: o corredor de araras, a sombra entre as roupas penduradas, o azul do jeans e a luz quente que cai na peça do fim. Os valores exatos são finalizados depois que a filmagem for aprovada, amostrando o quadro final.

Decisões firmes: o fundo nunca é preto puro, o acento aparece em dose rara e nenhum dos visuais batidos de site feito por IA entra aqui. Fundo índigo profundo com acento coral não é o caminho padrão, e é proposital.

```css
:root{
  --canvas:#141A24;        /* a sombra entre as roupas penduradas, índigo profundo, nunca preto */
  --panel:#1C2432;         /* cartões e superfícies elevadas */
  --accent:#FF4D6D;        /* coral quente: só o botão principal e o foco */
  --accent-hover:#FF6B84;
  --accent-muted:#5A2A38;  /* bordas, brilho fraco, partículas */
  --text-primary:#F2EFE9;  /* branco morno, da luz na peça */
  --text-secondary:#A9B2C2;
  --denim:#3E5C86;         /* o azul que passa no meio da descida */
}
```

---

## 3. O trio tipográfico

| Papel | Fonte | Pesos |
|---|---|---|
| Display | Bricolage Grotesque | 700, 800 |
| Corpo | Hanken Grotesk | 400, 500, 600 |
| Mono | DM Mono | 400, 500 |

Nenhuma delas é Inter nem Roboto. O mono carrega preço, tamanho e data de chegada, que é onde ele faz sentido.

**Acentos:** o espanhol precisa de ñ, á, é, í, ó, ú, ü, ¿ e ¡. As três famílias cobrem Latin e Latin Extended, o que inclui tudo isso. **Verificar com renderização real na construção**, escrevendo "¿Qué talla buscás? Mañana llega más" e conferindo caractere por caractere. Fonte que quebra em ñ está fora, por mais bonita que seja.

---

## 4. O mapa de faixas do vídeo

Vídeo: uma tomada de 6 segundos, descida entre as araras. Altura da região fixa: **400vh**. Os intervalos abaixo são ponto de partida e são validados depois pelo teste de rolagem rápida.

| Faixa | Intervalo | Momento da filmagem | Cópia (verbatim, espanhol) | Entrada |
|---|---|---|---|---|
| 1 | 0.00 a 0.16 | a descida começa, tecido escuro dos dois lados | **"Cada semana entra ropa nueva."** | Deriva para baixo, palavra por palavra, acompanhando a queda da câmera |
| 2 | 0.22 a 0.42 | o azul do jeans passa e o tecido roça a lente | **"Cruzó el río desde Brasil."** | Tecelagem: letras chegando alternadas de cima e de baixo, como fios se cruzando |
| 3 | 0.48 a 0.66 | as cores estampadas passam, a descida acelera | **"Pocas piezas de cada talla."** | Soco na palavra, com "Pocas" estourando e assentando |
| 4 | 0.74 a 1.00 | a câmera para na peça única sob a luz quente | Título **"Michely Modas"**, linha **"Ropa de Brasil, en la Federico Román."**, botão **"Guardar el número"** | Subida palavra a palavra, depois a linha, depois o botão: três chegadas numa faixa só |

A faixa 1 abre já montada, com rampa de carregamento única na abertura. A faixa 4 não tem saída, porque é onde a página assenta.

**A pista da ação fica livre.** Na descida entre araras a ação vive no centro vertical do quadro. As faixas 1 a 3 ficam no terço inferior, largas, com respiro nas laterais. A faixa 4 sobe para o centro-alto, porque o quadro final tem a peça embaixo.

**Espanhol é mais comprido que inglês.** Cada faixa foi escrita curta de propósito. A mais longa, "Cruzó el río desde Brasil", tem 25 caracteres e cabe em uma linha a partir de 360px de largura.

---

## 5. O bloco do herói estático

Para celular e para quem pede menos movimento. Fica sobre o quadro final da filmagem, sem jornada atrás.

- Título: **"Ropa de Brasil, recién llegada."**
- Linha: **"Cada semana cruza el río algo nuevo. Pocas piezas de cada talla."**
- Botão: **"Guardar el número"**

---

## 6. O que vem depois da parada

Tudo funila para uma única ação: a pessoa salvar o número e entrar na lista de novidades.

**Detalhe que decide o desenho do botão:** a lista de transmissão do WhatsApp só entrega mensagem para quem tem o número salvo na agenda, e vai até 256 contatos por lista. Então o botão não abre só uma conversa. Ele pede para salvar o contato, e a mensagem já vai escrita pedindo a entrada na lista. Sem isso, a lista não entrega.

### 6.1 Nav

`Lo nuevo` · `La travesía` · `Tallas` · `Dónde estamos` · botão `Guardar el número`

### 6.2 Seção "Lo que cruzó esta semana"

Vitrine com as fotos reais das peças. Cada peça leva a etiqueta de chegada, que é o elemento assinatura (seção 7).

- Chapéu: **"RECIÉN LLEGADO"**
- Título: **"Lo que cruzó esta semana"**
- Linha: **"Estas piezas están en la tienda ahora. Cuando se acaban, se acaban."**
- Em cada cartão: nome da peça, tamanhos disponíveis em mono, etiqueta com a semana de chegada
- Botão de cada cartão: **"Preguntar por esta"** (abre o WhatsApp com a peça já citada na mensagem)

### 6.3 Seção "La travesía"

A história física, que é o coração da premissa. Três passos, os três com imagem, porque passo sem imagem lê como buraco.

- Título: **"De Brasil a la Federico Román"**
- Passo 1, **"Se elige allá"** — "La ropa se compra en Brasil, pieza por pieza. No viene en lote cerrado."
- Passo 2, **"Cruza el Mamoré"** — "Llega en bote, como llega todo acá. Son veinte minutos de río."
- Passo 3, **"Entra a la tienda"** — "Se cuelga el mismo día. Por eso lo nuevo se nota apenas entrás."
- Linha de fecho: **"Esa es toda la cadena. Sin intermediarios y sin vueltas."**

A linha desenhada que liga os três passos é o traçado do rio, em SVG, desenhando-se conforme a rolagem.

### 6.4 Seção "Por qué ropa de Brasil"

Responde o argumento de qualidade, que a pesquisa mostrou ser o motivo real de preferência.

- Título: **"Por qué ropa brasileña"**
- Corpo: **"Tela que aguanta el lavado, corte que cae bien y modelos que acá no se consiguen. No es que sea de afuera: es que dura más puesta."**

### 6.5 Seção "Tu talla" (responde a objeção número 1 em roupa)

- Título: **"Tu talla, antes de venir"**
- Corpo: **"Te pasamos la medida real de la pieza por WhatsApp: busto, cintura y largo en centímetros. Así no venís a probarte algo que no te va a entrar."**
- Nota: **"Las tallas brasileñas corren distinto. Preguntá siempre."**

### 6.6 O momento interativo

Um só no site, feito, não decorativo. A pessoa **pressiona e segura** a etiqueta de chegada. Enquanto segura, o carimbo da semana vai aparecendo na etiqueta. Quando completa, as peças da vitrine acendem em sequência.

- Instrução: **"Mantené apretado el sello"**
- Estado completo: **"Listo. Esto entró esta semana."**

Soltar antes volta o progresso suave, nunca em corte seco. Quem pede menos movimento recebe o estado final pronto, sem precisar segurar.

### 6.7 Perguntas frequentes

Escritas em cima das três reclamações que a pesquisa achou em compra de roupa: não era igual à foto, o tamanho não serviu, não me responderam.

| Pergunta | Resposta (verbatim) |
|---|---|
| **"¿La ropa es igual a la foto?"** | "Las fotos son de las piezas que están colgadas en la tienda, sacadas acá. Si una se acaba, te avisamos antes de que vengas." |
| **"¿Y si no me queda la talla?"** | `[CONFIRMAR: política de troca do dono]` |
| **"¿En cuánto responden?"** | `[CONFIRMAR: compromisso real de tempo de resposta]` |
| **"¿De dónde viene la ropa?"** | "De Brasil. Cruza el Mamoré en bote y se cuelga el mismo día." |
| **"¿Qué formas de pago aceptan?"** | `[CONFIRMAR: dinheiro, QR, Tigo Money, cartão]` |
| **"¿Hacen envíos?"** | `[CONFIRMAR]` |

### 6.8 Chamada final

- Título: **"Enterate antes que el resto"**
- Corpo: **"Guardá el número de Michely Modas y te mandamos las fotos de lo que llega, apenas llega. Sin spam y sin grupos: un mensaje por semana."**
- Botão: **"Guardar el número y entrar a la lista"**
- Letra miúda: **"Solo funciona si tenés el número guardado en tus contactos. Es así en WhatsApp para todos."**
- Mensagem já escrita no link: **"Hola, ya guardé el número. Quiero entrar a la lista de lo nuevo."**

### 6.9 Onde estamos

- Título: **"Dónde estamos"**
- Endereço: **"Av. Federico Román, entre Av. 25 de Mayo y C. Sucre. Guayaramerín, Beni."**
- Horário: **"Lunes a sábado de 8:30 a 19:30. Domingos y feriados de 9:00 a 13:00."**

### 6.10 Rodapé

Nome, endereço, horário, WhatsApp, Instagram se existir. Sem aviso de marca fictícia, porque a loja é real.

---

## 7. A camada de vetores desenhados à mão

- **O elemento assinatura: a etiqueta de chegada.** Uma etiqueta pendurada, desenhada em SVG, com um furo, um cordão e o carimbo da semana. Aparece em cada peça da vitrine e balança devagar, bem de leve. É o elemento que carrega a premissa: se ela sumisse, a página perderia o sentido inteiro. O orçamento de ousadia do site é gasto aqui, e o resto fica quieto para ela aparecer.
- **O traçado do rio:** uma linha curva em SVG ligando os três passos da travessia, que se desenha conforme a rolagem.
- **Partículas no nível do sussurro:** poeira de tecido flutuando devagar na camada de fundo fixa, que é o ambiente único da página inteira, com ciclo acima de 60 segundos.
- Tudo honra o pedido de menos movimento: estados finais mostrados, motores parados.

---

## 8. A lista de engenharia

A construção segue o padrão completo do `scrub-pipeline.md`, sem meio termo: vídeo buscado como Blob, tempo exibido suavizado com normalização por quadro, buscas de tempo com trava contra sobreposição e escape de travamento, escrita no DOM só quando muda, faixas de legenda passadas em distância de rolagem e validadas no teste de rolagem rápida, o sistema de legibilidade de quatro camadas com auditoria do pior quadro a 3.5:1, os cinco portões do herói estático idênticos em CSS e JS e mantidos vivos por ouvintes de mudança, página completa e bonita mesmo se o vídeo nunca carregar, e o padrão de qualidade inteiro.

Mais o padrão de site todo animado: entrada única por momento, um elemento vivo por seção no nível do sussurro, suavização em tudo, nada em corte seco.

---

## 9. O portão da cópia

Toda linha marcada verbatim acima entra no site como está. A página construída passa pelos portões antes de qualquer pessoa ver: zero travessões, espanhol correto do começo ao fim, `lang="es"`, charset utf-8, nenhum acento quebrado, nenhuma palavra solta em português ou inglês em botão, texto alternativo ou campo de formulário, e a varredura de palavra batida de marketing.

Os recursos de marca propositais, como a tríade dos três passos da travessia, são ofício e ficam. A varredura caça o que entrou sem convite.

---

## 10. A linha do idioma

Toda cópia acima está em **espanhol**, final e pronta para subir. Duas coisas viajam junto:

- **Comprimento.** O espanhol corre mais longo que o inglês. Cada faixa do herói foi escrita curta de propósito e a mais longa foi conferida contra a largura de 360px.
- **Acentos.** As três fontes cobrem Latin Extended. Confirmar na construção com renderização real, não no catálogo da fonte.

Os prompts de geração são a única exceção: ficam em inglês.
