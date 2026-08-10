# TabsCustomContentTransitionCallback

```TypeScript
export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)
```

自定义Tabs页面切换动画开始时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)--><!--Device-unnamed-export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | int | Yes | 动画开始时，当前页面的index值，索引从0开始。<br/> 取值范围为全体整数 取值限定为整数。取值约束:取值范围：[0, index-1] 当设置的值超过索引值或小于0时无转场动画。 |
| to | int | Yes | 动画开始时，目标页面的index值，索引从0开始。<br/> 取值范围为全体整数 取值限定为整数。取值约束:取值范围：[0,索引值] 当设置的值超过索引值或小于0时无转场动画。 |

**Return value:**

| Type | Description |
| --- | --- |
| (TabContentAnimatedTransition \| undefined) | Returns animated transition options of tab or undefined. |

