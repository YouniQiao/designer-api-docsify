# TabsCustomContentTransitionCallback

```TypeScript
export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)
```

Defines a tabs callback when customContentTransition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)--><!--Device-unnamed-export type TabsCustomContentTransitionCallback = (from: int, to: int) => (TabContentAnimatedTransition | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | int | Yes | The index value of the current tab when the animation begins. The value range is all integers The value should be an integer.Value constraint:Value range: [0, index-1] There is no transition animation when the set value exceeds the index value or is less than 0.  |
| to | int | Yes | The index value of the target tab when the animation begins. The value range is all integers The value should be an integer.Value constraint:Value range: [0, index] There is no transition animation when the set value exceeds the index value or is less than 0.  |

**Return value:**

| Type | Description |
| --- | --- |
| (TabContentAnimatedTransition \| undefined) | Returns animated transition options of tab or undefined. |

