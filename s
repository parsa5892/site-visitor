Help on function send in module scapy.sendrecv:

sseenndd(x, iface=None, **kargs)
    Send packets at layer 3
    
    :param x: the packets
    :param inter: time (in s) between two packets (default 0)
    :param loop: send packet indefinetly (default 0)
    :param count: number of packets to send (default None=1)
    :param verbose: verbose mode (default None=conf.verbose)
    :param realtime: check that a packet was sent before sending the next one
    :param return_packets: return the sent packets
    :param socket: the socket to use (default is conf.L3socket(kargs))
    :param iface: the interface to send the packets on
    :param monitor: (not on linux) send in monitor mode
    :returns: None
