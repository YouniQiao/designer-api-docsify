# InteropAbilityMonitor

Provide methods for matching monitored Ability objects that meet specified conditions.The most recently matched Ability objects will be saved in the InteropAbilityMonitor object.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface InteropAbilityMonitor--><!--Device-unnamed-export interface InteropAbilityMonitor-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityBackground

```TypeScript
onAbilityBackground?: AbilityCallbackFn
```

Called back when the state of the ability changes to background.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onAbilityBackground?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onAbilityBackground?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityCreate

```TypeScript
onAbilityCreate?: AbilityCallbackFn
```

Called back when the ability is created.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onAbilityCreate?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onAbilityCreate?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityDestroy

```TypeScript
onAbilityDestroy?: AbilityCallbackFn
```

Called back before the ability is destroyed.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onAbilityDestroy?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onAbilityDestroy?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onAbilityForeground

```TypeScript
onAbilityForeground?: AbilityCallbackFn
```

Called back when the state of the ability changes to foreground.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onAbilityForeground?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onAbilityForeground?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onWindowStageCreate

```TypeScript
onWindowStageCreate?: AbilityCallbackFn
```

Called back when an ability window stage is created.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onWindowStageCreate?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onWindowStageCreate?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy?: AbilityCallbackFn
```

Called back when an ability window stage is destroyed.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onWindowStageDestroy?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onWindowStageDestroy?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onWindowStageRestore

```TypeScript
onWindowStageRestore?: AbilityCallbackFn
```

Called back when an ability window stage is restored.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-onWindowStageRestore?: AbilityCallbackFn--><!--Device-InteropAbilityMonitor-onWindowStageRestore?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## abilityName

```TypeScript
abilityName: string
```

The name of the ability to monitor.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-abilityName: string--><!--Device-InteropAbilityMonitor-abilityName: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName?: string
```

The name of the module to monitor.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-InteropAbilityMonitor-moduleName?: string--><!--Device-InteropAbilityMonitor-moduleName?: string-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

