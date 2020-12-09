import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = 'Q: '
question_suffix = "\n"
answer_prefix = "A: "
answer_suffix = "\n\n"
# Construct GPT object and show some examples
gpt = GPT(engine="babbage",
          temperature=0.4,
          max_tokens=150,
          input_prefix=question_prefix,
          input_suffix=question_suffix,
          output_prefix=answer_prefix,
          output_suffix=answer_suffix,
          append_output_prefix_to_query=True)

gpt.add_example(Example('When did merengue become popular in New York City?',
                        'Merengue has been heard in New York since the 1930s, when Eduardo Brito became the first to sing the Dominican national music there. In 1967, Joseíto Mateo, Alberto Beltrán, and Primitivo Santos took merengue to Madison Square Garden for the first time. By the 1980s merengue was so big in New York City it was dominating salsa on the radio.  '))
gpt.add_example(
    Example('What role does merengue play in dominican identity?', 'The merengue is considered part of the national identity of the Dominican community. It plays an active role in various aspects of people’s daily lives – from their education to social gatherings and celebrations, even political campaigning. In 2005, the traditional practice was recognised by presidential decree with November 26 declared National Merengue Day. Merengue festivals are held in cities in the Dominican Republic like Santo Domingo and Puerto Plata every year.'))
gpt.add_example(Example(
    'Is there a similarity between the Dominican merengue and the Haitian meringue?', 'Influenced by Spanish decema and plena, merengue can be considered a close cousin of the Haitian "meringue," a musical genre sung in Creole but with a slower tempo and more sentimental melody. This is likely because both styles emerged because of the slave trade of their respective regions, which integrated large swaths of African prisoners with the culture of their new homes.'))

gpt.add_example(Example('Who is Juan Luis Guerra and what characterizes his music?',
                        "Drawing on influences ranging from the Beatles, American rock, folk, r&b, jazz, and traditional Dominican music, Guerra features his rich tenor voice and agile guitar work with sophisticated backing vocals for a new take on merengue. Guerra's merengues are characterized by breakneck tempos, lightening-fast horn lines and jabs, and highly polished productions. While Guerra's music is great for dancing, those listening closely to the words will be rewarded for the effort with his poetic imagery and thoughtful commentary on a range of contemporary subjects."))
gpt.add_example(Example('What is the most popular music in Haiti? What are its characteristics?',
                        "Kompa is the most popular music in Haiti, known as Haiti's national music. Kompa is characterized by several elements: its steady brass orchestra, which maintains a danceable beat, a big band feel, and a solid melody; its space for musical improvisation over the orchestral backbone; and its spicy Latin-esque rhythm. Generally, in instrumental compas direct, a sultry saxophone is the leading voice – it aims to tell a piercing yet captivating story. Lyrics for konpa dirèk are normally written in any of the languages of Haiti or the neighboring Caribbean islands: Creole, French, Spanish, English, or Portuguese."))

gpt.add_example(Example('What is the most popular music in Haiti? What are its characteristics?',
                        "Kompa is the most popular music in Haiti, known as Haiti's national music. Kompa is characterized by several elements: its steady brass orchestra, which maintains a danceable beat, a big band feel, and a solid melody; its space for musical improvisation over the orchestral backbone; and its spicy Latin-esque rhythm. Generally, in instrumental compas direct, a sultry saxophone is the leading voice – it aims to tell a piercing yet captivating story. Lyrics for konpa dirèk are normally written in any of the languages of Haiti or the neighboring Caribbean islands: Creole, French, Spanish, English, or Portuguese. Kompa makes use of the tambour and conga instruments, which gives Kompa its own unique style and taste. What also gives Kompa its unique style is the fact that its mixed between African Vodun music along with Western and Catholic influences as well."))
gpt.add_example(Example('Tell me about Marc Anthony and his influence on Salsa Romantica in New York and the US',
                        "Born in 1968 to Puerto Rican parents, Marco Antonio Muñiz, known professionally as Marc Anthony, grew up in East Harlem. Together, the three albums, Otra Nota, Todo a Su Tiempo, and Contra La Corriente, established Marc Anthony as one of the top-selling singer in the history of Salsa, able to sell out Madison Square Garden and prestigious venues internationally. The two-time Grammy Award and five-time Latin Grammy Award winner has sold over 12 million albums worldwide. According to Anthony, renowned Puerto Rican percussionist and bandleader Tito Puente in particular wielded a profound personal and professional influence throughout his life. "))

gpt.add_example(Example('Who is La India in the world of Salsa music?',
                        "La India was born on March 9, 1969 as Linda Viera Caballero in Río Piedras, Puerto Rico, and raised in the Bronx, New York City, USA. Known as  'The Princess Of Salsa' garnering three Grammy Award and two Latin Grammy Award nominations, La India is perhaps the most famous female salsa singer and songwriter."))



# Define UI configuration
config = UIConfig(description="NYC Carribbean Music Virtual Tour AI Powered Chat Assistant. Built by Jaidev Shah",
                  button_text="Answer",
                  placeholder="Who was Tito Puente and what his influence on the music of New York?")

demo_web_app(gpt, config)
