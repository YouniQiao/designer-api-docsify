# ChainEdgeEffect (System API)

设置链式动效的边缘效果，用于决定列表滚动到边缘后继续拖动时列表项间距的变化方式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum ChainEdgeEffect--><!--Device-unnamed-declare enum ChainEdgeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## DEFAULT

```TypeScript
DEFAULT
```

默认效果，列表滚动到边缘以后继续拖动，拖拽方向上的列表项间距缩小，

拖拽反方向上的列表项间距扩大，适用于需要方向性拉伸、回弹反馈的场景。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainEdgeEffect-DEFAULT--><!--Device-ChainEdgeEffect-DEFAULT-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## STRETCH

```TypeScript
STRETCH
```

列表滚动到边缘以后继续拖动，所有列表项间距扩大，适用于需要所有列表项同步拉伸反馈的场景。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChainEdgeEffect-STRETCH--><!--Device-ChainEdgeEffect-STRETCH-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

