# startSnoopCapture

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## startSnoopCapture

```TypeScript
function startSnoopCapture(): number
```

Start capturing HCI packet and returns a socket file descriptor carrying the real-time HCI data stream.

The data stream is encapsulated in the standard btsnoop format and can be forwarded to a PC for real-time parsing (for example, Wireshark). Multiple applications are not allowed to capture HCI packet simultaneously.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-access-function startSnoopCapture(): int--><!--Device-access-function startSnoopCapture(): int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the socket file descriptor carrying the real-time HCI data stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [204](../../errorcode-universal.md#204-access-denied-by-user-access-control-policy) | Access denied due to user access control policy. Possible causes: <br>1. The operation is restricted by the OS-account constraint; <br>2. The required privilege for the operation has not been granted. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900003 | Bluetooth disabled. |
| 2900020 | Another HCI sniffing session is in progress. |
| 2900099 | Operation failed. |
