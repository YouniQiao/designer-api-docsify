# MeasureText

Defines the Measure interface.

**Since:** 9

<!--Device-unnamed-export default class MeasureText--><!--Device-unnamed-export default class MeasureText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MeasureOptions } from '@kit.ArkUI';
```

## measureText

```TypeScript
static measureText(options: MeasureOptions): number
```

Measures the single-line display width of the specified text. For multi-line text (separated by newline characters  
**\n**), this API returns the width of the longest line.

> **NOTE：**
> 
> - Since API version 12, you can use the
> [getMeasureUtils](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils12) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [MeasureUtils](@ohos.arkui.UIContext) object
> associated with the current UI context.
> 
> - **measureText** always measures single-line text width. Layout constraints in **options** (**constraintWidth**,
> **maxLines**, and more) do not affect results. For layout-constrained width measurement, use
> [measureTextSize](../../../reference/apis-arkui/arkts-apis-uicontext-measureutils.md#measuretextsize12).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [measureText](ohos.arkui.UIContext.MeasureUtils#measureText)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MeasureText-static measureText(options: MeasureOptions): number--><!--Device-MeasureText-static measureText(options: MeasureOptions): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State textWidth: number = MeasureText.measureText({
    // You are advised to use this.getUIContext().getMeasureUtils().measureText().
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(`The width of 'Hello World': ${this.textWidth}`)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## measureTextSize

```TypeScript
static measureTextSize(options: MeasureOptions): SizeOptions
```

Measures the width and height of the given text.

> **NOTE：**
> 
> - Since API version 12, you can use the
> [getMeasureUtils](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils12) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [MeasureUtils](@ohos.arkui.UIContext) object
> associated with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [measureTextSize](ohos.arkui.UIContext.MeasureUtils#measureTextSize)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MeasureText-static measureTextSize(options: MeasureOptions): SizeOptions--><!--Device-MeasureText-static measureTextSize(options: MeasureOptions): SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeOptions](arkts-arkui-sizeoptions-i.md) |

## Examples

```TypeScript
import { MeasureText } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  textSize: SizeOptions = MeasureText.measureTextSize({
    // You are advised to use this.getUIContext().getMeasureUtils().measureTextSize().
    textContent: "Hello World",
    fontSize: '50px'
  });

  build() {
    Row() {
      Column() {
        Text(`The width of 'Hello World': ${this.textSize.width}`)
        Text(`The height of 'Hello World': ${this.textSize.height}`)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
