# offSteadyStandingDetect

## Modules to Import

```TypeScript
```

## offSteadyStandingDetect

```TypeScript
function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing status detection events.

**Since:** 23

<!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32500003](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500003-unsubscription-failed) |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-abnormal-service) |
