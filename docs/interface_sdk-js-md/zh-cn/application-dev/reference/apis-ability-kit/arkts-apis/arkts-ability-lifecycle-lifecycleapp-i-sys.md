# LifecycleApp

interface of app lifecycle.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

<!--Device-unnamed-export declare interface LifecycleApp--><!--Device-unnamed-export declare interface LifecycleApp-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

## onWindowDisplayModeChanged

```TypeScript
onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void
```

Called when the window display mode of this ability changes, for example, from fullscreen mode  to multi-window mode or from multi-window mode to fullscreen mode.

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-LifecycleApp-onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void--><!--Device-LifecycleApp-onWindowDisplayModeChanged?(isShownInMultiWindow: boolean, newConfig: resourceManager.Configuration): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.FAModel

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShownInMultiWindow | boolean | 是 | Specifies whether this ability is currently in multi-window mode.The value {@code true} indicates the multi-window mode, and {@code false} indicates another mode. |
| newConfig | resourceManager.Configuration | 是 | Indicates the new configuration information about Page ability. |

