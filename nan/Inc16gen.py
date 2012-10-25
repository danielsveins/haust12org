""" Intended for generating code for Inc16.hdl"""
for x in xrange(1, 16):
    print "FullAdder(a=in[%d], b=false, c=carry%d, sum=out[%d], carry=carry%d);" % (x,x-1,x,x)
