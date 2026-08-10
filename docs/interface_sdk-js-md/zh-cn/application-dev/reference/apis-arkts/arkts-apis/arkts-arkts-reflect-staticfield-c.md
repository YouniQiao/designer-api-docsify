# StaticField

Represents static field of class

**继承/实现关系：** StaticField extends [Field](Field)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-reflect-class StaticField extends Field--><!--Device-reflect-class StaticField extends Field-End-->

**系统能力：** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: StaticField): boolean
```

Determine whether the current Static Field object is equal to another object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-equals(other: StaticField): boolean--><!--Device-StaticField-equals(other: StaticField): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StaticField](arkts-arkts-reflect-staticfield-c.md) | 是 | Another Static Field object to compare. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | If two objects are equal, return true; otherwise, return false. |

## getValue

```TypeScript
getValue(): Any
```

Reads value from an instance field.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-getValue(): Any--><!--Device-StaticField-getValue(): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | field value. |

## setValue

```TypeScript
setValue(value: Any): void
```

Writes value into a static field.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-setValue(value: Any): void--><!--Device-StaticField-setValue(value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | value to write. |

