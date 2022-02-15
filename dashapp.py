from app import create_app
import multiprocessing as mp
# import pip
# package_name = 'pytest-cov'
#
# pip.main(['install', package_name])

app = create_app()

if __name__ == "__main__":
    mp.set_start_method('spawn')
    #server.run(host='0.0.0.0', port='8080')
    app.run_server(host='0.0.0.0', port='8081', debug=True)
