# SysVpnConfig（系统接口）

Define configuration of the system VPN network.

**继承/实现关系：** SysVpnConfig extends [VpnConfig](arkts-network-vpn-vpnconfig-i-sys.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-vpn-export interface SysVpnConfig extends VpnConfig--><!--Device-vpn-export interface SysVpnConfig extends VpnConfig-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## forwardingRoutes

```TypeScript
forwardingRoutes?: string
```

The forwarding routes for the VPN network.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-forwardingRoutes?: string--><!--Device-SysVpnConfig-forwardingRoutes?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## localAddresses

```TypeScript
localAddresses?: Array<LinkAddress>
```

The array of local addresses for VPN interface.

**类型：** Array&lt;LinkAddress&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SysVpnConfig-localAddresses?: Array<LinkAddress>--><!--Device-SysVpnConfig-localAddresses?: Array<LinkAddress>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## password

```TypeScript
password?: string
```

The user password for the VPN network.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-password?: string--><!--Device-SysVpnConfig-password?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## pkcs12FileData

```TypeScript
pkcs12FileData?: Uint8Array
```

The p12 cert data for the ipsec VPN network.

**类型：** Uint8Array

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-SysVpnConfig-pkcs12FileData?: Uint8Array--><!--Device-SysVpnConfig-pkcs12FileData?: Uint8Array-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## pkcs12Password

```TypeScript
pkcs12Password?: string
```

The p12 cert password for the ipsec VPN network.

**类型：** string

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-SysVpnConfig-pkcs12Password?: string--><!--Device-SysVpnConfig-pkcs12Password?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## remoteAddresses

```TypeScript
remoteAddresses?: Array<string>
```

The array of addresses for remote server.

**类型：** Array&lt;string&gt;

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-SysVpnConfig-remoteAddresses?: Array<string>--><!--Device-SysVpnConfig-remoteAddresses?: Array<string>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## saveLogin

```TypeScript
saveLogin?: boolean
```

Whether the VPN network save login name and password. The default value is false.

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-saveLogin?: boolean--><!--Device-SysVpnConfig-saveLogin?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## userId

```TypeScript
userId?: number
```

The system user id for the VPN network.

**类型：** number

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-userId?: number--><!--Device-SysVpnConfig-userId?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## userName

```TypeScript
userName?: string
```

The user name for the VPN network.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-userName?: string--><!--Device-SysVpnConfig-userName?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## vpnId

```TypeScript
vpnId?: string
```

The uuid for the VPN network.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-vpnId?: string--><!--Device-SysVpnConfig-vpnId?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## vpnName

```TypeScript
vpnName?: string
```

The name for the VPN network.

**类型：** string

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-vpnName?: string--><!--Device-SysVpnConfig-vpnName?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

## vpnType

```TypeScript
vpnType?: SysVpnType
```

The type for the VPN network.

**类型：** [SysVpnType](arkts-network-vpn-sysvpntype-e-sys.md)

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

<!--Device-SysVpnConfig-vpnType?: SysVpnType--><!--Device-SysVpnConfig-vpnType?: SysVpnType-End-->

**系统能力：** SystemCapability.Communication.NetManager.Vpn

**系统接口：** 此接口为系统接口。

