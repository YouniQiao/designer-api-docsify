# HashMapCbFn

```TypeScript
export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void
```

The type of HashMap callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void--><!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | V | Yes | The value of the current entry |
| key | K | Yes | The key of the current entry |
| map | [HashMap](arkts-arkts-util-hashmap-hashmap-c.md)&lt;K, V&gt; | Yes | The HashMap instance being traversed |

