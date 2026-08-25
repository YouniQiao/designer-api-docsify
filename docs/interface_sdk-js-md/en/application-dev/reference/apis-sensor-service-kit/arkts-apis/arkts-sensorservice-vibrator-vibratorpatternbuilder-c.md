# VibratorPatternBuilder

Provide methods for adding number or short vibration events and generate VibratorPattern objects.

**Since:** 18

**System capability:** SystemCapability.Sensors.MiscDevice

## Modules to Import

```TypeScript
import { vibrator } from 'kits/@kit.SensorServiceKit';
```

## addContinuousEvent

```TypeScript
addContinuousEvent(time: number, duration: number, options?: ContinuousParam): VibratorPatternBuilder
```

Adds a number vibration event as a **VibratorPattern** object.

**Since:** 18

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## addTransientEvent

```TypeScript
addTransientEvent(time: number, options?: TransientParam): VibratorPatternBuilder
```

Adds a short vibration event as a **VibratorPattern** object.

**Since:** 18

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## build

```TypeScript
build(): VibratorPattern
```

Constructor used to create a **VibratorPattern** object, which determines the vibration sequence of short or number events.

**Since:** 18

**System capability:** SystemCapability.Sensors.MiscDevice

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VibratorPattern](arkts-sensorservice-vibrator-vibratorpattern-i.md) |
