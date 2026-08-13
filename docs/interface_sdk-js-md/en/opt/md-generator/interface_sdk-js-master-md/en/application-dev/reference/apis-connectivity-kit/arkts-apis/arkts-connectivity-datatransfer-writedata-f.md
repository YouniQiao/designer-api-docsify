# writeData

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## writeData

```TypeScript
function writeData(params: DataParams): Promise<void>
```

Writes data by address and UUID.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function writeData(params: DataParams): Promise<void>--><!--Device-dataTransfer-function writeData(params: DataParams): Promise<void>-End-->

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100023 |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |
| 36100041 |
