# writeData

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## writeData

```TypeScript
function writeData(params: DataParams): Promise<void>
```

Sends data to a remote device using the device address and UUID. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [DataParams](arkts-connectivity-datatransfer-dataparams-i.md) | Yes | Parameters for sending data, including the remote device address, service UUID, and data packet to send. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100023 | Data transmission congested. |
| 36100041 | Invalid address. |
| 36100043 | Invalid UUID. |
| 36100044 | NearLink standard UUID not allowed. |
| 36100099 | Operation failed. |
