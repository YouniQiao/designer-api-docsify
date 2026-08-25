# matchFontDescriptors

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## matchFontDescriptors

```TypeScript
function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>
```

Obtains all system font descriptors that match the provided font descriptor. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| desc | [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
