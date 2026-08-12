# AggregateError

AggregateError object represents an error when several errors need to be wrapped in a single error.

**Inheritance/Implementation:** AggregateError extends [Error](Error)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class AggregateError extends Error--><!--Device-unnamed-export class AggregateError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | Yes | Errors to be aggregated. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | Newly created AggregateError instance |

## $_invoke

```TypeScript
static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError--><!--Device-AggregateError-static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errors | Error[] | Yes | Errors to be aggregated. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) | Newly created AggregateError instance |

## constructor

```TypeScript
constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errors | Iterable&lt;Error&gt; | Yes | Errors to be aggregated. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

## constructor

```TypeScript
constructor(errors: Error[], message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)--><!--Device-AggregateError-constructor(errors: Error[], message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errors | Error[] | Yes | Errors to be aggregated. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

## errors

```TypeScript
errors: Array<Error>
```

Defines an array with aggregated errors

**Type:** Array&lt;Error&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AggregateError-errors: Array<Error>--><!--Device-AggregateError-errors: Array<Error>-End-->

**System capability:** SystemCapability.Utils.Lang

