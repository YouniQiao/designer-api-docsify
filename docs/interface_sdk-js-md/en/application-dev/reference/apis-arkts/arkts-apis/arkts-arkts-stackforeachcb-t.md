# StackForEachCb

```TypeScript
export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void
```

Stack的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void--><!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前遍历到的元素。 |
| index | int | Yes | 当前遍历到的下标值。 该值为整数。 |
| stack | [Stack](../../apis-arkui/arkts-apis/arkts-arkui-typenode-stack-t.md)&lt;T&gt; | Yes | 当前正在遍历的Stack实例。 |

