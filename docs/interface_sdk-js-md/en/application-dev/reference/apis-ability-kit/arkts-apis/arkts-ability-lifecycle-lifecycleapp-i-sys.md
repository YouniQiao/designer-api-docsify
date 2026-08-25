# LifecycleApp

interface of app lifecycle.@interface LifecycleApp

**Since:** 7

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## Modules to Import

```TypeScript
```

## onWindowDisplayModeChanged

```TypeScript
onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void
```

Called when the window display mode of this ability changes, for example, from fullscreen mode to multi-window mode or from multi-window mode to fullscreen mode.

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShownInMultiWindow | boolean | Yes |
| newConfig | resourceManager.Configuration | Yes |
