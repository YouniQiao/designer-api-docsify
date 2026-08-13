# Error

Error class for representing errors.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class Error--><!--Device-unnamed-export class Error-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): Error
```

Creates a new error instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-static $_invoke(message?: string, options?: ErrorOptions): Error--><!--Device-Error-static $_invoke(message?: string, options?: ErrorOptions): Error-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| Error | the new Error instance. |

## constructor

```TypeScript
constructor(code: int, message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided code, message and cause.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-constructor(code: int, message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(code: int, message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Error code.. &lt;br&gt;The value should be an integer. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided message and cause.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-constructor(message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

## constructor

```TypeScript
constructor(name: string, code: int, message?: string, options?: ErrorOptions)
```

Constructs a new error instance with provided name, code, message and options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-constructor(name: string, code: int, message?: string, options?: ErrorOptions)--><!--Device-Error-constructor(name: string, code: int, message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Error name. |
| code | int | Yes | Error code. &lt;br&gt;The value should be an integer. |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

## constructor

```TypeScript
constructor(name: string, message: string | undefined, options?: ErrorOptions)
```

Constructs a new error instance with provided name, message and options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-constructor(name: string, message: string | undefined, options?: ErrorOptions)--><!--Device-Error-constructor(name: string, message: string | undefined, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Error name. |
| message | string \| undefined | Yes | Error text. |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options. |

## toString

```TypeScript
toString(): string
```

Converts this error to a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Error-toString(): string--><!--Device-Error-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | the string representation. |

