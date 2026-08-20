# InstanceField

表示类或接口的实例字段。

**继承/实现关系：** InstanceField extends Field

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-reflect-class InstanceField--><!--Device-reflect-class InstanceField-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## equals

```TypeScript
equals(other: InstanceField): boolean
```

检查当前实例字段是否与给定的实例字段相等。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-equals(other: InstanceField): boolean--><!--Device-InstanceField-equals(other: InstanceField): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [InstanceField](arkts-arkts-reflect-instancefield-c.md) | 是 | 用于与当前字段实例比较的另一个字段对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个实例字段相等则返回true，否则返回false。 |

## getValue

```TypeScript
getValue(thisObj: Object): Any
```

从该实例字段读取值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-getValue(thisObj: Object): Any--><!--Device-InstanceField-getValue(thisObj: Object): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | 作为`this`上下文的目标对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 从该实例字段读取的值。当thisobj为null时返回null； 当其为undefined时返回undefined。 |

## setValue

```TypeScript
setValue(thisObj: Object, value: Any): void
```

向该实例字段写入值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InstanceField-setValue(thisObj: Object, value: Any): void--><!--Device-InstanceField-setValue(thisObj: Object, value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thisObj | Object | 是 | 作为`this`上下文的目标对象。 |
| value | Any | 是 | 待写入的值。 |

