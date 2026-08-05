# EvalError

Represents an evaluation error

**Inheritance/Implementation:** EvalError extends [Error](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-error-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class EvalError extends Error--><!--Device-unnamed-export class EvalError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): EvalError
```

Constructs a new EvalError instance with provided message and options

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EvalError-static $_invoke(message?: string, options?: ErrorOptions): EvalError--><!--Device-EvalError-static $_invoke(message?: string, options?: ErrorOptions): EvalError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - Newly created EvalError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new EvalError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EvalError-constructor(message?: string, options?: ErrorOptions)--><!--Device-EvalError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

