# @ohos.net.connection(网络连接管理)

网络连接管理提供管理网络一些基础能力，包括获取默认激活的网络、获取所有激活网络列表、获取网络能力信息等功能。

> **说明：**&gt;
> 无特殊说明，接口默认不支持并发。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addCustomDnsRule(网络连接管理)](arkts-network-connection-addcustomdnsrule-f.md) |
| [addCustomDnsRule(网络连接管理)](arkts-network-connection-addcustomdnsrule-f.md) |
| [clearCustomDnsRules(网络连接管理)](arkts-network-connection-clearcustomdnsrules-f.md) |
| [clearCustomDnsRules(网络连接管理)](arkts-network-connection-clearcustomdnsrules-f.md) |
| [createNetConnection(网络连接管理)](arkts-network-connection-createnetconnection-f.md) |
| [findProxyForUrl(网络连接管理)](arkts-network-connection-findproxyforurl-f.md) |
| [getAddressesByName(网络连接管理)](arkts-network-connection-getaddressesbyname-f.md) |
| [getAddressesByName(网络连接管理)](arkts-network-connection-getaddressesbyname-f.md) |
| [getAddressesByNameWithOptions(网络连接管理)](arkts-network-connection-getaddressesbynamewithoptions-f.md) |
| [getAllNets(网络连接管理)](arkts-network-connection-getallnets-f.md) |
| [getAllNets(网络连接管理)](arkts-network-connection-getallnets-f.md) |
| [getAllNetsSync(网络连接管理)](arkts-network-connection-getallnetssync-f.md) |
| [getAppNet(网络连接管理)](arkts-network-connection-getappnet-f.md) |
| [getAppNet(网络连接管理)](arkts-network-connection-getappnet-f.md) |
| [getAppNetSync(网络连接管理)](arkts-network-connection-getappnetsync-f.md) |
| [getConnectionProperties(网络连接管理)](arkts-network-connection-getconnectionproperties-f.md) |
| [getConnectionProperties(网络连接管理)](arkts-network-connection-getconnectionproperties-f.md) |
| [getConnectionPropertiesSync(网络连接管理)](arkts-network-connection-getconnectionpropertiessync-f.md) |
| [getConnectOwnerUid(网络连接管理)](arkts-network-connection-getconnectowneruid-f.md) |
| [getConnectOwnerUidSync(网络连接管理)](arkts-network-connection-getconnectowneruidsync-f.md) |
| [getDefaultHttpProxy(网络连接管理)](arkts-network-connection-getdefaulthttpproxy-f.md) |
| [getDefaultHttpProxy(网络连接管理)](arkts-network-connection-getdefaulthttpproxy-f.md) |
| [getDefaultNet(网络连接管理)](arkts-network-connection-getdefaultnet-f.md) |
| [getDefaultNet(网络连接管理)](arkts-network-connection-getdefaultnet-f.md) |
| [getDefaultNetSync(网络连接管理)](arkts-network-connection-getdefaultnetsync-f.md) |
| [getDnsAscii(网络连接管理)](arkts-network-connection-getdnsascii-f.md) |
| [getDnsUnicode(网络连接管理)](arkts-network-connection-getdnsunicode-f.md) |
| [getIpNeighTable(网络连接管理)](arkts-network-connection-getipneightable-f.md) |
| [getNetCapabilities(网络连接管理)](arkts-network-connection-getnetcapabilities-f.md) |
| [getNetCapabilities(网络连接管理)](arkts-network-connection-getnetcapabilities-f.md) |
| [getNetCapabilitiesSync(网络连接管理)](arkts-network-connection-getnetcapabilitiessync-f.md) |
| [getNetExtAttribute(网络连接管理)](arkts-network-connection-getnetextattribute-f.md) |
| [getNetExtAttributeSync(网络连接管理)](arkts-network-connection-getnetextattributesync-f.md) |
| [getPacFileUrl(网络连接管理)](arkts-network-connection-getpacfileurl-f.md) |
| [getPacUrl(网络连接管理)](arkts-network-connection-getpacurl-f.md) |
| [getSystemNetPortStates(网络连接管理)](arkts-network-connection-getsystemnetportstates-f.md) |
| [hasDefaultNet(网络连接管理)](arkts-network-connection-hasdefaultnet-f.md) |
| [hasDefaultNet(网络连接管理)](arkts-network-connection-hasdefaultnet-f.md) |
| [hasDefaultNetSync(网络连接管理)](arkts-network-connection-hasdefaultnetsync-f.md) |
| [isDefaultNetMetered(网络连接管理)](arkts-network-connection-isdefaultnetmetered-f.md) |
| [isDefaultNetMetered(网络连接管理)](arkts-network-connection-isdefaultnetmetered-f.md) |
| [isDefaultNetMeteredSync(网络连接管理)](arkts-network-connection-isdefaultnetmeteredsync-f.md) |
| [queryProbeResult(网络连接管理)](arkts-network-connection-queryproberesult-f.md) |
| [queryTraceRoute(网络连接管理)](arkts-network-connection-querytraceroute-f.md) |
| [refreshGlobalHttpProxy(网络连接管理)](arkts-network-connection-refreshglobalhttpproxy-f.md) |
| [removeCustomDnsRule(网络连接管理)](arkts-network-connection-removecustomdnsrule-f.md) |
| [removeCustomDnsRule(网络连接管理)](arkts-network-connection-removecustomdnsrule-f.md) |
| [reportNetConnected(网络连接管理)](arkts-network-connection-reportnetconnected-f.md) |
| [reportNetConnected(网络连接管理)](arkts-network-connection-reportnetconnected-f.md) |
| [reportNetDisconnected(网络连接管理)](arkts-network-connection-reportnetdisconnected-f.md) |
| [reportNetDisconnected(网络连接管理)](arkts-network-connection-reportnetdisconnected-f.md) |
| [setAppHttpProxy(网络连接管理)](arkts-network-connection-setapphttpproxy-f.md) |
| [setAppNet(网络连接管理)](arkts-network-connection-setappnet-f.md) |
| [setAppNet(网络连接管理)](arkts-network-connection-setappnet-f.md) |
| [setNetExtAttribute(网络连接管理)](arkts-network-connection-setnetextattribute-f.md) |
| [setNetExtAttributeSync(网络连接管理)](arkts-network-connection-setnetextattributesync-f.md) |
| [setPacFileUrl(网络连接管理)](arkts-network-connection-setpacfileurl-f.md) |
| [setPacUrl(网络连接管理)](arkts-network-connection-setpacurl-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addVlanIp(网络连接管理)](arkts-network-connection-addvlanip-f-sys.md) |
| [createVlanInterface(网络连接管理)](arkts-network-connection-createvlaninterface-f-sys.md) |
| [deleteVlanIp(网络连接管理)](arkts-network-connection-deletevlanip-f-sys.md) |
| [destroyVlanInterface(网络连接管理)](arkts-network-connection-destroyvlaninterface-f-sys.md) |
| [disableAirplaneMode(网络连接管理)](arkts-network-connection-disableairplanemode-f-sys.md) |
| [disableAirplaneMode(网络连接管理)](arkts-network-connection-disableairplanemode-f-sys.md) |
| [enableAirplaneMode(网络连接管理)](arkts-network-connection-enableairplanemode-f-sys.md) |
| [enableAirplaneMode(网络连接管理)](arkts-network-connection-enableairplanemode-f-sys.md) |
| [factoryReset(网络连接管理)](arkts-network-connection-factoryreset-f-sys.md) |
| [getGlobalHttpProxy(网络连接管理)](arkts-network-connection-getglobalhttpproxy-f-sys.md) |
| [getGlobalHttpProxy(网络连接管理)](arkts-network-connection-getglobalhttpproxy-f-sys.md) |
| [getProxyMode(网络连接管理)](arkts-network-connection-getproxymode-f-sys.md) |
| [setGlobalHttpProxy(网络连接管理)](arkts-network-connection-setglobalhttpproxy-f-sys.md) |
| [setGlobalHttpProxy(网络连接管理)](arkts-network-connection-setglobalhttpproxy-f-sys.md) |
| [setInterfaceUp(网络连接管理)](arkts-network-connection-setinterfaceup-f-sys.md) |
| [setProxyMode(网络连接管理)](arkts-network-connection-setproxymode-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [ConnectionProperties(网络连接管理)](arkts-network-connection-connectionproperties-i.md) |
| [HttpProxy(网络连接管理)](arkts-network-connection-httpproxy-i.md) |
| [LinkAddress(网络连接管理)](arkts-network-connection-linkaddress-i.md) |
| [NetAddress(网络连接管理)](arkts-network-connection-netaddress-i.md) |
| [NetBlockStatusInfo(网络连接管理)](arkts-network-connection-netblockstatusinfo-i.md) |
| [NetCapabilities(网络连接管理)](arkts-network-connection-netcapabilities-i.md) |
| [NetCapabilityInfo(网络连接管理)](arkts-network-connection-netcapabilityinfo-i.md) |
| [NetConnection(网络连接管理)](arkts-network-connection-netconnection-i.md) |
| [NetConnectionPropertyInfo(网络连接管理)](arkts-network-connection-netconnectionpropertyinfo-i.md) |
| [NetHandle(网络连接管理)](arkts-network-connection-nethandle-i.md) |
| [NetIpMacInfo(网络连接管理)](arkts-network-connection-netipmacinfo-i.md) |
| [NetPortStatesInfo(网络连接管理)](arkts-network-connection-netportstatesinfo-i.md) |
| [NetSpecifier(网络连接管理)](arkts-network-connection-netspecifier-i.md) |
| [ProbeResultInfo(网络连接管理)](arkts-network-connection-proberesultinfo-i.md) |
| [QueryOptions(网络连接管理)](arkts-network-connection-queryoptions-i.md) |
| [RouteInfo(网络连接管理)](arkts-network-connection-routeinfo-i.md) |
| [Socks5Proxy(网络连接管理)](arkts-network-connection-socks5proxy-i.md) |
| [TcpNetPortStatesInfo(网络连接管理)](arkts-network-connection-tcpnetportstatesinfo-i.md) |
| [TraceRouteInfo(网络连接管理)](arkts-network-connection-tracerouteinfo-i.md) |
| [TraceRouteOptions(网络连接管理)](arkts-network-connection-tracerouteoptions-i.md) |
| [UdpNetPortStatesInfo(网络连接管理)](arkts-network-connection-udpnetportstatesinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [ConversionProcess(网络连接管理)](arkts-network-connection-conversionprocess-e.md) |
| [FamilyType(网络连接管理)](arkts-network-connection-familytype-e.md) |
| [NetBearType(网络连接管理)](arkts-network-connection-netbeartype-e.md) |
| [NetCap(网络连接管理)](arkts-network-connection-netcap-e.md) |
| [PacketsType(网络连接管理)](arkts-network-connection-packetstype-e.md) |
| [ProtocolType(网络连接管理)](arkts-network-connection-protocoltype-e.md) |
| [Socks5DnsStrategy(网络连接管理)](arkts-network-connection-socks5dnsstrategy-e.md) |
| [TcpState(网络连接管理)](arkts-network-connection-tcpstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ProxyMode(网络连接管理)](arkts-network-connection-proxymode-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [HttpRequest(网络连接管理)](arkts-network-connection-httprequest-t.md) |
| [TCPSocket(网络连接管理)](arkts-network-connection-tcpsocket-t.md) |
| [UDPSocket(网络连接管理)](arkts-network-connection-udpsocket-t.md) |
