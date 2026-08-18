# IllegalArgumentError

Represents an error thrown when a method is passed an illegal argument.

**Inheritance/Implementation:** IllegalArgumentError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class IllegalArgumentError--><!--Device-unnamed-export class IllegalArgumentError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an IllegalArgumentError instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

