# MenuGridStyleOptions

菜单栅格样式选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare interface MenuGridStyleOptions--><!--Device-unnamed-declare interface MenuGridStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: number
```

栅格中元素的数量。

默认值：3

取值范围：

当为上图下文形的栅格样式时，元素数量范围为[0, 6]。

当为纯图标形的栅格样式时，元素数量范围[0, 4]。 

未设置、异常值按照默认值处理。

**Type:** number

**Default:** 3

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MenuGridStyleOptions-count?: number--><!--Device-MenuGridStyleOptions-count?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## horizontalSize

```TypeScript
horizontalSize?: number
```

栅格中元素的水平尺寸，表示栅格内每行可显示的元素数量。

默认值：3

**说明：**

当为上图下文形的栅格样式时，水平尺寸范围为[1, 3]，即栅格行数为[1, 2]。

当为纯图标形的栅格样式时，水平尺寸范围为[1, 4]，即栅格行数为1。

未设置、异常值按照默认值处理。

**Type:** number

**Default:** 3

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MenuGridStyleOptions-horizontalSize?: number--><!--Device-MenuGridStyleOptions-horizontalSize?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position?: MenuGridPosition
```

栅格在菜单中的位置。

默认值：MenuGridPosition.TOP

**Type:** [MenuGridPosition](../arkts-apis/arkts-arkui-common-menugridposition-e.md)

**Default:** MenuGridPosition.TOP

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MenuGridStyleOptions-position?: MenuGridPosition--><!--Device-MenuGridStyleOptions-position?: MenuGridPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

