# LinkedListForEachCb

```TypeScript
export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void
```

LinkedList的回调函数类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| index | int | 是 |
| linkedList | [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md)&lt;T&gt; | 是 |
