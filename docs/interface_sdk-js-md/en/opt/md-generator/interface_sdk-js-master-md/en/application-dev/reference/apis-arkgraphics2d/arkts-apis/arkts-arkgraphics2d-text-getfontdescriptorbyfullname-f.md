# getFontDescriptorByFullName

## Modules to Import

```TypeScript
```

## getFontDescriptorByFullName

```TypeScript
function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>
```

Obtains the font descriptor based on the font name and type. This API uses a promise to return the result. A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-text-function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>--><!--Device-text-function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>-End-->

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

**Examples**

```TypeScript
import { text } from '@kit.ArkGraphics2D'
import { BusinessError } from '@kit.BasicServicesKit'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("get fontDescriptor")
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .width(300)
          .height(80)
          .onClick(() => {
            let fontType:text.SystemFontType = text.SystemFontType.GENERIC
            let promise = text.getFontDescriptorByFullName("HarmonyOS Sans", fontType)
            promise.then((fontDescriptor) => {
              console.info(`desc: ${JSON.stringify(fontDescriptor)}`)
            }).catch((error: BusinessError) => {
              console.error(`Failed to get fontDescriptor by fullName, error: ${JSON.stringify(error)}`);
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
