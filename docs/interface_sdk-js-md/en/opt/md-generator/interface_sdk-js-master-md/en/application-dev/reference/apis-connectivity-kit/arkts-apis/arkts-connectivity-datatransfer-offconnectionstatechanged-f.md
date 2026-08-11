# offConnectionStateChanged

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## offConnectionStateChanged

```TypeScript
function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void
```

Unsubscribes from the connection state change event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void--><!--Device-dataTransfer-function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionResult&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100099 |
