# CoroutinesLimitExceedError

Represents error that is thrown when coroutines limit is reached

**Inheritance/Implementation:** CoroutinesLimitExceedError extends [Error](arkts-arkts-error-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class CoroutinesLimitExceedError extends Error--><!--Device-unnamed-export class CoroutinesLimitExceedError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new CoroutinesLimitExceedError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CoroutinesLimitExceedError-constructor(message?: string, options?: ErrorOptions)--><!--Device-CoroutinesLimitExceedError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

