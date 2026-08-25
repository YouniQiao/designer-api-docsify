# onAcbStateChange

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## onAcbStateChange

```TypeScript
function onAcbStateChange(callback: Callback<AcbStateParam>): void
```

Subscribes to the logical link connection status change event. This API uses an asynchronous callback to return the result. This API is applicable when corresponding processing needs to be triggered when a logical link is established or disconnected, for example, checking whether the link is ready before data transfer or clearing resources after disconnection. Unlike [remoteDevice.onConnectionStateChange](arkts-connectivity-remotedevice-onconnectionstatechange-f.md) which listens for the connection status change at the device level, this API listens for the connection status change at the logical link level.The app must have the **ohos.permission.ACCESS_NEARLINK** permission to receive this event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AcbStateParam](arkts-connectivity-remotedevice-acbstateparam-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100099 |
