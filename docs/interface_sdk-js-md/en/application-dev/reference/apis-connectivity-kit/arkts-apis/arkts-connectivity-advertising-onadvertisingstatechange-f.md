# onAdvertisingStateChange

## Modules to Import

```TypeScript
import { advertising } from 'advertising';
```

## onAdvertisingStateChange

```TypeScript
function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void
```

Subscribes to the advertising state change event. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void--><!--Device-advertising-function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | Yes | Callback used to listen for the advertising state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |

