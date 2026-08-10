# ApplicationStateChangeCallback

本模块用于监听当前应用进程的状态变化。为了便于表述，下文中将“应用进程”简称为“进程”。开发者可调用  
[ApplicationContext.on('applicationStateChange')](./application/ApplicationContext:ApplicationContext.on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback))方法传入自定义ApplicationStateChangeCallback来监听当前进程的前后台状态变化，从而根据进程前后台状态变化来执行某些操作。例如，统计进程前后台时长、或者当进程退到后台时清理内存缓存。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare interface ApplicationStateChangeCallback--><!--Device-unnamed-declare interface ApplicationStateChangeCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { ApplicationStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## onApplicationBackground

```TypeScript
onApplicationBackground(): void
```

当前进程从前台切换到后台时触发回调。当该回调触发时，表示进程已完全处于后台状态，可以执行适合在后台状态下完成的操作（例如清理内存缓存）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationStateChangeCallback-onApplicationBackground(): void--><!--Device-ApplicationStateChangeCallback-onApplicationBackground(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onApplicationForeground

```TypeScript
onApplicationForeground(): void
```

当前进程从后台切换到前台时触发回调。当该回调触发时，并不表示进程已完全处于前台状态，而是即将进入前台状态，此时无法执行需要依赖前台状态的操作（例如启动其他UIAbility）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationStateChangeCallback-onApplicationForeground(): void--><!--Device-ApplicationStateChangeCallback-onApplicationForeground(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

