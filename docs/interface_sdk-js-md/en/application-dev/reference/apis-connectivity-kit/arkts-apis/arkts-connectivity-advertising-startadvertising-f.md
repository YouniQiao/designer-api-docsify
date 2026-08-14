# startAdvertising

## Modules to Import

```TypeScript
import { advertising } from 'advertising';
```

## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams): Promise<int>
```

Starts advertising.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function startAdvertising(advertisingParams: AdvertisingParams): Promise<int>--><!--Device-advertising-function startAdvertising(advertisingParams: AdvertisingParams): Promise<int>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advertisingParams | AdvertisingParams | Yes | Indicates the param for advertising. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Returns the promise object advertise handle. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100043 | Invalid UUID. |
| 36100040 | Integer out of range. |

