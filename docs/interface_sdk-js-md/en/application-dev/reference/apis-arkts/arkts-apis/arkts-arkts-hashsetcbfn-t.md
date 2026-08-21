# HashSetCbFn

```TypeScript
export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void
```

The type of HashSet callback function.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void--><!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The current element being processed |
| key | T | Yes | [Deprecated] HashSet does not use key-value pairs, this parameter exists only for API compatibility |
| set | [HashSet](arkts-arkts-utilhashset-hashset-c.md)&lt;T&gt; | Yes | The HashSet instance being traversed |

