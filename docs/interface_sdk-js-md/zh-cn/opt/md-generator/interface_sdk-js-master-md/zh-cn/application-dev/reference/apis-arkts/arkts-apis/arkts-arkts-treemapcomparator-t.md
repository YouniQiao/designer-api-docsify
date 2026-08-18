# TreeMapComparator

```TypeScript
export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => number
```

TreeMap的比较器类型。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double--><!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| firstValue | K | 是 |
| secondValue | K | 是 |

**返回值：**

| 类型 |
| --- |
| number |
