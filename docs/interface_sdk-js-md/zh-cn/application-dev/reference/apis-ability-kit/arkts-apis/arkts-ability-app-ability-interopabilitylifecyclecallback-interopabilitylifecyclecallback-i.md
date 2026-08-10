# InteropAbilityLifecycleCallback

The interop ability lifecycle callback.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-declare interface InteropAbilityLifecycleCallback--><!--Device-unnamed-declare interface InteropAbilityLifecycleCallback-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 导入模块

```TypeScript
import { InteropAbilityLifecycleCallback } from 'kits/@kit.AbilityKit';
```

## onAbilityBackground

```TypeScript
onAbilityBackground: AbilityCallbackFn
```

Called back when the state of an ability changes to background.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityBackground: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityBackground: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityContinue

```TypeScript
onAbilityContinue?: AbilityCallbackFn
```

Called back when an ability prepares to continue.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityContinue?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityContinue?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityCreate

```TypeScript
onAbilityCreate: AbilityCallbackFn
```

Called back when an ability is started for initialization.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityCreate: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityCreate: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityDestroy

```TypeScript
onAbilityDestroy: AbilityCallbackFn
```

Called back when an ability is destroyed.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityDestroy: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityDestroy: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityForeground

```TypeScript
onAbilityForeground: AbilityCallbackFn
```

Called back when the state of an ability changes to foreground.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityForeground: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityForeground: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilitySaveState

```TypeScript
onAbilitySaveState?: AbilityCallbackFn
```

Called back when the ability has called onSaveState.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilitySaveState?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilitySaveState?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillBackground

```TypeScript
onAbilityWillBackground?: AbilityCallbackFn
```

Called back before the state of an ability changes to background.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillBackground?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillBackground?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillContinue

```TypeScript
onAbilityWillContinue?: AbilityCallbackFn
```

Called back when the ability prepares to call onContinue.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillContinue?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillContinue?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillCreate

```TypeScript
onAbilityWillCreate?: AbilityCallbackFn
```

Called back before an ability is started for initialization.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillCreate?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillCreate?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillDestroy

```TypeScript
onAbilityWillDestroy?: AbilityCallbackFn
```

Called back before an ability is destroyed.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillDestroy?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillDestroy?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillForeground

```TypeScript
onAbilityWillForeground?: AbilityCallbackFn
```

Called back before the state of an ability changes to foreground.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillForeground?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillForeground?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillSaveState

```TypeScript
onAbilityWillSaveState?: AbilityCallbackFn
```

Called back when the ability prepares to call onSaveState.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onAbilityWillSaveState?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onAbilityWillSaveState?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onNewWant

```TypeScript
onNewWant?: AbilityCallbackFn
```

Called back after the UIAbility called onNewWant.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onNewWant?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onNewWant?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWillNewWant

```TypeScript
onWillNewWant?: AbilityCallbackFn
```

Called back before the UIAbility will called onNewWant.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWillNewWant?: AbilityCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWillNewWant?: AbilityCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageActive

```TypeScript
onWindowStageActive?: WindowStageCallbackFn
```

Called back when a window stage is active.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageActive?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageActive?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageCreate

```TypeScript
onWindowStageCreate: WindowStageCallbackFn
```

Called back when a window stage is created.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageCreate: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageCreate: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy: WindowStageCallbackFn
```

Called back when a window stage is destroyed.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageDestroy: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageDestroy: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageInactive

```TypeScript
onWindowStageInactive?: WindowStageCallbackFn
```

Called back when a window stage is inactive.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageInactive?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageInactive?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageRestore

```TypeScript
onWindowStageRestore?: WindowStageCallbackFn
```

Called back when the ability has called onWindowStageRestore.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageRestore?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageRestore?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillCreate

```TypeScript
onWindowStageWillCreate?: WindowStageCallbackFn
```

Called back before a window stage is created.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageWillCreate?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageWillCreate?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy?: WindowStageCallbackFn
```

Called back before a window stage is destroyed.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageWillDestroy?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageWillDestroy?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillRestore

```TypeScript
onWindowStageWillRestore?: WindowStageCallbackFn
```

Called back when the ability has called onWindowStageWillRestore.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InteropAbilityLifecycleCallback-onWindowStageWillRestore?: WindowStageCallbackFn--><!--Device-InteropAbilityLifecycleCallback-onWindowStageWillRestore?: WindowStageCallbackFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

