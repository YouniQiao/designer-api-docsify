# VibratorPatternBuilder

Provide methods for adding long or short vibration events and generate VibratorPattern objects.

**Since:** 18

<!--Device-vibrator-class VibratorPatternBuilder--><!--Device-vibrator-class VibratorPatternBuilder-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
```

## addContinuousEvent

```TypeScript
addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder
```

Adds a long vibration event as a **VibratorPattern** object.

**Since:** 18

<!--Device-VibratorPatternBuilder-addContinuousEvent(time: int, duration: int, options?: ContinuousParam): VibratorPatternBuilder--><!--Device-VibratorPatternBuilder-addContinuousEvent(time: int, duration: int, options?: ContinuousParam): VibratorPatternBuilder-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |
| duration | number | Yes |
| options | [ContinuousParam](arkts-sensorservice-vibrator-continuousparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
// Use try catch to capture possible exceptions.
try {
  let pointsMe: vibrator.VibratorCurvePoint[] = [
    { time: 0, intensity: 0, frequency: -7 },
    { time: 42, intensity: 1, frequency: -6 },
    { time: 128, intensity: 0.94, frequency: -4 },
    { time: 217, intensity: 0.63, frequency: -14 },
    { time: 763, intensity: 0.48, frequency: -14 },
    { time: 1125, intensity: 0.53, frequency: -10 },
    { time: 1503, intensity: 0.42, frequency: -14 },
    { time: 1858, intensity: 0.39, frequency: -14 },
    { time: 2295, intensity: 0.34, frequency: -17 },
    { time: 2448, intensity: 0.21, frequency: -14 },
    { time: 2468, intensity: 0, frequency: -21 }
  ] // No less than four VibratorCurvePoint objects must be set. The maximum value is 16.
  let param: vibrator.ContinuousParam = {
    intensity: 97,
    frequency: 34,
    points:pointsMe,
    index: 0
  }
  builder.addContinuousEvent(0, 2468, param);
  console.info(`addContinuousEvent builder is ${builder.build()}`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(`Exception. Code ${e.code}`);
}
```

## addTransientEvent

```TypeScript
addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder
```

Adds a short vibration event as a **VibratorPattern** object.

**Since:** 18

<!--Device-VibratorPatternBuilder-addTransientEvent(time: int, options?: TransientParam): VibratorPatternBuilder--><!--Device-VibratorPatternBuilder-addTransientEvent(time: int, options?: TransientParam): VibratorPatternBuilder-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |
| options | [TransientParam](arkts-sensorservice-vibrator-transientparam-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VibratorPatternBuilder](arkts-sensorservice-vibrator-vibratorpatternbuilder-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
// Use try catch to capture possible exceptions.
try {
  let param: vibrator.TransientParam = {
    intensity: 80,
    frequency: 70,
    index: 0
  }
  builder.addTransientEvent(0, param);
  console.info(`addTransientEvent builder is ${builder.build()}`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```

## build

```TypeScript
build(): VibratorPattern
```

Constructor used to create a **VibratorPattern** object, which determines the vibration sequence of short or long events.

**Since:** 18

<!--Device-VibratorPatternBuilder-build(): VibratorPattern--><!--Device-VibratorPatternBuilder-build(): VibratorPattern-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md) |

## Examples

```TypeScript
import { vibrator } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let builder = new vibrator.VibratorPatternBuilder();
try {
  let param: vibrator.TransientParam = {
    intensity: 80,
    frequency: 70,
    index: 0
  }
  builder.addTransientEvent(0, param);
  console.info(`addTransientEvent builder is ${builder.build()}`);
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
try {
  vibrator.startVibration({
    type: "pattern",
    pattern: builder.build()
  }, {
  usage: "alarm", // The switch control is subject to the selected type.
  }, (error) => {
  if (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`Vibrate fail. Code: ${e.code}, message: ${e.message}`);
  } else {
    console.info(`vibrate success`);
  }
  });
} catch(error) {
  let e: BusinessError = error as BusinessError;
  console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
}
```
