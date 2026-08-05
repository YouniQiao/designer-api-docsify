# IllegalMonitorStateError

Represents an error that is thrown when attempting to wait, notify or notifyAll on object, that hasn't been synchronised

**Inheritance/Implementation:** IllegalMonitorStateError extends [Error](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-error-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class IllegalMonitorStateError extends Error--><!--Device-unnamed-export class IllegalMonitorStateError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new IllegalMonitorStateError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IllegalMonitorStateError-constructor(message?: string, options?: ErrorOptions)--><!--Device-IllegalMonitorStateError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

