# ConcatArray

这是concatArray接口。

**继承/实现关系：** ConcatArray extends ArrayLike<T>

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ConcatArray--><!--Device-unnamed-export interface ConcatArray-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## at

```TypeScript
at(index: int): T | undefined
```

返回数组中指定索引处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-at(index: int): T | undefined--><!--Device-ConcatArray-at(index: int): T | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待返回元素的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| undefined | 指定索引处的元素，如果索引越界则返回undefined。 |

## join

```TypeScript
join(separator?: string): string
```

将数组的所有元素连接成一个字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-join(separator?: string): string--><!--Device-ConcatArray-join(separator?: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string | 否 | 在结果字符串中用于分隔数组相邻元素的字符串。 省略时，数组元素之间以逗号分隔。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 包含数组所有元素连接结果的字符串。 |

## slice

```TypeScript
slice(start?: int, end?: int): Array<T>
```

返回数组中一部分的浅拷贝，作为一个新数组。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>--><!--Device-ConcatArray-slice(start?: int, end?: int): Array<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | int | 否 | 切片的起始索引。如果为负数，则视为length + start。 <br>取值约束：应为整数。 |
| end | int | 否 | 切片的结束索引（不包含）。如果为负数，则视为length + end。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;T&gt; | 包含所提取元素的新数组。 |

