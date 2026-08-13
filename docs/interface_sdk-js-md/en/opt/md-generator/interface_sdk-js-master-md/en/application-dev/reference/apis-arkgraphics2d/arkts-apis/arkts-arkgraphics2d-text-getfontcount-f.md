# getFontCount

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## getFontCount

```TypeScript
function getFontCount(path: string | Resource) : number
```

Obtains the number of font files contained in a font file based on the font file path. Returns **0** if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-text-function getFontCount(path: string | Resource) : int--><!--Device-text-function getFontCount(path: string | Resource) : int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct GetFontCountTest {
  build() {
    Column({ space: 10 }) {
      Button("get fontCount")
        .onClick(() => {
          let fontCount = text.getFontCount("file:///system/fonts/NotoSansCJK-Regular.ttc")
          console.info("file count: " + fontCount)
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```
