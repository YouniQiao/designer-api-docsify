# stopSnoopCapture

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## stopSnoopCapture

```TypeScript
function stopSnoopCapture(): void
```

Stop capturing HCI packet.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-access-function stopSnoopCapture(): void--><!--Device-access-function stopSnoopCapture(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [204](../../errorcode-universal.md#204-access-denied-by-user-access-control-policy) | Access denied due to user access control policy. Possible causes: <br>1. The operation is restricted by the OS-account constraint; <br>2. The required privilege for the operation has not been granted. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900003 | Bluetooth disabled. |
| 2900021 | The HCI capture session is initiated by another application. |
| 2900099 | Operation failed. |
