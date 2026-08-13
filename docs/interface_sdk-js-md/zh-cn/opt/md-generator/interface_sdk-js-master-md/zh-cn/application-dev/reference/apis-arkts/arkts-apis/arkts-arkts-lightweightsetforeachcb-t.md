# LightWeightSetForEachCb

```TypeScript
export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void
```

LightWeightSet的回调函数类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void--><!--Device-unnamed-export type LightWeightSetForEachCb<T> = (value: T, key: T, set: LightWeightSet<T>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| key | T | 是 |
| set | [LightWeightSet](arkts-arkts-util-lightweightset-lightweightset-c.md)&lt;T&gt; | 是 |
