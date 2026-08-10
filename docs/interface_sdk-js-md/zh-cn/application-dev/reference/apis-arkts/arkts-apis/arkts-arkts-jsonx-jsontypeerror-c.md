# JsonTypeError

Error thrown when attempting to access a JSON element with an incompatible type.For example, trying to get a string value from a number element.

**继承/实现关系：** JsonTypeError extends [JsonError](arkts-arkts-jsonx-jsonerror-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export class JsonTypeError extends JsonError--><!--Device-jsonx-export class JsonTypeError extends JsonError-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(msg: string)
```

Constructs a new JsonTypeError with the specified message.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonTypeError-public constructor(msg: string)--><!--Device-JsonTypeError-public constructor(msg: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | Error message. |

