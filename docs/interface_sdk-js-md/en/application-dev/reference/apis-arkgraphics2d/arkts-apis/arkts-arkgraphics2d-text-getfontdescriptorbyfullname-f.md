# getFontDescriptorByFullName

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontDescriptorByFullName

```TypeScript
function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>
```

Obtains the font descriptor based on the font name and type. This API uses a promise to return the result.A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullName | string | Yes |
| fontType | [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
