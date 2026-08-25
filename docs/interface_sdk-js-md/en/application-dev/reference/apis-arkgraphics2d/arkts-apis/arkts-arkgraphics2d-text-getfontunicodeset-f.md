# getFontUnicodeSet

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontUnicodeSet

```TypeScript
function getFontUnicodeSet(path: string | Resource, index: number) : Promise<Array<number>>
```

Obtains an array of font Unicode by font file path. This API uses a promise to return the result.An empty array is returned if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |
