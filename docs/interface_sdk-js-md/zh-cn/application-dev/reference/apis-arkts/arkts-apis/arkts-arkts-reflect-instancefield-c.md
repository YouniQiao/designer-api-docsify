# InstanceField

Represents an instance field of a class or interface.

**继承/实现关系：** InstanceField extends [Field](Field)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-reflect-class InstanceField extends Field--><!--Device-reflect-class InstanceField extends Field-End-->

**系统能力：** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: InstanceField): boolean
```

Checks if the current instance field is equal to the given instance field.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-equals(other: InstanceField): boolean--><!--Device-InstanceField-equals(other: InstanceField): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [InstanceField](arkts-arkts-reflect-instancefield-c.md) | 是 | Another StaticField object to compare with the current StaticField instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the two instance fields are equal, otherwise returns false. |

## getValue

```TypeScript
getValue(thisObj: Object): Any
```

Reads the value from the instance field.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-getValue(thisObj: Object): Any--><!--Device-InstanceField-getValue(thisObj: Object): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | The target object as the `this` context. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | Returns the value read from the instance field.When thisobj is null, it returns null; when it is undefined, it returns undefined. |

## setValue

```TypeScript
setValue(thisObj: Object, value: Any): void
```

Writes a value to the instance field.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-setValue(thisObj: Object, value: Any): void--><!--Device-InstanceField-setValue(thisObj: Object, value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | The target object as the `this` context. |
| value | Any | 是 | The value to write. |

