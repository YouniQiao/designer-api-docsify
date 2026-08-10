# ScrollState

滑动状态枚举。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum ScrollState--><!--Device-unnamed-declare enum ScrollState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Idle

```TypeScript
Idle
```

空闲状态。滚动状态回归空闲时触发，控制器提供的无动画方法控制滚动时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ScrollState-Idle--><!--Device-ScrollState-Idle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Scroll

```TypeScript
Scroll
```

滚动状态。手指拖动List，拖动滚动条和滚动鼠标滚轮时触发。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ScrollState-Scroll--><!--Device-ScrollState-Scroll-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Fling

```TypeScript
Fling
```

惯性滚动状态。动画控制的滚动都会触发。包括快速划动松手后的惯性滚动，

划动到边缘回弹的滚动，快速拖动内置滚动条松手后的惯性滚动，

使用滚动控制器提供的带动画的方法控制的滚动。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ScrollState-Fling--><!--Device-ScrollState-Fling-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

