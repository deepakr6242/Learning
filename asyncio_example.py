import asyncio

def bar(*args):
    if args[0]%2==0:
         import time
         time.sleep(30)
         return ('slept for {args[0]}')
    else:
        return('awoke')
   
async def foo():
    loop = asyncio.get_event_loop()
    
    tasks = [loop.run_in_executor(None,bar,i) for i in range(10)]
    # print(tasks)
    for i in tasks:
        print(i,i.done())
        
    done, pending = await asyncio.wait(tasks,
                                       return_when=asyncio.FIRST_COMPLETED)
    for coro in done:
        print(await coro)
    for coro in pending:
       print(await coro)
    # print(pending)
    # for response in await asyncio.gather(*tasks):
    #     print(response)
    
    
    
if  __name__=="__main__":
    asyncio.run(foo())
