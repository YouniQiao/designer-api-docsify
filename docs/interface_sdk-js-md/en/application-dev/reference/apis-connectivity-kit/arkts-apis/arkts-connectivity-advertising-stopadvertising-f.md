# stopAdvertising

## Modules to Import

```TypeScript
import { advertising } from '@kit.ConnectivityKit';
```

## stopAdvertising

```TypeScript
function stopAdvertising(advertisingId: int): Promise<void>
```

Stops advertising with advertising ID.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>--><!--Device-advertising-function stopAdvertising(advertisingId: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advertisingId | int | Yes | Indicates the ID for this advertising &lt;br&gt;The value must be an integer greater than or equal to 0, The value is the current advertising ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 36100040 | Invalid advertising ID. |

