# TabsCustomContentTransitionCallback

```TypeScript
declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined
```

自定义Tabs页面切换动画开始时触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined--><!--Device-unnamed-declare type TabsCustomContentTransitionCallback = (from: number, to: number) => TabContentAnimatedTransition | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | number | Yes | 动画开始时，当前页面的index值，索引从0开始。<br/>取值范围：[0, 页签总数-1]，当设置的值超过索引值或小于0时无转场动画。 |
| to | number | Yes | 动画开始时，目标页面的index值，索引从0开始。<br/>取值范围：[0, 页签总数-1]，当设置的值超过索引值或小于0时无转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TabContentAnimatedTransition](../arkts-apis/arkts-arkui-tabs-tabcontentanimatedtransition-i.md) \| undefined | Information about the custom tab switching animation. |

