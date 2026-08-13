# StackOverflowError

Represents an error that occurs when the available memory is not sufficient to create the activation frame

**Inheritance/Implementation:** StackOverflowError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class StackOverflowError--><!--Device-unnamed-export class StackOverflowError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new StackOverflowError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StackOverflowError-constructor(message?: string, options?: ErrorOptions)--><!--Device-StackOverflowError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

