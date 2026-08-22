# EvalError

Represents an evaluation error

**Inheritance/Implementation:** EvalError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class EvalError--><!--Device-unnamed-export class EvalError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): EvalError
```

Constructs a new EvalError instance with provided message and options

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EvalError-static $_invoke(message?: string, options?: ErrorOptions): EvalError--><!--Device-EvalError-static $_invoke(message?: string, options?: ErrorOptions): EvalError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [EvalError](arkts-arkts-errors-evalerror-c.md) | Newly created EvalError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new EvalError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EvalError-constructor(message?: string, options?: ErrorOptions)--><!--Device-EvalError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

