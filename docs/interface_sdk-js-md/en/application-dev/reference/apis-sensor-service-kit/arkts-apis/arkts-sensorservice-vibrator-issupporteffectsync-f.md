# isSupportEffectSync

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## isSupportEffectSync

```TypeScript
function isSupportEffectSync(effectId: string): boolean
```

查询当前设备是否支持预设的振动效果。此接口为同步接口，会阻塞主线程直到查询完成，容易影响UI交互，需谨慎使用。当开发者需要在触发预置振动前立即确认当前设备是否支持指定的振动效果时使用此接口。适用于对实时性要求高且查询逻辑简单的场景。返回boolean结果：返回true表示设备支持该effectId，可用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)；返回false表示不支持，使用该effectId触发振动可能效果不佳或无法振动。与异步版本  
[vibrator.isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md#issupporteffect)相比，本接口为同步接口，直接返回结果无需回调，但会阻塞主线程。建议在非UI线程中使用，或在UI线程中优先使用异步版本以避免影响交互响应。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-vibrator-function isSupportEffectSync(effectId: string): boolean--><!--Device-vibrator-function isSupportEffectSync(effectId: string): boolean-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effectId | string | Yes | 待确认的预置振动效果ID。字符串最大长度64，超出部分截取前64个字符。使用场景：不同设备预置的振动效果可能不同，需传入具体的effectId查询是否支持。取值可参考 [EffectId](arkts-sensorservice-vibrator-effectid-e.md)和[HapticFeedback](arkts-sensorservice-vibrator-hapticfeedback-e.md)中定义的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回对象。返回true表示设备支持该effectId，可用于 [startVibration]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14600101 | Device operation failed. |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // Check whether the preset 'haptic.notice.success' is supported.
  let ret = vibrator.isSupportEffectSync('haptic.notice.success');
  console.info(`The query result is ${ret}`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```

