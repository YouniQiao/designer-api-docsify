# TypedArrayPredicateFn

```TypeScript
type TypedArrayPredicateFn<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => boolean
```

ArkTS TypedArray断言函数类型，被TypedArray类的'some'、'every'、'filter'、'find'和'findIndex'接口使用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

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
| boolean |
