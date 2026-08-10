# on

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## on('vibratorStateChange')

```TypeScript
function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void
```

注册马达上线或下线事件的回调函数。当马达设备上线或下线时触发回调。当开发者需要实时感知马达设备的上下线状态变化时使用此接口。适用于分布式多设备场景中动态获取马达设备信息，以便在马达上线时及时触发振动或在下线时停止振动。注册成功后，当马达设备上线或下线时，系统将回调VibratorStatusEvent对象，包含设备ID、马达数量、上下线状态等信息。回调中获取的deviceId可用于  
[startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)和[stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)等接口指定目标设备。注册回调后，需在合适的时机调用  
[vibrator.off](vibrator.off(type: 'vibratorStateChange', callback?: Callback&lt;VibratorStatusEvent&gt;))注销回调，避免内存泄露。同一type重复注册同一callback不会覆盖，需先off再on。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-vibrator-function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'vibratorStateChange' | Yes | 监听类型，该值固定为vibratorStateChange，表示马达上下线状态变化事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VibratorStatusEvent&gt; | Yes | 回调函数。当马达设备上线或下线时触发，回调参数为VibratorStatusEvent对象，包含timestamp、deviceId、 vibratorCount、isVibratorOnline等信息。回调中获取的deviceId可用于 [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration) 和[stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)等接口指定目标设备。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14600101 | Device operation failed. |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Callback
const vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
  console.info('vibrator state callback info:', JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  // Subscribe to vibratorStateChange events.
  vibrator.on('vibratorStateChange', vibratorStateChangeCallback);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```

