# VpnConfig

Define configuration of the VPN network.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-vpnExtension-export interface VpnConfig--><!--Device-vpnExtension-export interface VpnConfig-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## 导入模块

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## addresses

```TypeScript
addresses: Array<LinkAddress>
```

The array of addresses for VPN interface.

**类型：** Array&lt;LinkAddress&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-addresses: Array<LinkAddress>--><!--Device-VpnConfig-addresses: Array<LinkAddress>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## blockedApplications

```TypeScript
blockedApplications?: Array<string>
```

The array of blocklist for the VPN network. The string indicates package name.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-blockedApplications?: Array<string>--><!--Device-VpnConfig-blockedApplications?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## dnsAddresses

```TypeScript
dnsAddresses?: Array<string>
```

The array of DNS servers for the VPN network.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-dnsAddresses?: Array<string>--><!--Device-VpnConfig-dnsAddresses?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## isBlocking

```TypeScript
isBlocking?: boolean
```

Whether the VPN interface's file descriptor is in blocking/non-blocking mode. The default value is false.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-isBlocking?: boolean--><!--Device-VpnConfig-isBlocking?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## isIPv4Accepted

```TypeScript
isIPv4Accepted?: boolean
```

Whether ipv4 is supported. The default value is true.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-isIPv4Accepted?: boolean--><!--Device-VpnConfig-isIPv4Accepted?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## isIPv6Accepted

```TypeScript
isIPv6Accepted?: boolean
```

Whether ipv6 is supported. The default value is false.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-isIPv6Accepted?: boolean--><!--Device-VpnConfig-isIPv6Accepted?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## isInternal

```TypeScript
isInternal?: boolean
```

Whether to use the built-in VPN. The default value is false.

**类型：** boolean

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-isInternal?: boolean--><!--Device-VpnConfig-isInternal?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## mtu

```TypeScript
mtu?: number
```

The maximum transmission unit (MTU) for the VPN interface.

**类型：** number

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-mtu?: number--><!--Device-VpnConfig-mtu?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## routes

```TypeScript
routes?: Array<RouteInfo>
```

The array of routes for VPN interface.

**类型：** Array&lt;RouteInfo&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-routes?: Array<RouteInfo>--><!--Device-VpnConfig-routes?: Array<RouteInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## searchDomains

```TypeScript
searchDomains?: Array<string>
```

The array of search domains for the DNS resolver.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-searchDomains?: Array<string>--><!--Device-VpnConfig-searchDomains?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## trustedApplications

```TypeScript
trustedApplications?: Array<string>
```

The array of trustlist for the VPN network. The string indicates package name.

**类型：** Array&lt;string&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-VpnConfig-trustedApplications?: Array<string>--><!--Device-VpnConfig-trustedApplications?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

## vpnId

```TypeScript
vpnId?: string
```

The uuid for the VPN network.

**类型：** string

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-VpnConfig-vpnId?: string--><!--Device-VpnConfig-vpnId?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

