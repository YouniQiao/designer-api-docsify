# UnsupportedOperationError

表示请求的操作不受支持时抛出的错误。

**继承/实现关系：** UnsupportedOperationError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class UnsupportedOperationError--><!--Device-unnamed-export class UnsupportedOperationError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

构造一个UnsupportedOperationError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UnsupportedOperationError-constructor(message?: string, options?: ErrorOptions)--><!--Device-UnsupportedOperationError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误信息。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项， 通常包含错误堆栈信息。 |

