# StaticField

表示类的静态字段。

**继承/实现关系：** StaticField extends Field

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-reflect-class StaticField--><!--Device-reflect-class StaticField-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## equals

```TypeScript
equals(other: StaticField): boolean
```

判断当前静态字段对象是否与另一个对象相等。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-equals(other: StaticField): boolean--><!--Device-StaticField-equals(other: StaticField): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [StaticField](arkts-arkts-reflect-staticfield-c.md) | 是 | 待比较的另一个静态字段对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个对象相等则返回true，否则返回false。 |

## getValue

```TypeScript
getValue(): Any
```

从实例字段读取值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-getValue(): Any--><!--Device-StaticField-getValue(): Any-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Any | 字段值。 |

## setValue

```TypeScript
setValue(value: Any): void
```

向静态字段写入值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StaticField-setValue(value: Any): void--><!--Device-StaticField-setValue(value: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | 待写入的值。 |

