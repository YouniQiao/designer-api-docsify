# DeviceNodeInfo (System API)

设备节点信息，包括networkId、设备名称、设备类型标识符、近场状态和UDID。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-conversation-interface DeviceNodeInfo--><!--Device-conversation-interface DeviceNodeInfo-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## deviceName

```TypeScript
deviceName: string
```

设备名称。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceNodeInfo-deviceName: string--><!--Device-DeviceNodeInfo-deviceName: string-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## deviceTypeId

```TypeScript
deviceTypeId: int
```

设备类型标识符，表示设备的类别，取值为整数，例如：0x0E-手机、0x11-平板、0x9C-电视、0x0C-PC等（具体数值以系统定义为准）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceNodeInfo-deviceTypeId: int--><!--Device-DeviceNodeInfo-deviceTypeId: int-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## nearby

```TypeScript
nearby: boolean
```

设备是否在近场。true表示设备在近场，false表示设备不在近场。

**Type:** boolean

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceNodeInfo-nearby: boolean--><!--Device-DeviceNodeInfo-nearby: boolean-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## networkId

```TypeScript
networkId: string
```

设备的networkId，在分布式网络中唯一标识一台设备，用于发送数据时的设备寻址。与UDID互为替代，发送数据时可任选其一。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceNodeInfo-networkId: string--><!--Device-DeviceNodeInfo-networkId: string-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

## udid

```TypeScript
udid: string
```

设备的UDID，唯一标识一台设备，用于发送数据时的设备寻址。与networkId不同，UDID为设备的永久唯一标识，不随网络拓扑变化而改变，两者互为替代，发送数据时可任选其一。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceNodeInfo-udid: string--><!--Device-DeviceNodeInfo-udid: string-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

