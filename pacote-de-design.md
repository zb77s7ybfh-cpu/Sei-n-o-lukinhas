# Pacote de design: Michely Modas

Documento único do projeto. Guarda toda decisão tomada e é a fonte da verdade do site.

**Idioma:** este documento está em português, porque é para o dono da loja. **Toda a cópia do site está em espanhol, com voseo**, como se fala no Beni. Os prompts de geração ficam em inglês. A separação é proposital.

**Regra:** toda linha marcada verbatim entra no site exatamente como está. A construção liga os fios, não reescreve o texto.

---

## 0. Ficha do negócio

| | |
|---|---|
| Nome | Michely Modas |
| Cidade | Guayaramerín, Beni, Bolívia |
| Endereço | Av. Federico Román, entre Av. 25 de Mayo y C. Sucre |
| Horário | Segunda a sábado, 8:30 às 19:30. Domingo e feriado, 9:00 às 13:00 |
| Produto | Roupa importada do Brasil: jeans, vestido, conjunto, blusa e masculino |
| Marcas | Tranze Jeans e Driton Jeans, fábrica brasileira |
| Entrega | Para toda a Bolívia |
| Pagamento | QR, Pix e dinheiro em espécie |
| Troca | Até uma semana depois da compra |
| Chegada de mercadoria | Sem dia fixo |
| Idioma do site | Espanhol com voseo (guardá, preguntá, tenés, entrás) |
| WhatsApp | +591 67820413 |
| Instagram | `[CONFIRMAR: existe? qual?]` |
| Logo | Não existe. A marca é tipográfica, desenhada neste projeto |

### Pendências que só o dono responde

1. ~~Número do WhatsApp~~ **recebido: +591 67820413, ligado nos 37 botões.**
2. ~~Grade de tamanhos~~ **resolvido: P, M, G nos oito vestidos.** As cinco
   peças restantes (conjunto blanco, conjunto verde, top blanco con pedrería,
   polo negra, camisa celeste) ficam com "Consultar tallas" — decisão do dono.
3. ~~Instagram~~ **resolvido: @michely_modasbo**, ligado no rodapé e na
   seção "Dónde estamos". Conta conferida: responde como perfil existente.
4. ~~Autorização do fornecedor~~ **confirmada pelo dono** para as fotos de
   catálogo da Tranze e da Driton.
5. ~~Cartão de compartilhamento (og:)~~ **resolvido:** aponta para
   https://michelymodas.netlify.app/ e assets/og.jpg, em 1200x630.
6. **Preços: inventados por mim, a pedido do dono, na faixa 110 a 290 Bs.**
   Precisam ser conferidos peça a peça antes de virarem rotina — cliente
   paga o que está na tela.
7. **O QR do BNB vence em 2 de março de 2027.** Depois disso tem que gerar
   outro no banco e trocar `assets/qr.jpg`, ou esvaziar a constante `QR`
   no index.html — a página volta sozinha a dizer que o QR vai pelo
   WhatsApp. Conta: Velasco Ramirez Alexandre, BNB 3503690542.

---

## 1. A premissa da marca

**A loja está aqui, e se você estiver longe, a roupa vai até você.**

O centro continua sendo a loja física da Federico Román, com vitrine, arara e atendimento de gente. A entrega para toda a Bolívia entra como pilar forte do lado: o mesmo atendimento, por WhatsApp, para quem não tem como chegar na fronteira.

Isso saiu do dono, não de uma ideia de fora. Toda seção serve essa ideia. A que não servir, sai da página.

**Ideias descartadas, com o motivo, para não voltarem por engano:** a travessia do rio Mamoré, que o dono cansou; e as três alternativas que vieram depois (o giro semanal, o foco em tamanho e o foco em marca), que não convenceram. Pedaços delas sobrevivem como seções, não como premissa.

---

## 2. A paleta, como tokens CSS

Tirada do mundo da filmagem: parede rosada da loja, azul do jeans, coral das peças estampadas. Fundo claro de propósito, porque a loja é clara e porque fundo escuro com acento quente é o visual padrão de site feito por IA.

```css
:root{
  --canvas:#F7F4F4;        /* quase branco, com o véu da marca */
  --canvas-deep:#EDE4E5;   /* mauve bem claro, das faixas alternadas */
  --panel:#FFFFFF;         /* cartões */
  --ink:#3E3238;           /* mauve profundo: o texto, 11,18:1 */
  --ink-soft:#6B5A60;      /* secundário, 5,90:1 */
  --accent:#77545C;        /* mauve da marca no tom que se lê, 5,51:1 com branco */
  --accent-hover:#5F424A;
  --accent-soft:#F2E3E6;
  --brand:#845F66;         /* a cor exata do círculo do logo, medida no arquivo */
  --rose:#C38B95;          /* rose gold escuro do M: só decoração, nunca texto */
  --rose-light:#EBC1CB;    /* rose gold claro do M */
  --denim:#2E4C7E;
  --line:#E0D3D5;
}
```

