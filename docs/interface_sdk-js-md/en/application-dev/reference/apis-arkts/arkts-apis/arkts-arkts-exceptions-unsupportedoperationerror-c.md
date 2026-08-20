# UnsupportedOperationError

Represents error that is thrown when the requested operation is not supported.

**Inheritance/Implementation:** UnsupportedOperationError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class UnsupportedOperationError--><!--Device-unnamed-export class UnsupportedOperationError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an UnsupportedOperationError instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnsupportedOperationError-constructor(message?: string, options?: ErrorOptions)--><!--Device-UnsupportedOperationError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

