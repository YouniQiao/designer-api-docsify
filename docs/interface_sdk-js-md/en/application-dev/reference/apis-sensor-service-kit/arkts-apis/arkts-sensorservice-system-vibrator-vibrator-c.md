# Vibrator

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [vibrator/vibrator](arkts-vibrator.md)

**Required permissions:** ohos.permission.VIBRATE

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## Modules to Import

```TypeScript
import { Vibrator, VibrateOptions } from 'kits/@kit.SensorServiceKit';
```

## vibrate

```TypeScript
static vibrate(options?: VibrateOptions): void
```

Triggers device vibration.

> **NOTE：**&gt;
> Except for lite wearables. You are advised to use
> [vibrator.startVibration()](arkts-sensorservice-vibrator-startvibration-f.md) since API version 8.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md)(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [VibrateOptions](arkts-sensorservice-system-vibrator-vibrateoptions-i.md) | No |
