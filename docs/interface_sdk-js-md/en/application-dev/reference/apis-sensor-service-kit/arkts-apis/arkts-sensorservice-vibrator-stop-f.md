# stop

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## stop

```TypeScript
function stop(stopMode: VibratorStopMode): Promise<void>
```

按照指定模式停止马达的振动。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)(stopMode:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function stop(stopMode: VibratorStopMode): Promise<void>--><!--Device-vibrator-function stop(stopMode: VibratorStopMode): Promise<void>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes | 马达停止指定的振动模式。需与启动振动时的模式对应：VIBRATOR_STOP_MODE_TIME用于停止时长振动， VIBRATOR_STOP_MODE_PRESET用于停止预置效果振动。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。调用成功时Promise resolve，表示振动成功停止；调用失败时Promise reject，返回错误对象包含错误码和错误信息。 |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Start vibration based on the specified effect ID.
vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
// Stop vibration in VIBRATOR_STOP_MODE_PRESET mode.
vibrator.stop(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET).then(() => {
  console.info('Succeed in stopping');
}, (error: BusinessError) => {
  console.error(`Failed to stop. Code: ${error.code}, message: ${error.message}`);
});
```


## stop

```TypeScript
function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void
```

按照指定模式停止马达的振动。

> **说明：**
> 
> 从API version 8 开始支持，从API version 9 开始废弃，建议使用
> [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)
> 替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)(stopMode:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| stopMode | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes | 马达停止指定的振动模式。需与启动振动时的模式对应：VIBRATOR_STOP_MODE_TIME用于停止时长振动， VIBRATOR_STOP_MODE_PRESET用于停止预置效果振动。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No | 回调函数，当马达停止振动成功，err为undefined，否则为错误对象。使用场景：不填写时仅停止振动不获取回调结果。 |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Start vibration based on the specified effect ID.
vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
// Stop vibration in VIBRATOR_STOP_MODE_PRESET mode.
vibrator.stop(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to stop. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in stopping');
  }
})
```

