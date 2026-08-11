# OnFailedFn

```TypeScript
type OnFailedFn = (code: int) => void
```

Callback invoked when a connection fails.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-type OnFailedFn = (code: int) => void--><!--Device-unnamed-type OnFailedFn = (code: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Result code. The value 0 means that the connection is successful, -1 means that a parameter is incorrect, and -2 means that the ability is not found |

