# getCarKeyDfxData (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## getCarKeyDfxData

```TypeScript
function getCarKeyDfxData(): string
```

Get the dfx data of car key.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getCarKeyDfxData(): string--><!--Device-connection-function getCarKeyDfxData(): string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the dfx data in character string format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

<!--Del-->
**Examples**

```TypeScript
try {
    let dfxData = connection.getCarKeyDfxData();
} catch (err) {
    console.error(`Failed to get car key dfx data. Code: ${err.code}, message: ${err.message}`);
}
```

<!--DelEnd-->
