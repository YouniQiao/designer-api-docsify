# MeasureText

Defines the Measure interface.

**Since:** 9

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MeasureText, MeasureOptions } from 'kits/@kit.ArkUI';
```

## measureText

```TypeScript
static measureText(options: MeasureOptions): number
```

Measures the single-line display width of the specified text. For multi-line text (separated by newline characters **\n**), this API returns the width of the longest line.

> **NOTE：**&gt;
> - Since API version 12, you can use the
> [getMeasureUtils](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [MeasureUtils](arkts-arkui-arkui-uicontext-uicontext-c.md) object
> associated with the current UI context.&gt;
> - **measureText** always measures single-line text width. Layout constraints in **options** (**constraintWidth**,
> **maxLines**, and more) do not affect results. For layout-constrained width measurement, use
> [measureTextSize](../../../reference/apis-arkui/arkts-apis-uicontext-measureutils.md#measuretextsize12).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** measureText

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## measureTextSize

```TypeScript
static measureTextSize(options: MeasureOptions): SizeOptions
```

Measures the width and height of the given text.

> **NOTE：**&gt;
> - Since API version 12, you can use the
> [getMeasureUtils](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [MeasureUtils](arkts-arkui-arkui-uicontext-uicontext-c.md) object
> associated with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** measureTextSize

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SizeOptions](arkts-arkui-sizeoptions-i.md) |
