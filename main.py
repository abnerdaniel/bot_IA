import os
import json
import openai
from dotenv import load_dotenv
from pydantic_core.core_schema import none_schema, nullable_schema

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(title):
    prompt = (
        f"Me dê as seguintes informações sobre o filme '{title}': "
        "data de lançamento, bilheteria e sinopse. "
        "Responda apenas em JSON com as chaves: data_lancamento, bilheteria, sinopse."
    )

    try:
        response = openai.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        
        print("DEBUG - Resposta bruta:", response)

        content = response.choices[0].message.content
        if content is not None:
            response_text = content.strip()
        else:
            response_text = "Não foi possível obter os dados do filme."

        print("DEBUG - recebido:", response_text)

        # Remove formatacacao markdown
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "").replace("```", "").strip()
        elif response_text.startswith("```"):
            response_text = response_text.replace("```", "").strip()

        print("DEBUG - Texto limpo:", response_text)

        try:
            dados = json.loads(response_text)
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON. Resposta recebida:", response_text)
            return {"erro": "A resposta não está em formato JSON válido."}

        # Verifica se todos os valores são NULOS
        if all(value is None for value in dados.values()):
            return {"erro": "Não foi possível obter os dados do filme."}
            
        else:
            return dados

    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return {"erro": "Não foi possível obter os dados do filme."}

# Teste
if __name__ == "__main__":
    titulo = input("Digite o título do filme: ")
    resultado = generate_response(titulo)
    print(json.dumps(resultado, indent=4, ensure_ascii=False))

        