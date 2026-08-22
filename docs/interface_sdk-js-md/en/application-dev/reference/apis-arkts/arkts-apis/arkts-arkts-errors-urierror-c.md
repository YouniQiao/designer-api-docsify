# URIError

Represents an error that occurs when a global URI handling function was used in a wrong way

**Inheritance/Implementation:** URIError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class URIError--><!--Device-unnamed-export class URIError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(message?: string, options?: ErrorOptions): URIError
```

Constructs a new URIError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-URIError-static $_invoke(message?: string, options?: ErrorOptions): URIError--><!--Device-URIError-static $_invoke(message?: string, options?: ErrorOptions): URIError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

**Return value:**

| Type | Description |
| --- | --- |
| [URIError](arkts-arkts-errors-urierror-c.md) | Newly created URIError instance |

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new URIError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-URIError-constructor(message?: string, options?: ErrorOptions)--><!--Device-URIError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

