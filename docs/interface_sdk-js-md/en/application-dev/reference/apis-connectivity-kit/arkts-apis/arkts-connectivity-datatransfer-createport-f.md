# createPort

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## createPort

```TypeScript
function createPort(uuid: string): void
```

Registers a port channel. A port channel can be used to connect to a remote device only after being registered. If the port channel is no longer needed after use, call [dataTransfer.destroyPort](arkts-connectivity-datatransfer-destroyport-f.md) to destroy it.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100020 |
| 36100021 |
| 36100043 |
| 36100044 |
| 36100099 |
