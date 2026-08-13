# createPlainTextData

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## createPlainTextData

```TypeScript
function createPlainTextData(text: string): PasteData
```

Creates a **PasteData** object of the plain text type.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [createData](arkts-basicservices-pasteboard-createdata-f.md#createData)(mimeType: string, value: ValueType)

<!--Device-pasteboard-function createPlainTextData(text: string): PasteData--><!--Device-pasteboard-function createPlainTextData(text: string): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
```
