# IllegalStateError

Represents error that is thrown when a method has been invoked at an illegal or inappropriate time.

**Inheritance/Implementation:** IllegalStateError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class IllegalStateError--><!--Device-unnamed-export class IllegalStateError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an IllegalStateError instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IllegalStateError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalStateError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

