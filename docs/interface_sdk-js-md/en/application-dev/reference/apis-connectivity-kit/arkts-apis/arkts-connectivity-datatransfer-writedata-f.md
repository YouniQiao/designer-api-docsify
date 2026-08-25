# writeData

## Modules to Import

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [DataParams](arkts-connectivity-datatransfer-dataparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100003 |
| 36100023 |
| 36100041 |
| 36100043 |
| 36100044 |
| 36100099 |
