# ArgumentOutOfRangeError

表示传入参数的值超出允许范围时抛出的异常。

**继承/实现关系：** ArgumentOutOfRangeError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class ArgumentOutOfRangeError--><!--Device-unnamed-export class ArgumentOutOfRangeError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

构造一个ArgumentOutOfRangeError实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArgumentOutOfRangeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ArgumentOutOfRangeError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误信息。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项，通常包含错误堆栈信息。 |

