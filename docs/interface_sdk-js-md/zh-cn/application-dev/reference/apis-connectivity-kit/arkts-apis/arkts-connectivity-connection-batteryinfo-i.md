# BatteryInfo

Describes the contents of the battery information.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-connection-interface BatteryInfo--><!--Device-connection-interface BatteryInfo-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## batteryLevel

```TypeScript
batteryLevel: int
```

Electricity value of the general device. {@code -1} means no power information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-batteryLevel: int--><!--Device-BatteryInfo-batteryLevel: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## boxBatteryLevel

```TypeScript
boxBatteryLevel: int
```

Electricity value of the box. {@code -1} means no power information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-boxBatteryLevel: int--><!--Device-BatteryInfo-boxBatteryLevel: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## boxChargeState

```TypeScript
boxChargeState: DeviceChargeState
```

The charge state of the box.

**类型：** [DeviceChargeState](arkts-connectivity-connection-devicechargestate-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-boxChargeState: DeviceChargeState--><!--Device-BatteryInfo-boxChargeState: DeviceChargeState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## leftEarBatteryLevel

```TypeScript
leftEarBatteryLevel: int
```

Electricity value of the left ear. {@code -1} means no power information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-leftEarBatteryLevel: int--><!--Device-BatteryInfo-leftEarBatteryLevel: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## leftEarChargeState

```TypeScript
leftEarChargeState: DeviceChargeState
```

The charge state of the left ear.

**类型：** [DeviceChargeState](arkts-connectivity-connection-devicechargestate-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-leftEarChargeState: DeviceChargeState--><!--Device-BatteryInfo-leftEarChargeState: DeviceChargeState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rightEarBatteryLevel

```TypeScript
rightEarBatteryLevel: int
```

Electricity value of the right ear. {@code -1} means no power information.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-rightEarBatteryLevel: int--><!--Device-BatteryInfo-rightEarBatteryLevel: int-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## rightEarChargeState

```TypeScript
rightEarChargeState: DeviceChargeState
```

The charge state of the right ear.

**类型：** [DeviceChargeState](arkts-connectivity-connection-devicechargestate-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatteryInfo-rightEarChargeState: DeviceChargeState--><!--Device-BatteryInfo-rightEarChargeState: DeviceChargeState-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

