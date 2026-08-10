# NullPointerError

Represents an error that occurs when a null pointer is dereferenced.

**继承/实现关系：** NullPointerError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class NullPointerError extends Error--><!--Device-unnamed-class NullPointerError extends Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new NullPointerError instance with provided message and error specific information

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options |

