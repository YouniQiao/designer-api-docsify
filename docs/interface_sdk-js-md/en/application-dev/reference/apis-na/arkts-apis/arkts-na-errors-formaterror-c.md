# FormatError(Defines the commonly used Errors for ArkTS)

Represents an error that occurs when an input string contains invalid or incorrectly formatted data.

**Inheritance/Implementation:** FormatError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class FormatError--><!--Device-unnamed-export class FormatError-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): FormatError
```

Constructs a new FormatError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormatError-static $_invoke(message?: string, options?: ErrorOptions): FormatError--><!--Device-FormatError-static $_invoke(message?: string, options?: ErrorOptions): FormatError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [FormatError](arkts-na-errors-formaterror-c.md) | Newly created FormatError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new FormatError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormatError-constructor(message?: string, options?: ErrorOptions)--><!--Device-FormatError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

