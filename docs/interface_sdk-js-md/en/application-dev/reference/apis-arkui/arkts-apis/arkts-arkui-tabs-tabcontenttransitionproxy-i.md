# TabContentTransitionProxy

Tabs自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画的起始和目标页面信息，同时，也可以通过调用该对象的finishTransition接口通知Tabs组件自定义动画已结束。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TabContentTransitionProxy--><!--Device-unnamed-export declare interface TabContentTransitionProxy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishTransition

```TypeScript
finishTransition(): void
```

通知Tabs组件，此页面的自定义动画已结束。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentTransitionProxy-finishTransition(): void--><!--Device-TabContentTransitionProxy-finishTransition(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## from

```TypeScript
from: int
```

自定义动画起始页面对应的index值，索引从0开始。取值范围为全体整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentTransitionProxy-from: int--><!--Device-TabContentTransitionProxy-from: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## to

```TypeScript
to: int
```

自定义动画目标页面对应的index值，索引从0开始。取值范围为全体整数。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabContentTransitionProxy-to: int--><!--Device-TabContentTransitionProxy-to: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

