# createHtmlData

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createHtmlData

```TypeScript
function createHtmlData(htmlText: string): PasteData
```

Creates a **PasteData** object of the HTML type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [createData](arkts-basicservices-pasteboard-createdata-f.md)(mimeType: string, value: ValueType)

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [htmlText](arkts-basicservices-pasteboard-pastedatarecord-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) |
