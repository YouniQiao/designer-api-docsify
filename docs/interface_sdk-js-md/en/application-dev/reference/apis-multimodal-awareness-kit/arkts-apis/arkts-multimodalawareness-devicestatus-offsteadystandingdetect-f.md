# offSteadyStandingDetect

## Modules to Import

```TypeScript
import { deviceStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## offSteadyStandingDetect

```TypeScript
function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing status detection events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function offSteadyStandingDetect(callback?: Callback<SteadyStandingStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;SteadyStandingStatus&gt; | No | Indicates the callback for getting the event data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [32500003](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500003-unsubscription-failed) | Unsubscription failed. |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-abnormal-service) | Service exception. |

