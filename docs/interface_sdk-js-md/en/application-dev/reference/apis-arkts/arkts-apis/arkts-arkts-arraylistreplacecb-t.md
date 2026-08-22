# ArrayListReplaceCb

```TypeScript
export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T
```

The type of ArrayList callback function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T--><!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The current element being processed |
| index | int | Yes | The index of the current element |
| arrlist | [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; | Yes | The ArrayList instance being traversed |

**Return value:**

| Type | Description |
| --- | --- |
| T | This callback does not return a value |

