# TreeMapForEachCb

```TypeScript
export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void
```

The type of TreeMap callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void--><!--Device-unnamed-export type TreeMapForEachCb<K, V> = (value: V, key: K, map: TreeMap<K, V>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | The value of current element  |
| key | K | Yes | The key of current element  |
| map | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;K, V&gt; | Yes | The TreeMap instance being traversed  |

