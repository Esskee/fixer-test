# import pip
# package_name = 'mypy'
#
# pip.main(['install', package_name])
import multiprocessing as mp
from app import create_app

app = create_app()

if __name__ == "__main__":
    mp.set_start_method('spawn')
    #server.run(host='0.0.0.0', port='8080')
    app.run_server(host='0.0.0.0', port='8081', debug=True)
