# LifecycleApp

interface of app lifecycle.

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-export declare interface LifecycleApp--><!--Device-unnamed-export declare interface LifecycleApp-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## onWindowDisplayModeChanged

```TypeScript
onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void
```

Called when the window display mode of this ability changes, for example, from fullscreen mode to multi-window mode or from multi-window mode to fullscreen mode.

**Since:** 7

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleApp-onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void--><!--Device-LifecycleApp-onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShownInMultiWindow | boolean | Yes |
| newConfig | resourceManager.Configuration | Yes |
