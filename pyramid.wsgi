from pyramid.paster import get_app, setup_logging
ini_path = '/Users/kteague/buildouts/sample-app-env/production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
