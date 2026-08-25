# isFontSupported

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## isFontSupported

```TypeScript
function isFontSupported(fontURL: string | Resource): boolean
```

Checks whether the system supports the specified font file. You can use this API to verify the availability of a font file before loading a custom font, preventing text rendering exceptions caused by unsupported fonts.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontURL | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
