# QueueForEachCb

```TypeScript
export type QueueForEachCb<T> = (value: T, index: number, queue: Queue<T>) => void
```

Queue的回调函数类型。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void--><!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| index | number | 是 |
| queue | [Queue](arkts-arkts-util-queue-queue-c.md)&lt;T&gt; | 是 |
