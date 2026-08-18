# HashSetCbFn

```TypeScript
export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void
```

HashSet中forEach方法的回调函数。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void--><!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| key | T | 是 |
| set | [HashSet](arkts-arkts-util-hashset-hashset-c.md)&lt;T&gt; | 是 |
