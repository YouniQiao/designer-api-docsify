# CustomComponentContext

CustomComponentContext is a state management tool for operating the observed data.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface CustomComponentContext--><!--Device-unnamed-export declare interface CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getReusePool

```TypeScript
getReusePool(): IReusePool | undefined
```

Get global reuse pool from current custom component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined--><!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IReusePool](arkts-na-utils-ireusepool-i.md) \| undefined | Returns the recyclepool instance. |

## registerActiveAndInactiveCallback

```TypeScript
registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,
    inactive?: ActiveAndInactiveCallbackType): void
```

Register active and inactive callback.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentContext-registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,    inactive?: ActiveAndInactiveCallbackType): void--><!--Device-CustomComponentContext-registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,    inactive?: ActiveAndInactiveCallbackType): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| active | [ActiveAndInactiveCallbackType](arkts-na-activeandinactivecallbacktype-t.md) | No | active function callback. |
| inactive | [ActiveAndInactiveCallbackType](arkts-na-activeandinactivecallbacktype-t.md) | No | inactive function callback. |

