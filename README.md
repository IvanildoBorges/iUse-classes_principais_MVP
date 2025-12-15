# Sistema iUse
*A educação que circula entre todos*

## Projeto
- O projeto utiliza uma organização inspirada em Clean Architecture, separando o domínio da aplicação das camadas de serviço e interface.
- A pasta ```app/domain``` contém as entidades centrais e regras de negócio, enquanto ```app/services``` concentra serviços de aplicação, como autenticação.
Essa separação melhora a legibilidade, manutenção e testabilidade do sistema.

## Ambiente de execução e dependências
Este projeto utiliza ```Python 3``` e faz uso de um ambiente virtual ```(venv)``` para garantir o isolamento das dependências e a reprodutibilidade do ambiente de desenvolvimento.

**1. Requisitos:**
- **Python 3.10+** (recomendado)
- ```pip``` (gerenciador de pacotes do Python)

**2. Criação do ambiente virtual**
Na raiz do projeto, execute:

```bash
python -m venv venv
```

Em alguns sistemas, pode ser necessário usar:

```bash
python3 -m venv venv
```

**3. Ativação do ambiente virtual**

Windows (cmd ou PowerShell)

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Após a ativação, o terminal exibirá ```(venv)``` indicando que o ambiente está ativo.

Para desativar, basta digitar no terminal 
```bash
deactivate
```

**4. Instalação das dependências**
Todas as dependências do projeto estão listadas no arquivo ```requirements.txt```.
Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

**Dependências incluídas:**
- **pytest** — framework de testes automatizados
- Outras bibliotecas necessárias ao funcionamento da aplicação

As dependências são instaladas **exclusivamente no ambiente virtual**, não afetando o Python global do sistema.

**5. Execução do projeto**
Com o ambiente configurado:

```bash
python main.py
```

Para execução dos testes:
Os testes automatizados estão localizados na pasta ```tests/``` e podem ser executados com:

```bash
pytest
```

ou mais verbosamente:

```bash
pytest -v
```

## Estrutura de pastas
```bash
iuse/
├── main.py
├── app/
│   ├── domain/
│   │   ├── models/
│   │   └── mixins/
│   │
│   ├── services/
│   ├── utils/
│   └── interfaces/
│
├── docs/
│   └── imagens/
│
└── tests/
```

## Responsabilidades por camada

```app/domain/models```

Entidades do negócio (UML):
- ```Usuario```, ```Doador```, ```Beneficiario``` e ```Item```
- ```Reserva```, ```PontoColeta``` e ```Entrega```
- ```Retirada``` e ```Impacto```

**Sem dependência de serviços ou interface**

```app/domain/mixins```

Comportamentos reutilizáveis:
- ```AutenticavelMixin```

```app/services```

Regras de aplicação:
- Login/Logout
- Orquestração de fluxos
- Validações entre entidades

**Pode depender do domain, mas não o contrário**

```app/interfaces```

Camada de interação:
```CLI```
(futuro) ```API```/Web

## Fluxo principal
O arquivo ```main.py``` atua apenas como ponto de entrada da aplicação, delegando a execução para a camada de interface. Os fluxos de uso e simulações encontram-se na camada interfaces, enquanto os testes automatizados estão isolados na pasta tests, seguindo boas práticas de arquitetura.