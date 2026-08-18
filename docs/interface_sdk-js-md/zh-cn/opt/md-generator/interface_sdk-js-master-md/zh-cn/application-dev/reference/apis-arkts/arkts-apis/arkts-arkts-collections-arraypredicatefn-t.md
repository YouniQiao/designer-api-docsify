# ArrayPredicateFn

```TypeScript
type ArrayPredicateFn<ElementType, ArrayType> =
    (value: ElementType, index: number, array: ArrayType) => boolean
```

ArkTS Array断言函数类型，被Array类的'some'和'every'接口使用，用来判断数组元素是否满足测试条件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-collections-type ArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean--><!--Device-collections-type ArrayPredicateFn<ElementType, ArrayType> =    (value: ElementType, index: number, array: ArrayType) => boolean-End-->

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
