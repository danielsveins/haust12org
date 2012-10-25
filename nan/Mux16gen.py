""" for x in xrange(0, 16):

{And(a=a[%d], b=notsel, out=s%d);
And(a=b[%d], b=sel, out=t%d);
Or(a=s%d,b=t%d, out=out[%d]);
"""

for x in xrange(0, 16):
    print "And(a=a[%d], b=notsel, out=s%d);" % (x,x)
    print "And(a=b[%d], b=sel, out=t%d);" % (x,x)
    print "Or(a=s%d,b=t%d, out=out[%d]);" % (x,x,x)



    
