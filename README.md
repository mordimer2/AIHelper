# AIHelper
Speech to text -> text to OpenAI GPT-3 model -> text to speech 

# Assumptions
1. Continuously listening to a speech in a room
2. Whenever I want to ask something speech to text will send it to chatGPT and return its answer
3. Speech-to-text module would read the response aloud so that I don't need to stop my work
4. Additionally there is conversation history in case of some code would be returned to easy copy-paste

# Is it done?
Technically yes. the GPT-3 model has mostly perfect answers for simple questions, but the speech recognition AI (especially free ones) isn't that great. I've tested a few of them and google recognition is so far the best, but still far enough from what I imagined when starting. 
I may resume this project in the future. There needs to be either better speech AI for free or I will simply earn more to have a not-so-cost-effective AI helper.

# How does it work?
1. Fork or download the repo
2. Rename config.ini.sample to config.ini and insert a GPT3 api key (https://platform.openai.com/account/api-keys)
The GPT3 model is not free but you gain 18 dollars to spend after registration.
3. Simply run main.py. The listener will listen for 17 seconds, then send a text to GPT3 and read aloud the response.

I haven't made any changeable configurations like the maximum limit of GPT3 tokens (https://openai.com/api/pricing/#faq-token), but to be fair I didn't even consider you can read this paragraph, so I didn't put many thoughts in this.
