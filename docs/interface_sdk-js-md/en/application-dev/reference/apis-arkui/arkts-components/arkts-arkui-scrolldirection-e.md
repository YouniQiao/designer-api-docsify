# ScrollDirection

滚动方向枚举。

FREE（自由滚动）模式下支持的能力：

> **说明：**
> 
> - `edgeEffect`属性仅支持`Spring`和`None`边缘滑动效果。
> 
> - `onWillScroll`回调仅支持在跟手滑动阶段重载偏移量。
> 
> - `onScrollEdge`回调只在到达边缘时触发一次，回弹后不会重复触发。
> 
> - 在抛滑动画过程中切换边缘模式不会打断动画。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum ScrollDirection--><!--Device-unnamed-declare enum ScrollDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Vertical

```TypeScript
Vertical
```

仅支持竖直方向滚动。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollDirection-Vertical--><!--Device-ScrollDirection-Vertical-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Horizontal

```TypeScript
Horizontal
```

仅支持水平方向滚动。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollDirection-Horizontal--><!--Device-ScrollDirection-Horizontal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Free

```TypeScript
Free
```

支持水平和垂直方向滚动

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [ScrollDirection#FREE](arkts-arkui-scrolldirection-e.md#free)

<!--Device-ScrollDirection-Free--><!--Device-ScrollDirection-Free-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None
```

不可滚动。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollDirection-None--><!--Device-ScrollDirection-None-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FREE

```TypeScript
FREE = 4
```

自由滚动。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollDirection-FREE = 4--><!--Device-ScrollDirection-FREE = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

