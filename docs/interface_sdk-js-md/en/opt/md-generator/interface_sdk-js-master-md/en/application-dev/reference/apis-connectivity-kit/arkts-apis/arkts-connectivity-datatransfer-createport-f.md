# createPort

## Modules to Import

```TypeScript
import { dataTransfer } from '@kit.ConnectivityKit';
```

## createPort

```TypeScript
function createPort(uuid: string): void
```

Creates a NearLink listening port that can receive data by UUID.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-dataTransfer-function createPort(uuid: string): void--><!--Device-dataTransfer-function createPort(uuid: string): void-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 36100020 |
| 36100021 |
| 36100003 |
| 36100099 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 36100044 |
| 36100043 |
