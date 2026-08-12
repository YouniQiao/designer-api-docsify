# IndexOutOfBoundsError

Represents error that is thrown when provided collection index is out of bounds

**Inheritance/Implementation:** IndexOutOfBoundsError extends [RangeError](arkts-arkts-errors-rangeerror-c.md#RangeError)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class IndexOutOfBoundsError extends RangeError--><!--Device-unnamed-export class IndexOutOfBoundsError extends RangeError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new IndexOutOfBoundsError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

