**alexa-reply : 0.1.2**

**About** : An ai python package to respond to any message suitably. 

**PyPI repo** : https://pypi.org/project/alexa-reply/

**Installation**: 
```cmd
# from github : unstable

pip install git+https://pypi.org/project/alexa-reply/
```

```cmd
# from github : stable

pip install alexa-reply
```

**Example Usage**:
```py
from alexa_reply import reply

owner = "your name"

bot =  "bot's name"

message = "the message u wanna reply to"

resp = reply(message, bot, owner)

print(resp)```