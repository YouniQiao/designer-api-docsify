# TraceRouteOptions

Network traceroute option definition.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-connection-export interface TraceRouteOptions--><!--Device-connection-export interface TraceRouteOptions-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## maxJumpNumber

```TypeScript
maxJumpNumber?: int
```

Maximum number of jumps, max is 30. Default is 30.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TraceRouteOptions-maxJumpNumber?: int--><!--Device-TraceRouteOptions-maxJumpNumber?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## packetsType

```TypeScript
packetsType?: PacketsType
```

Packets type. Default is NETCONN_PACKETS_ICMP.

**类型：** [PacketsType](arkts-network-connection-packetstype-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TraceRouteOptions-packetsType?: PacketsType--><!--Device-TraceRouteOptions-packetsType?: PacketsType-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

