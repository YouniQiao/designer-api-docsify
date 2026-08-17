# JSONTypeError(Defines the commonly used Errors for ArkTS)

Represents an error that occurs when JSONValue can not be assigned to a type

**Inheritance/Implementation:** JSONTypeError extends Error

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export class JSONTypeError--><!--Device-unnamed-export class JSONTypeError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new JSONTypeError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSONTypeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-JSONTypeError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

