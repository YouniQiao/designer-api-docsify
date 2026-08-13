# createServer

## Modules to Import

```TypeScript
import { ssap } from '@kit.ConnectivityKit';
```

## createServer

```TypeScript
function createServer(): Server
```

Creates a SSAP server instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-ssap-function createServer(): Server--><!--Device-ssap-function createServer(): Server-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| Type | Description |
| --- | --- |
| Server | Returns a SSAP server instance { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100099 | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

