# createPlainTextData

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createPlainTextData

```TypeScript
function createPlainTextData(text: string): PasteData
```

构建一个纯文本剪贴板内容对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [pasteboard.createData](arkts-basicservices-pasteboard-createdata-f.md#createdata)(mimeType:

<!--Device-pasteboard-function createPlainTextData(text: string): PasteData--><!--Device-pasteboard-function createPlainTextData(text: string): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 纯文本内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 剪贴板内容对象。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createPlainTextData('content');
```

