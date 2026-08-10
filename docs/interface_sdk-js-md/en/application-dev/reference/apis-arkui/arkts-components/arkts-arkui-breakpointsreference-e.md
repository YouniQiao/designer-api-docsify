# BreakpointsReference

设置栅格容器组件的断点参照物。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare enum BreakpointsReference--><!--Device-unnamed-declare enum BreakpointsReference-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WindowSize

```TypeScript
WindowSize = 0
```

以窗口为参照。断点计算基于应用窗口尺寸，适用于需要根据窗口整体大小变化进行响应式布局的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BreakpointsReference-WindowSize = 0--><!--Device-BreakpointsReference-WindowSize = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ComponentSize

```TypeScript
ComponentSize = 1
```

以容器为参照。断点计算基于GridRow组件自身尺寸，适用于需要根据组件容器尺寸变化进行响应式布局的场景，例如GridRow嵌套在其他容器中时。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BreakpointsReference-ComponentSize = 1--><!--Device-BreakpointsReference-ComponentSize = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

