<h2>Introdução e Técnicas Clássicas de Criptografia</h2>

<h3>Conceitos Básicos:</h3>
<ul>
  <li><b>Integridade:</b> Garantia de que as informações e programas só sejam alterados de forma autorizada, sem manipulações. </li>
  <li><b>Disponibilidade:</b> Assegura que os sistemas operem prontamente e seus serviços não quem indisponíveis para usuários autorizados. </li>
  <li><b>Confidencialidade:</b> Garante que as pessoas controlem ou influenciem quais informações relacionadas a elas podem ser acessadas e armazenadas.</li>
  <li><b>Privacidade:</b> Refere-se a quem pode acessar, como e para quem as informações podem ser reveladas.</li>
  <li><b>Autenticidade:</b> Garantia de que algo verificado e confiável, permitindo confiança na identificação da fonte de uma mensagem ou transmissão, e na validação dos usuários.</li>
  <li><b>Responsabilização:</b> Garantia de que as ações de uma entidade possam ser atribuídas exclusivamente a ela, fornecendo irretratabilidade, dissuasão, isolamento de falhas, detecção e prevenção de intrusões, recuperação após ação e possibilidade de ações legais.</li>
</ul>
<br>

<h3>Ameaça X Ataque</h3>
<p><b>Ameaça: </b> possível perigo a explorar uma vulnerabilidade, ou seja, uma brecha de violação de segurança.</p>
<p><b>Ataque: </b> ataque ao sistema, derivado de uma ameaça inteligente, ou seja, violar a segurança do sistema.</p>

<ul>
  <li><b>Ataques Passivos:</b> tenta descobrir ou utilizar informações do sistema, mas não afeta os seus recursos.
    <p>O objetivo é obter informações que estão sendo transmitidas e pode ser subdividido em:</p>
    <ul>
      <ol><b>Vazamento de conteúdo de mensagem:</b> acesso a informações sensíveis/confidenciais.</ol>
      <ol><b>Análise de tráfego:</b> captura de dados.</ol>
    </ul>
  </li>
  
  <li><b>Ataques Ativos:</b> tenta alterar recursos do sistema ou afetar sua operação.
    <p>Esses ataques envolvem alguma modificação do fluxo de dados ou a criação de um fluxo falso e podem ser subdivididos em:</p>
    <ul>
      <ol><b>Disfarce:</b> ocorre quando uma entidade finge ser outra. Geralmente é integrado junto com uma das outras formas de ataque ativo.</ol>
      <ol><b>Repasse:</b> captura passiva de uma unidade de dados e sua subsequente retransmissão para produzir um efeito não autorizado.</ol>
      <ol><b>Modificação de Mensagens:</b> alterar alguma parte da mensagem legítima, adiar ou reordenar mensagens para produzir um efeito não autorizado.</ol>
      <ol><b>Negação dde Serviço:</b> impede ou inibe o uso ou gerenciamento normal das instalações de comunicação, ou seja, desativar ou sobrecarregar sistemas, prejudicando seu desempenho.</ol>
    </u>  
  </li>
</ul>

<br>

<h3>Criptografia:</h3>
<p>É o processo de transformar informações legíveis em um formato ilegível e incompreensível, com objetivo de proteger as informações.</p>
<p><b>Principais Termos:</b></p>
  <ul>
    <li><b>Texto Claro:</b> consiste na mensagem original (lingua nativa).</li>
    <li><b>Texto Cifrado:</b> consiste na mensagem codificada (secreta ou ilegível).</li>
    <li><b>Encriptação:</b> converter texto claro para cifrado.</li>
    <li><b>Dencriptação:</b> restaurar o texto claro a partir do cifrado.</li>
    <li><b>Criptografia:</b> Estuda como codificar informações para protegê-las.</li>
    <li><b>Criptoanálise:</b> Técnicas para decifrar mensagens sem conhecer a codificação (leigos chamam de “quebrar o código”).</li>
    <li><b>Criptologia:</b> Consiste na criptografia e criptoanálise juntas.</li>
  </ul>
<br>

<h3>Códigos X Cifras</h3>
<p><b>Códigos: </b> fazem substituição simples de letras por símbolos, ex.: Código Morse.</p>
<p><b>Cifras: </b> usam regras para transformar uma mensagem original em uma mensagem codificada. Normalmente, estas regras recebem como entrada uma <b>chave secreta</b> que apenas os que estão se comunicando conhecem.</p>
<br>

<h3>Modelo de Cifra Simétrica:</h3>
<p> Também chamada de encriptação convencional ou de chave única, era o único tipo em uso antes do desenvolvimento da encriptação por chave pública na década de 1970.</p>
<img src="https://github.com/daneneutzling/seguranca_sistemas/assets/91130447/4e419692-61fb-40c0-b632-d01e477449ee">
<br>

<h3>Sistemas Criptográficos</h3>
<p>São caracterizados ao londo de três dimensões independentes:</p>
<ol>
  <li type="1"><b>O tipo das operações usadas para transformar texto claro em texto cifrado.</b> Todos os algoritmos de encriptação são baseados em dois princípio gerais:</li>
  <ul>
    <li><b>substituição</b>, em que cada elemento no texto claro (bit, letra, grupo de bits ou letras) é mapeado em outro elemento;</li>
    <li><b>transposição</b>, em que os elementos no texto claro são rearranjados. O requisito fundamental é que nenhuma informação seja perdida (que todas as operações sejam reversíveis).</li>
  </ul>
  
  <li type="1"><b>O número de chaves usadas.</b> Se tanto o emissor quanto o receptor utilizarem a mesma chave, o sistema é considerado de encriptação simétrica, de chave única, de chave secreta ou convencional. Se emissor e receptor usarem chaves diferentes, o sistema é considerado de encriptação assimétrica, de duas chaves ou de chave pública</li>

  <li type="1"><b>O modo em que o texto claro é processado:</b></li>
  <ul style="list-style-type: circle;">
    <li>Uma <b>cifra de bloco</b> processa a entrada de um bloco de elementos de cada vez, produzindo um de saída para cada de entrada.</li>
    <li>Uma <b>cifra em fluxo</b> processa os elementos da entrada continuamente, proporcionando a saída de um elemento de cada vez.</li>
  </ul>
</ol>






