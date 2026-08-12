# IllegalArgumentError

Represents an error thrown when a method is passed an illegal argument.

**Inheritance/Implementation:** IllegalArgumentError extends [Error](Error)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class IllegalArgumentError extends Error--><!--Device-unnamed-export class IllegalArgumentError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an IllegalArgumentError instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalArgumentError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

