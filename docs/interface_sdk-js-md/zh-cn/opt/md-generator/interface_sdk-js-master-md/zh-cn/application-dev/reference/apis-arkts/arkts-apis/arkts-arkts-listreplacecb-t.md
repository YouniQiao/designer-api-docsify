# ListReplaceCb

```TypeScript
export type ListReplaceCb<T> = (value: T, index: number, list: List<T>) => T
```

List的回调函数类型。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T--><!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | T | 是 |
| index | number | 是 |
| list | [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |
