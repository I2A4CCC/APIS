import openai

from dotenv import dotenv_values
config = dotenv_values('.env')

openai.api_key = config['API_KEY'] # Fill in your own key

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )
  

  retrieve_blog = response.choices[0].text

  return retrieve_blog

ask_gpt = input('Ask me a question and I will try to asnwer it in my best abilities: ')

print(generate_blog(ask_gpt))
# keep asking this model to write you paragraphs

keep_writing = True
while keep_writing:
  print('===================')
  answer = input("Would you like to prompt a different questio? Press 'Y' for yes, anything else for no. ")
  if (answer.upper() == 'Y'):
    paragraph_topics = input('What eles would you like to ask? ')
    print(generate_blog(paragraph_topics))
  else:
    keep_writing = False


