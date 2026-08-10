# LayoutMode

页签内容排布方式枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum LayoutMode--><!--Device-unnamed-declare enum LayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

若页签宽度大于104vp，页签内容为左右排布（图标在左，文字在右），否则页签内容为上下排布（图标在上，文字在下）。仅TabBar为垂直模式或Fixed水平模式时有效。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutMode-AUTO = 0--><!--Device-LayoutMode-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## VERTICAL

```TypeScript
VERTICAL = 1
```

页签内容上下排布，图标在上，文字在下。适用于页签宽度有限、需要节省空间的场景。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutMode-VERTICAL = 1--><!--Device-LayoutMode-VERTICAL = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## HORIZONTAL

```TypeScript
HORIZONTAL = 2
```

页签内容左右排布，图标在左，文字在右。适用于页签宽度充足、需要展示更多内容的场景。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LayoutMode-HORIZONTAL = 2--><!--Device-LayoutMode-HORIZONTAL = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

