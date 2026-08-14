# onSteadyStandingDetect

## Modules to Import

```TypeScript
import { deviceStatus } from 'deviceStatus';
```

## onSteadyStandingDetect

```TypeScript
function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void
```

Subscribes to steady standing status detection events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-deviceStatus-function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | Yes | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function can not work correctly due to limited <br> device capabilities. |
| [32500002](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500002-subscription-failed) | Subscription failed. |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-abnormal-service) | Service exception. |

