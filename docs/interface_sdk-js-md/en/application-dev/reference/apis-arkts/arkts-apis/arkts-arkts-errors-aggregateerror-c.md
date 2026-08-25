# AggregateError

AggregateError object represents an error when several errors need to be wrapped in a single error.

**Inheritance/Implementation:** AggregateError extends Error

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(errors: Iterable<Error>, message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errors](#errors) | Iterable & lt;Error & gt; | Yes |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) |

## $_invoke

```TypeScript
static $_invoke(errors: Error[], message?: string, options?: ErrorOptions): AggregateError
```

Constructs a new AggregateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errors](#errors) | Error[] | Yes |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [AggregateError](arkts-arkts-errors-aggregateerror-c.md) |

## constructor

```TypeScript
constructor(errors: Iterable<Error>, message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errors](#errors) | Iterable & lt;Error & gt; | Yes |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |

## constructor

```TypeScript
constructor(errors: Error[], message?: string, options?: ErrorOptions)
```

Constructs a new AggregateError instance with provided errors, message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [errors](#errors) | Error[] | Yes |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |

## errors

```TypeScript
errors: Array<Error>
```

Defines an array with aggregated errors

**Type:** Array&lt;Error&gt;

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
