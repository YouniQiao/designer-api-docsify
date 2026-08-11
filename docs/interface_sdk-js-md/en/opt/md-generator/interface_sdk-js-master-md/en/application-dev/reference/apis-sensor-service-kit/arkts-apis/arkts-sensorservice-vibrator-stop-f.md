# stop

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## stop

```TypeScript
function stop(stopMode: VibratorStopMode): Promise<void>
```

Stops vibration in the specified mode. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)(stopMode:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function stop(stopMode: VibratorStopMode): Promise<void>--><!--Device-vibrator-function stop(stopMode: VibratorStopMode): Promise<void>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| stopMode | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

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

Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md#stopvibration)(stopMode:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| stopMode | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

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
