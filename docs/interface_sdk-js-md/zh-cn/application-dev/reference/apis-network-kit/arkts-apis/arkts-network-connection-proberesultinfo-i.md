# ProbeResultInfo

Defines the probe result information.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-connection-export interface ProbeResultInfo--><!--Device-connection-export interface ProbeResultInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## lossRate

```TypeScript
lossRate: int
```

Packet loss rate. The value 100 indicates 100% packet loss, and 50 indicates 50% packet loss.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProbeResultInfo-lossRate: int--><!--Device-ProbeResultInfo-lossRate: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## rtt

```TypeScript
rtt: int[]
```

RTT in microseconds, min/avg/max/std.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ProbeResultInfo-rtt: int[]--><!--Device-ProbeResultInfo-rtt: int[]-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

