# SyntaxError(Defines the commonly used Errors for ArkTS)

Represents an error that occurs when trying to interpret syntactically invalid code

**Inheritance/Implementation:** SyntaxError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class SyntaxError--><!--Device-unnamed-export class SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): SyntaxError
```

Constructs a new SyntaxError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError--><!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| SyntaxError |  |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new SyntaxError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)--><!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

