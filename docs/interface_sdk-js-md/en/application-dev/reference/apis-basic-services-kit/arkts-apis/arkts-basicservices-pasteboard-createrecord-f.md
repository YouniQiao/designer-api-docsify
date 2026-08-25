# createRecord

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createRecord

```TypeScript
function createRecord(mimeType: string, value: ValueType): PasteDataRecord
```

Creates a **PasteDataRecord** object of the specified type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
| value | [ValueType](arkts-basicservices-pasteboard-valuetype-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
