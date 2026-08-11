# TypedArrayForEachCallback

```TypeScript
type TypedArrayForEachCallback<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => void
```

ArkTS TypedArray遍历函数类型，被TypedArray类的'forEach'接口使用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void--><!--Device-collections-type TypedArrayForEachCallback<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ElementType | 是 |
| index | number | 是 |
| array | ArrayType | 是 |
