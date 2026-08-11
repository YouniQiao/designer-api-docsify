# RouteInfo

Defines network route information.

**Since:** 8

<!--Device-connection-export interface RouteInfo--><!--Device-connection-export interface RouteInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## destination

```TypeScript
destination: LinkAddress
```

Destination Address

**Type:** [LinkAddress](arkts-network-vpnextension-linkaddress-t.md)

**Since:** 8

<!--Device-RouteInfo-destination: LinkAddress--><!--Device-RouteInfo-destination: LinkAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## gateway

```TypeScript
gateway: NetAddress
```

Gateway address.

**Type:** [NetAddress](arkts-network-connection-netaddress-i.md)

**Since:** 8

<!--Device-RouteInfo-gateway: NetAddress--><!--Device-RouteInfo-gateway: NetAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## hasGateway

```TypeScript
hasGateway: boolean
```

Whether a gateway is present.

**Type:** boolean

**Since:** 8

<!--Device-RouteInfo-hasGateway: boolean--><!--Device-RouteInfo-hasGateway: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## interface

```TypeScript
interface: string
```

Network card name.

**Type:** string

**Since:** 8

<!--Device-RouteInfo-interface: string--><!--Device-RouteInfo-interface: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## isDefaultRoute

```TypeScript
isDefaultRoute: boolean
```

Whether the route is the default route.

**Type:** boolean

**Since:** 8

<!--Device-RouteInfo-isDefaultRoute: boolean--><!--Device-RouteInfo-isDefaultRoute: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## isExcludedRoute

```TypeScript
isExcludedRoute?: boolean
```

Whether the route is the excluded route.

**Type:** boolean

**Since:** 20

<!--Device-RouteInfo-isExcludedRoute?: boolean--><!--Device-RouteInfo-isExcludedRoute?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core
