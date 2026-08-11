# StackForEachCb

```TypeScript
export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void
```

The type of Stack callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void--><!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| index | int | Yes | The key of current element The value should be an integer. |
| stack | [Stack](../../apis-arkui/arkts-apis/arkts-arkui-typenode-stack-t.md)&lt;T&gt; | Yes | The Stack instance being traversed |

