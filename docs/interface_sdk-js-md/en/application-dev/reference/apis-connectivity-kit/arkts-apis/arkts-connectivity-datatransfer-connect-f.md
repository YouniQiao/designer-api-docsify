# connect

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## connect

```TypeScript
function connect(params: ConnectionParams): Promise<void>
```

Connects to a server. If the connection is successful, data can be sent to the server.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function connect(params: ConnectionParams): Promise<void>--><!--Device-dataTransfer-function connect(params: ConnectionParams): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ConnectionParams](arkts-connectivity-datatransfer-connectionparams-i.md) | Yes | Indicates the connection params. |

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
| 36100044 | NearLink standard UUID not allowed. |
| 36100043 | Invalid UUID. |
| 36100041 | Invalid address. |

