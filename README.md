# Bot com OpenAI

Este projeto é um bot em Python que utiliza a API da OpenAI para buscar informações sobre filmes, como data de lançamento, bilheteria e sinopse, retornando os dados em formato JSON.

## 🚀 Funcionalidades
- Busca informações de filmes usando IA (GPT-4)
- Retorna os dados em JSON estruturado
- Tratamento de erros e respostas vazias

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## ⚙️ Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### 2. Instale as dependências
```bash
pip install openai python-dotenv
```

### 3. Configure sua chave da OpenAI
Crie um arquivo `.env` na raiz do projeto com o conteúdo:
```
OPENAI_API_KEY=sua-chave-aqui
```

### 4. Execute o bot
```bash
python main.py
```
Digite o nome do filme quando solicitado.

## 📦 Exemplo de uso
```
Digite o título do filme: The Founder
{
    "data_lancamento": "2016-01-20",
    "bilheteria": "$24.1 milhões",
    "sinopse": "The Founder conta a história de Ray Kroc..."
}
```

## 📝 Observações
- Se não houver informações disponíveis, o bot retorna uma mensagem de erro.
- Nunca compartilhe sua chave da OpenAI publicamente.

---

Feito com 💡 por [Seu Nome] 