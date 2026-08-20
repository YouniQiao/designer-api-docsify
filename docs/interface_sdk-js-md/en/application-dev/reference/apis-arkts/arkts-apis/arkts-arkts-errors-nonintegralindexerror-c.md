# NonIntegralIndexError

Represents an error that occurs when a numeric types conversion is performed on an index expression, and the fractional part differs from 0.

**Inheritance/Implementation:** NonIntegralIndexError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class NonIntegralIndexError--><!--Device-unnamed-export class NonIntegralIndexError-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NonIntegralIndexError-static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError--><!--Device-NonIntegralIndexError-static $_invoke(message?: string, options?: ErrorOptions): NonIntegralIndexError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [NonIntegralIndexError](arkts-arkts-errors-nonintegralindexerror-c.md) | Newly created NonIntegralIndexError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new NonIntegralIndexError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NonIntegralIndexError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NonIntegralIndexError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

