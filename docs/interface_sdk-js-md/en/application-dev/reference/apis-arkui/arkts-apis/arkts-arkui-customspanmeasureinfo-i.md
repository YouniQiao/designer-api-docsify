# CustomSpanMeasureInfo

Defines the CustomSpanMeasureInfo interface.

**Since:** 12

<!--Device-unnamed-declare interface CustomSpanMeasureInfo--><!--Device-unnamed-declare interface CustomSpanMeasureInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## fontSize

```TypeScript
fontSize: number
```

Text font size.Unit: fp

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomSpanMeasureInfo-fontSize: number--><!--Device-CustomSpanMeasureInfo-fontSize: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutPolicy

```TypeScript
layoutPolicy?: LayoutPolicy
```

Width layout policy of the parent component of the custom span.  
**NOTE：**When the value is **null** or **undefined**, the parent component does not have a width layout policy set.

**Type:** LayoutPolicy

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomSpanMeasureInfo-layoutPolicy?: LayoutPolicy--><!--Device-CustomSpanMeasureInfo-layoutPolicy?: LayoutPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxWidth

```TypeScript
maxWidth?: number
```

Maximum width constraint of the custom span within the parent component's content area.Unit: px

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomSpanMeasureInfo-maxWidth?: number--><!--Device-CustomSpanMeasureInfo-maxWidth?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

