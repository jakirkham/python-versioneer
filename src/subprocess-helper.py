
import subprocess

def run_command(args, cwd=None, verbose=False):
    try:
        p = subprocess.Popen(list(args), stdout=subprocess.PIPE, cwd=cwd)
    except EnvironmentError, e:
        if verbose:
            print "unable to run %s" % args[0]
            print e
        return None
    stdout = p.communicate()[0].strip()
    if p.returncode != 0:
        if verbose:
            print "unable to run %s (error)" % args[0]
        return None
    return stdout
