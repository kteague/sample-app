from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    # framework
    config = Configurator(settings=settings,)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    # routes
    config.add_route('hello', '/')
    
    config.scan()
    return config.make_wsgi_app()
