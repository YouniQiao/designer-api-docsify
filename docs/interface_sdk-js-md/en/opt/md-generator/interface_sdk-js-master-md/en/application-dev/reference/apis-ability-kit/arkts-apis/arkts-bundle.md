# @ohos.bundle

The module provides APIs for obtaining information about an application, including  
[bundle information](arkts-ability-bundleinfo-i.md),  
[application information](arkts-ability-applicationinfo-i.md), and  
[ability information](arkts-ability-abilityinfo-i.md). It also provides APIs to obtain and set the application disabling state.

> **NOTE：**
> 
> The APIs of this module have been deprecated since API version 9. You are advised to use
> [@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [@ohos.bundle.bundleManager:bundleManager](arkts-bundle-bundlemanager.md)

<!--Device-unnamed-declare namespace bundle--><!--Device-unnamed-declare namespace bundle-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getabilityicon) |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getabilityicon-1) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo-1) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getabilitylabel) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getabilitylabel-1) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo-1) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo-2) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo-1) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo-2) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo-1) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo-2) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getbundlearchiveinfo) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getbundlearchiveinfo-1) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo-1) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo-2) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getlaunchwantforbundle) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getlaunchwantforbundle-1) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getnameforuid) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getnameforuid-1) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isabilityenabled) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isabilityenabled-1) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isapplicationenabled) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isapplicationenabled-1) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant-1) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant-2) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles) |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles-1) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getapplicationinfos) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getapplicationinfos-1) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getapplicationinfos-2) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getbundleinfos) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getbundleinfos-1) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getbundleinfos-2) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getbundleinstaller) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getbundleinstaller-1) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getpermissiondef) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getpermissiondef-1) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setabilityenabled) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setabilityenabled-1) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setapplicationenabled) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setapplicationenabled-1) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ModuleRemoveFlag](arkts-ability-bundle-moduleremoveflag-e-sys.md) |
| [QueryShortCutFlag](arkts-ability-bundle-queryshortcutflag-e-sys.md) |
| [ShortcutExistence](arkts-ability-bundle-shortcutexistence-e-sys.md) |
| [SignatureCompareResult](arkts-ability-bundle-signaturecompareresult-e-sys.md) |
<!--DelEnd-->
