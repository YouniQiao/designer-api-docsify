# setCarKeyDfxData (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## setCarKeyDfxData

```TypeScript
function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void
```

Set the dfx data of car key.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void--><!--Device-connection-function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates device ID. For example, "11:22:33:AA:BB:FF". |
| action | [CarKeyActionType](arkts-connectivity-connection-carkeyactiontype-e-sys.md) | Yes | Indicates the action to set the data. |

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
    connection.setCarKeyDfxData('11:22:33:44:55:66', connection.CarKeyActionType.CAR_KEY_ACTION_ADD);
} catch (err) {
    console.error(`Failed to set car key dfx data. Code: ${err.code}, message: ${err.message}`);
}
```

<!--DelEnd-->
