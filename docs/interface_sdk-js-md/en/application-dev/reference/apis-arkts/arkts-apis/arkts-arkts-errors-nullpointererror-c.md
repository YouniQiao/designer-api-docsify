# NullPointerError

Represents an error that occurs when null pointer is dereferenced.

**Inheritance/Implementation:** NullPointerError extends Error

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class NullPointerError--><!--Device-unnamed-export class NullPointerError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new NullPointerError instance with provided message and error specific information

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

