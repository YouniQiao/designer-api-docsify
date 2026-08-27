# getConnectionState

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## getConnectionState

```TypeScript
function getConnectionState(params: ConnectionStateParams): ConnectionState
```

Obtains the port channel connection state with a remote device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | Yes | Connection parameters of the port. |

**Return value:**

| Type | Description |
| --- | --- |
| ConnectionState | NearLink port channel connection state with a remote device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100041 | Invalid address. |
| 36100043 | Invalid UUID in connection parameters. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100099 | Operation failed. |
