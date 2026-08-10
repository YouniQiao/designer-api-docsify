# ScrollSnapAnimationSpeed

设置列表项滚动限位动画速度。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare enum ScrollSnapAnimationSpeed--><!--Device-unnamed-declare enum ScrollSnapAnimationSpeed-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NORMAL

```TypeScript
NORMAL = 0
```

默认列表限位动画速度，适用于列表项主轴方向尺寸较大（如接近列表视口主轴尺寸），每次划动仅滚动一个列表项的场景。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollSnapAnimationSpeed-NORMAL = 0--><!--Device-ScrollSnapAnimationSpeed-NORMAL = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLOW

```TypeScript
SLOW = 1
```

列表限位动画速度低于NORMAL，适用于列表项主轴方向尺寸较小（如远小于列表视口主轴尺寸），每次划动需滚动多个列表项的场景。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollSnapAnimationSpeed-SLOW = 1--><!--Device-ScrollSnapAnimationSpeed-SLOW = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

