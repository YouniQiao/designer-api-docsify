# @ohos.bundle

The module provides APIs for obtaining information about an application, including bundle information, [application information](arkts-ability-applicationinfo-applicationinfo-depr-i.md#applicationinfo), and [ability information](arkts-ability-abilityinfo-abilityinfo-depr-i.md#abilityinfo). It also provides APIs to obtain and set the application disabling state.

> **NOTE：**&gt;
> The APIs of this module have been deprecated since API version 9. You are advised to use
> [@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [bundleManager](arkts-bundle-bundlemanager.md)

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md) |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilitySubType](arkts-ability-bundle-abilitysubtype-e.md) |
| [AbilityType](arkts-ability-bundle-abilitytype-e.md) |
| [BundleFlag](arkts-ability-bundle-bundleflag-e.md) |
| [ColorMode](arkts-ability-bundle-colormode-e.md) |
| [DisplayOrientation](arkts-ability-bundle-displayorientation-e.md) |
| [GrantStatus](arkts-ability-bundle-grantstatus-e.md) |
| [InstallErrorCode](arkts-ability-bundle-installerrorcode-e.md) |
| [LaunchMode](arkts-ability-bundle-launchmode-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ModuleRemoveFlag](arkts-ability-bundle-moduleremoveflag-e-sys.md) |
| [QueryShortCutFlag](arkts-ability-bundle-queryshortcutflag-e-sys.md) |
| [ShortcutExistence](arkts-ability-bundle-shortcutexistence-e-sys.md) |
| [SignatureCompareResult](arkts-ability-bundle-signaturecompareresult-e-sys.md) |
<!--DelEnd-->
