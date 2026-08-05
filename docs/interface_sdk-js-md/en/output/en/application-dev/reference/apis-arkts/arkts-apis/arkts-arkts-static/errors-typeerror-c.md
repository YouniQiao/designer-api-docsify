# TypeError

Represents an error that occurs when an operation could not be performed, typically (but not exclusively) when a value is not of the expected type

**Inheritance/Implementation:** TypeError extends [Error](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-error-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class TypeError extends Error--><!--Device-unnamed-export class TypeError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): TypeError
```

Constructs a new TypeError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError--><!--Device-TypeError-static $_invoke(message?: string, options?: ErrorOptions): TypeError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| TypeError | - Newly created TypeError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new TypeError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)--><!--Device-TypeError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Error options. |

