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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function onConnectionStateChanged(callback: Callback<ConnectionResult>): void--><!--Device-dataTransfer-function onConnectionStateChanged(callback: Callback<ConnectionResult>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ConnectionResult](arkts-connectivity-datatransfer-connectionresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100099 |
