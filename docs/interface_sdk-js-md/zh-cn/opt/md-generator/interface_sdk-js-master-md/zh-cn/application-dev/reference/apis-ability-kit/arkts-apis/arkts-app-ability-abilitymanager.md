# @ohos.app.ability.abilityManager

AbilityManager模块提供获取、新增、修改Ability相关信息和运行状态信息的能力。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace abilityManager--><!--Device-unnamed-declare namespace abilityManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 汇总

### 函数

| 名称 |
| --- |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md#getAbilityRunningInfos) |
| [isEmbeddedUIExtensionSupported](arkts-ability-abilitymanager-isembeddeduiextensionsupported-f.md#isEmbeddedUIExtensionSupported) |
| [restartSelfAtomicService](arkts-ability-abilitymanager-restartselfatomicservice-f.md#restartSelfAtomicService) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData（系统接口）) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData（系统接口）) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData（系统接口）) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData（系统接口）) |
| [clearPreloadedUIExtensionAbilities](arkts-ability-abilitymanager-clearpreloadeduiextensionabilities-f-sys.md#clearPreloadedUIExtensionAbilities（系统接口）) |
| [clearPreloadedUIExtensionAbility](arkts-ability-abilitymanager-clearpreloadeduiextensionability-f-sys.md#clearPreloadedUIExtensionAbility（系统接口）) |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f-sys.md#getAbilityRunningInfos（系统接口）) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getExtensionRunningInfos（系统接口）) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getExtensionRunningInfos（系统接口）) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getForegroundUIAbilities（系统接口）) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getForegroundUIAbilities（系统接口）) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#getTopAbility（系统接口）) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#getTopAbility（系统接口）) |
| [isEmbeddedOpenAllowed](arkts-ability-abilitymanager-isembeddedopenallowed-f-sys.md#isEmbeddedOpenAllowed（系统接口）) |
| [notifyDebugAssertResult](arkts-ability-abilitymanager-notifydebugassertresult-f-sys.md#notifyDebugAssertResult（系统接口）) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifySaveAsResult（系统接口）) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifySaveAsResult（系统接口）) |
| [offAbilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md#offAbilityForegroundState（系统接口）) |
| [offPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-offpreloadeduiextensionabilitydestroyed-f-sys.md#offPreloadedUIExtensionAbilityDestroyed（系统接口）) |
| [offPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-offpreloadeduiextensionabilityloaded-f-sys.md#offPreloadedUIExtensionAbilityLoaded（系统接口）) |
| [off_abilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md) |
| [onAbilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md#onAbilityForegroundState（系统接口）) |
| [onPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-onpreloadeduiextensionabilitydestroyed-f-sys.md#onPreloadedUIExtensionAbilityDestroyed（系统接口）) |
| [onPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-onpreloadeduiextensionabilityloaded-f-sys.md#onPreloadedUIExtensionAbilityLoaded（系统接口）) |
| [on_abilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md) |
| [preloadUIExtensionAbility](arkts-ability-abilitymanager-preloaduiextensionability-f-sys.md#preloadUIExtensionAbility（系统接口）) |
| [queryAtomicServiceStartupRule](arkts-ability-abilitymanager-queryatomicservicestartuprule-f-sys.md#queryAtomicServiceStartupRule（系统接口）) |
| [setResidentProcessEnabled](arkts-ability-abilitymanager-setresidentprocessenabled-f-sys.md#setResidentProcessEnabled（系统接口）) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateConfiguration（系统接口）) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateConfiguration（系统接口）) |
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
