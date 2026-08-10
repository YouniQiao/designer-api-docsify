# Comparable

Can be implemented by any type that supports comparison.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface Comparable<in T>--><!--Device-unnamed-export interface Comparable<in T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## compareTo

```TypeScript
compareTo(to: T): int
```

Compares this instance to other object, treated as a `T`.The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Comparable-compareTo(to: T): int--><!--Device-Comparable-compareTo(to: T): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| to | T | 是 | the object to compare. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | the comparison result. |

