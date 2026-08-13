# TypeError

Represents an error that occurs when an operation could not be performed, typically (but not exclusively) when a value is not of the expected type

**Inheritance/Implementation:** TypeError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class TypeError--><!--Device-unnamed-export class TypeError-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): TypeError
```

Constructs a new TypeError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError--><!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| TypeError | Newly created TypeError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new TypeError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

