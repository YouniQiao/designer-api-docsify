# VibratorInfoParam

Defines the vibrator parameters. If **VibratorInfoParam** is left unspecified, an API applies to all vibrators of the local device by default.

**Since:** 23

<!--Device-vibrator-interface VibratorInfoParam--><!--Device-vibrator-interface VibratorInfoParam-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## deviceId

```TypeScript
deviceId?: int
```

Device ID. The default value is **-1**, indicating the local device. Since API version 19, you can use [getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md#getvibratorinfosync) or [on](arkts-sensorservice-vibrator-onvibratorstatechange-f.md#onvibratorstatechange) to query the device ID.

**Type:** int

**Since:** 23

<!--Device-VibratorInfoParam-deviceId?: int--><!--Device-VibratorInfoParam-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## vibratorId

```TypeScript
vibratorId?: int
```

Vibrator ID. The default value is **0**, which indicates all vibrators of the local device. Since API version 19, you can use [getVibratorInfoSync](arkts-sensorservice-vibrator-getvibratorinfosync-f.md#getvibratorinfosync) or [on](arkts-sensorservice-vibrator-onvibratorstatechange-f.md#onvibratorstatechange) to query the vibrator ID.

**Type:** int

**Since:** 23

<!--Device-VibratorInfoParam-vibratorId?: int--><!--Device-VibratorInfoParam-vibratorId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

