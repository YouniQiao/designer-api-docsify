# NavigationTransitionProxy

自定义转场动画代理对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface NavigationTransitionProxy--><!--Device-unnamed-declare interface NavigationTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelTransition

```TypeScript
cancelTransition?(): void
```

取消本次交互转场，恢复到页面跳转前的路由栈(不支持取消不可交互转场动画)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-cancelTransition?(): void--><!--Device-NavigationTransitionProxy-cancelTransition?(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishTransition

```TypeScript
finishTransition(): void
```

结束本次自定义转场动画，开发者需要主动触发该方法来结束本次转场，否则系统会在timeout的时间后结束本次转场。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-finishTransition(): void--><!--Device-NavigationTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateTransition

```TypeScript
updateTransition?(progress: number): void
```

更新交互转场动画进度(不可交互动画不支持动画进度设置)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-updateTransition?(progress: number): void--><!--Device-NavigationTransitionProxy-updateTransition?(progress: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | number | Yes | 设置交互转场动画进度值。取值范围：[0, 1] |

## from

```TypeScript
from: NavContentInfo
```

退场页面信息。

**Type:** [NavContentInfo](arkts-arkui-navcontentinfo-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-from: NavContentInfo--><!--Device-NavigationTransitionProxy-from: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isInteractive

```TypeScript
isInteractive?: boolean
```

本次转场动画是否为可交互转场。

true：本次转场动画是可交互转场；false：本次转场动画不是可交互转场。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-isInteractive?: boolean--><!--Device-NavigationTransitionProxy-isInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: NavContentInfo
```

进场页面信息。

**Type:** [NavContentInfo](arkts-arkui-navcontentinfo-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationTransitionProxy-to: NavContentInfo--><!--Device-NavigationTransitionProxy-to: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

