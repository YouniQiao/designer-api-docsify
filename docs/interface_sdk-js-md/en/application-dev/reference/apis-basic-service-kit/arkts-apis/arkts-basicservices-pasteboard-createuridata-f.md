# createUriData

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## createUriData

```TypeScript
function createUriData(uri: string): PasteData
```

构建一个URI剪贴板内容对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [pasteboard.createData](arkts-basicservices-pasteboard-createdata-f.md#createdata)(mimeType:

<!--Device-pasteboard-function createUriData(uri: string): PasteData--><!--Device-pasteboard-function createUriData(uri: string): PasteData-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | URI内容，需符合标准URI格式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PasteData](arkts-basicservices-pasteboard-pastedata-i.md) | 剪贴板内容对象。 |

## Examples

```TypeScript
let pasteData: pasteboard.PasteData = pasteboard.createUriData('dataability:///com.example.myapplication1/user.txt');
```

