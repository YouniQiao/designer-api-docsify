# CustomSpan

Describes the custom span. Only the base class is provided. You need to define the specific implementation. The drag preview of a custom span is blank.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare abstract class CustomSpan--><!--Device-unnamed-declare abstract class CustomSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## invalidate

```TypeScript
invalidate(): void
```

Manually triggers a refresh of the **Text** component that uses this **CustomSpan**.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CustomSpan-invalidate(): void--><!--Device-CustomSpan-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDraw

```TypeScript
abstract onDraw(context: DrawContext,  drawInfo: CustomSpanDrawInfo): void
```

Called to draw a custom span.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomSpan-abstract onDraw(context: DrawContext,  drawInfo: CustomSpanDrawInfo): void--><!--Device-CustomSpan-abstract onDraw(context: DrawContext,  drawInfo: CustomSpanDrawInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [DrawContext](../../apis-na/arkts-apis/arkts-na-graphics-drawcontext-c.md) | Yes |
| drawInfo | [CustomSpanDrawInfo](arkts-arkui-customspandrawinfo-i.md) | Yes |

## onMeasure

```TypeScript
abstract onMeasure(measureInfo: CustomSpanMeasureInfo) : CustomSpanMetrics
```

Called to obtain the size of a custom span.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomSpan-abstract onMeasure(measureInfo: CustomSpanMeasureInfo) : CustomSpanMetrics--><!--Device-CustomSpan-abstract onMeasure(measureInfo: CustomSpanMeasureInfo) : CustomSpanMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| measureInfo | [CustomSpanMeasureInfo](arkts-arkui-customspanmeasureinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CustomSpanMetrics](arkts-arkui-customspanmetrics-i.md) |
