# ArrayStoreError

Represents error that is thrown when attempting to store an object of different type in array of type-erased objects

**Inheritance/Implementation:** ArrayStoreError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class ArrayStoreError--><!--Device-unnamed-export class ArrayStoreError-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new ArrayStoreError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArrayStoreError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ArrayStoreError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

