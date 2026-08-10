# DeviceCapability

Describes the capability of a partner device.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-partnerAgent-interface DeviceCapability--><!--Device-partnerAgent-interface DeviceCapability-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## supportBR

```TypeScript
supportBR?: boolean
```

Whether the partner device supports the Bluetooth Basic Rate (BR) capability.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceCapability-supportBR?: boolean--><!--Device-DeviceCapability-supportBR?: boolean-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## supportBleAdvertiser

```TypeScript
supportBleAdvertiser?: boolean
```

Whether the partner device supports the Bluetooth Low Energy (BLE) advertiser capability.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DeviceCapability-supportBleAdvertiser?: boolean--><!--Device-DeviceCapability-supportBleAdvertiser?: boolean-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

