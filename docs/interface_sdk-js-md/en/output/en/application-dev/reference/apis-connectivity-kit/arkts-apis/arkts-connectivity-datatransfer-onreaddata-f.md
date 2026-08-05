# onReadData

## onReadData

```TypeScript
function onReadData(callback: Callback<DataParams>): void
```

Subscribes to the event reported when data is read from the port. This event is accessible only to applications that granted the ohos.permission.NEARLINK\_ACCESS permission.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function onReadData(callback: Callback<DataParams>): void--><!--Device-dataTransfer-function onReadData(callback: Callback<DataParams>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DataParams&gt; | Yes | Callback used to listen for the port read event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

