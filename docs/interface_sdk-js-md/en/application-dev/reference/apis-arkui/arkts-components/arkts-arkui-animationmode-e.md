# AnimationMode

点击[TabBar](../arkts-apis/arkts-arkui-tabcontent-tabcontentattribute-i.md/arkts-arkui-tabcontent-tabcontentattribute-i.md#tabbar)页签时切换TabContent的动画形式枚举。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare enum AnimationMode--><!--Device-unnamed-declare enum AnimationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_FIRST

```TypeScript
CONTENT_FIRST = 0
```

先加载目标页内容，再开始切换动画。适用于需要先确保内容加载完成再展示动画的场景，可避免动画过程中出现空白内容，推荐用于内容加载较快、需要平滑过渡的场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimationMode-CONTENT_FIRST = 0--><!--Device-AnimationMode-CONTENT_FIRST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTION_FIRST

```TypeScript
ACTION_FIRST = 1
```

先开始切换动画，再加载目标页内容；生效需要同时需要满足：Tabs的height、width没有设置成auto。适用于需要立即响应用户操作、快速开始动画的场景，推荐用于内容加载较慢但希望提供快速视觉反馈的场景。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimationMode-ACTION_FIRST = 1--><!--Device-AnimationMode-ACTION_FIRST = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NO_ANIMATION

```TypeScript
NO_ANIMATION = 2
```

关闭默认动画。调用TabsController的[changeIndex](arkts-arkui-tabscontroller-c.md#changeindex)接口切换TabContent时该枚举值不生效。

可以通过设置[animationDuration](TabsAttribute#animationDuration)为0实现调用TabsController的changeIndex接口时不带动画。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimationMode-NO_ANIMATION = 2--><!--Device-AnimationMode-NO_ANIMATION = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_FIRST_WITH_JUMP

```TypeScript
CONTENT_FIRST_WITH_JUMP = 3
```

先加载目标页内容，再无动画跳转到目标页附近，最后有动画跳转到目标页。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AnimationMode-CONTENT_FIRST_WITH_JUMP = 3--><!--Device-AnimationMode-CONTENT_FIRST_WITH_JUMP = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ACTION_FIRST_WITH_JUMP

```TypeScript
ACTION_FIRST_WITH_JUMP = 4
```

先无动画跳转到目标页附近，再有动画跳转到目标页，最后加载目标页内容。此项生效需要同时需要满足：Tabs的height、width没有设置成auto。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AnimationMode-ACTION_FIRST_WITH_JUMP = 4--><!--Device-AnimationMode-ACTION_FIRST_WITH_JUMP = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

