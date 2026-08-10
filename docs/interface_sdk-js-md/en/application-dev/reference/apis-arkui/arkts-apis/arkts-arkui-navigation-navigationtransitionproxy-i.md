# NavigationTransitionProxy

自定义转场动画代理对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NavigationTransitionProxy--><!--Device-unnamed-export declare interface NavigationTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishTransition

```TypeScript
finishTransition(): void
```

结束本次自定义转场动画，开发者需要主动触发该方法来结束本次转场，否则系统会在timeout的时间后结束本次转场。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-finishTransition(): void--><!--Device-NavigationTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## updateTransition

```TypeScript
updateTransition?: UpdateTransitionCallback
```

更新交互转场动画进度(不可交互动画不支持动画进度设置)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-updateTransition?: UpdateTransitionCallback--><!--Device-NavigationTransitionProxy-updateTransition?: UpdateTransitionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cancelTransition

```TypeScript
cancelTransition?: VoidCallback
```

取消本次交互转场，恢复到页面跳转前的路由栈(不支持取消不可交互转场动画)。

**Type:** [VoidCallback](arkts-arkui-voidcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-cancelTransition?: VoidCallback--><!--Device-NavigationTransitionProxy-cancelTransition?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: NavContentInfo
```

退场页面信息。

**Type:** [NavContentInfo](../arkts-components/arkts-arkui-navcontentinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-from: NavContentInfo--><!--Device-NavigationTransitionProxy-from: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isInteractive

```TypeScript
isInteractive?: boolean
```

本次转场动画是否为可交互转场。true：本次转场动画是可交互转场；false：本次转场动画不是可交互转场。默认值： false。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-isInteractive?: boolean--><!--Device-NavigationTransitionProxy-isInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: NavContentInfo
```

进场页面信息。

**Type:** [NavContentInfo](../arkts-components/arkts-arkui-navcontentinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NavigationTransitionProxy-to: NavContentInfo--><!--Device-NavigationTransitionProxy-to: NavContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

