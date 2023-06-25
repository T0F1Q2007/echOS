# echOS
A new Operating System that uses python.

version 0.13d : Online updating future added.

version 0.14 : Some changes.

version 0.15p : Changing the main(opened) directory.

--------------------------------------------------------
<h1>Download with python</h1>

import requests
location = os.getcwd()
link="https://raw.githubusercontent.com/T0F1Q2007/echOS/main/echOS.py"
path=os.path.join(location,"echOS.py")
echOs_py = requests.get(link)
with open(path, 'wb') as file:
	file.write(echOs_py.content)
