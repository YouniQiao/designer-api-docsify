# ConnectionProperties

Defines the network connection properties.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-connection-export interface ConnectionProperties--><!--Device-connection-export interface ConnectionProperties-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## dnses

```TypeScript
dnses: Array<NetAddress>
```

Network address, refer to [NetAddress].

**类型：** Array&lt;NetAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-dnses: Array<NetAddress>--><!--Device-ConnectionProperties-dnses: Array<NetAddress>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## domains

```TypeScript
domains: string
```

Domain. The default value is "".

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-domains: string--><!--Device-ConnectionProperties-domains: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## interfaceName

```TypeScript
interfaceName: string
```

Network card name.

**类型：** string

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-interfaceName: string--><!--Device-ConnectionProperties-interfaceName: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## isIPv4LinkValid

```TypeScript
isIPv4LinkValid?: boolean
```

Whether the IPv4 address of the interface is valid.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionProperties-isIPv4LinkValid?: boolean--><!--Device-ConnectionProperties-isIPv4LinkValid?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## isIPv6LinkValid

```TypeScript
isIPv6LinkValid?: boolean
```

Whether the IPv6 address of the interface is valid.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为24；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConnectionProperties-isIPv6LinkValid?: boolean--><!--Device-ConnectionProperties-isIPv6LinkValid?: boolean-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## linkAddresses

```TypeScript
linkAddresses: Array<LinkAddress>
```

Link information.

**类型：** Array&lt;LinkAddress&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-linkAddresses: Array<LinkAddress>--><!--Device-ConnectionProperties-linkAddresses: Array<LinkAddress>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## mtu

```TypeScript
mtu: int
```

Maximum transmission unit.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-mtu: int--><!--Device-ConnectionProperties-mtu: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## routes

```TypeScript
routes: Array<RouteInfo>
```

Routing information.

**类型：** Array&lt;RouteInfo&gt;

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-ConnectionProperties-routes: Array<RouteInfo>--><!--Device-ConnectionProperties-routes: Array<RouteInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

