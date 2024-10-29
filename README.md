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
---

Um projeto Django é dividido em:
- Módulo obrigatório: de mesmo nome do projeto, por padrão;
- Módulos internos: não visíveis, mas importantes para o funcionamento;
- Módulos complementares: criados pelos devs. Podem representar bancos, entidades ou funções, conforme a preferência do dev e nenhuma abordagem está errada.

Um módulo deve conter arquivos e esses carregam diversas funções. Seguem tabelas explicando:
- Módulo obrigatório
| Nome arquivo | É obrigatório? | Função |
| :------------: | :-------------- | :------ |
| `__init__.py` | Sim | Identificar um módulo Python. |
| `settings.py` | Sim | Guarda **todas** as configurações de um projeto Django. |
| `urls.py` | Sim | Interliga os arquivos `urls.py` de cada módulo complementar. |
| `asgi.py` | Sim | Necessário quando você deseja implementar funcionalidades assíncronas em seu projeto Django, como chat em tempo real ou notificações via WebSocket. |
| `wsgi.py` | Sim | É utilizado quando você está implantando seu projeto Django em servidores que seguem o padrão WSGI. |
- Módulos complementares
| Nome arquivo | É obrigatório? | Função |
| :------------: | :-------------- | :------ |
| `__init__.py` | Sim | Identificar um módulo Python. |
| `admin.py` | Não | Registrar os models no painel de administrador do Django. |
| `apps.py` | Sim | Identifica um módulo Django. |
| `models.py` | Não | Guarda as classes de model (representações das entidades no banco de dados). |
| `urls.py` | Não | Guarda as urls/rotas do módulo complementar, apontando para uma view específica. |
| `forms.py` | Não | Guarda as classes de formulário (automação de formulário para os HTML’s). |
| `views.py` | Não | Faz todo o processo, ele manipula dados e renderiza templates. |
| `tests.py` | Não | Usado para executar testes. |

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
Abra o `settings.py` que está dentro do módulo obrigatório e adicione a importação `import os`. Vamos configurar!

### Local e hora
  Desça e encontre as duas configurações `LANGUAGE_CODE` e `TIME_ZONE` e altera os valores:
```python
# <Módulo_obrigatório> > settings.py

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

### Templates
Ainda dentro do `settings.py`, encontre a configuração `TEMPLATES` e adicione:
```python
# <Módulo_obrigatório> > settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Altere esta linha!
        <...>  # Existem outras definições abaixo. Não altere!
    }
]
```

### Arquivos estáticos (CSS, JS e imagens)
Também dentro do `settings.py`, encontre `STATIC` para alterar e adicionar:
```python
# <Módulo_obrigatório> > settings.py

STATIC_URL = '/static/'  # Adicione uma barra aqui!
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # Adicione esta linha!
]
```

### Estilos prontos
Você sabia que existem bibliotecas Python que interagem com o Django e trazem muitos estilos prontos?!
Eu conhece e lhe apresentarei o `Django Crispy Forms`. Esta biblioteca aplica estilos a formulários. Vamos aplicar:
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
- Adicione as bibliotecas ao projeto Django. Abra o `settings.py`, encontre a constante `INSTALLED_APPS` e adicione as linhas:
```python
# <Módulo_obrigatório> > settings.py

INSTALLED_APPS = [
    <...>  # Não altere as linhas que já existem, apenas adione novas!
    'crispy_forms',
    'crispy_bootstrap5',
]
```
- Configure o Bootstrap do Crispy. Adicione a seguinte constante ao `settings.py`, logo abaixo de `INSTALLED_APPS`:
```python
# <Módulo_obrigatório> > settings.py

CRISPY_TEMPLATE_PACK = 'bootstrap5'
```
Agora, para utilizar, basta adicionar a tag `{% load crispy_forms_tags %}` em uma das primeiras linhas de um template e renderizar o formulário com `{{ form|crispy }}`. Você poderá ver os campos com tamanho e espaçamento definido, todo um estilo pronto!
Você ainda pode combinar o Crispy com o Bootstrap e acelerar o desenvolvimento.

## Desenvolvimento Django
### Metodologia de views
Antes de tudo, precisamos definir se utilizaremos views baseadas em _funções_ ou _classes_.

Quando optamos por **funções**, precisamos programar toda a manipulação de método _HTTP_ e retorno de resposta e outros, mas temos mais liberdade.

Quando se opta por **classes**, o código diminui drasticamente, pois já está programado, basta utilizarmos. 

**OBS:** Neste projeto, usaremos classes, porque não precisamos reinventar a roda e somos iniciantes, né?

### Primeiro módulo
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

**OBS:** Se haverá rotas/URLs no seu módulo, faça:
- Dentro do módulo recém-criado, crie um arquivo `urls.py`:
```python
# <nome_do_seu_módulo> > urls.py

from django.urls import path

urlpatterns = []
```
- Dentro do `urls.py` do módulo obrigatório, adicione a importação e inclua as URLs do módulo complementar:
```python
# Módulo obrigatório > urls.py

from django.contrib import admin
from django.urls import path, include  # Adicionar o 'include' aqui!

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclua as urls do módulo:
    path('', include('<nome_do_seu_módulo>.urls')),
]
```

### Criando uma view simples
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
- Acesse `localhost:8000/home`. Você deve ver uma página branca com a mensdagem e isso quer dizer que funcionou. Você criou sua primeira view, parabéns!

### Criando uma view de criação
- Crie um módulo com o nome _Cidade_;
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
**OBS:** Não, não estou usando as melhores práticas de modelagem, mas... Dá um desconto, é só um exemplo!
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
    success_url = reverse_lazy('ListCidade')
```
- Crie uma URL:
```python

```

# !!! | Atenção: Repositório em construção | !!!