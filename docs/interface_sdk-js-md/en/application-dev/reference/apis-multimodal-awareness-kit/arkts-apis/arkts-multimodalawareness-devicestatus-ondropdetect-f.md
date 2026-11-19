# onDropDetect

## Modules to Import

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## onDropDetect

```TypeScript
function onDropDetect(callback: Callback<DropDetectionStatus>): void
```

Subscribes to device drop detection events.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceStatus-function onDropDetect(callback: Callback<DropDetectionStatus>): void--><!--Device-deviceStatus-function onDropDetect(callback: Callback<DropDetectionStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DropDetectionStatus](arkts-multimodalawareness-devicestatus-dropdetectionstatus-e.md)&gt; | Yes | Callback used to return the device drop detection status <br> information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br> 1. The hardware does not support the capability; <br> 2. The chip does not support the capability; <br> 3. A dependent service feature is not supported. |
| [32500001](../errorcode-deviceStatus.md#32500001-abnormal-service) | Service exception. |
| [32500002](../errorcode-deviceStatus.md#32500002-subscription-failed) | Subscription failed. |
