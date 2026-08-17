# TreeSetForEachCb

```TypeScript
export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void
```

The type of TreeSet callback function.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void--><!--Device-unnamed-export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| key | T | Yes | The key of current element(same as value) |
| set | [TreeSet](arkts-arkts-util-treeset-treeset-c.md)&lt;T&gt; | Yes | The TreeSet instance being traversed |

