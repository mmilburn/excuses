from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
while True:
    print("Please excuse me from: ", end="")
    obligation = input().strip()
    print()
    excuse = remote_chain.invoke({"text": obligation})
    print(excuse)
