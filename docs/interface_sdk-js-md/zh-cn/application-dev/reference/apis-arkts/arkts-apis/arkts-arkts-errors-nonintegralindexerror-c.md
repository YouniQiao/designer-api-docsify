# NonIntegralIndexError

表示对索引表达式执行数值类型转换且小数部分不为0时 发生的错误。

**继承/实现关系：** NonIntegralIndexError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class NonIntegralIndexError--><!--Device-unnamed-export class NonIntegralIndexError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError
```

使用指定的错误信息和错误相关信息构造新的NonIntegralIndexError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NonIntegralIndexError-static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError--><!--Device-NonIntegralIndexError-static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NonIntegralIndexError](arkts-arkts-errors-nonintegralindexerror-c.md) | 新创建的NonIntegralIndexError实例。 |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用指定的错误信息和错误相关信息构造新的NonIntegralIndexError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NonIntegralIndexError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NonIntegralIndexError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

