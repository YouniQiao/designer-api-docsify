# ContentCoverOptions

继承自[BindOptions](arkts-arkui-bindoptions-i.md)。

全屏模态页面内容选项。

**Inheritance/Implementation:** ContentCoverOptions extends [BindOptions](arkts-arkui-bindoptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ContentCoverOptions extends BindOptions--><!--Device-unnamed-declare interface ContentCoverOptions extends BindOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSafeArea

```TypeScript
enableSafeArea?: boolean
```

全屏模态是否适配安全区域，true表示全屏模态适配安全区域，将内容限制在安全区内，避让导航条和状态栏，false表示不做处理，和之前的样式保持一致。默认值为false。

**Type:** boolean

**Default:** false

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ContentCoverOptions-enableSafeArea?: boolean--><!--Device-ContentCoverOptions-enableSafeArea?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modalTransition

```TypeScript
modalTransition?: ModalTransition
```

全屏模态页面的系统转场方式。

默认值：ModalTransition.DEFAULT。

**说明：**

与transition同时设置时，此属性不生效。

**Type:** [ModalTransition](arkts-arkui-modaltransition-e.md)

**Default:** ModalTransition.DEFAULT

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ContentCoverOptions-modalTransition?: ModalTransition--><!--Device-ContentCoverOptions-modalTransition?: ModalTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onWillDismiss

```TypeScript
onWillDismiss?: Callback<DismissContentCoverAction>
```

全屏模态页面交互式关闭回调函数。

**说明：**

当用户执行back事件关闭交互操作时，如果注册该回调函数，则不会立刻关闭。在回调函数中可以通过reason得到阻拦关闭页面的操作类型，从而根据原因选择是否关闭全屏模态页面。在onWillDismiss回调中，不能再做onWillDismiss拦截。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;DismissContentCoverAction&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContentCoverOptions-onWillDismiss?: Callback<DismissContentCoverAction>--><!--Device-ContentCoverOptions-onWillDismiss?: Callback<DismissContentCoverAction>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## transition

```TypeScript
transition?: TransitionEffect
```

全屏模态页面的自定义转场方式。

**Type:** [TransitionEffect](../arkts-apis/arkts-arkui-common-transitioneffect-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ContentCoverOptions-transition?: TransitionEffect--><!--Device-ContentCoverOptions-transition?: TransitionEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

