# @ohos.app.ability.abilityManager

The AbilityManager module provides APIs for obtaining, adding, and updating ability information and running status information.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace abilityManager--><!--Device-unnamed-declare namespace abilityManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md#getAbilityRunningInfos) |
| [isEmbeddedUIExtensionSupported](arkts-ability-abilitymanager-isembeddeduiextensionsupported-f.md#isEmbeddedUIExtensionSupported) |
| [restartSelfAtomicService](arkts-ability-abilitymanager-restartselfatomicservice-f.md#restartSelfAtomicService) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData-(System-API)) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData-(System-API)) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData-(System-API)) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquireShareData-(System-API)) |
| [clearPreloadedUIExtensionAbilities](arkts-ability-abilitymanager-clearpreloadeduiextensionabilities-f-sys.md#clearPreloadedUIExtensionAbilities-(System-API)) |
| [clearPreloadedUIExtensionAbility](arkts-ability-abilitymanager-clearpreloadeduiextensionability-f-sys.md#clearPreloadedUIExtensionAbility-(System-API)) |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f-sys.md#getAbilityRunningInfos-(System-API)) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getExtensionRunningInfos-(System-API)) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getExtensionRunningInfos-(System-API)) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getForegroundUIAbilities-(System-API)) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getForegroundUIAbilities-(System-API)) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#getTopAbility-(System-API)) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#getTopAbility-(System-API)) |
| [isEmbeddedOpenAllowed](arkts-ability-abilitymanager-isembeddedopenallowed-f-sys.md#isEmbeddedOpenAllowed-(System-API)) |
| [notifyDebugAssertResult](arkts-ability-abilitymanager-notifydebugassertresult-f-sys.md#notifyDebugAssertResult-(System-API)) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifySaveAsResult-(System-API)) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifySaveAsResult-(System-API)) |
| [offAbilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md#offAbilityForegroundState-(System-API)) |
| [offPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-offpreloadeduiextensionabilitydestroyed-f-sys.md#offPreloadedUIExtensionAbilityDestroyed-(System-API)) |
| [offPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-offpreloadeduiextensionabilityloaded-f-sys.md#offPreloadedUIExtensionAbilityLoaded-(System-API)) |
| [off_abilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md) |
| [onAbilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md#onAbilityForegroundState-(System-API)) |
| [onPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-onpreloadeduiextensionabilitydestroyed-f-sys.md#onPreloadedUIExtensionAbilityDestroyed-(System-API)) |
| [onPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-onpreloadeduiextensionabilityloaded-f-sys.md#onPreloadedUIExtensionAbilityLoaded-(System-API)) |
| [on_abilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md) |
| [preloadUIExtensionAbility](arkts-ability-abilitymanager-preloaduiextensionability-f-sys.md#preloadUIExtensionAbility-(System-API)) |
| [queryAtomicServiceStartupRule](arkts-ability-abilitymanager-queryatomicservicestartuprule-f-sys.md#queryAtomicServiceStartupRule-(System-API)) |
| [setResidentProcessEnabled](arkts-ability-abilitymanager-setresidentprocessenabled-f-sys.md#setResidentProcessEnabled-(System-API)) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateConfiguration-(System-API)) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateConfiguration-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AtomicServiceStartupRule](arkts-ability-abilitymanager-atomicservicestartuprule-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityState](arkts-ability-abilitymanager-abilitystate-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UserStatus](arkts-ability-abilitymanager-userstatus-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityRunningInfo](arkts-ability-abilitymanager-abilityrunninginfo-t.md) |
| [AbilityStateData](arkts-ability-abilitymanager-abilitystatedata-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityForegroundStateObserver](arkts-ability-abilitymanager-abilityforegroundstateobserver-t-sys.md) |
| [ExtensionRunningInfo](arkts-ability-abilitymanager-extensionrunninginfo-t-sys.md) |
| [PreloadedUIExtensionAbilityDestroyedFn](arkts-ability-abilitymanager-preloadeduiextensionabilitydestroyedfn-t-sys.md) |
| [PreloadedUIExtensionAbilityLoadedFn](arkts-ability-abilitymanager-preloadeduiextensionabilityloadedfn-t-sys.md) |
<!--DelEnd-->
