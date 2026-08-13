# TraceRouteInfo

Defines the trace route information structure.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-connection-export interface TraceRouteInfo--><!--Device-connection-export interface TraceRouteInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Host name or address.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TraceRouteInfo-address: string--><!--Device-TraceRouteInfo-address: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## jumpNo

```TypeScript
jumpNo: int
```

Number of jumps.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TraceRouteInfo-jumpNo: int--><!--Device-TraceRouteInfo-jumpNo: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## rtt

```TypeScript
rtt: int[]
```

RTT in microseconds, min/avg/max/std.

**Type:** int[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TraceRouteInfo-rtt: int[]--><!--Device-TraceRouteInfo-rtt: int[]-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

