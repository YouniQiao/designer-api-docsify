# offConnectionStateChange

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
```

## offConnectionStateChange

```TypeScript
function offConnectionStateChange(callback?: Callback<ConnectionStateParam>): void
```

Unsubscribes from the connection status change event. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ConnectionStateParam](arkts-connectivity-remotedevice-connectionstateparam-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100099 |
