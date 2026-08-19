# onConnectionStateChanged

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## onConnectionStateChanged

```TypeScript
function onConnectionStateChanged(callback: Callback<ConnectionResult>): void
```

Subscribes to the connection state change event. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function onConnectionStateChanged(callback: Callback<ConnectionResult>): void--><!--Device-dataTransfer-function onConnectionStateChanged(callback: Callback<ConnectionResult>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ConnectionResult](arkts-connectivity-datatransfer-connectionresult-i.md)&gt; | Yes | Callback used to listen for the state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

