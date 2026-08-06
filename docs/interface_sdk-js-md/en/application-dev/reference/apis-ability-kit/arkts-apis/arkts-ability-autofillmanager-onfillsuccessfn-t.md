# OnFillSuccessFn

```TypeScript
type OnFillSuccessFn = (viewData: ViewData) => void
```

Called when auto fill request is successfully handled.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-autoFillManager-type OnFillSuccessFn = (viewData: ViewData) => void--><!--Device-autoFillManager-type OnFillSuccessFn = (viewData: ViewData) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| viewData | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the ui context where the filling operation will be performed.  |