**De onde vieram.** Da folha da marca entregue pelo dono. A folha escreve `#6C646E` como cor base, mas a cor medida no próprio arquivo do logo é `#845F66`, mais quente e mais rosada. Vale a medida, porque é a imagem do logo que aparece na página. O gradiente rose gold `#EBC1CB` a `#C38B95` bate com o arquivo.

**Regra do rose gold:** decoração apenas. Medido em 2,58 de contraste sobre o fundo, abaixo do piso de 3,0 até para texto grande. Vive na linha do percurso, nas bordas finas e nos brilhos, nunca em palavra.

---

## 3. O trio tipográfico

| Papel | Fonte | Pesos |
|---|---|---|
| Display | **Prata** | 400 |
| Corpo | Hanken Grotesk | 400, 500, 600, 700 |
| Mono | DM Mono | 400, 500 |

Prata é a fonte do próprio logo, nomeada na folha da marca. Tem um peso só, então os títulos usam 400 e o tamanho faz o trabalho do negrito. O nome das peças ficou na fonte de corpo, porque serif pequeno perde nitidez no cartão.

Acentos conferidos com renderização real no navegador: ñ, á, é, í, ó, ú, ü, ¿ e ¡ saem corretos nas três famílias.

**O logo.** O selo circular foi recortado da folha da marca e entra na navegação (34px) e no rodapé (46px), com recorte redondo. O ícone da aba é um desenho em vetor do selo: círculo mauve, anel claro e um M em rose gold.

---

## 4. O mapa de faixas do vídeo

Vídeo: tomada original de 5 segundos, descida entre as araras, 3,9 MB. Altura da região fixa: **540vh**, validada pelo teste de rolagem rápida.

| Faixa | Intervalo | Cópia (verbatim, espanhol) | Entrada |
|---|---|---|---|
| 1 | 0.00 a 0.17 | chapéu **"Guayaramerín"**, linha **"Ropa de Brasil, en Guayaramerín."** | Deriva para baixo, palavra por palavra |
| 2 | 0.22 a 0.42 | **"Pocas piezas de cada talla."** | Tecelagem, letras alternando de cima e de baixo |
| 3 | 0.47 a 0.65 | **"Y si estás lejos, te llega."** com "lejos" em destaque | Soco na palavra, com passagem do ponto |
| 4 | 0.72 a 1.00 | **"Michely Modas"**, linha **"Av. Federico Román, Guayaramerín. Y envíos a toda Bolivia."**, botão **"Guardar el número"** | Subida palavra a palavra, depois a linha, depois o botão |

As frases vivem no canto inferior esquerdo, sobre a massa escura de jeans. A faixa 4 sobe para o alto, porque o quadro final tem a arara embaixo.

**Medido, não estimado.** Rolagem rápida de 120px: faixas legíveis por 5, 6, 6 e 12 toques, contra um mínimo de 5. Contraste do pior quadro sob cada frase: entre 6,3 e 7,2, contra um piso de 3,5.

---

## 5. O bloco do herói estático

Para celular e para quem pede menos movimento, sobre o quadro final.

- Título: **"Ropa de Brasil, recién llegada."**
- Linha: **"Marcas brasileñas, pocas piezas de cada talla. Enviamos a toda Bolivia."**
- Botões: **"Guardar el número"** e **"Ver lo que hay"**

---

## 6. O que vem depois da parada

Tudo funila para uma ação: salvar o número e entrar na lista de novidades.

**Detalhe que decide o desenho do botão:** a lista de transmissão do WhatsApp só entrega para quem tem o número salvo, e vai até 256 contatos. O botão pede para salvar o contato, e a mensagem já vai escrita.

### 6.1 Nav
`Lo nuevo` · `Envíos` · `Tallas` · `Dónde estamos` · botão `Guardar el número`

### 6.2 "Lo que hay ahora en la tienda"
28 peças com foto real, filtro por tipo (Todo, Vestidos, Conjuntos, Blusas, Jean, Hombre) e contador. Cada cartão leva a etiqueta de chegada desenhada em SVG com a referência de fábrica, o nome, a grade de tamanhos e o botão de perguntar pela peça no WhatsApp com a peça já citada.

- Chapéu: **"RECIÉN LLEGADO"**
- Título: **"Lo que hay ahora en la tienda"**
- Linha: **"Estas piezas están colgadas ahora mismo en la Federico Román. Cuando se acaban, se acaban: de cada modelo entran pocas por talla."**

