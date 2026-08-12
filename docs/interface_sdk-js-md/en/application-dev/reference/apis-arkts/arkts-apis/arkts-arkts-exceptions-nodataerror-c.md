# NoDataError

Represents an error thrown when data is expected but not provided.

**Inheritance/Implementation:** NoDataError extends [Error](Error)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class NoDataError extends Error--><!--Device-unnamed-export class NoDataError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs an NoDataError instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NoDataError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NoDataError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | The error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options, usually containing the error stack information. |

