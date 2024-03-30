# %%
#cashing
#cash를 사용하면 LM의 응답을 저장할 수 있다.
#만약 어떤 질문에 대해 LLM이 항상 같은 답변을 내놓는다면 캐싱을 이용해서 저장해둔 답을
#재사용할 수 있어 비용을 절감한다.
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.globals import set_llm_cache, set_debug
from langchain.cache import InMemoryCache, SQLiteCache
                            # 메모리에 캐시 vs DB에 캐시
set_llm_cache(SQLiteCache("cache.db")) #database path를 제공해야함.   
# set_llm_cache(InMemoryCache()) # 이것만으로 모든 reponse가 메모리에 저장됨
# set_debug(True)  # predict시 프롬프트와 함께 진행상황, 로그 등을 보여줌
                 # 디버그시 사용한다.

chat = ChatOpenAI(
    # model_name="gpt-3.5-turbo",
     temperature=0.1,
    # streaming=True,
    # callbacks=[StreamingStdOutCallbackHandler()],
)

chat.predict("How do you make italian pasta")



# %%
chat.predict("How do you make italian pasta")


