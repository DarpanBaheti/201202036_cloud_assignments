from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections                                                                   
from mininet.node import Controller, RemoteController, OVSController, CPULimitedHost
from mininet.cli import CLI
from mininet.link import TCIntf, TCLink
import os                                                               

class MyTopo( Topo ):

    def __init__( self, snum, hnum ):

        Topo.__init__( self )
        swi = {}
        hos = {}
        snum = int(snum)
        hnum = int(hnum)
        for x in xrange(snum):
            s = self.addSwitch("s" +str(x+1))
            swi[x+1]= s

        for x in xrange(hnum):
            h = self.addHost("h" +str(x+1))
            hos[x+1]= h

        
        for x in xrange(snum):
            for y in xrange(x):
                self.addLink(swi[x+1],swi[y+1])

        sph = hnum/snum
        sin = swi.keys()
        skey = sin*int(hnum/snum)
        #print skey
        tmp = sin[:(hnum%snum)]
        #print tmp
        skey = skey + tmp
        skey.sort()
        #print skey
        i = 1
        for x in skey:
            self.addLink(swi[x], hos[i],bw=((x%2)+1))
            i = i+1

def testTopo(snum,hnum):
    topo = MyTopo(snum, hnum)
    net = Mininet(topo, link=TCLink, controller=RemoteController)
    net.start()
    net.addController('c0', controller=RemoteController,ip="127.0.0.1",port=6633)
    for x in xrange(hnum):
        for y in xrange(hnum):
            if x%2==0 and y%2==1:
                net.nameToNode["h"+str(x+1)].cmd("iptables -A OUTPUT -o h"+str(x+1)+"-eth0 -d 10.0.0."+ str(y+1)+" -j DROP")
    dumpNodeConnections(net.switches)
    CLI(net)

if __name__ == '__main__':
    snum = int(raw_input("Number of Switches : "))
    hnum = int(raw_input("Number of Hosts : "))
    topos = { 'mytopo': ( lambda: MyTopo( snum, hnum) ) }
    testTopo(snum, hnum)