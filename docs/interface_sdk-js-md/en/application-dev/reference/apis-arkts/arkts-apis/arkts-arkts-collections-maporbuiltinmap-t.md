# MapOrBuiltinMap

```TypeScript
type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>
```

Defines the type for ArkTS Map APIs that accept either an ArkTS Map or a built-in Map.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-collections-type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>--><!--Device-collections-type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>-End-->

**System capability:** SystemCapability.Utils.Lang

| Type | Description |
| --- | --- |
| Map&lt;K, V&gt; | ArkTS Map. |
| BuiltinMap&lt;K, V&gt; | Built-in Map. |

