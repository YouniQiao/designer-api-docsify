# Error

用于表示错误的Error类。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): Error
```

创建一个新的错误实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [message](#message) | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Error |

## constructor

```TypeScript
constructor(code: int, message?: string, options?: ErrorOptions)
```

使用给定的错误码、错误信息和原因构造一个新的错误实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [code](#code) | int | 是 |
| [message](#message) | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用给定的错误信息和原因构造一个新的错误实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [message](#message) | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |

## constructor

```TypeScript
constructor(name: string, code: int, message?: string, options?: ErrorOptions)
```

使用给定的名称、错误码、错误信息和选项构造一个新的错误实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |
| [code](#code) | int | 是 |
| [message](#message) | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |

## constructor

```TypeScript
constructor(name: string, message: string | undefined, options?: ErrorOptions)
```

使用给定的名称、错误信息和选项构造一个新的错误实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [name](#name) | string | 是 |
| [message](#message) | string \| undefined | 是 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |

## toString

```TypeScript
toString(): string
```

将该错误转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## cause

```TypeScript
set cause(val: Object | undefined)
```

设置该错误的原因。

**类型：** Object

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## code

```TypeScript
set code(val: int)
```

设置该错误的错误码。

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## message

```TypeScript
set message(val: string)
```

设置该错误的错误信息。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## name

```TypeScript
set name(val: string)
```

设置该错误的名称。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## stack

```TypeScript
set stack(newStack: string | undefined)
```

设置该错误的堆栈信息。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
