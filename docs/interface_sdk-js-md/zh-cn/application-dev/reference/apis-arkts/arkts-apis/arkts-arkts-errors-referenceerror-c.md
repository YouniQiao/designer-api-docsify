# ReferenceError

表示在当前作用域中引用不存在（或尚未初始化）的变量时 发生的错误。

**继承/实现关系：** ReferenceError extends Error

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export class ReferenceError--><!--Device-unnamed-export class ReferenceError-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): ReferenceError
```

使用指定的错误信息和错误相关信息构造新的ReferenceError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReferenceError-static $_invoke(message?: string, options?: ErrorOptions): ReferenceError--><!--Device-ReferenceError-static $_invoke(message?: string, options?: ErrorOptions): ReferenceError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ReferenceError](arkts-arkts-errors-referenceerror-c.md) | 新创建的ReferenceError实例。 |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用指定的错误信息和错误相关信息构造新的ReferenceError实例。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ReferenceError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ReferenceError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | 错误文本。 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | 错误选项。 |

