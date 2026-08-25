# getFontDescriptorsFromPath

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontDescriptorsFromPath

```TypeScript
function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>
```

Obtains an array of font descriptors by font file path. This API uses a promise to return the result.

> **NOTE：**&gt;
> - An empty array is returned if the font file is not found, the font file path is invalid, the font file does not
> have the required permission, or the file is not in the font format.&gt;
> - The **weight** field in [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) does not exactly correspond to the weight
> value in the font file. Instead, the actual weight value in the font file is rounded off and mapped to the
> [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md) enum value. For example, the weight value 350 in the font file is mapped to 4
> 00, and the corresponding enum value is W400.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt;&gt; |
