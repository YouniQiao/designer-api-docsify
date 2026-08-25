# getSystemFontFullNamesByType

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getSystemFontFullNamesByType

```TypeScript
function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>
```

Obtains the full names of all fonts of the specified type. This API uses a promise to return the result.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontType | [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
