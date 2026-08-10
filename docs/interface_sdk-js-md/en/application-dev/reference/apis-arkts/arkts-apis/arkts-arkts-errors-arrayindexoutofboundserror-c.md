# ArrayIndexOutOfBoundsError

Represents an error that occurs when array is oging to be indexed out of its bounds

**Inheritance/Implementation:** ArrayIndexOutOfBoundsError extends [RangeError](arkts-arkts-errors-rangeerror-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class ArrayIndexOutOfBoundsError extends RangeError--><!--Device-unnamed-export class ArrayIndexOutOfBoundsError extends RangeError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new ArrayIndexOutOfBoundsError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ArrayIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

