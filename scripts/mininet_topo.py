from mininet.topo import Topo
from mininet.net import Mininet

def test_connectivity(net):
    print("Testing connectivity between hosts...")
    for host_src in net.hosts:
        for host_dst in net.hosts:
            if host_src != host_dst:
                result = host_src.cmd('ping -c 3', host_dst.IP())
                print(f"{host_src.name} -> {host_dst.name}:")
                print(result)

net = Mininet()

# Creating nodes in the network.
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')

# Creating links between nodes in network (2-ways)
net.addLink(h0, s0)
net.addLink(h1, s0)

# Configuration of IP Addresses in interfaces
h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)

net.start()

# Testing connectivity
test_connectivity(net)

net.stop()
