# TypeError

表示操作无法执行时发生的错误，通常（但不限于）是因为 值的类型不符合预期。

**继承/实现关系：** TypeError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class TypeError--><!--Device-unnamed-export class TypeError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): TypeError
```

使用指定的错误信息和错误相关信息构造新的TypeError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError--><!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| TypeError | 新创建的TypeError实例。 |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用指定的错误信息和错误相关信息构造新的TypeError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

