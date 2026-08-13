# offAdvertisingStateChange

## Modules to Import

```TypeScript
import { advertising } from '@kit.ConnectivityKit';
```

## offAdvertisingStateChange

```TypeScript
function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void
```

Unsubscribes from the advertising state change event.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void--><!--Device-advertising-function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
