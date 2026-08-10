# JsonError

Base error class for JSON-related errors.Thrown when general JSON parsing or manipulation errors occur.

**继承/实现关系：** JsonError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export class JsonError extends Error--><!--Device-jsonx-export class JsonError extends Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(msg: string)
```

Constructs a new JsonError with the specified message.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonError-public constructor(msg: string)--><!--Device-JsonError-public constructor(msg: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | Error message. |

