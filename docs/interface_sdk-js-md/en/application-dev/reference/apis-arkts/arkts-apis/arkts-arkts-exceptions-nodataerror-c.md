# NoDataError

Represents an error thrown when data is expected but not provided.

**Inheritance/Implementation:** NoDataError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class NoDataError--><!--Device-unnamed-export class NoDataError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an NoDataError instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NoDataError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NoDataError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

