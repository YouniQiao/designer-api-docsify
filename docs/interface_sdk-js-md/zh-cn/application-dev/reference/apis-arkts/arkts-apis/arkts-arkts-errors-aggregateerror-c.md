# AggregateError

AggregateError object represents an error when several errors need to be wrapped in a single error.

**继承/实现关系：** AggregateError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class AggregateError extends Error--><!--Device-unnamed-export class AggregateError extends Error-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | 是 | Errors to be aggregated. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | Newly created AggregateError instance |

## $_invoke

```TypeScript
static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Error[] | 是 | Errors to be aggregated. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | Newly created AggregateError instance |

## constructor

```TypeScript
constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | 是 | Errors to be aggregated. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## constructor

```TypeScript
constructor(errors: Error[], message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errors | Error[] | 是 | Errors to be aggregated. |
| message | string | 否 | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 | Error options. |

## errors

```TypeScript
errors: Array<Error>
```

Defines an array with aggregated errors

**类型：** Array&lt;Error&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AggregateError-errors: Array<Error>--><!--Device-AggregateError-errors: Array<Error>-End-->

**系统能力：** SystemCapability.Utils.Lang

