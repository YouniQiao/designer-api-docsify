# TypedArrayFromMapFn

```TypeScript
type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType
```

ArkTS TypedArray映射函数类型。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-collections-type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType--><!--Device-collections-type TypedArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | FromElementType | 是 |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| ToElementType |
