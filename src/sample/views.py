from pyramid.view import view_config
import subprocess

@view_config(route_name='hello', renderer='templates/hello.pt')
def request_reset_view(request):
    """Request password reset form"""
    
    output = subprocess.check_output('pip list', shell=True)
    output = output.decode('ascii')
    output = output.split('\n')
    output = [lib for lib in output if (not lib.startswith('sample-app') and lib)]
    
    return {'libs':output}

