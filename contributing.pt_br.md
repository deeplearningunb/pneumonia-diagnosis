[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Olá, seja bem-vindo ao projeto **Pneumonia Diagnosis from Chest Ray**!

Antes de tudo, agradecemos pelo seu tempo e interesse em contribuir para este projeto.

Mais abaixo, você encontra tudo o que precisa saber sobre este projeto e como você pode fazer parte disso.

Aproveite !

# Primeiras Contribuições

É difícil. É sempre difícil fazer algo pela primeira vez. Especialmente quando se está colaborando, cometer erros não é algo agradável. Mas _open source_ (código aberto) se trata de colaboração e de trabalharmos juntos. Queremos simplificar a forma com que novos colaboradores _open source_ aprendem e contribuem pela primeira vez.

Ler artigos e ver tutoriais pode ajudar, mas o que é melhor do que realmente pôr a mão na massa em um ambiente prático? Este projeto visa guiar e simplificar a forma com que os novatos fazem a sua primeira contribuição. Se quiser fazer a sua primeira contribuição, siga os passos abaixo.

<img align="right" width="300" src="assets/fork.png" alt="fork deste repositório" />

Se não possui o git em sua máquina, [instale-o aqui](https://help.github.com/articles/set-up-git/).

## Faça um Fork deste repositório

Faça um Fork clicando no botão "Fork" no topo desta página. Isto irá criar uma cópia deste repositório na sua conta.

## Clone o repositório

<img align="right" width="300" src="assets/clone.png" alt="clonar este repositório" />

Agora clone este repositório para a sua máquina. Clique no botão "Clone or download" e, em seguida, clique no ícone "Copy to clipboard" para copiar a URL.

Abra seu terminal e execute o seguinte comando do git:

```
git clone "url que copiou"
```

onde "url que copiou" (sem as aspas) é a URL deste repositório. Consulte as etapas anteriores para obter a URL.

<img align="right" width="300" src="assets/copy-to-clipboard.png" alt="copiar URL" />

Por exemplo:

```
git clone https://github.com/seu-usuario/pneumonia-diagnose.md
```

onde "seu-usuário" é o seu usuário do GitHub. Aqui você está copiando o conteúdo do repositório first-contributions para o seu computador.

## Crie um Branch

Vá para o diretório do repositório no seu computador (caso você não esteja lá):

```
cd pneumonia-diagnose
```

Agora crie um Branch usando o comando `git checkout`:

```
git checkout -b <add-seu-nome>-<issueNumber>-<issue-description>
```


Obs.: O nome do Branch não precisa ter a sigla "add", mas nesse caso é recomendável, porque a finalidade deste Branch é a de adicionar o seu nome a uma lista.

## Efetue as alterações necessárias e faça um Commit

Agora abra os arquivo em seu editor de código, adicione as alterações e salve o arquivo.

<img align="right" width="450" src="assets/git-status.png" alt="git status" />

Se você for para o diretório do projeto e executar o comando `git status`, verá que há alterações. Adicione essas alterações ao Branch que você acabou de criar utilizando o comando `git add`:

```
git add *
```

Agora faça um Commit dessas alterações utilizando o comando `git commit`:

```
git commit -m "<seu-nome> MENSAGEM DO COMMIT"
```

preenchendo `<seu-nome>` com o seu nome.

## Faça um Push das alterações para o GitHub

Faça um Push utilizando o comando `git push`:

```
git push origin <add-seu-nome>
```

substituindo `<add-seu-nome>` pelo nome do Branch que você criou anteriormente.

## Envie suas alterações para serem revisadas

Se você for para o seu repositório no GitHub, verá um botão `Compare & pull request`. Clique nesse botão.

<img style="float: right;" src="assets/compare-and-pull.png" alt="Crie um Pull Request" />

Agora envie um Pull Request.

<img style="float: right;" src="assets/submit-pull-request.png" alt="Envie o Pull Request" />

Logo estarei mesclando ('mergeando') as suas mudanças no Branch principal (master) deste projeto. Você receberá um e-mail de notificação quando as alterações forem mescladas.

## Parabéns!

Você completou o fluxo de trabalho básico _fork -> clone -> edit -> PR_ que você encontrará frequentemente como contribuidor!
