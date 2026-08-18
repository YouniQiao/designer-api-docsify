# getLocalName

## Modules to Import

```TypeScript
import { manager } from '@kit.ConnectivityKit';
```

## getLocalName

```TypeScript
function getLocalName(): string
```

Gets the local device's name.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getLocalName(): string--><!--Device-manager-function getLocalName(): string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the device's name. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

