# onCarAwareness (System API)

## Modules to Import

```TypeScript
import { carAwareness } from '@kit.MultimodalAwarenessKit';
```

## onCarAwareness

```TypeScript
function onCarAwareness(capability: Capability, callback: Callback<CarAwarenessInfo[]>, options?:
  CarAwarenessOptions): void
```

Enables vehicle awareness and subscribes to vehicle awareness results. If this function is not supported, no callback will be triggered. You can use the getAllCapacityList method to obtain the supported capabilities.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-carAwareness-function onCarAwareness(capability: Capability, callback: Callback<CarAwarenessInfo[]>, options?:  CarAwarenessOptions): void--><!--Device-carAwareness-function onCarAwareness(capability: Capability, callback: Callback<CarAwarenessInfo[]>, options?:  CarAwarenessOptions): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.CarAwareness

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capability | Capability | Yes | Specific capability. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CarAwarenessInfo](arkts-multimodalawareness-carawareness-carawarenessinfo-i-sys.md)[]&gt; | Yes | Callback used to return obtaining corresponding capability data. |
| options | [CarAwarenessOptions](arkts-multimodalawareness-carawareness-carawarenessoptions-i-sys.md) | No | Indicates options to specific capability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [34000002](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-unsupported-application-or-page) | Specific capability not supported. |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) | Service exception. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission check failed. A non-system application uses the system capability. |

