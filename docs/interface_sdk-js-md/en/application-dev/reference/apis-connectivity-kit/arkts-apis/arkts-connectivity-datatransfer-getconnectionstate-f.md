# getConnectionState

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [ConnectionStateParams](arkts-connectivity-datatransfer-connectionstateparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConnectionState](arkts-connectivity-remotedevice-connectionstate-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100041 |
| 36100043 |
| 36100044 |
| 36100099 |
