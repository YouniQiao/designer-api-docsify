# NavigationAnimatedTransition

自定义转场动画协议，开发者需实现该协议来定义Navigation路由跳转的跳转动画。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface NavigationAnimatedTransition--><!--Device-unnamed-declare interface NavigationAnimatedTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTransitionEnd

```TypeScript
onTransitionEnd?: (success: boolean) => void
```

转场完成回调。

success：转场是否成功。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationAnimatedTransition-onTransitionEnd?: (success: boolean) => void--><!--Device-NavigationAnimatedTransition-onTransitionEnd?: (success: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| success | boolean | Yes |  |

## transition

```TypeScript
transition: (transitionProxy: NavigationTransitionProxy) => void
```

自定义转场动画执行回调。

transitionProxy：自定义转场动画代理对象。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationAnimatedTransition-transition: (transitionProxy: NavigationTransitionProxy) => void--><!--Device-NavigationAnimatedTransition-transition: (transitionProxy: NavigationTransitionProxy) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transitionProxy | [NavigationTransitionProxy](arkts-arkui-navigationtransitionproxy-i.md) | Yes |  |

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

<!--Device-NavigationAnimatedTransition-isInteractive?: boolean--><!--Device-NavigationAnimatedTransition-isInteractive?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timeout

```TypeScript
timeout?: number
```

动画超时结束时间。

单位：ms。

取值范围：[0, +∞)。

默认值：可交互动画无默认值，不可交互动画默认超时时间为1000ms。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NavigationAnimatedTransition-timeout?: number--><!--Device-NavigationAnimatedTransition-timeout?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

