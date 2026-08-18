# @ohos.app.ability.abilityManager

The AbilityManager module provides APIs for obtaining, adding, and updating ability information and running status information.

**Since:** 23

<!--Device-unnamed-declare namespace abilityManager--><!--Device-unnamed-declare namespace abilityManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
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
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata-system-api) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata-system-api) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata-system-api) |
| [acquireShareData](arkts-ability-abilitymanager-acquiresharedata-f-sys.md#acquiresharedata-system-api) |
| [clearPreloadedUIExtensionAbilities](arkts-ability-abilitymanager-clearpreloadeduiextensionabilities-f-sys.md#clearpreloadeduiextensionabilities-system-api) |
| [clearPreloadedUIExtensionAbility](arkts-ability-abilitymanager-clearpreloadeduiextensionability-f-sys.md#clearpreloadeduiextensionability-system-api) |
| [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f-sys.md#getabilityrunninginfos-system-api) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getextensionrunninginfos-system-api) |
| [getExtensionRunningInfos](arkts-ability-abilitymanager-getextensionrunninginfos-f-sys.md#getextensionrunninginfos-system-api) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getforegrounduiabilities-system-api) |
| [getForegroundUIAbilities](arkts-ability-abilitymanager-getforegrounduiabilities-f-sys.md#getforegrounduiabilities-system-api) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#gettopability-system-api) |
| [getTopAbility](arkts-ability-abilitymanager-gettopability-f-sys.md#gettopability-system-api) |
| [isEmbeddedOpenAllowed](arkts-ability-abilitymanager-isembeddedopenallowed-f-sys.md#isembeddedopenallowed-system-api) |
| [notifyDebugAssertResult](arkts-ability-abilitymanager-notifydebugassertresult-f-sys.md#notifydebugassertresult-system-api) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifysaveasresult-system-api) |
| [notifySaveAsResult](arkts-ability-abilitymanager-notifysaveasresult-f-sys.md#notifysaveasresult-system-api) |
| [offAbilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md#offabilityforegroundstate) |
| [offPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-offpreloadeduiextensionabilitydestroyed-f-sys.md#offpreloadeduiextensionabilitydestroyed-system-api) |
| [offPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-offpreloadeduiextensionabilityloaded-f-sys.md#offpreloadeduiextensionabilityloaded-system-api) |
| [off_abilityForegroundState](arkts-ability-abilitymanager-offabilityforegroundstate-f-sys.md#offabilityforegroundstate) |
| [onAbilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md#onabilityforegroundstate) |
| [onPreloadedUIExtensionAbilityDestroyed](arkts-ability-abilitymanager-onpreloadeduiextensionabilitydestroyed-f-sys.md#onpreloadeduiextensionabilitydestroyed-system-api) |
| [onPreloadedUIExtensionAbilityLoaded](arkts-ability-abilitymanager-onpreloadeduiextensionabilityloaded-f-sys.md#onpreloadeduiextensionabilityloaded-system-api) |
| [on_abilityForegroundState](arkts-ability-abilitymanager-onabilityforegroundstate-f-sys.md#onabilityforegroundstate) |
| [preloadUIExtensionAbility](arkts-ability-abilitymanager-preloaduiextensionability-f-sys.md#preloaduiextensionability-system-api) |
| [queryAtomicServiceStartupRule](arkts-ability-abilitymanager-queryatomicservicestartuprule-f-sys.md#queryatomicservicestartuprule-system-api) |
| [setResidentProcessEnabled](arkts-ability-abilitymanager-setresidentprocessenabled-f-sys.md#setresidentprocessenabled-system-api) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateconfiguration-system-api) |
| [updateConfiguration](arkts-ability-abilitymanager-updateconfiguration-f-sys.md#updateconfiguration-system-api) |
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
