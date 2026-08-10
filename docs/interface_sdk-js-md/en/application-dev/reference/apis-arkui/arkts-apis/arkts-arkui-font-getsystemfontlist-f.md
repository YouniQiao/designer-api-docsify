# getSystemFontList

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## getSystemFontList

```TypeScript
function getSystemFontList(): Array<string>
```

获取系统字体列表。

该接口仅在PC/2in1设备上生效，在其他设备上返回空数组。

推荐使用[getSystemFontFullNamesByType](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-getsystemfontfullnamesbytype-f.md/arkts-arkgraphics2d-text-getsystemfontfullnamesbytype-f.md#getsystemfontfullnamesbytype)接口获取系统最新支持的字体列表数据。

> **说明：**
> 
> -getSystemFontList需要先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取
> [Font](arkts-arkui-uicontext.md)对象，然后通过该对象进行调用。且直接使用getSystemFontList可能导致
> [UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的问题。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getFont](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont)方法获取当前UI上下文关联的
> [Font](arkts-arkui-uicontext.md)对象。

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
| Array&lt;string&gt; | 系统的字体名列表。 |

## Examples

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

