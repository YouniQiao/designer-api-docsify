# RouteInfo

Defines network route information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-connection-export interface RouteInfo--><!--Device-connection-export interface RouteInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## destination

```TypeScript
destination: LinkAddress
```

Destination Address

**Type:** LinkAddress

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RouteInfo-destination: LinkAddress--><!--Device-RouteInfo-destination: LinkAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## gateway

```TypeScript
gateway: NetAddress
```

Gateway address.

**Type:** NetAddress

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RouteInfo-gateway: NetAddress--><!--Device-RouteInfo-gateway: NetAddress-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## hasGateway

```TypeScript
hasGateway: boolean
```

Whether a gateway is present.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RouteInfo-hasGateway: boolean--><!--Device-RouteInfo-hasGateway: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## iface

```TypeScript
iface: string
```

Network card name.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RouteInfo-iface: string--><!--Device-RouteInfo-iface: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## interface

```TypeScript
interface: string
```

Network card name.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-RouteInfo-interface: string--><!--Device-RouteInfo-interface: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## isDefaultRoute

```TypeScript
isDefaultRoute: boolean
```

Whether the route is the default route.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-RouteInfo-isDefaultRoute: boolean--><!--Device-RouteInfo-isDefaultRoute: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## isExcludedRoute

```TypeScript
isExcludedRoute?: boolean
```

Whether the route is the excluded route.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-RouteInfo-isExcludedRoute?: boolean--><!--Device-RouteInfo-isExcludedRoute?: boolean-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

