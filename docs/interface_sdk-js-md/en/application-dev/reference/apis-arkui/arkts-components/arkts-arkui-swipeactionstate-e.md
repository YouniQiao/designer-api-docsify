# SwipeActionState

列表项滑动状态枚举。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum SwipeActionState--><!--Device-unnamed-declare enum SwipeActionState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COLLAPSED

```TypeScript
COLLAPSED
```

收起状态，操作项处于隐藏状态。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeActionState-COLLAPSED--><!--Device-SwipeActionState-COLLAPSED-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## EXPANDED

```TypeScript
EXPANDED
```

展开状态，操作项处于显示状态。

**说明：**

需要ListItem设置划出操作项。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeActionState-EXPANDED--><!--Device-SwipeActionState-EXPANDED-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTIONING

```TypeScript
ACTIONING
```

长距离状态，当ListItem进入长距删除区后删除ListItem的状态。

**说明：**

actionAreaDistance的最终取值大于0，且小于ListItem在划动方向上的尺寸减去划出组件在划动方向上的尺寸时，滑动后松手的位置超过或等于该取值才能进入该状态。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SwipeActionState-ACTIONING--><!--Device-SwipeActionState-ACTIONING-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

