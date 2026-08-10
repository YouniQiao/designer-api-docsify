# Tuple

Marker interface for tuple types.

**继承/实现关系：** Tuple extends [Iterable<Any>](Iterable<Any>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Tuple extends Iterable<Any>--><!--Device-unnamed-export interface Tuple extends Iterable<Any>-End-->

**系统能力：** SystemCapability.Utils.Lang

## unsafeGet

```TypeScript
unsafeGet(index: int): Any
```

Get the element at the specified index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Tuple-unsafeGet(index: int): Any--><!--Device-Tuple-unsafeGet(index: int): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | the index of the element to get. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | the element at the specified index. |

## length

```TypeScript
readonly length: int
```

The number of elements in this tuple.The value should be an integer.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Tuple-readonly length: int--><!--Device-Tuple-readonly length: int-End-->

**系统能力：** SystemCapability.Utils.Lang

