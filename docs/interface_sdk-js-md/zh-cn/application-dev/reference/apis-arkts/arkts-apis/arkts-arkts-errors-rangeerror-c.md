# RangeError

表示传入的集合索引超出范围时发生的错误。

**继承/实现关系：** RangeError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class RangeError--><!--Device-unnamed-export class RangeError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): RangeError
```

使用指定的错误信息和错误相关信息构造新的RangeError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangeError-static $_invoke(message?: string, options?: ErrorOptions): RangeError--><!--Device-RangeError-static $_invoke(message?: string, options?: ErrorOptions): RangeError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RangeError |  |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用指定的错误信息和错误相关信息构造新的RangeError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RangeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-RangeError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

