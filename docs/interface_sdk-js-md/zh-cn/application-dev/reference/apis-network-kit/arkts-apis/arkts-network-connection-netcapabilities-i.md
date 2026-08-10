# NetCapabilities

Defines the network capability set.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-connection-export interface NetCapabilities--><!--Device-connection-export interface NetCapabilities-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## bearerTypes

```TypeScript
bearerTypes: Array<NetBearType>
```

Network type.

**类型：** Array&lt;NetBearType&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NetCapabilities-bearerTypes: Array<NetBearType>--><!--Device-NetCapabilities-bearerTypes: Array<NetBearType>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## linkDownBandwidthKbps

```TypeScript
linkDownBandwidthKbps?: int
```

Downstream (network-to-device) bandwidth.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NetCapabilities-linkDownBandwidthKbps?: int--><!--Device-NetCapabilities-linkDownBandwidthKbps?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## linkUpBandwidthKbps

```TypeScript
linkUpBandwidthKbps?: int
```

Uplink (device-to-network) bandwidth.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

<!--Device-NetCapabilities-linkUpBandwidthKbps?: int--><!--Device-NetCapabilities-linkUpBandwidthKbps?: int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

## networkCap

```TypeScript
networkCap?: Array<NetCap>
```

Network-specific capabilities.

**类型：** Array&lt;NetCap&gt;

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-NetCapabilities-networkCap?: Array<NetCap>--><!--Device-NetCapabilities-networkCap?: Array<NetCap>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

