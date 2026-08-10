# TraceRouteInfo

Defines the trace route information structure.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-connection-export interface TraceRouteInfo--><!--Device-connection-export interface TraceRouteInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address: string
```

Host name or address.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TraceRouteInfo-address: string--><!--Device-TraceRouteInfo-address: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## jumpNo

```TypeScript
jumpNo: int
```

Number of jumps.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TraceRouteInfo-jumpNo: int--><!--Device-TraceRouteInfo-jumpNo: int-End-->

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

<!--Device-TraceRouteInfo-rtt: int[]--><!--Device-TraceRouteInfo-rtt: int[]-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

