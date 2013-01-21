## compile shellsort.f to produce a f2py binary module.
def main(optimization=3, aargs=[], filename ='shellsort.f', outbin='sort'):
    """
    Arguments
    =========
    optimization = 0, 1, 2, 3
    aargs = [] addition of non-default arguments.
    filename='*.f'
    outbin='evpsc_f2py'
    """
    args = ['-finit-local-zero','-fno-automatic','-g','-Wall',
            '-fno-align-commons','-finit-integer=zero', '-fbackslash',
            '-finit-real=zero','-fdefault-double-8','-fdefault-real-8']

    for i in range(len(aargs)):
        args.append(aargs[i])

    print 'Automatic python script for compilation of f2py-wrapped EVPSC Fortran code'
    print 'for an interactive python environment.\n'

    print 'Arguments for the fixed gfortran compiler are:'

    for a in args:
        print a

    import os
    if os.name!='posix':
        print "This script is for posix systems: Unix, Linux, and Mac."
        return -1
    cmp_path = os.popen('which gfortran').readline().split('\n')[0]
    cmd = "f2py -c --f90exec='%s' --f77exec='%s' "%(cmp_path, cmp_path)

    ## flags ---
    cmd = cmd+"--f77flags='"
    for s in args:
        cmd = cmd+'%s '%s

    cmd = cmd + "-O%i"%optimization
    cmd = cmd + "' "

    cmd = cmd+"--f90flags='"
    for s in args:
        cmd = cmd+'%s '%s

    cmd = cmd + "-O%i"%optimization
    cmd = cmd + "' "
    ## ----
    cmd = cmd + "-m %s %s"%(outbin, filename)

    print "%s > f2py_cmp_temp"%cmd

    iflag = os.system("%s > f2py_cmp_temp"%cmd)

    ## remove the exsiting binary
    try: os.remove('%s'%outbin)
    except: pass
    ##

    if iflag!=0:
        print iflag
        print 'Compilation error, got %i'%iflag
        return -1
    else: return 0

if __name__=='__main__':
    import getopt, sys, os
    try: opts, args = getopt.getopt(sys.argv[1:],'bo:')
    except getopt.GetoptError, err: print str(err); sys.exit(2)

    run = False
    aargs = []
    optimization = 3
    exefn = 'evpsc'

    for o, a in opts:
        if o=='-b': aargs.append('-fbounds-check')
        elif o=='-o': optimization=int(a)

    iflag =  main(aargs = aargs, optimization=optimization, outbin='sort')

    if iflag!=0: raise IOError, 'Not successful compilation.'
    if run: os.system('./%s'%exefn)

