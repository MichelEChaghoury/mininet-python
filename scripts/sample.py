from mininet.net import Mininet
from mininet.topo import LinearTopo

linear = LinearTopo(k=4)
net = Mininet(topo=linear)

net.start()
net.pingAll()
net.stop()