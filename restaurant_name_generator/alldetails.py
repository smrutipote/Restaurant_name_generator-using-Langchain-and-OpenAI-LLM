import os
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
os.environ['OPENAI_API_KEY']='sk-'
llm=OpenAI(temperature=0.6)
def  restaurant_generator(cuisine):
    prompt_template_name=PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food.suggest a fancy name for this '
    )
    prompt_template_items=PromptTemplate(
        input_variables=['restaurant_name'],
        template = 'Suggest me menu items for {restaurant_name},return it as separated string '
    )

    chain_name=LLMChain(llm=llm,prompt=prompt_template_name,output_key='restaurant_name')
    chain_items=LLMChain(llm=llm,prompt=prompt_template_items,output_key='menu_items')
    chaining=SequentialChain(chains=[chain_name,chain_items],input_variables=['cuisine'],output_variables=['restaurant_name','menu_items'])

    reply=chaining({'cuisine':'cuisine'})
    return reply

# if __name__ == '__main__':
#     print(restaurant_generator('Chinese'))