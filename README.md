# !!! | Atenção: Repositório em construção | !!!

# Guia de apresentação do Django

## Introdução

### Eu e o Django
Há muito tempo, eu tinha uma ideia de projeto para a WEB, mas eu só sabia Python, HTML e CSS. Procurei por algo que me ajudasse a construir este tal projeto, encontrei o Django, me apaixonei e hoje tenho alguns projetos de estudo e amostras produzidas em Django.

### Django e o mundo profissional
Django é amplamente usado no meio profissional para desenvolver aplicações web robustas e escaláveis. Ele é especialmente popular em empresas que valorizam rapidez no desenvolvimento, segurança e uma estrutura "baterias incluídas" que oferece muitos recursos prontos para uso.

### Mas afinal, o que é Django?
Django é um framework front-end e back-end desenvolvido para Python. Você cuida do fornt e do back em apenas um projeto, levando-os juntos!
O Django tem muitos pontos fortes, por exemplo: segurança, escalabilidade, integração com diversos bancos de dados, rico ecossistema de bibliotecas, ótima comunidade ([Visite-nos!](https://www.djangoproject.com/community/)) e ainda incentiva boas práticas de codificação. Além de quê, um dos lemas do Django é "baterias inclusas", portanto ele tem muitos recursos prontos para usar que aceleram o desenvolvimento. Exemplos:
- Internacionalização e localização;
- Autenticação (login/logout);
- Funções CRUD prontas;
- Migrações de tabelas para o banco de dados;
- Interface para adminstradores pronta;
- Formulários prontos;
- Linguagem própria para templates HTML que simplificam a dinamização, esta chamada de DTL (Django Template Language);
- Roteamento de URLs;
- Sistema de mensagens e email;
- Entre outros.

#### Arquitetura Django
Diferentemente de outros frameworks comuns, o Django usa o modelo MTV (Model - Template - View). Nele acontece a seguinte hierarquia:
- Um usuário/cliente acessa uma rota/URL;
- A URL aponta para uma view;
- A view obtém um template HTML;
- A view acessa um model, se necessário, e realiza operações no banco de dados;
- A view retorna uma resposta ao cliente.

## Preparando o ambiente
Nós precisaremos de algumas ferramentas:
- IDE para codificação (recomendo [Visual Studio Code](https://code.visualstudio.com/) pelo suporte a múltiplas linguagens e extensões de arquivos e a ampla biblioteca de extensões);
- IDE para banco de dados SQLite (recomendo [DB Browser](https://sqlitebrowser.org/) por ser simples e cumprir muito bem sua função, mas eu recomendo também por EU estar mais acostumado com a ferramenta rsrs);
- Um navegador, pode ser qualquer um (não vou expor a minha preferência, pois costuma dar briga rsrs);
- Obviamente, precisaremos do Python (eu utilizei o Python 3.11.9, mas instale a versão que você quiser e sempre do [site oficial do Python](https://www.python.org/downloads/);
**OBS:** Se o Python, o PIP ou uma biblioteca Python não forem reconhecidos no Windows, muito provavelmente o erro estará no PATH do Windows. Verifique se o caminho do interpretador Python e da pasta "Scripts", que são as bibliotecas, estejam adicionadas ao PATH.
***

Ótimo! Agora vamos organizar e só então, vamos ao Django. No seu terminal:
- Instale a biblioteca Virtualenv. Use:
```cmd
pip install virtualenv
```
- Instale, também, a biblioteca Virtualenvwrapper. Para quem estiver no Windows, use:
```cmd
pip install virtualenvwrapper-win
```
- Agora crie um VENV: Tendo o Virtualenvwrapper, use:
```cmd
mkvirtualenv <nome_do_seu_venv>
```
**OBS:** Um venv, ou virtual environment (ambiente virtual, em tradução livre) é como uma "caixa" isolada que você cria no seu computador para trabalhar em um projeto Python. Dentro dessa caixa, você pode instalar versões específicas de bibliotecas e pacotes sem interferir com outros projetos ou com as configurações globais do seu sistema. Vantagens: isolamento, versões específicas para cada projeto e facilidade no gerenciamento.
- Após a criação com sucesso, o venv já deve estar ativo. Dessa forma:
```cmd
(<nome_do_seu_venv>) C:\seu\diretorio> |
```
**Dica:** O Virtualenvwrapper tem comandos que facilitam a manipulação dos venvs. São alguns deles:
```text
"mkvirtualenv <nome_do_seu_venv>" - Cria um venv;
"rmvirtualenv <nome_do_seu_venv>" - Exclui um venv;
"workon <nome_do_seu_venv>" - Ativa um venv;
"deactivate" - Desativa um venv.
```
- Com o VENV ativo, instale o Django. Use:
```cmd
pip install django
```
**OBS:** Neste projeto foi utilizada a versão 5.1.2. Para instalar esta exata versão: `pip install django==5.1.2`.

## Iniciando um projeto Django
Navegue até o diretório que você deseja iniciar seu projeto Django. No `command prompt` se comandos como:
- `cd <nome_pasta>` - Escolhe um diretório;
- `cd ..` - Volta um diretório;
- `cd \` - Volta todo o diretório até a raiz (o C:).

E finalmente, Django!
- Com o VENV ativo, crie um projeto Django. Use:
```cmd
django-admin startproject <nome_do_seu_projeto>
```
- Com VENV ativo e dentro do diretório do seu projeto Django, inicie o servidor do Django para testarmos. Use:
```cmd
python manage.py runserver
```
- Abra seu navegador de preferência e acesse a URL `localhost:8000`. Deve aparecer uma tela de boas vindas do Django e isto signfica que está tudo certo!

## Primeiras configurações dentro do Django
### Local e hora

# !!! | Atenção: Repositório em construção | !!!