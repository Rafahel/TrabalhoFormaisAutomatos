# TrabalhoFormaisAutomatos

O programa foi feito para eliminar estados mortos e inalcansáveis de um AFD.

  Para utilizar o programa basta compilar e digitar o nome de um dos exemplos(aut1 ao aut6). O programa vai eliminar todos os estados
  mortos, inalcaçaveis e improdutivos (se for improdutivo mas final o estado não sera removido). Para criar outros casos de teste é só seguir as regras abaixo.


REGRAS de entrada:

  PRIMEIRA LINHA: Descrição do teste
  SEGUNDA LINHA: Lista dos simbolos que podem ser lidos (cabeçalho)
  TERCEIRA LINHA: pode ser iniciado o automato.

  A lista de simbolos lidos deve sempre iniciar com um - seguido de espaço e ai devem ser colocados os simbolos

  Estados INICIAIS devem conter -> e se forem iniciais e finais devem conter *-> e depois do nome do estado deve conter "="
  exemplo: *->A= G B

  Estados FINAIS devem conter * antes do nome do estado.
  exemplo: *B G H

  Demais estados: Devem ser escritos como no exemplo abaixo onde B é o nome do estado F e E são os estados que ele chama ao ler os simbolos.
  Exemplo : B F E

  Exemplo final de um arquivo de automato válido começando da linha 0 do arquivo:

        Este automato... <- Descrição do automato
        - a b <- cabeçalho de simbolos lidos.
        *->A= G B <- estado inicial (primeiro estado).
        B F E
        C C G
        *D A H <- estado final.
        E E A
        F B C
        *G G F <- estado final.
        H H D <- Fim do automato sem nova linha.

Qualquer dúvida é só olhar os arquivos de exemplo (aut1 a aut6) e modifica-los conforme necessário.

Qualquer problema enviar email para rafahelmello@gmail.com

Grupo Fernando, Rafahel e Tayrone.
