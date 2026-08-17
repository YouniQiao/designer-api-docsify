# clearTimeout

## clearTimeout

```TypeScript
function clearTimeout(timerId?: int | null): void
```

Cancel the specified timer.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-function clearTimeout(timerId?: int | null): void--><!--Device-unnamed-function clearTimeout(timerId?: int | null): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| timerId | int \| null | No | The id of the timer returned from setTimeout, if pass empty or null or undefined will do nothing. |

