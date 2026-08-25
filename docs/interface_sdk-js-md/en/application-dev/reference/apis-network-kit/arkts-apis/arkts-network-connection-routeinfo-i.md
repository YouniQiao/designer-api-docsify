# RouteInfo

Defines network route information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## destination

```TypeScript
destination: LinkAddress
```

Destination address.

**Type:** LinkAddress

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## gateway

```TypeScript
gateway: NetAddress
```

Gateway address.

**Type:** NetAddress

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## hasGateway

```TypeScript
hasGateway: boolean
```

Whether a gateway is present. Whether a gateway is available. The value **true** indicates that a gateway is available, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## iface

```TypeScript
iface: string
```

Network card name.

**Type:** string

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## interface

```TypeScript
interface: string
```

NIC name.

**Type:** string

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**System capability:** SystemCapability.Communication.NetManager.Core

## isDefaultRoute

```TypeScript
isDefaultRoute: boolean
```

Whether the route is the default one. Whether the route is the default route. The value **true** indicates that the route is the default route, and the value **false** indicates the opposite.Note: The IPv4 default route refers to the route whose destination address is **0.0.0.0/0**. The IPv6 default route refers to the route whose destination address is **::/0**.

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## isExcludedRoute

```TypeScript
isExcludedRoute?: boolean
```

Whether the route is excluded. The value **true** indicates that the route is excluded, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**System capability:** SystemCapability.Communication.NetManager.Core
