# ProbeResultInfo

Defines the probe result information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-connection-export interface ProbeResultInfo--><!--Device-connection-export interface ProbeResultInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## lossRate

```TypeScript
lossRate: int
```

Packet loss rate. The value 100 indicates 100% packet loss, and 50 indicates 50% packet loss.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProbeResultInfo-lossRate: int--><!--Device-ProbeResultInfo-lossRate: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## rtt

```TypeScript
rtt: int[]
```

RTT in microseconds, min/avg/max/std.

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProbeResultInfo-rtt: int[]--><!--Device-ProbeResultInfo-rtt: int[]-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

