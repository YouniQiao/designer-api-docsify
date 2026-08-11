# ListComparatorFn

```TypeScript
export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => number
```

List中sort方法的回调函数。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => double--><!--Device-unnamed-export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| firstValue | T | 是 |
| secondValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| number |
