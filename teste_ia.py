import spacy

# Carregue o modelo de linguagem
nlp = spacy.load("pt_core_news_sm")

def atribuir_tag(texto):
    # Processar o texto usando spaCy
    doc = nlp(texto)

    # Extrair entidades nomeadas (tags) do texto
    tags = [entidade.text for entidade in doc.ents]

    # Retornar as tags encontradas
    return tags

# Exemplo de uso
texto_do_usuario = "controle remoto 5 botões"
tags = atribuir_tag(texto_do_usuario)

# Salvar no banco de dados ou realizar outras ações com as tags
print(f'Texto: "{texto_do_usuario}"')
print(f'Tags: {tags}')
