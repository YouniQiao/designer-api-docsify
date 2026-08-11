# @ohos.app.ability.abilityManager

The AbilityManager module provides APIs for obtaining, adding, and updating ability information and running status information.

**Since:** 9

<!--Device-unnamed-declare namespace abilityManager--><!--Device-unnamed-declare namespace abilityManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md#getabilityrunninginfos) |
| [isEmbeddedUIExtensionSupported](arkts-ability-abilitymanager-isembeddeduiextensionsupported-f.md#isembeddeduiextensionsupported) |
| [restartSelfAtomicService](arkts-ability-abilitymanager-restartselfatomicservice-f.md#restartselfatomicservice) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata-1) |
| [clearPreloadedUIExtensionAbilities](arkts-ability-abilitymanager-clearpreloadeduiextensionabilities-f-sys.md#clearpreloadeduiextensionabilities) |
| [clearPreloadedUIExtensionAbility](arkts-ability-abilitymanager-clearpreloadeduiextensionability-f-sys.md#clearpreloadeduiextensionability) |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f-sys.md#getabilityrunninginfos-1) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getextensionrunninginfos) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getextensionrunninginfos-1) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getforegrounduiabilities) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getforegrounduiabilities-1) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#gettopability) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#gettopability-1) |
| [isEmbeddedOpenAllowed](arkts-ability-abilitymanager-isembeddedopenallowed-f-sys.md#isembeddedopenallowed) |
| [notifyDebugAssertResult](arkts-ability-abilitymanager-notifydebugassertresult-f-sys.md#notifydebugassertresult) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifysaveasresult) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifysaveasresult-1) |
| [off](arkts-ability-abilitymanager-off-f-sys.md#off) |
| [offPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-offpreloadeduiextensionabilitydestroyed-f-sys.md#offpreloadeduiextensionabilitydestroyed) |
| [offPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-offpreloadeduiextensionabilityloaded-f-sys.md#offpreloadeduiextensionabilityloaded) |
| [on](arkts-ability-abilitymanager-on-f-sys.md#on) |
| [onPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-onpreloadeduiextensionabilitydestroyed-f-sys.md#onpreloadeduiextensionabilitydestroyed) |
| [onPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-onpreloadeduiextensionabilityloaded-f-sys.md#onpreloadeduiextensionabilityloaded) |
| [preloadUIExtensionAbility](arkts-ability-abilitymanager-preloaduiextensionability-f-sys.md#preloaduiextensionability) |
| [queryAtomicServiceStartupRule](arkts-ability-abilitymanager-queryatomicservicestartuprule-f-sys.md#queryatomicservicestartuprule) |
| [setResidentProcessEnabled](arkts-ability-abilitymanager-setresidentprocessenabled-f-sys.md#setresidentprocessenabled) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateconfiguration) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateconfiguration-1) |
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
