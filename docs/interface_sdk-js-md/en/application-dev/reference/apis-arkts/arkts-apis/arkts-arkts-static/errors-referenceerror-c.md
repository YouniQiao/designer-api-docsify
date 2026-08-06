# ReferenceError

Represents an error that occurs when a variable that doesn't exist (or hasn't yet been initialized)in the current scope is referenced

**Inheritance/Implementation:** ReferenceError extends [Error](error-error-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class ReferenceError extends Error--><!--Device-unnamed-export class ReferenceError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): ReferenceError
```

Constructs a new ReferenceError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReferenceError-static $_invoke(message?: string, options?: ErrorOptions): ReferenceError--><!--Device-ReferenceError-static $_invoke(message?: string, options?: ErrorOptions): ReferenceError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  Newly created ReferenceError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new ReferenceError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReferenceError-constructor(message?: string, options?: ErrorOptions)--><!--Device-ReferenceError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

