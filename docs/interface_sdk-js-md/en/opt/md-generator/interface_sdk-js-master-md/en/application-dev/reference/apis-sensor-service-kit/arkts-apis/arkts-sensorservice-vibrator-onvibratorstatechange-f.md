# onVibratorStateChange

## Modules to Import

```TypeScript
```

## onVibratorStateChange

```TypeScript
function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void
```

Register a callback function to be called when a vibrator plugin or unplug event occurs.

**Since:** 23

<!--Device-vibrator-function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void--><!--Device-vibrator-function onVibratorStateChange(callback: Callback<VibratorStatusEvent>): void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VibratorStatusEvent](arkts-sensorservice-vibrator-vibratorstatusevent-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14600101](../errorcode-vibrator.md#14600101-device-operation-failed) |
