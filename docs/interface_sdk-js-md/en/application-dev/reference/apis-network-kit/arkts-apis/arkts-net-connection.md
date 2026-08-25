# @ohos.net.connection(Network Connection Management)

The network connection management module provides basic network management capabilities. You can obtain the default active network, the list of all active networks, and network capability information.

> **NOTE：**&gt;
> Unless otherwise specified, the APIs of this module do not support concurrent calls.

**Since:** 8

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCustomDnsRule(Network Connection Management)](arkts-network-connection-addcustomdnsrule-f.md) |
| [addCustomDnsRule(Network Connection Management)](arkts-network-connection-addcustomdnsrule-f.md) |
| [clearCustomDnsRules(Network Connection Management)](arkts-network-connection-clearcustomdnsrules-f.md) |
| [clearCustomDnsRules(Network Connection Management)](arkts-network-connection-clearcustomdnsrules-f.md) |
| [createNetConnection(Network Connection Management)](arkts-network-connection-createnetconnection-f.md) |
| [findProxyForUrl(Network Connection Management)](arkts-network-connection-findproxyforurl-f.md) |
| [getAddressesByName(Network Connection Management)](arkts-network-connection-getaddressesbyname-f.md) |
| [getAddressesByName(Network Connection Management)](arkts-network-connection-getaddressesbyname-f.md) |
| [getAddressesByNameWithOptions(Network Connection Management)](arkts-network-connection-getaddressesbynamewithoptions-f.md) |
| [getAllNets(Network Connection Management)](arkts-network-connection-getallnets-f.md) |
| [getAllNets(Network Connection Management)](arkts-network-connection-getallnets-f.md) |
| [getAllNetsSync(Network Connection Management)](arkts-network-connection-getallnetssync-f.md) |
| [getAppNet(Network Connection Management)](arkts-network-connection-getappnet-f.md) |
| [getAppNet(Network Connection Management)](arkts-network-connection-getappnet-f.md) |
| [getAppNetSync(Network Connection Management)](arkts-network-connection-getappnetsync-f.md) |
| [getConnectionProperties(Network Connection Management)](arkts-network-connection-getconnectionproperties-f.md) |
| [getConnectionProperties(Network Connection Management)](arkts-network-connection-getconnectionproperties-f.md) |
| [getConnectionPropertiesSync(Network Connection Management)](arkts-network-connection-getconnectionpropertiessync-f.md) |
| [getConnectOwnerUid(Network Connection Management)](arkts-network-connection-getconnectowneruid-f.md) |
| [getConnectOwnerUidSync(Network Connection Management)](arkts-network-connection-getconnectowneruidsync-f.md) |
| [getDefaultHttpProxy(Network Connection Management)](arkts-network-connection-getdefaulthttpproxy-f.md) |
| [getDefaultHttpProxy(Network Connection Management)](arkts-network-connection-getdefaulthttpproxy-f.md) |
| [getDefaultNet(Network Connection Management)](arkts-network-connection-getdefaultnet-f.md) |
| [getDefaultNet(Network Connection Management)](arkts-network-connection-getdefaultnet-f.md) |
| [getDefaultNetSync(Network Connection Management)](arkts-network-connection-getdefaultnetsync-f.md) |
| [getDnsAscii(Network Connection Management)](arkts-network-connection-getdnsascii-f.md) |
| [getDnsUnicode(Network Connection Management)](arkts-network-connection-getdnsunicode-f.md) |
| [getIpNeighTable(Network Connection Management)](arkts-network-connection-getipneightable-f.md) |
| [getNetCapabilities(Network Connection Management)](arkts-network-connection-getnetcapabilities-f.md) |
| [getNetCapabilities(Network Connection Management)](arkts-network-connection-getnetcapabilities-f.md) |
| [getNetCapabilitiesSync(Network Connection Management)](arkts-network-connection-getnetcapabilitiessync-f.md) |
| [getNetExtAttribute(Network Connection Management)](arkts-network-connection-getnetextattribute-f.md) |
| [getNetExtAttributeSync(Network Connection Management)](arkts-network-connection-getnetextattributesync-f.md) |
| [getPacFileUrl(Network Connection Management)](arkts-network-connection-getpacfileurl-f.md) |
| [getPacUrl(Network Connection Management)](arkts-network-connection-getpacurl-f.md) |
| [getSystemNetPortStates(Network Connection Management)](arkts-network-connection-getsystemnetportstates-f.md) |
| [hasDefaultNet(Network Connection Management)](arkts-network-connection-hasdefaultnet-f.md) |
| [hasDefaultNet(Network Connection Management)](arkts-network-connection-hasdefaultnet-f.md) |
| [hasDefaultNetSync(Network Connection Management)](arkts-network-connection-hasdefaultnetsync-f.md) |
| [isDefaultNetMetered(Network Connection Management)](arkts-network-connection-isdefaultnetmetered-f.md) |
| [isDefaultNetMetered(Network Connection Management)](arkts-network-connection-isdefaultnetmetered-f.md) |
| [isDefaultNetMeteredSync(Network Connection Management)](arkts-network-connection-isdefaultnetmeteredsync-f.md) |
| [queryProbeResult(Network Connection Management)](arkts-network-connection-queryproberesult-f.md) |
| [queryTraceRoute(Network Connection Management)](arkts-network-connection-querytraceroute-f.md) |
| [refreshGlobalHttpProxy(Network Connection Management)](arkts-network-connection-refreshglobalhttpproxy-f.md) |
| [removeCustomDnsRule(Network Connection Management)](arkts-network-connection-removecustomdnsrule-f.md) |
| [removeCustomDnsRule(Network Connection Management)](arkts-network-connection-removecustomdnsrule-f.md) |
| [reportNetConnected(Network Connection Management)](arkts-network-connection-reportnetconnected-f.md) |
| [reportNetConnected(Network Connection Management)](arkts-network-connection-reportnetconnected-f.md) |
| [reportNetDisconnected(Network Connection Management)](arkts-network-connection-reportnetdisconnected-f.md) |
| [reportNetDisconnected(Network Connection Management)](arkts-network-connection-reportnetdisconnected-f.md) |
| [setAppHttpProxy(Network Connection Management)](arkts-network-connection-setapphttpproxy-f.md) |
| [setAppNet(Network Connection Management)](arkts-network-connection-setappnet-f.md) |
| [setAppNet(Network Connection Management)](arkts-network-connection-setappnet-f.md) |
| [setNetExtAttribute(Network Connection Management)](arkts-network-connection-setnetextattribute-f.md) |
| [setNetExtAttributeSync(Network Connection Management)](arkts-network-connection-setnetextattributesync-f.md) |
| [setPacFileUrl(Network Connection Management)](arkts-network-connection-setpacfileurl-f.md) |
| [setPacUrl(Network Connection Management)](arkts-network-connection-setpacurl-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addVlanIp(Network Connection Management)](arkts-network-connection-addvlanip-f-sys.md) |
| [createVlanInterface(Network Connection Management)](arkts-network-connection-createvlaninterface-f-sys.md) |
| [deleteVlanIp(Network Connection Management)](arkts-network-connection-deletevlanip-f-sys.md) |
| [destroyVlanInterface(Network Connection Management)](arkts-network-connection-destroyvlaninterface-f-sys.md) |
| [disableAirplaneMode(Network Connection Management)](arkts-network-connection-disableairplanemode-f-sys.md) |
| [disableAirplaneMode(Network Connection Management)](arkts-network-connection-disableairplanemode-f-sys.md) |
| [enableAirplaneMode(Network Connection Management)](arkts-network-connection-enableairplanemode-f-sys.md) |
| [enableAirplaneMode(Network Connection Management)](arkts-network-connection-enableairplanemode-f-sys.md) |
| [factoryReset(Network Connection Management)](arkts-network-connection-factoryreset-f-sys.md) |
| [getGlobalHttpProxy(Network Connection Management)](arkts-network-connection-getglobalhttpproxy-f-sys.md) |
| [getGlobalHttpProxy(Network Connection Management)](arkts-network-connection-getglobalhttpproxy-f-sys.md) |
| [getProxyMode(Network Connection Management)](arkts-network-connection-getproxymode-f-sys.md) |
| [setGlobalHttpProxy(Network Connection Management)](arkts-network-connection-setglobalhttpproxy-f-sys.md) |
| [setGlobalHttpProxy(Network Connection Management)](arkts-network-connection-setglobalhttpproxy-f-sys.md) |
| [setInterfaceUp(Network Connection Management)](arkts-network-connection-setinterfaceup-f-sys.md) |
| [setProxyMode(Network Connection Management)](arkts-network-connection-setproxymode-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionProperties(Network Connection Management)](arkts-network-connection-connectionproperties-i.md) |
| [HttpProxy(Network Connection Management)](arkts-network-connection-httpproxy-i.md) |
| [LinkAddress(Network Connection Management)](arkts-network-connection-linkaddress-i.md) |
| [NetAddress(Network Connection Management)](arkts-network-connection-netaddress-i.md) |
| [NetBlockStatusInfo(Network Connection Management)](arkts-network-connection-netblockstatusinfo-i.md) |
| [NetCapabilities(Network Connection Management)](arkts-network-connection-netcapabilities-i.md) |
| [NetCapabilityInfo(Network Connection Management)](arkts-network-connection-netcapabilityinfo-i.md) |
| [NetConnection(Network Connection Management)](arkts-network-connection-netconnection-i.md) |
| [NetConnectionPropertyInfo(Network Connection Management)](arkts-network-connection-netconnectionpropertyinfo-i.md) |
| [NetHandle(Network Connection Management)](arkts-network-connection-nethandle-i.md) |
| [NetIpMacInfo(Network Connection Management)](arkts-network-connection-netipmacinfo-i.md) |
| [NetPortStatesInfo(Network Connection Management)](arkts-network-connection-netportstatesinfo-i.md) |
| [NetSpecifier(Network Connection Management)](arkts-network-connection-netspecifier-i.md) |
| [ProbeResultInfo(Network Connection Management)](arkts-network-connection-proberesultinfo-i.md) |
| [QueryOptions(Network Connection Management)](arkts-network-connection-queryoptions-i.md) |
| [RouteInfo(Network Connection Management)](arkts-network-connection-routeinfo-i.md) |
| [Socks5Proxy(Network Connection Management)](arkts-network-connection-socks5proxy-i.md) |
| [TcpNetPortStatesInfo(Network Connection Management)](arkts-network-connection-tcpnetportstatesinfo-i.md) |
| [TraceRouteInfo(Network Connection Management)](arkts-network-connection-tracerouteinfo-i.md) |
| [TraceRouteOptions(Network Connection Management)](arkts-network-connection-tracerouteoptions-i.md) |
| [UdpNetPortStatesInfo(Network Connection Management)](arkts-network-connection-udpnetportstatesinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConversionProcess(Network Connection Management)](arkts-network-connection-conversionprocess-e.md) |
| [FamilyType(Network Connection Management)](arkts-network-connection-familytype-e.md) |
| [NetBearType(Network Connection Management)](arkts-network-connection-netbeartype-e.md) |
| [NetCap(Network Connection Management)](arkts-network-connection-netcap-e.md) |
| [PacketsType(Network Connection Management)](arkts-network-connection-packetstype-e.md) |
| [ProtocolType(Network Connection Management)](arkts-network-connection-protocoltype-e.md) |
| [Socks5DnsStrategy(Network Connection Management)](arkts-network-connection-socks5dnsstrategy-e.md) |
| [TcpState(Network Connection Management)](arkts-network-connection-tcpstate-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProxyMode(Network Connection Management)](arkts-network-connection-proxymode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HttpRequest(Network Connection Management)](arkts-network-connection-httprequest-t.md) |
| [TCPSocket(Network Connection Management)](arkts-network-connection-tcpsocket-t.md) |
| [UDPSocket(Network Connection Management)](arkts-network-connection-udpsocket-t.md) |
