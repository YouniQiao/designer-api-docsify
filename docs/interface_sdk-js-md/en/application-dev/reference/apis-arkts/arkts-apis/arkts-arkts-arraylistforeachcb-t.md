# ArrayListForEachCb

```TypeScript
export type ArrayListForEachCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => void
```

ArrayList中forEach方法的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ArrayListForEachCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => void--><!--Device-unnamed-export type ArrayListForEachCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前遍历到的元素。 |
| index | int | Yes | 当前遍历到的下标值。 |
| arrlist | [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; | Yes | 当前调用forEach方法的实例对象。 |

