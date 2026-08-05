# HashMapCbFn

```TypeScript
export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void
```

The type of HashMap callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void--><!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | The value of the current entry  |
| key | K | Yes | The key of the current entry  |
| map | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;K, V&gt; | Yes | The HashMap instance being traversed  |

