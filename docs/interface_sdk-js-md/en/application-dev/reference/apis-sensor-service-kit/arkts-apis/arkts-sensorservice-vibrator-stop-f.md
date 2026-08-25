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

**Substitutes:** [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)(stopMode: VibratorStopMode)

**Required permissions:** ohos.permission.VIBRATE

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [stopMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## stop

```TypeScript
function stop(stopMode: VibratorStopMode, callback?: AsyncCallback<void>): void
```

Stops vibration in the specified mode. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [stopVibration](arkts-sensorservice-vibrator-stopvibration-f.md)(stopMode: VibratorStopMode, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.VIBRATE

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [stopMode](../../apis-arkui/arkts-apis/arkts-arkui-arkui-drawabledescriptor-animationoptions-i.md) | [VibratorStopMode](arkts-sensorservice-vibrator-vibratorstopmode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |
