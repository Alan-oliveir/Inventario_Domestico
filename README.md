# Inventário Doméstico
 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Alan-oliveir/Inventario_Domestico/blob/main/LICENSE)

# Sobre o projeto

Inventário Doméstico é um programa simples de cadastro de móveis e eletrodomésticos escrito em python que armazena informações sobre e valores de bens pessoais. Com o programa pode registrar o nome do produto, marca, valor, local, data da compra, etc. O sistema permite cadastrar novos itens, visualizar as informações referentes aos produtos já cadastrados, atualizar os dados de cada item e excluir um produto registrado no sistema.

Na interface de usuário foi utilizada a biblioteca customtkinter. CustomTkinter é uma biblioteca python baseada em Tkinter, que fornece widgets novos, modernos e totalmente personalizáveis: <https://github.com/TomSchimansky/CustomTkinter>

O banco de dados utilizado foi o SQLite. SQLite é uma base de dados relacional de código aberto e que dispensa o uso de um servidor na sua atuação, armazenando seus arquivos dentro de sua própria estrutura.

## Layout 
![Windows](https://github.com/Alan-oliveir/Inventario_Domestico/blob/main/images/screenshot/inv_dom_screenshot.png) 

# Como usar o programa

O programa foi desenvolvido para ser usado no Windows. Baixe o arquivo DomInventory.exe e execute o programa.

### Inserir
- Para inserir um novo item no sistema de cadastro digite no formulário as informações do item e selecione uma foto do item que deseja adicionar no inventário, logo em seguida clique no botão adicionar e aguarde a mensagem de confirmação. O cadastro do produto só será realizado se todos os itens estiverem preenchidos e uma foto do produto for selecionada. 
### Visualizar
- Para visualizar um item cadastrado selecione o item desejado na tabela e depois clique no botão visualizar. As informações cadastradas aparecerão no formulário e a foto no local destinado para ver a imagem.
### Atualizar
- Para modificar as informações de um produto cadastrado primeiro selecione o produto que deseje alterar algum dado na tabela, depois clique no botão visualizar. Depois pode modificar os dados desejados nos respectivos campos para preencher os dados. Após fazer as modificações clique no botão atualizar e aguarde a mensagem de confirmação.
### Excluir
- Para excluir um produto cadastrado, selecione o item que deseja excluir na tabela, clique primeiro no botão visualizar e em seguida no botão excluir, se o processo for concluído com sucesso uma mensagem de confirmação será exibida.
### Pesquisar
- Para pesquisar um item na tabela digite na entrada apropriada o nome do item e clique no botão pesquisar, se tiver um item com o mesmo nome cadastrado será exibida uma mensagem na tela informando que o item foi encontrado e o mesmo ficará destacado na tabela. Caso contrário será mostrada uma mensagem informando que não foram encontrados resultados com o nome do item pesquisado. 

# Tecnologias utilizadas
## Linguagem
- Python

## Interface
- Tkinter
- Customtkinter

## Bibliotecas
- OS
- Pillow

## Banco de dados
- SQLite




# Autor

Alan de Oliveira Gonçalves

- Linkedin: www.linkedin.com/in/alan-de-oliveira-gonçalves-207549258
