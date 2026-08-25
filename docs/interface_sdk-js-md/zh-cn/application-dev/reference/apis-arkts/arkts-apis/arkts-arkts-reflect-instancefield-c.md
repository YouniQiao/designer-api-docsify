# InstanceField

表示类或接口的实例字段。

**继承/实现关系：** InstanceField extends Field

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [InstanceField](arkts-arkts-reflect-instancefield-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getValue

```TypeScript
getValue(thisObj: Object): Any
```

从该实例字段读取值。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| thisObj | Object | 是 |

**返回值：**

| 类型 |
| --- |
| Any |

## setValue

```TypeScript
setValue(thisObj: Object, value: Any): void
```

向该实例字段写入值。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| thisObj | Object | 是 |
| value | Any | 是 |
