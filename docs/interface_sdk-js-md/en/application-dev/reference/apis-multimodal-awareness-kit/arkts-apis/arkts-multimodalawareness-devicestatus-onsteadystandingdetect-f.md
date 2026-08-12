# onSteadyStandingDetect

## Modules to Import

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## onSteadyStandingDetect

```TypeScript
function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void
```

Subscribes to steady standing status detection events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-deviceStatus-function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function onSteadyStandingDetect(callback: Callback<SteadyStandingStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | Yes | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [32500002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500002-subscription-failed) | Subscription failed. |
| [32500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-abnormal-service) | Service exception. |

