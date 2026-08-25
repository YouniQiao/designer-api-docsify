# stopVibrationSync

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## stopVibrationSync

```TypeScript
function stopVibrationSync(): void
```

Stops any form of motor vibration.

**Since:** 12

**Required permissions:** ohos.permission.VIBRATE

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Sensors.MiscDevice

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |
