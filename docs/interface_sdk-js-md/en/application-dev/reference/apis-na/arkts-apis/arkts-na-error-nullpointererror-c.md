# NullPointerError

Represents an error that occurs when a null pointer is dereferenced.

**Inheritance/Implementation:** NullPointerError extends [Error](arkts-na-error-c.md#error)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-class NullPointerError--><!--Device-unnamed-class NullPointerError-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

Constructs a new NullPointerError instance with provided message and error specific information

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)--><!--Device-NullPointerError-constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error text |
| options | [ErrorOptions](arkts-na-error-erroroptions-i.md) | No | Error options |

