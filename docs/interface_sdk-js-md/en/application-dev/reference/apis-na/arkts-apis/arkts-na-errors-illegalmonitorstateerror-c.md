# IllegalMonitorStateError

Represents an error that is thrown when attempting to wait, notify or notifyAll on object, that hasn't been synchronised

**Inheritance/Implementation:** IllegalMonitorStateError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class IllegalMonitorStateError--><!--Device-unnamed-export class IllegalMonitorStateError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new IllegalMonitorStateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IllegalMonitorStateError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalMonitorStateError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

