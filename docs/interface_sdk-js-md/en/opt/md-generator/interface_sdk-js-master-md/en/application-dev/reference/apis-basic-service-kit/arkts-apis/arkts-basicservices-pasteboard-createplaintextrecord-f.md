# createPlainTextRecord

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createPlainTextRecord

```TypeScript
function createPlainTextRecord(text: string): PasteDataRecord
```

Creates a **PasteDataRecord** object of the plain text type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [pasteboard.createRecord](arkts-basicservices-pasteboard-createrecord-f.md#createrecord)(mimeType:

<!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord--><!--Device-pasteboard-function createPlainTextRecord(text: string): PasteDataRecord-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteDataRecord](arkts-basicservices-pasteboard-pastedatarecord-i.md) |

## Examples

```TypeScript
let record: pasteboard.PasteDataRecord = pasteboard.createPlainTextRecord('hello');
```
