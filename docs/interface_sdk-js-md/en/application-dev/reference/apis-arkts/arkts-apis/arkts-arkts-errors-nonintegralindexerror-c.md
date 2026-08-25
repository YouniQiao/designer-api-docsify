# NonIntegralIndexError

Represents an error that occurs when a numeric types conversion is performed on an index expression, and the fractional part differs from 0.

**Inheritance/Implementation:** NonIntegralIndexError extends Error

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError
```

Constructs a new NonIntegralIndexError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [NonIntegralIndexError](arkts-arkts-errors-nonintegralindexerror-c.md) |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new NonIntegralIndexError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |
