# VibratorStatusEvent

Defines the vibrator status change event.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorStatusEvent--><!--Device-vibrator-interface VibratorStatusEvent-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId: int
```

Device ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorStatusEvent-deviceId: int--><!--Device-VibratorStatusEvent-deviceId: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## isVibratorOnline

```TypeScript
isVibratorOnline: boolean
```

Vibrator status. The value **true** indicates that the device is online, and the value **false** indicates the opposite.

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorStatusEvent-isVibratorOnline: boolean--><!--Device-VibratorStatusEvent-isVibratorOnline: boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## timestamp

```TypeScript
timestamp: long
```

Event timestamp, in ms.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorStatusEvent-timestamp: long--><!--Device-VibratorStatusEvent-timestamp: long-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## vibratorCount

```TypeScript
vibratorCount: int
```

Number of vibrators on the device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorStatusEvent-vibratorCount: int--><!--Device-VibratorStatusEvent-vibratorCount: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

