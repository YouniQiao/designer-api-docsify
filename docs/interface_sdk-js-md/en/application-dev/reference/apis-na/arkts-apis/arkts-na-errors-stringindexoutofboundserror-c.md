# StringIndexOutOfBoundsError(Defines the commonly used Errors for ArkTS)

Represents error that is thrown when provided string index is out of bounds

**Inheritance/Implementation:** StringIndexOutOfBoundsError extends [RangeError](arkts-na-errors-rangeerror-c.md#rangeerror)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class StringIndexOutOfBoundsError--><!--Device-unnamed-export class StringIndexOutOfBoundsError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new StringIndexOutOfBoundsError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StringIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)--><!--Device-StringIndexOutOfBoundsError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

