# getSystemFontList

## getSystemFontList

```TypeScript
function getSystemFontList(): Array<string>
```

Obtains this system font list. This API only takes effect on PCs/2-in-1 devices and returns an empty array on other devices. You are advised to use the [getSystemFontFullNamesByType]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API to obtain the latest system-supported font list data. > **NOTE** > > - Since API version 10, you can use the > \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ API in > [UIContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to obtain the [Font]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ object associated with > the current UI context.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.Font#getSystemFontList

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-font-function getSystemFontList(): Array<string>--><!--Device-font-function getSystemFontList(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | List of supported fonts. |

**Example**

```TypeScript
// xxx.ets
import { font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  fontList: Array<string> = new Array<string>();

  build() {
    Column() {
      Button("getSystemFontList")
        .width('60%')
        .height('6%')
        .onClick(() => {
          this.fontList = font.getSystemFontList(); // You are advised to use the this.getUIContext().getFont().getSystemFontList() API.
        })
    }.width('100%')
  }
}
```

