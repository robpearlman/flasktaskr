#run.py 

#from views import app
#app.run()#debug=True

# run.py


import os

from app import app
app.run(debug=True)
#port = int(os.environ.get('PORT', 5000))
#app.run(host='0.0.0.0', port=port, debug=True) 

