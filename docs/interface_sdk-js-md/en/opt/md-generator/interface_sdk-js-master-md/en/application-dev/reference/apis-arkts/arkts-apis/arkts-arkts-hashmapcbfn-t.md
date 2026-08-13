# HashMapCbFn

```TypeScript
export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void
```

The type of HashMap callback function.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void--><!--Device-unnamed-export type HashMapCbFn<K, V> = (value: V, key: K, map: HashMap<K, V>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | V | Yes |
| key | K | Yes |
| map | [HashMap](arkts-arkts-util-hashmap-hashmap-c.md)&lt;K, V&gt; | Yes |
