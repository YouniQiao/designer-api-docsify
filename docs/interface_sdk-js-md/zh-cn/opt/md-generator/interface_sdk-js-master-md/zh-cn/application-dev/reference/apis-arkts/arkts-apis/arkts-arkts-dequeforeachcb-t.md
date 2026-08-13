# DequeForEachCb

```TypeScript
export type DequeForEachCb<T> = (value: T, index: number, deque: Deque<T>) => void
```

Deque中forEach方法的回调函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void--><!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| index | number | 是 |
| deque | [Deque](arkts-arkts-util-deque-deque-c.md)&lt;T&gt; | 是 |
