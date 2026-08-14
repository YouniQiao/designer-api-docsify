# offAdvertisingStateChange

## Modules to Import

```TypeScript
import { advertising } from 'advertising';
```

## offAdvertisingStateChange

```TypeScript
function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void
```

Unsubscribes from the advertising state change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void--><!--Device-advertising-function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | No | Callback used to listen for the advertising state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |

