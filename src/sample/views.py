from pyramid.view import view_config
import subprocess
import re


@view_config(route_name='hello', renderer='templates/hello.pt')
def hello_world(request):
    """Main applicaiton view"""
    
    output = subprocess.check_output('pip list', shell=True)
    output = output.decode('ascii')
    output = output.split('\n')

    version = '' 
    for item in output:
        if item.startswith('data-analysis'):
            version = re.match('data-analysis \((.*)\)', item).groups()[0]

    extra_libs = [lib for lib in output if (
        not lib.startswith('sample-app') and
        not lib.startswith('data-analysis')
        and lib
    )]
        
    return {'libs':extra_libs, 'data_analysis_version':version}
