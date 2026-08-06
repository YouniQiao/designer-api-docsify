# onPairingRequest (System API)

## onPairingRequest

```TypeScript
function onPairingRequest(callback: Callback<PairingRequestParam>): void
```

Subscribes to pairing request events from remote NearLink devices.

This event is accessible only to system applications that granted the ohos.permission.NEARLINK\_ACCESS permission.If the application is granted the ohos.permission.GET\_NEARLINK\_PEER\_MAC permission,the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-remoteDevice-function onPairingRequest(callback: Callback<PairingRequestParam>): void--><!--Device-remoteDevice-function onPairingRequest(callback: Callback<PairingRequestParam>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;PairingRequestParam&gt; | Yes | Callback used to listen for the pairing request event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

