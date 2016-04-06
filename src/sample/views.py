from pyramid.view import view_config

@view_config(route_name='hello', renderer='templates/hello.pt')
def request_reset_view(request):
    """Request password reset form"""
    return {}

