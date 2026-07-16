# BatteryInfo

Describes the contents of the battery information.

**Since:** 12

<!--Device-connection-interface BatteryInfo--><!--Device-connection-interface BatteryInfo-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## batteryLevel

```TypeScript
batteryLevel: number
```

Electricity value of the general device. {@code -1} means no power information.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-batteryLevel: int--><!--Device-BatteryInfo-batteryLevel: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## boxBatteryLevel

```TypeScript
boxBatteryLevel: number
```

Electricity value of the box. {@code -1} means no power information.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-boxBatteryLevel: int--><!--Device-BatteryInfo-boxBatteryLevel: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## boxChargeState

```TypeScript
boxChargeState: DeviceChargeState
```

The charge state of the box.

**Type:** DeviceChargeState

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-boxChargeState: DeviceChargeState--><!--Device-BatteryInfo-boxChargeState: DeviceChargeState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## leftEarBatteryLevel

```TypeScript
leftEarBatteryLevel: number
```

Electricity value of the left ear. {@code -1} means no power information.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-leftEarBatteryLevel: int--><!--Device-BatteryInfo-leftEarBatteryLevel: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## leftEarChargeState

```TypeScript
leftEarChargeState: DeviceChargeState
```

The charge state of the left ear.

**Type:** DeviceChargeState

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-leftEarChargeState: DeviceChargeState--><!--Device-BatteryInfo-leftEarChargeState: DeviceChargeState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rightEarBatteryLevel

```TypeScript
rightEarBatteryLevel: number
```

Electricity value of the right ear. {@code -1} means no power information.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-rightEarBatteryLevel: int--><!--Device-BatteryInfo-rightEarBatteryLevel: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## rightEarChargeState

```TypeScript
rightEarChargeState: DeviceChargeState
```

The charge state of the right ear.

**Type:** DeviceChargeState

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-BatteryInfo-rightEarChargeState: DeviceChargeState--><!--Device-BatteryInfo-rightEarChargeState: DeviceChargeState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

