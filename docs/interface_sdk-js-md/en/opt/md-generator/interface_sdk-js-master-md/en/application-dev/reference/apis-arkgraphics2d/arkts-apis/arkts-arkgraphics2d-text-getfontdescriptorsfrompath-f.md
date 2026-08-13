# getFontDescriptorsFromPath

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## getFontDescriptorsFromPath

```TypeScript
function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>
```

Obtains an array of font descriptors by font file path. This API uses a promise to return the result. > **NOTE：**> > - An empty array is returned if the font file is not found, the font file path is invalid, the font file does not > have the required permission, or the file is not in the font format. > > - The **weight** field in [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md#FontDescriptor) does not exactly correspond to the weight > value in the font file. Instead, the actual weight value in the font file is rounded off and mapped to the > [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md#FontWeight) enum value. For example, the weight value 350 in the font file is mapped to 4 > 00, and the corresponding enum value is W400.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-text-function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>--><!--Device-text-function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt;&gt; |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct GetFontDescriptorsFromPathTest {
  build() {
    Column({ space: 10 }) {
      Button("get fontDescriptors")
        .onClick(() => {
          let promise = text.getFontDescriptorsFromPath("file:///system/fonts/NotoSansCJK-Regular.ttc")
          promise.then((fontFullDescriptors) => {
            for (let index = 0; index < fontFullDescriptors.length; index++) {
              console.info("Path:" + fontFullDescriptors[index].path +
                          "\npostScriptName:" + fontFullDescriptors[index].postScriptName +
                          "\nfullName:" + fontFullDescriptors[index].fullName +
                          "\nfamilyName:" + fontFullDescriptors[index].fontFamily +
                          "\nfontSubName:" + fontFullDescriptors[index].fontSubfamily +
                          "\nweight:" + fontFullDescriptors[index].weight +
                          "\nwidth:" + fontFullDescriptors[index].width +
                          "\nitalic:" + fontFullDescriptors[index].italic +
                          "\nmonoSpace:" + fontFullDescriptors[index].monoSpace +
                          "\nsymbolic:" + fontFullDescriptors[index].symbolic)
            }
          })
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```
