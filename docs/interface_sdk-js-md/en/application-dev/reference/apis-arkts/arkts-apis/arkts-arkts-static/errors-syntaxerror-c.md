# SyntaxError

Represents an error that occurs when trying to interpret syntactically invalid code

**Inheritance/Implementation:** SyntaxError extends [Error](error-error-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class SyntaxError extends Error--><!--Device-unnamed-export class SyntaxError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): SyntaxError
```

Constructs a new SyntaxError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError--><!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| SyntaxError |  |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new SyntaxError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)--><!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

