# PlainArrayForEachCb

```TypeScript
export type PlainArrayForEachCb<T> = (value: T, key: number, PlainArray: PlainArray<T>) => void
```

PlainArray的回调函数类型。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void--><!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| key | number | 是 |
| [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md) | [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md)&lt;T&gt; | 是 |
