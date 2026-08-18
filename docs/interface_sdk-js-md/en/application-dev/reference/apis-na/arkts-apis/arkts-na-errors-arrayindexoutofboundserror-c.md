# ArrayIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)

Represents an error that occurs when array is oging to be indexed out of its bounds

**Inheritance/Implementation:** ArrayIndexOutOfBoundsError extends [RangeError](arkts-na-errors-rangeerror-c.md#rangeerror)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class ArrayIndexOutOfBoundsError--><!--Device-unnamed-export class ArrayIndexOutOfBoundsError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new ArrayIndexOutOfBoundsError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ArrayIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

