# SyntaxError

Represents an error that occurs when trying to interpret syntactically invalid code

**Inheritance/Implementation:** SyntaxError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class SyntaxError--><!--Device-unnamed-export class SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): SyntaxError
```

Constructs a new SyntaxError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError--><!--Device-SyntaxError-static $_invoke(message?: string, options?: ErrorOptions): SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)--><!--Device-SyntaxError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