### 6.3 "Cómo te llega"
- Título: **"Estés en la vuelta o en Santa Cruz"**
- Linha: **"La tienda está en la Federico Román y ahí te atendemos en persona. Si estás lejos, te atendemos igual por WhatsApp y te lo enviamos."**
- 01 **"Nos escribís"** — "Nos decís qué prenda te gustó, o qué andás buscando."
- 02 **"Te pasamos todo"** — "Fotos de lo que hay en la tienda, la medida en centímetros y el precio."
- 03 **"Pagás y te llega"** — "QR, Pix o efectivo. Enviamos a toda Bolivia."

Uma linha em SVG liga os três passos e se desenha conforme a rolagem. Os pontos são posicionados por cálculo em cima da linha, alinhados com o centro de cada coluna.

### 6.4 "Por qué ropa brasileña"
- **"Tela que aguanta el lavado, corte que cae bien y modelos que acá no se consiguen."**
- **"No es que sea de afuera: es que dura más puesta. Trabajamos con marcas de fábrica brasileña, no con imitación."**
- Marcas em destaque: Tranze Jeans, Driton Jeans

### 6.5 "Tu talla, antes de venir"
- **"Te pasamos la medida real de la pieza por WhatsApp: cintura, cadera y largo en centímetros. Así no venís a probarte algo que no te va a entrar."**
- Aviso: **"Las tallas brasileñas corren distinto a las de acá. Preguntá siempre antes de venir."**
- Duas grades: 36 a 46 em jeans e calça, P M G em blusa e vestido

### 6.6 O momento interativo
A pessoa pressiona e segura o botão redondo. O arco vai se preenchendo. Ao completar, as peças da vitrine acendem em sequência.

- Título: **"Así se aparta una prenda"**
- Instrução: **"Mantené apretado"**
- Estado completo: **"Lista. Así de fácil: nos escribís y te la guardamos."**

Soltar antes volta o progresso suave. Quem pede menos movimento recebe o estado final pronto.

### 6.7 Perguntas frequentes (respostas do dono, verbatim)

| Pergunta | Resposta |
|---|---|
| ¿La ropa es igual a la foto? | "Las fotos son de las piezas que están colgadas en la tienda. Si una se acaba, te avisamos antes de que vengas o de que pagues." |
| ¿Y si no me queda la talla? | "Tenés una semana desde la compra para cambiarla." |
| ¿Hacen envíos? | "Sí, enviamos a toda Bolivia. Escribinos y coordinamos el envío a tu ciudad." |
| ¿Qué formas de pago aceptan? | "QR, Pix y efectivo." |
| ¿En cuánto responden por WhatsApp? | "Escribinos en horario de tienda y te respondemos rápido." |
| ¿De dónde viene la ropa? | "De Brasil. Trabajamos con marcas de fábrica como Tranze y Driton." |

### 6.8 Chamada final
- Título: **"Enterate antes que el resto"**
- Corpo: **"Guardá el número de Michely Modas y te mandamos las fotos de lo que llega, apenas llega. Sin spam y sin grupos: un mensaje por semana."**
- Botão: **"Guardar el número y entrar a la lista"**
- Letra miúda: **"Solo funciona si tenés el número guardado en tus contactos. Es así en WhatsApp para todos."**

### 6.9 "Dónde estamos"
Endereço, horário e a foto real da fachada à noite.

### 6.10 Rodapé
Nome, endereço, horário, WhatsApp. Sem aviso de marca fictícia, porque a loja é real.

---

## 7. A camada de vetores desenhados à mão

- **O elemento assinatura: a etiqueta de chegada.** Etiqueta pendurada em SVG, com furo, cordão e a referência de fábrica. Aparece nas 15 peças que têm referência e balança devagar. É o que carrega a marca.
- **A linha do percurso:** liga os três passos do envio e se desenha na rolagem.
- **Partículas no nível do sussurro** na camada de fundo fixa, ciclo acima de 60 segundos.
- Tudo honra o pedido de menos movimento.

---

## 8. O que foi medido, não estimado

| Verificação | Resultado |
|---|---|
| Rolagem rápida de 120px | 5, 6, 6 e 12 toques por faixa. Mínimo exigido: 5 |
| Contraste do pior quadro sob cada frase | 6,3 a 7,2. Piso exigido: 3,5 |
| Tempo do vídeo contra a rolagem | Erro de 0,000s em todas as posições |
| 18 idas e vindas violentas | Sem travamento, sem erro |
| Erros de console | Zero |
| Rolagem lateral de 320px a 1920px | Nenhuma |
| Celular e movimento reduzido | Vídeo nem é baixado |
| Com o vídeo bloqueado | Página continua completa sobre a foto |
| Peso total | 7 MB, contra um teto de 15 MB |

---

## 9. O portão da cópia

Toda linha verbatim entra como está. Antes de qualquer pessoa ver: zero travessões, espanhol correto, `lang="es"`, charset utf-8, nenhum acento quebrado, nenhuma palavra solta em português ou inglês, e a varredura de palavra batida de marketing.
