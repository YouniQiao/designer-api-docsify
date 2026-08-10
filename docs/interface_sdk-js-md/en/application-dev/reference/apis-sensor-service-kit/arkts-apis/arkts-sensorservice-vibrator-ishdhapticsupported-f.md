# isHdHapticSupported

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## isHdHapticSupported

```TypeScript
function isHdHapticSupported(): boolean
```

查询当前设备是否支持高清振动。适用于在触发高清振动前确认设备是否支持，避免在不支持的设备上调用VibrateFromFile或VibrateFromPattern类型振动导致振动效果不佳或返回错误码801。返回true表示设备支持高清振动，可使用VibrateFromFile和VibrateFromPattern类型触发振动；返回false表示不支持，使用自定义振动类型将返回错误码801或效果不佳。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-vibrator-function isHdHapticSupported(): boolean--><!--Device-vibrator-function isHdHapticSupported(): boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持高清振动。true表示支持高清振动，可使用VibrateFromFile和VibrateFromPattern类型；false表示不支持，使用自定义振动类型可能返回错误码801或效果不佳。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14600101 | Device operation failed. |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether HD vibration is supported.
  let ret = vibrator.isHdHapticSupported();
  console.info(`The query result is ${ret}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```

