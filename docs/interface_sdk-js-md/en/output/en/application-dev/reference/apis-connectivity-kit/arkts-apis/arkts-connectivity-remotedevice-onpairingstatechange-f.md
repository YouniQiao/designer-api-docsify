# onPairingStateChange

## onPairingStateChange

```TypeScript
function onPairingStateChange(callback: Callback<PairingStateParam>): void
```

Subscribes to NearLink pairing state change events. This event is accessible only to applications that granted the ohos.permission.NEARLINK\_ACCESS permission. If the application is granted the ohos.permission.GET\_NEARLINK\_PEER\_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-remoteDevice-function onPairingStateChange(callback: Callback<PairingStateParam>): void--><!--Device-remoteDevice-function onPairingStateChange(callback: Callback<PairingStateParam>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;PairingStateParam&gt; | Yes | Callback function used to listen for the pairing state event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported because the chip does not support it. |
| 36100099 | Operation failed. |

