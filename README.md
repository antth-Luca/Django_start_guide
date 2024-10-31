# !!! | Atenção: Repositório em construção | !!!

# Guia para iniciantes - framework Django
Este guia destina-se a pessoas que querem aprender um framework para WEB, mas não sabem por onde começar.

Eu sempre recomendo o Django, pelo seu lema "baterias inclusas" e por ser em Python, uma linguagem de sintaxe transparente, de fácil compreensão.

Vamos lá?!

# Sumário

## 1. Introdução
### 1.1 - Eu e o Django
Há muito tempo, eu tinha uma ideia de projeto para a WEB, mas eu só sabia Python, HTML e CSS. Procurei por algo que me ajudasse a construir este tal projeto, encontrei o Django, me apaixonei e hoje tenho alguns projetos de estudo e amostras produzidas em Django.

### 1.2 - Django e o mundo profissional
Django é amplamente usado no meio profissional para desenvolver aplicações web robustas e escaláveis. Ele é especialmente popular em empresas que valorizam rapidez no desenvolvimento, segurança e uma estrutura "baterias incluídas" que oferece muitos recursos prontos para uso.

### 1.3 - Mas afinal, o que é Django?
Django é um framework front-end e back-end desenvolvido para Python. Você cuida do front e do back em apenas um projeto, levando-os juntos!
O Django tem muitos pontos fortes, por exemplo: segurança, escalabilidade, integração com diversos bancos de dados, rica quantidade de bibliotecas, ótima comunidade ([Visite-nos!](https://www.djangoproject.com/community/)) e ainda incentiva boas práticas de codificação. Além de quê, um dos lemas do Django é "baterias inclusas", portanto ele tem muitos recursos prontos para usar que aceleram o desenvolvimento. Exemplos:
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

#### 1.3.1 - Arquitetura Django
Diferentemente de outros frameworks comuns, o Django usa o modelo MTV (Model - Template - View). Nele acontece a seguinte hierarquia:
- Um usuário/cliente acessa uma rota/URL;
- A URL aponta para uma view;
- A view obtém um template HTML;
- A view acessa um model, se necessário, e realiza operações no banco de dados;
- A view retorna uma resposta ao cliente.
---

Um projeto Django é dividido em:
- **Módulo obrigatório**: de mesmo nome do projeto, por padrão;
- **Módulos internos**: não visíveis, mas importantes para o funcionamento. Por exemplo: `admin`, `auth`, `contenttypes` e `sessions`;
- **Módulos complementares**: criados pelos devs. Podem representar bancos, entidades ou funções, conforme a preferência do dev e nenhuma abordagem está errada.

Um módulo deve conter arquivos e esses carregam diversas funções. Seguem tabelas explicando:
- Módulo obrigatório

| Nome arquivo | É obrigatório? | Função |
| :------------: | :-------------- | :------ |
| __init__.py | Sim | Identificar um módulo Python. |
| settings.py | Sim | Guarda *todas* as configurações de um projeto Django. |
| urls.py | Sim | Interliga os arquivos urls.py de cada módulo complementar. |
| asgi.py | Sim | Necessário quando você deseja implementar funcionalidades assíncronas em seu projeto Django, como chat em tempo real ou notificações via WebSocket. |
| wsgi.py | Sim | É utilizado quando você está implantando seu projeto Django em servidores que seguem o padrão WSGI. |

- Módulos complementares

| Nome arquivo | É obrigatório? | Função |
| :------------: | :-------------- | :------ |
| __init__.py | Sim | Identificar um módulo Python. |
| apps.py | Sim | Identifica um módulo Django. |
| admin.py | Não | Registrar os models no painel de administrador do Django. |
| models.py | Não | Guarda as classes de model (representações das entidades no banco de dados). |
| forms.py | Não | Guarda as classes de formulário (automação de formulário para os HTML’s). |
| views.py | Não | Faz todo o processo, ele manipula dados e renderiza templates. |
| urls.py | Não | Guarda as urls/rotas do módulo complementar, apontando para uma view específica. |
| tests.py | Não | Usado para executar testes. |

## 2. Preparando o ambiente
Nós precisaremos de algumas ferramentas:
- IDE para codificação (recomendo [Visual Studio Code](https://code.visualstudio.com/) pelo suporte a múltiplas linguagens e extensões de arquivos e a ampla biblioteca de extensões);
- IDE para banco de dados SQLite (recomendo [DB Browser](https://sqlitebrowser.org/) por ser simples e cumprir muito bem sua função, mas eu recomendo também por EU estar mais acostumado com a ferramenta rsrs);
- Um navegador, pode ser qualquer um (não vou expor a minha preferência, pois costuma dar briga rsrs);
- Obviamente, precisaremos do Python (eu utilizei o Python 3.11.9, mas instale a versão que você quiser e sempre do [site oficial do Python](https://www.python.org/downloads/);

> [!NOTE]
> **OBS:** Se o Python, o PIP ou uma biblioteca Python não forem reconhecidos no Windows, muito provavelmente o erro estará no PATH do Windows. Verifique se o caminho do interpretador Python e da pasta "Scripts" estejam adicionadas ao PATH nas variáveis de ambiente:
> ```text
> # Variável de ambiente "Path"
> 
> C:\Users\<seu_user>\AppData\Local\Programs\Python\Python<versão>\
> C:\Users\<seu_user>\AppData\Local\Programs\Python\Python<versão>\Scripts\
> ```
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

> [!NOTE]
> **OBS:** Um venv, ou virtual environment (ambiente virtual, em tradução livre) é como uma "caixa" isolada que você cria no seu computador para trabalhar em um projeto Python. Dentro dessa caixa, você pode instalar versões específicas de bibliotecas e pacotes sem interferir com outros projetos ou com as configurações globais do seu sistema. Vantagens: isolamento, versões específicas para cada projeto e facilidade no gerenciamento.

- Após a criação com sucesso, o venv já deve estar ativo. Dessa forma:
```cmd
(<nome_do_seu_venv>) C:\seu\diretorio>
```
> [!TIP]
> **Dica:** O Virtualenvwrapper tem comandos que facilitam a manipulação dos venvs. São alguns deles:
> - `mkvirtualenv <nome_do_seu_venv>` - Cria um venv;
> - `rmvirtualenv <nome_do_seu_venv>` - Exclui um venv;
> - `workon <nome_do_seu_venv>` - Ativa um venv;
> - `deactivate` - Desativa um venv.

- Com o VENV ativo, instale o Django. Use:
```cmd
pip install django
```
> [!NOTE]
> **OBS:** Neste projeto foi utilizada a versão 5.1.2. Para instalar esta exata versão: `pip install django==5.1.2`.

## 3. Iniciando um projeto Django
Navegue até o diretório que você deseja iniciar seu projeto Django. No command prompt se comandos como:
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

![Boas vindas do Django](https://github.com/antth-Luca/Django_start_guide/blob/main/images/django/boas-vindas.png)

## 4. Primeiras configurações dentro do Django
Abra o `settings.py` que está dentro do módulo obrigatório e adicione a importação `import os`. Vamos configurar!

### 4.1 - Local e hora
  Desça e encontre as duas configurações `LANGUAGE_CODE` e `TIME_ZONE` e altera os valores:
```python
# <módulo_obrigatório> > settings.py

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

### 4.2 - Templates
Ainda dentro do `settings.py`, encontre a configuração `TEMPLATES` e adicione:
```python
# <módulo_obrigatório> > settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Altere esta linha!
        <...>  # Existem outras definições abaixo. Não altere!
    }
]
```

### 4.3 - Arquivos estáticos (CSS, JS e imagens)
Também dentro do `settings.py`, encontre `STATIC` para alterar e adicionar:
```python
# <módulo_obrigatório> > settings.py

STATIC_URL = '/static/'  # Adicione uma barra aqui!
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # Adicione esta linha!
]
```

### 4.4 - Estilos prontos (Crispy Forms)
Você sabia que existem bibliotecas Python que interagem com o Django e trazem muitos estilos prontos?!
Eu conheço e lhe apresentarei o **Django Crispy Forms**. Esta biblioteca aplica estilos a formulários. Vamos prepará-la:
- Abra o terminal;
- Verifique que o VENV esteja ativo;
- Instale o Django Crispy Forms. Use:
```cmd
pip install django-crispy-forms
```
- Instale o Crispy Bootstrap 5. Use:
```cmd
pip install crispy-bootstrap5
```
- Adicione as bibliotecas ao projeto Django. Abra o settings.py, encontre a constante INSTALLED_APPS e adicione as linhas:
```python
# <módulo_obrigatório> > settings.py

INSTALLED_APPS = [
    <...>  # Não altere as linhas que já existem, apenas adione novas!
    'crispy_forms',
    'crispy_bootstrap5',
]
```
- Configure o Bootstrap do Crispy. Adicione a seguinte constante ao `settings.py`, logo abaixo de INSTALLED_APPS:
```python
# <módulo_obrigatório> > settings.py

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```
Agora, para utilizar, basta adicionar a tag `{% load crispy_forms_tags %}` em uma das primeiras linhas de um template e renderizar o formulário com `{{ form|crispy }}`. Você poderá ver os campos com tamanho e espaçamento definido, todo um estilo pronto!
Você ainda pode combinar o Crispy com o Bootstrap e acelerar o desenvolvimento.

## 5. Desenvolvimento Django
### 5.1 - Metodologia para as view
Antes de tudo, precisamos definir se utilizaremos views baseadas em _funções_ ou _classes_.

Quando optamos por **funções**, precisamos programar toda a manipulação de método HTTP e retorno de resposta e outros, mas temos mais liberdade.

Quando se opta por **classes**, o código diminui drasticamente, pois já está programado, basta utilizarmos. 

> [!NOTE]
> **OBS:** Neste projeto, usaremos classes, porque não precisamos reinventar a roda e somos iniciantes, né?

### 5.2 - Primeiro módulo
Para continuarmos nossa jornada, vamos criar um módulo complementar. Para isso, abra o terminal com o VENV ativo e dentro do diretório do projeto Django e use:
```cmd
python manage.py startapp <nome_do_seu_módulo>
```
O Django exige que registremos os novos módulos. Para isso:
- Abra o `settings.py`;
- Encontre `INSTALLED_APPS`;
- Adicione a linha:
```python
# <módulo_obrigatório> > settings.py

INSTALLED_APPS = [
    <...>  # Linhas padrão do Django
    # Linhas que você já adicionou
    'crispy_forms',
    'crispy_bootstrap5',
    # Adicione a seguinte linha:
    '<nome_do_seu_módulo>.apps.<nome_do_seu_módulo>Config',
]
```

> [!NOTE]
> **OBS:** Se haverá rotas/URLs no seu módulo, faça:
> 
> - Dentro do módulo recém-criado, crie um arquivo `urls.py`:
> ```python
> # <nome_do_seu_módulo> > urls.py
> 
> from django.urls import path
> 
> urlpatterns = []
> ```
> - Dentro do `urls.py` do módulo obrigatório, adicione a importação e inclua as URLs do módulo complementar:
> ```python
> # <módulo_obrigatório> > urls.py
> 
> from django.contrib import admin
> from django.urls import path, include  # Adicionar o 'include' aqui!
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     # Inclua as urls do módulo:
>     path('', include('<nome_do_seu_módulo>.urls')),
> ]
> ```

### 5.3 - Criando uma view simples
Vamos criar nossa primeira view! Uma view com o clássico texto "Olá, mundo!":
- Abra seu módulo complementar;
- Procure o arquivo `views.py`;
- Adicione a importação e crie a view:
```python
# <nome_do_seu_módulo> > views.py

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = '<nome_do_seu_módulo>/home.html'
```
- Vá até o arquivo `urls.py` e adicione a importação e a URL:
```python
# <nome_do_seu_módulo> > urls.py

from django.urls import path
from .views import HomeView

urlpatterns = [
    path('home', HomeView.as_view(), name='Home'),
]
```
- Crie o diretório: `<seu_projeto>\<nome_do_seu_módulo>\templates\<nome_do_seu_módulo>`;
- Dentro deste, crie o template HTML `home.html` com uma tag **h1** com a mensagem:
```html
<h1>Olá, mundo!</h1>
```
- Inicie o servidor do Django. Use:
```cmd
python manage.py runserver
```
- Acesse [`localhost:8000/home`](http://localhost:8000/home). Você deve ver uma página branca com a mensagem e isso quer dizer que funcionou. Você criou sua primeira view, parabéns!

### 5.4 - Criando uma view de criação
Agora criaremos uma view um pouco além. Ela não apenas mostrará um texto, agora vamos mexer com o banco de dados e fazer registros nele. Faça:
- Crie um módulo com o nome Cidade;
- Registre o módulo no `settings.py`;
- Inclua as URLs do novo módulo;
- Dentro de `models.py` modele a entidade de cidade:
```python
# Cidade > models.py

from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} - {self.uf}'
```
> [!NOTE]
> **OBS:** Não, não estou usando as melhores práticas de modelagem, mas... Dá um desconto, é só um exemplo!

> [!IMPORTANT]
> #### -( Migrações Django )-
> Preciso interromper aqui para lhe dizer que o Django tem um ORM (Object Relational Mapper - Mapeamento objeto-relacional) e já trata das criações de tabela no banco de dados, mas para isso, precisamos solicitar que ele realize as migrações. Use:
> - `python manage.py makemigrations` - Para criar as migrações;
> - `python manage.py migrate` - Para aplicar as migrações no banco.
> 
> Tudo pronto para continuar!

#### ...Prosseguindo com a view de criação:

- Vamos construir a view. Em `views.py` faça:
```python
# Cidade > views.py

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Cidade

class CreateCidadeView(CreateView):
    model = Cidade
    fields = '__all__'
    template_name = 'Cidade/create-cidade.html'
    success_url = reverse_lazy('Home')
```
- Crie o arquivo `urls.py`:
```python
# Cidade > urls.py

from django.urls import path
from .views import CreateCidadeView

urlpatterns = [
    path('criar-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
]
```
- Dentro do seu projeto Django, crie o diretório `<projeto_django>\templates\Bases`;
- Dentro de Bases, crie o template `base-global.html`:
```html
{% load static %}

<!DOCTYPE html>
<html lang="pt-br" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block titulo %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
</head>
<body>
    {% block body %}
    {% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
- Também dentro de Bases, crie o `base-navbar.html`:
```html
{% extends 'Bases/base-global.html' %}

{% block body %}
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'Home' %}">
                <i class="bi bi-building me-2"></i>Meu app Django
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link d-flex align-items-center" href="#"><i class="bi bi-person-circle me-2" style="font-size: 32px;"></i></i>Olá, {{ user.username }}!</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main>
        {% block main %}
        {% endblock %}
    </main>
{% endblock %}
```
- Ainda dentro de Bases, crie `base-create.html`:
```html
{% extends 'Bases/base-global.html' %}
{% load crispy_forms_tags %}

{% block titulo %}
    Cadastrar
{% endblock %}

{% block body %}
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-md-8 col-xl-4 mx-auto">
                <form method="post">
                    {% csrf_token %}

                    <h6 class="display-6 text-center">Novo registro</h6>
                    <h4 class="h4 mt-2 text-center">Cadastrando {% block 'tipo_cadastro' %}{% endblock %}</h4>
                    <h6 class="h6 mb-4 text-center">Os campos com (*) são obrigatórios!</h6>
                    <h6 class="text-danger">{{ form.errors }}</h6>

                    <div class="d-flex flex-column">
                        {{ form|crispy }}

                        <button type="submit" class="btn btn-primary mt-4 align-self-end">{% block botao_submit %}Salvar{% endblock %}</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
{% endblock %}
```
> [!WARNING]
> **OBS:** Este template está usando *Django Crispy Forms*. Caso não tenha instalado, volte para [instalar Crispy Forms](#estilos-prontos)!
- Agora, dentro do seu módulo Cidade, crie o diretório `<módulo_Cidade>\templates\Cidade`;
- E dentro dele, adicione um `create-cidade.html`:
```html
{% extends 'Bases/base-create.html' %}

{% block tipo_cadastro %}Cidade{% endblock %}
```
- Inicie o servidor com o comando `python manage.py runserver` e acesse no navegador [`localhost:8000/criar-cidade`](http://localhost:8000/criar-cidade);
- Você deve ver um lindo formulário para cadastrar uma cidade e isso significa que está tudo certo!
- Preencha os campos e clique no botão Salvar;
- Abra o **DB Browser**:

![DB Browser após aberto](https://github.com/antth-Luca/Django_start_guide/blob/main/images/db-browser/interface-inicial.png)
- Clique em **arquivo** no canto superior esquerdo da tela. Depois **Abrir banco de dados somente leitura** e escolha o arquivo `<projeto_django>\db.sqlite`:

![Opções de arquivo no DB Browser](https://github.com/antth-Luca/Django_start_guide/blob/main/images/db-browser/opcoes-arquivo.png)

- Você poderá encontrar uma tabela chamada de `Cidade_cidade`. Este é um padrão do Django: "`<nome_do_módulo>_<nome_do_model>`";
- Se você clicar com o botão direito em cima da tabela e usar a opção **Navegar tabela**, poderá ver a cidade que acabou de cadastrar lá no sistema e isso quer dizer que funciona!

### 5.5 - Criando uma view de listagem
Bem, ficar vendo os registros diretamente no banco não é viável quando se pensa nos usuários, certo?

Então vamos construir uma view de listagem:
- Primeiramente, em `views.py` adicione a importação e crie a view de listagem:
```python
# Cidade > views.py

from django.views.generic import CreateView, ListView  # Adicione a importação de 'ListView'!
from django.urls import reverse_lazy
from .models import Cidade

# Adicione a view de listagem!
class ListCidadeView(ListView):
    model = Cidade
    template_name = 'Cidade/list-cidade.html'
    context_object_name = 'cidades'


# Esta view deve permanecer. É a view de criação de cidades...
class CreateCidadeView(CreateView):
    model = Cidade
    fields = '__all__'
    template_name = 'Cidade/create-cidade.html'
    success_url = reverse_lazy('Home')
```
- Em `urls.py`, registre a URL:
```python
# Cidade > urls.py

from django.urls import path
from .views import CreateCidadeView, ListCidadeView  # Adicione a importação da view de listagem!

urlpatterns = [
    path('criar-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
    path('lista-cidade', ListCidadeView.as_view(), name='ListCidade'),  # Adicione a URL!
]
```
- Agora crie uma base de listagens `base-list.html` dentro de `<projeto_django>\templates\Bases`:
```html
{% extends 'Bases/base-navbar.html' %}

{% block titulo %}
    Listagem
{% endblock %}

{% block main %}
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-lg-8 mx-auto p-3 d-flex flex-column">
                {% block btn_add %}<a href="{% block url_regist %}{% endblock %}" class="btn btn-primary align-self-end me-3 mt-3"><i class="bi bi-plus" me-2></i>Novo</a>{% endblock %}
                <p class="h4 mt-5">Listando {% block tipo_listagem %}{% endblock %}</p>

                <table class="table table-sm table-striped table-hover">
                    <thead>
                        <tr>
                            {% block colunas %}{% endblock %}
                        </tr>
                    </thead>
                    <tbody>
                        {% block tratam_dados %}{% endblock %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
{% endblock %}
```
- Agora dentro de `<módulo_Cidade>\templates\Cidade`, crie o `list-cidade.html`:
```html
{% extends 'Bases/base-list.html' %}

{% block url_regist %}{% url 'CreateCidade' %}{% endblock %}
{% block tipo_listagem %}Cidade{% endblock %}

{% block colunas %}
    <th scope="col">Nº</th>
    <th scope="col">Nome</th>
    <th scope="col">UF</th>
    <th scope="col">Opções</th>
{% endblock %}

{% block tratam_dados %}
    {% for cidade in cidades %}
        <tr>
            <th scope="row">{{ forloop.counter }}</th>
            <td>{{ cidade.nome }}</td>
            <td>{{ cidade.uf }}</td>
            <td>
                <a href="#" class="btn btn-warning" title="Editar">
                    <i class="bi bi-pencil-fill"></i></a>
                
                <a href="#" class="btn btn-danger" title="Excluir">
                    <i class="bi bi-trash"></i></a>
            </td>
        </tr>
    {% empty %}
        <td><li class="text-danger">Nenhum registro encontrado.</li></td>
    {% endfor %}
{% endblock %}
```
#### -( Página Home 2.0 )-
Antes de testarmos a listagem de cidade, vamos refazer a página Home:
- Substitua o conteúdo de `home.html` por:
```html
{% extends 'Bases/base-navbar.html' %}

{% block titulo %}
    Home
{% endblock %}

{% block main %}
    <div class="container-fluid text-center mt-5">
        <h1 class="h1 mb-2">Central de Links</h1>
        <div class="row justify-content-center">
            <div class="col-8 col-md-6">
                <div class="list-group">
                    <a href="#" class="list-group-item list-group-item-action active">Home</a>
                    <a href="{% url 'ListCidade' %}" class="list-group-item list-group-item-action">Cidades</a>
                    <a href="#" class="list-group-item list-group-item-action">Clientes</a>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

#### ...E vamos ao teste da listagem:
- Inicie o servidor do Django e acesse [`localhost:8000/home`](http://localhost:8000/home);
- Clique em _Cidades_, se uma lista com as cidades abrir, é porque funcionou!

> [!NOTE]
> **OBS:** O botão de adicionar na lista, também já deve funcionar!

### 5.6 - Criando uma view de edição
E vamos fazer a edição!
- Adicione a importação e crie a view:
```python
# Cidade > views.py

from django.views.generic.edit import UpdateView

class EditCidadeView(UpdateView):
    model = Cidade
    fields = '__all__'
    template_name = 'Cidade/edit-cidade.html'
    success_url = reverse_lazy('ListCidade')
```
- Registre a URL:
```python
# Cidade > urls.py

from django.urls import path
from .views import CreateCidadeView, ListCidadeView, EditCidadeView  # Adicione a importação da view de edição!

urlpatterns = [
    path('criar-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
    path('lista-cidade', ListCidadeView.as_view(), name='ListCidade'),
    path('edit-cidade/<int:pk>', EditCidadeView.as_view(), name='EditCidade'),  # Adicione a URL!
]
```
- Crie o template `<projeto_django>\templates\Bases\base-edit.html`:
```html
{% extends 'Bases/base-global.html' %}
{% load crispy_forms_tags %}

{% block titulo %}
    Editando
{% endblock %}

{% block body %}
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-md-8 col-xl-4 mx-auto">
                <form method="post">
                    {% csrf_token %}

                    <h6 class="display-6 text-center">Editando registro</h6>
                    <h4 class="h4 mt-2 text-center">Editando {% block tipo_cadastro %}{% endblock %}</h4>
                    <h6 class="h6 mb-4 text-center">Os campos com (*) são obrigatórios!</h6>
                    <h6 class="text-danger">{{ form.errors }}</h6>

                    <div class="d-flex flex-column">
                        {{ form|crispy }}

                        <button type="submit" class="btn btn-primary mt-4 align-self-end">{% block botao_submit %}Salvar{% endblock %}</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
{% endblock %}
```
- E crie o template filho `Cidade\templates\Cidade\edit-cidade.html`:
```html
{% extends 'Bases/base-edit.html' %}

{% block tipo_edit %}Cidade{% endblock %}
```
- Adicione `{% url 'EditCidade cidade.pk %}` ao href da tag **a** de edição do `list-cidade.html`. Por exemplo:
```html
<...>
{% block tratam_dados %}
    {% for cidade in cidades %}
        <tr>
            <th scope="row">{{ forloop.counter }}</th>
            <td>{{ cidade.nome }}</td>
            <td>{{ cidade.uf }}</td>
            <td>
                <a href="{% url 'EditCidade' cidade.pk %}" class="btn btn-warning" title="Editar">
                    <i class="bi bi-pencil-fill"></i></a>
<...>
```
- Inicie o servidor do Django e acesse [`localhost:8000/list-cidade`](http://localhost:8000/list-cidade);
- Agora o botão de editar um registro estará funcionando!

### 5.7 - Criando uma view de deleção
Agora, a última função CRUD... Vamos fazer a view de deleção:
- Adicione a importa e view:
```python
# Cidade > views.py

from django.views.generic.edit import UpdateView, DeleteView

class DeleteCidadeView(DeleteView):
    model = Cidade
    template_name = 'Cidade/delete-cidade.html'
    success_url = reverse_lazy('ListCidade')
```
- Registre a URL:
```python
# Cidade > urls.py

from django.urls import path
from .views import CreateCidadeView, ListCidadeView, EditCidadeView, DeleteCidadeView  # Adicione a importação da view de deleção!

urlpatterns = [
    path('criar-cidade', CreateCidadeView.as_view(), name='CreateCidade'),
    path('lista-cidade', ListCidadeView.as_view(), name='ListCidade'),
    path('edit-cidade/<int:pk>', EditCidadeView.as_view(), name='EditCidade'),
    path('delete-cidade/<int:pk>', DeleteCidadeView.as_view(), name='DeleteCidade'),  # Adicione a URL!
]
```
- Crie o template base `base-delete.html`:
```html
{% extends 'Bases/base-global.html' %}

{% block body %}
    <main>
        <div class="container-fluid">
            <div class="row">
                <div class="col-12 col-md-8 col-xl-4 mx-auto p-4 painel-form">
                    <h4 class="text-center">Tem certeza de que deseja deletar "{{ object }}"?</h4>
                    <form method="post">
                        {% csrf_token %}
                        <div class="d-flex justify-content-around my-4">
                            <a href="{% block url_cancelamento %}{% endblock %}" class="btn btn-info">Cancelar</a>
                            <button type="submit" class="btn btn-danger">Confirmar</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
{% endblock %}
```
- E crie o template filho `delete-cidade.html`:
```html
{% extends 'Bases/base-delete.html' %}

{% block url_cancelamento %}{% url 'ListCidade' %}{% endblock %}
```
- Adicione `{% url 'DeleteCidade' cidade.pk %}` ao href da tag **a** de deleção do `list-cidade.html`. Por exemplo:
```html
<...>
                <a href="{% url 'DeleteCidade' cidade.pk %}" class="btn btn-danger" title="Excluir">
                    <i class="bi bi-trash"></i></a>
            </td>
        </tr>
    {% empty %}
        <td><li class="text-danger">Nenhum registro encontrado.</li></td>
    {% endfor %}
{% endblock %}
```
- Inicie o servidor do Django e acesse [`localhost:8000/list-cidade`](http://localhost:8000/list-cidade);
- Agora o botão de deleção um registro estará funcionando!

### 5.8 - Criando o módulo de Cliente
> [!IMPORTANT]
> Aqui fica um desafio, façam a criação, listagem, edição e deleção para a entidade **Clientes**. Não precisa recriar os templates base, apenas faça as heranças!

Vou deixar pelo menos o model de Cliente aqui:
```python
# Clientes > models.py

from django.db import models
from Cidade.models import Cidade

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'
```

### 5.9 - Painel administrativo do Django
O Django tem um painel administrativo imbutido e já pronto. Nele, nós podemos manipular os dados do banco sem estar dentro do sistema. Este painel é muito usado durante o período de testes e para manutenções do sistema. 

Para usarmos, basta o cadastro de um model no admin do Django. Vamos lá:
- Primeiramnete, vamos criar um superuser. No terminal:
```cmd
python manage.py createsuperuser
```
- Preencha o nome de usuário e senha, email pode ser vazio;
- Agora vamos ao módulo de Cidade. Abra o arquivo `Cidade\admin.py`;
- Adicione a importação do _model_ e registre no admin:
```python
# Cidade > admin.py

from django.contrib import admin
from .models import Cidade

# Register your models here.
admin.site.register(Cidade)
```
- Inicie o servidor do Django e acesse [`localhost:8000/admin`](http://localhost:8000/admin);
- Faça login com as credenciais inseridas na criação do _superuser_ que fizemos à pouco;

![Inicial do painel administrativo do Django](https://github.com/antth-Luca/Django_start_guide/blob/main/images/django/inicial-admin.png)

- Escolha a opção `Cidades`;
- Você deve ver uma lista de todas as cidades que registrou. Daqui você pode adicionar, editar e excluir elas.

![Cidades listadas no admin do Django](https://github.com/antth-Luca/Django_start_guide/blob/main/images/django/cidades-admin.png)

### 5.10 - Autenticação

## 6. Resumo comandos Django

## 7. DTL (Django Template Language)


# !!! | Atenção: Repositório em construção | !!!
