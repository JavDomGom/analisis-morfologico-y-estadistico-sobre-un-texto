# import languagemodels as lm
#
#
# print(
#     lm.chat(
#         '''
#         System: Respond as a helpful assistant.
#         User: I got: aaa, bbb, ccc, ddd. What is the next word?
#         Assistant:
#         '''
#     )
# )

import openai

openai.api_key = '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'

# response = openai.Completion.create(
#     engine='gpt-4',
#     prompt='¿Cómo puedo utilizar AWK para filtrar datos que comiencen por fechas y terminen en un número entero de 8 dígitos?',
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# response = openai.ChatCompletion.create(
#     model='gpt-4',
#     messages=[
#         {'role': 'system', 'content': 'You are a helpful assistant.'},
#         {'role': 'user', 'content': 'Who won the world series in 2020?'},
#         {'role': 'assistant', 'content': 'The Los Angeles Dodgers won the World Series in 2020.'},
#         {'role': 'user', 'content': 'Where was it played?'}
#     ],
#
# )

response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '¿Cómo puedo utilizar AWK para filtrar datos que comiencen por fechas y terminen en un número entero de 8 dígitos?'}
    ],

)

print(response.get('choices')[0].get('message').get('content'))
