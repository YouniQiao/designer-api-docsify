# RuntimeError

Represents an error that occurs during runtime.

**Inheritance/Implementation:** RuntimeError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class RuntimeError--><!--Device-unnamed-export class RuntimeError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a RuntimeError instance.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RuntimeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-RuntimeError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

