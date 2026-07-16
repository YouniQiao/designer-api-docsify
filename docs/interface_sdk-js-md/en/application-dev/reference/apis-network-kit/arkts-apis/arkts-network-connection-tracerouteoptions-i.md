# TraceRouteOptions

Network traceroute option definition.

**Since:** 26.0.0

<!--Device-connection-export interface TraceRouteOptions--><!--Device-connection-export interface TraceRouteOptions-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## maxJumpNumber

```TypeScript
maxJumpNumber?: number
```

Maximum number of jumps, max is 30. Default is 30.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-TraceRouteOptions-maxJumpNumber?: int--><!--Device-TraceRouteOptions-maxJumpNumber?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## packetsType

```TypeScript
packetsType?: PacketsType
```

Packets type. Default is NETCONN_PACKETS_ICMP.

**Type:** PacketsType

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-TraceRouteOptions-packetsType?: PacketsType--><!--Device-TraceRouteOptions-packetsType?: PacketsType-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

