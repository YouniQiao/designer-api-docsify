# TypedArrayMapCallback

```TypeScript
type TypedArrayMapCallback<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => ElementType
```

ArkTS TypedArray转换映射函数类型。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ElementType | 是 |
| index | number | 是 |
| array | ArrayType | 是 |

**返回值：**

| 类型 |
| --- |
| ElementType |
