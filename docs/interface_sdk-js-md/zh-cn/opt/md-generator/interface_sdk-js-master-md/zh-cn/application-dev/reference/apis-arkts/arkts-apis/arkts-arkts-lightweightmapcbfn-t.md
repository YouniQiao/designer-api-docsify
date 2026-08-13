# LightWeightMapCbFn

```TypeScript
export type LightWeightMapCbFn<K, V> = (value: V, key: K, map: LightWeightMap<K, V>) => void
```

LightWeightMap中forEach方法的回调函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type LightWeightMapCbFn<K, V> = (value: V, key: K, map: LightWeightMap<K, V>) => void--><!--Device-unnamed-export type LightWeightMapCbFn<K, V> = (value: V, key: K, map: LightWeightMap<K, V>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | V | 是 |
| key | K | 是 |
| map | [LightWeightMap](arkts-arkts-util-lightweightmap-lightweightmap-c.md)&lt;K, V&gt; | 是 |
