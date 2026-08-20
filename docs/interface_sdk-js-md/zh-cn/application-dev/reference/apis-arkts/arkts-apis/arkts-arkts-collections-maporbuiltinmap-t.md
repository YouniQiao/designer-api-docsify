# MapOrBuiltinMap

```TypeScript
type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>
```

ArkTS Map接口参数类型，表示ArkTS Map或内建Map。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务API中使用。

<!--Device-collections-type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>--><!--Device-collections-type MapOrBuiltinMap<K, V> = Map<K, V> | BuiltinMap<K, V>-End-->

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| Map&lt;K, V&gt; | ArkTS Map. |
| BuiltinMap&lt;K, V&gt; | 内建Map. |

