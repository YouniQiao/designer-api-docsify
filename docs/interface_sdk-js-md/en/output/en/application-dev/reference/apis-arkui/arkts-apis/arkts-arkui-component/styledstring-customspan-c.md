# CustomSpan

Defines CustomSpan.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class CustomSpan--><!--Device-unnamed-export declare abstract class CustomSpan-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## invalidate

```TypeScript
invalidate(): void
```

Invalidate all components that use the object, which will cause a re-render of all components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomSpan-invalidate(): void--><!--Device-CustomSpan-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDraw

```TypeScript
abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void
```

Draw the custom span.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomSpan-abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void--><!--Device-CustomSpan-abstract onDraw(context: DrawContext, drawInfo: CustomSpanDrawInfo): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| drawInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

## onMeasure

```TypeScript
abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics
```

Measure the size of custom span.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomSpan-abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics--><!--Device-CustomSpan-abstract onMeasure(measureInfo: CustomSpanMeasureInfo): CustomSpanMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| measureInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - CustomSpan Size |

