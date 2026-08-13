# @ohos.net.connection

Provides interfaces to manage and use data networks.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace connection--><!--Device-unnamed-declare namespace connection-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addCustomDnsRule](arkts-network-connection-addcustomdnsrule-f.md#addCustomDnsRule) |
| [addCustomDnsRule](arkts-network-connection-addcustomdnsrule-f.md#addCustomDnsRule) |
| [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md#clearCustomDnsRules) |
| [clearCustomDnsRules](arkts-network-connection-clearcustomdnsrules-f.md#clearCustomDnsRules) |
| [createNetConnection](arkts-network-connection-createnetconnection-f.md#createNetConnection) |
| [findProxyForUrl](arkts-network-connection-findproxyforurl-f.md#findProxyForUrl) |
| [getAddressesByName](arkts-network-connection-getaddressesbyname-f.md#getAddressesByName) |
| [getAddressesByName](arkts-network-connection-getaddressesbyname-f.md#getAddressesByName) |
| [getAddressesByNameWithOptions](arkts-network-connection-getaddressesbynamewithoptions-f.md#getAddressesByNameWithOptions) |
| [getAllNets](arkts-network-connection-getallnets-f.md#getAllNets) |
| [getAllNets](arkts-network-connection-getallnets-f.md#getAllNets) |
| [getAllNetsSync](arkts-network-connection-getallnetssync-f.md#getAllNetsSync) |
| [getAppNet](arkts-network-connection-getappnet-f.md#getAppNet) |
| [getAppNet](arkts-network-connection-getappnet-f.md#getAppNet) |
| [getAppNetSync](arkts-network-connection-getappnetsync-f.md#getAppNetSync) |
| [getConnectOwnerUid](arkts-network-connection-getconnectowneruid-f.md#getConnectOwnerUid) |
| [getConnectOwnerUidSync](arkts-network-connection-getconnectowneruidsync-f.md#getConnectOwnerUidSync) |
| [getConnectionProperties](arkts-network-connection-getconnectionproperties-f.md#getConnectionProperties) |
| [getConnectionProperties](arkts-network-connection-getconnectionproperties-f.md#getConnectionProperties) |
| [getConnectionPropertiesSync](arkts-network-connection-getconnectionpropertiessync-f.md#getConnectionPropertiesSync) |
| [getDefaultHttpProxy](arkts-network-connection-getdefaulthttpproxy-f.md#getDefaultHttpProxy) |
| [getDefaultHttpProxy](arkts-network-connection-getdefaulthttpproxy-f.md#getDefaultHttpProxy) |
| [getDefaultNet](arkts-network-connection-getdefaultnet-f.md#getDefaultNet) |
| [getDefaultNet](arkts-network-connection-getdefaultnet-f.md#getDefaultNet) |
| [getDefaultNetSync](arkts-network-connection-getdefaultnetsync-f.md#getDefaultNetSync) |
| [getDnsAscii](arkts-network-connection-getdnsascii-f.md#getDnsAscii) |
| [getDnsUnicode](arkts-network-connection-getdnsunicode-f.md#getDnsUnicode) |
| [getIpNeighTable](arkts-network-connection-getipneightable-f.md#getIpNeighTable) |
| [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md#getNetCapabilities) |
| [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md#getNetCapabilities) |
| [getNetCapabilitiesSync](arkts-network-connection-getnetcapabilitiessync-f.md#getNetCapabilitiesSync) |
| [getNetExtAttribute](arkts-network-connection-getnetextattribute-f.md#getNetExtAttribute) |
| [getNetExtAttributeSync](arkts-network-connection-getnetextattributesync-f.md#getNetExtAttributeSync) |
| [getPacFileUrl](arkts-network-connection-getpacfileurl-f.md#getPacFileUrl) |
| [getPacUrl](arkts-network-connection-getpacurl-f.md#getPacUrl) |
| [getSystemNetPortStates](arkts-network-connection-getsystemnetportstates-f.md#getSystemNetPortStates) |
| [hasDefaultNet](arkts-network-connection-hasdefaultnet-f.md#hasDefaultNet) |
| [hasDefaultNet](arkts-network-connection-hasdefaultnet-f.md#hasDefaultNet) |
| [hasDefaultNetSync](arkts-network-connection-hasdefaultnetsync-f.md#hasDefaultNetSync) |
| [isDefaultNetMetered](arkts-network-connection-isdefaultnetmetered-f.md#isDefaultNetMetered) |
| [isDefaultNetMetered](arkts-network-connection-isdefaultnetmetered-f.md#isDefaultNetMetered) |
| [isDefaultNetMeteredSync](arkts-network-connection-isdefaultnetmeteredsync-f.md#isDefaultNetMeteredSync) |
| [queryProbeResult](arkts-network-connection-queryproberesult-f.md#queryProbeResult) |
| [queryTraceRoute](arkts-network-connection-querytraceroute-f.md#queryTraceRoute) |
| [refreshGlobalHttpProxy](arkts-network-connection-refreshglobalhttpproxy-f.md#refreshGlobalHttpProxy) |
| [removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md#removeCustomDnsRule) |
| [removeCustomDnsRule](arkts-network-connection-removecustomdnsrule-f.md#removeCustomDnsRule) |
| [reportNetConnected](arkts-network-connection-reportnetconnected-f.md#reportNetConnected) |
| [reportNetConnected](arkts-network-connection-reportnetconnected-f.md#reportNetConnected) |
| [reportNetDisconnected](arkts-network-connection-reportnetdisconnected-f.md#reportNetDisconnected) |
| [reportNetDisconnected](arkts-network-connection-reportnetdisconnected-f.md#reportNetDisconnected) |
| [setAppHttpProxy](arkts-network-connection-setapphttpproxy-f.md#setAppHttpProxy) |
| [setAppNet](arkts-network-connection-setappnet-f.md#setAppNet) |
| [setAppNet](arkts-network-connection-setappnet-f.md#setAppNet) |
| [setNetExtAttribute](arkts-network-connection-setnetextattribute-f.md#setNetExtAttribute) |
| [setNetExtAttributeSync](arkts-network-connection-setnetextattributesync-f.md#setNetExtAttributeSync) |
| [setPacFileUrl](arkts-network-connection-setpacfileurl-f.md#setPacFileUrl) |
| [setPacUrl](arkts-network-connection-setpacurl-f.md#setPacUrl) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addVlanIp](arkts-network-connection-addvlanip-f-sys.md#addVlanIp-(System-API)) |
| [createVlanInterface](arkts-network-connection-createvlaninterface-f-sys.md#createVlanInterface-(System-API)) |
| [deleteVlanIp](arkts-network-connection-deletevlanip-f-sys.md#deleteVlanIp-(System-API)) |
| [destroyVlanInterface](arkts-network-connection-destroyvlaninterface-f-sys.md#destroyVlanInterface-(System-API)) |
| [disableAirplaneMode](arkts-network-connection-disableairplanemode-f-sys.md#disableAirplaneMode-(System-API)) |
| [disableAirplaneMode](arkts-network-connection-disableairplanemode-f-sys.md#disableAirplaneMode-(System-API)) |
| [enableAirplaneMode](arkts-network-connection-enableairplanemode-f-sys.md#enableAirplaneMode-(System-API)) |
| [enableAirplaneMode](arkts-network-connection-enableairplanemode-f-sys.md#enableAirplaneMode-(System-API)) |
| [factoryReset](arkts-network-connection-factoryreset-f-sys.md#factoryReset-(System-API)) |
| [getGlobalHttpProxy](arkts-network-connection-getglobalhttpproxy-f-sys.md#getGlobalHttpProxy-(System-API)) |
| [getGlobalHttpProxy](arkts-network-connection-getglobalhttpproxy-f-sys.md#getGlobalHttpProxy-(System-API)) |
| [getProxyMode](arkts-network-connection-getproxymode-f-sys.md#getProxyMode-(System-API)) |
| [setGlobalHttpProxy](arkts-network-connection-setglobalhttpproxy-f-sys.md#setGlobalHttpProxy-(System-API)) |
| [setGlobalHttpProxy](arkts-network-connection-setglobalhttpproxy-f-sys.md#setGlobalHttpProxy-(System-API)) |
| [setInterfaceUp](arkts-network-connection-setinterfaceup-f-sys.md#setInterfaceUp-(System-API)) |
| [setProxyMode](arkts-network-connection-setproxymode-f-sys.md#setProxyMode-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionProperties](arkts-network-connection-connectionproperties-i.md) |
| [HttpProxy](arkts-network-connection-httpproxy-i.md) |
| [LinkAddress](arkts-network-connection-linkaddress-i.md) |
| [NetAddress](arkts-network-connection-netaddress-i.md) |
| [NetBlockStatusInfo](arkts-network-connection-netblockstatusinfo-i.md) |
| [NetCapabilities](arkts-network-connection-netcapabilities-i.md) |
| [NetCapabilityInfo](arkts-network-connection-netcapabilityinfo-i.md) |
| [NetConnection](arkts-network-connection-netconnection-i.md) |
| [NetConnectionPropertyInfo](arkts-network-connection-netconnectionpropertyinfo-i.md) |
| [NetHandle](arkts-network-connection-nethandle-i.md) |
| [NetIpMacInfo](arkts-network-connection-netipmacinfo-i.md) |
| [NetPortStatesInfo](arkts-network-connection-netportstatesinfo-i.md) |
| [NetSpecifier](arkts-network-connection-netspecifier-i.md) |
| [ProbeResultInfo](arkts-network-connection-proberesultinfo-i.md) |
| [QueryOptions](arkts-network-connection-queryoptions-i.md) |
| [RouteInfo](arkts-network-connection-routeinfo-i.md) |
| [Socks5Proxy](arkts-network-connection-socks5proxy-i.md) |
| [TcpNetPortStatesInfo](arkts-network-connection-tcpnetportstatesinfo-i.md) |
| [TraceRouteInfo](arkts-network-connection-tracerouteinfo-i.md) |
| [TraceRouteOptions](arkts-network-connection-tracerouteoptions-i.md) |
| [UdpNetPortStatesInfo](arkts-network-connection-udpnetportstatesinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConversionProcess](arkts-network-connection-conversionprocess-e.md) |
| [FamilyType](arkts-network-connection-familytype-e.md) |
| [NetBearType](arkts-network-connection-netbeartype-e.md) |
| [NetCap](arkts-network-connection-netcap-e.md) |
| [PacketsType](arkts-network-connection-packetstype-e.md) |
| [ProtocolType](arkts-network-connection-protocoltype-e.md) |
| [Socks5DnsStrategy](arkts-network-connection-socks5dnsstrategy-e.md) |
| [TcpState](arkts-network-connection-tcpstate-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProxyMode](arkts-network-connection-proxymode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [HttpRequest](arkts-network-connection-httprequest-t.md) |
| [TCPSocket](arkts-network-connection-tcpsocket-t.md) |
| [UDPSocket](arkts-network-connection-udpsocket-t.md) |
