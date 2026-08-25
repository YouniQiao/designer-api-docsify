# setCarKeyDfxData (System API)

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## setCarKeyDfxData

```TypeScript
function setCarKeyDfxData(deviceId: string, action: CarKeyActionType): void
```

Set the dfx data of car key.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| action | [CarKeyActionType](arkts-connectivity-connection-carkeyactiontype-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900003 |
| 2900099 |
