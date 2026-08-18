# onDeviceFound

## Modules to Import

```TypeScript
```

## onDeviceFound

```TypeScript
function onDeviceFound(callback: Callback<ScanResults[]>): void
```

Subscribes to NearLink scan results. This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission. If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission, the callback returns the real device address; otherwise, a random device address is returned.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-scan-function onDeviceFound(callback: Callback<ScanResults[]>): void--><!--Device-scan-function onDeviceFound(callback: Callback<ScanResults[]>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScanResults](arkts-connectivity-scan-scanresults-i.md)[]&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
