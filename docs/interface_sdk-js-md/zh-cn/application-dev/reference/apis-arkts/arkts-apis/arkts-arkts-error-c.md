# Error

Error class for representing errors.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Error--><!--Device-unnamed-export class Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): Error
```

Creates a new error instance.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-static $_invoke(message?: string, options?: ErrorOptions): Error--><!--Device-Error-static $_invoke(message?: string, options?: ErrorOptions): Error-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Error | the new Error instance. |

## constructor

```TypeScript
constructor(code: int, message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided code, message and cause.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-constructor(code: int, message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(code: int, message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | int | 是 | Error code.. &lt;br&gt;The value should be an integer. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided message and cause.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-constructor(message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## constructor

```TypeScript
constructor(name: string, code: int, message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided name, code, message and options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-constructor(name: string, code: int, message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(name: string, code: int, message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Error name. |
| code | int | 是 | Error code. &lt;br&gt;The value should be an integer. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## constructor

```TypeScript
constructor(name: string, message: string | undefined, options?: ErrorOptions)
```

Constructs a new error instance with provided name, message and options.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-constructor(name: string, message: string | undefined, options?: ErrorOptions)--><!--Device-Error-constructor(name: string, message: string | undefined, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Error name. |
| message | string \| undefined | 是 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## toString

```TypeScript
toString(): string
```

Converts this error to a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-toString(): string--><!--Device-Error-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | the string representation. |

## cause

```TypeScript
set cause(val: Object | undefined)
```

Sets the cause of the error.

**类型：** Object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-set cause(val: Object | undefined)--><!--Device-Error-set cause(val: Object | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

## code

```TypeScript
set code(val: int)
```

Sets the code of the error.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-set code(val: int)--><!--Device-Error-set code(val: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

## message

```TypeScript
set message(val: string)
```

Sets the message of the error.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-set message(val: string)--><!--Device-Error-set message(val: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
set name(val: string)
```

Sets the name of the error.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-set name(val: string)--><!--Device-Error-set name(val: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

## stack

```TypeScript
set stack(newStack: string | undefined)
```

Sets the stack trace of the error.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Error-set stack(newStack: string | undefined)--><!--Device-Error-set stack(newStack: string | undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

