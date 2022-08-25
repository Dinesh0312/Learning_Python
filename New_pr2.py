str1="""vm6# show ip routes vpn 1 | tab
ADDRESS PATH PROTOCOL NEXTHOP NEXTHOP NEXTHOP
VPN FAMILY PREFIX ID PROTOCOL SUB TYPE METRIC IFNAME ADDR TLOC IP COLOR ENCAP VPN STATUS
--------------------------------------------------------------------------------------------------------------------------------------------------
1 ipv4 0.0.0.0/0 0 nat - 0 ge0/0 - - - - 0 F,S
1 ipv4 0.0.0.0/0 1 nat - 0 ge0/1 - - - - 0 F,S
1 ipv4 172.16.11.0/24 0 omp - 0 - - 172.16.255.15 mpls ipsec - F,S
1 ipv4 172.16.11.0/24 1 omp - 0 - - 172.16.255.15 public-internet ipsec - F,S
1 ipv4 172.16.21.0/24 0 bgp - 0 - - 172.16.21.1 - - - - I
1 ipv4 172.16.21.0/24 1 connected - 0 ge0/2.101 - - - - - F,S
1 ipv4 172.16.31.0/24 0 omp - 0 - - 172.16.255.14 mpls ipsec - F,S
1 ipv4 172.16.31.0/24 1 omp - 0 - - 172.16.255.14 public-internet ipsec - F,S
1 ipv4 172.16.41.0/24 0 omp - 0 - - 172.16.255.11 mpls ipsec - F,S
1 ipv4 172.16.41.0/24 1 omp - 0 - - 172.16.255.11 public-internet ipsec - F,S
1 ipv4 192.168.11.0/24 0 omp - 0 - - 172.16.255.15 mpls ipsec - F,S
1 ipv4 192.168.11.0/24 1 omp - 0 - - 172.16.255.15 public-internet ipsec - F,S
1 ipv4 192.168.21.0/24 0 bgp e 0 ge0/2.101 172.16.21.1 - - - - F,S
1 ipv4 192.168.31.0/24 0 omp - 0 - - 172.16.255.14 mpls ipsec - F,S
1 ipv4 192.168.31.0/24 1 omp - 0 - - 172.16.255.14 public-internet ipsec - F,S
1 ipv4 192.168.41.0/24 0 omp - 0 - - 172.16.255.11 mpls ipsec - F,S
1 ipv4 192.168.41.0/24 1 omp - 0 - - 172.16.255.11 public-internet ipsec - F,S
"""

str1 = str1.split('\n')

for i in str1[4:-1]:
    x = i.split()
    print(x[9])
