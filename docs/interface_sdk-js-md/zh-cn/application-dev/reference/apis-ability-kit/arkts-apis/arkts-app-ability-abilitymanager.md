# @ohos.app.ability.abilityManager

AbilityManager模块提供获取、新增、修改Ability相关信息和运行状态信息的能力。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md) |
| [isEmbeddedUIExtensionSupported](arkts-ability-abilitymanager-isembeddeduiextensionsupported-f.md) |
| [restartSelfAtomicService](arkts-ability-abilitymanager-restartselfatomicservice-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md) |
| [clearPreloadedUIExtensionAbilities](arkts-ability-abilitymanager-clearpreloadeduiextensionabilities-f-sys.md) |
| [clearPreloadedUIExtensionAbility](arkts-ability-abilitymanager-clearpreloadeduiextensionability-f-sys.md) |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f-sys.md) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md) |
| [isEmbeddedOpenAllowed](arkts-ability-abilitymanager-isembeddedopenallowed-f-sys.md) |
| [notifyDebugAssertResult](arkts-ability-abilitymanager-notifydebugassertresult-f-sys.md) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md) |
| off |
| [offPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-offpreloadeduiextensionabilitydestroyed-f-sys.md) |
| [offPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-offpreloadeduiextensionabilityloaded-f-sys.md) |
| on |
| [onPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-onpreloadeduiextensionabilitydestroyed-f-sys.md) |
| [onPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-onpreloadeduiextensionabilityloaded-f-sys.md) |
| [preloadUIExtensionAbility](arkts-ability-abilitymanager-preloaduiextensionability-f-sys.md) |
| [queryAtomicServiceStartupRule](arkts-ability-abilitymanager-queryatomicservicestartuprule-f-sys.md) |
| [setResidentProcessEnabled](arkts-ability-abilitymanager-setresidentprocessenabled-f-sys.md) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AtomicServiceStartupRule](arkts-ability-abilitymanager-atomicservicestartuprule-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AbilityState](arkts-ability-abilitymanager-abilitystate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [UserStatus](arkts-ability-abilitymanager-userstatus-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [AbilityRunningInfo](arkts-ability-abilitymanager-abilityrunninginfo-t.md) |
| [AbilityStateData](arkts-ability-abilitymanager-abilitystatedata-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) |
| [ExtensionRunningInfo](arkts-ability-abilitymanager-extensionrunninginfo-t-sys.md) |
| [PreloadedUIExtensionAbilityDestroyedFn](arkts-ability-abilitymanager-preloadeduiextensionabilitydestroyedfn-t-sys.md) |
| [PreloadedUIExtensionAbilityLoadedFn](arkts-ability-abilitymanager-preloadeduiextensionabilityloadedfn-t-sys.md) |
<!--DelEnd-->
