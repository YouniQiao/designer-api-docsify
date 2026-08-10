# off

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## off('vibratorStateChange')

```TypeScript
function off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void
```

注销马达上线或下线事件的回调函数。当开发者不再需要监听马达上下线状态变化时使用此接口注销回调。传入callback时注销指定回调；不传callback时注销该类型下所有已注册的回调。注销成功后，不再触发对应的回调函数。若传入的callback未注册过，注销操作无效但不会报错。需先通过[vibrator.on](arkts-sensorservice-vibrator-on-f.md#on)注册回调后才能注销。同一type重复注册同一callback不会覆盖，需先off再on。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

<!--Device-vibrator-function off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'vibratorStateChange' | Yes | 监听类型，该值固定为vibratorStateChange，表示马达上下线状态变化事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VibratorStatusEvent&gt; | No | 需要注销的回调函数。不传此参数时注销所有vibratorStateChange类型的回调。使用场景：若仅需注销特定回调则传入对应 callback；若需注销全部回调则不传此参数。 |

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
  // Unsubscribe from specified vibratorStateChange events.
  vibrator.off('vibratorStateChange', vibratorStateChangeCallback);
  // Unsubscribe from all vibratorStateChange events.
  // vibrator.off('vibratorStateChange');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```

