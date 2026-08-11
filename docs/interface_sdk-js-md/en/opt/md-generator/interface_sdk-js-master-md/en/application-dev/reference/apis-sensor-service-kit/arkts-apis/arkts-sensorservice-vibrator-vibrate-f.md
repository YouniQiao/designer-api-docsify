# vibrate

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## vibrate

```TypeScript
function vibrate(duration: number, callback?: AsyncCallback<void>): void
```

Triggers vibration based on a specified duration. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)(effect:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(duration: number, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function vibrate(duration: number, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
```


## vibrate

```TypeScript
function vibrate(duration: number): Promise<void>
```

Triggers vibration based on a specified duration. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)(effect:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(duration: number): Promise<void>--><!--Device-vibrator-function vibrate(duration: number): Promise<void>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(1000).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
});
```


## vibrate

```TypeScript
function vibrate(effectId: EffectId): Promise<void>
```

Triggers vibration based on a specified effect. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)(effect:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(effectId: EffectId): Promise<void>--><!--Device-vibrator-function vibrate(effectId: EffectId): Promise<void>-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER).then(() => {
  console.info('Succeed in vibrating');
}, (error: BusinessError) => {
  console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
});
```


## vibrate

```TypeScript
function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void
```

Triggers vibration based on a specified effect. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [vibrator.startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startvibration)(effect:

**Required permissions:** ohos.permission.VIBRATE

<!--Device-vibrator-function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void--><!--Device-vibrator-function vibrate(effectId: EffectId, callback?: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effectId | [EffectId](arkts-sensorservice-vibrator-effectid-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

vibrator.vibrate(vibrator.EffectId.EFFECT_CLOCK_TIMER, (error: BusinessError) => {
  if (error) {
    console.error(`Failed to vibrate. Code: ${error.code}, message: ${error.message}`);
  } else {
    console.info('Succeed in vibrating');
  }
})
```
