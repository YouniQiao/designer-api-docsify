# Tuple

元组类型的标记接口。

**继承/实现关系：** Tuple extends Iterable<Any>

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Tuple--><!--Device-unnamed-export interface Tuple-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## unsafeGet

```TypeScript
unsafeGet(index: int): Any
```

获取指定索引处的元素。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Tuple-unsafeGet(index: int): Any--><!--Device-Tuple-unsafeGet(index: int): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待获取元素的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 指定索引处的元素。 |

## length

```TypeScript
readonly length: int
```

该元组中的元素个数。 取值约束：应为整数。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Tuple-readonly length: int--><!--Device-Tuple-readonly length: int-End-->

**系统能力：** SystemCapability.Utils.Lang

