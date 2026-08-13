# @ohos.bundle

The module provides APIs for obtaining information about an application, including bundle information, [application information](arkts-ability-applicationinfo-applicationinfo-depr-i.md#ApplicationInfo), and [ability information](arkts-ability-abilityinfo-abilityinfo-depr-i.md#AbilityInfo). It also provides APIs to obtain and set the application disabling state. > **NOTE：**> > The APIs of this module have been deprecated since API version 9. You are advised to use > [@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md#@ohos.bundle.bundleManager) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [bundleManager](arkts-bundle-bundlemanager.md#@ohos.bundle.bundleManager)

<!--Device-unnamed-declare namespace bundle--><!--Device-unnamed-declare namespace bundle-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getAbilityIcon) |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getAbilityIcon) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getAbilityInfo) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getAbilityInfo) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getAbilityLabel) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getAbilityLabel) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getAllApplicationInfo) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getAllApplicationInfo) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getAllApplicationInfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getAllBundleInfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getAllBundleInfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getAllBundleInfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getApplicationInfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getApplicationInfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getApplicationInfo) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getBundleArchiveInfo) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getBundleArchiveInfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getBundleInfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getBundleInfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getBundleInfo) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getLaunchWantForBundle) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getLaunchWantForBundle) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getNameForUid) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getNameForUid) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isAbilityEnabled) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isAbilityEnabled) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isApplicationEnabled) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isApplicationEnabled) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryAbilityByWant) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryAbilityByWant) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryAbilityByWant) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles-(System-API)) |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles-(System-API)) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getApplicationInfos-(System-API)) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getApplicationInfos-(System-API)) |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md#getApplicationInfos-(System-API)) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getBundleInfos-(System-API)) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getBundleInfos-(System-API)) |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md#getBundleInfos-(System-API)) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getBundleInstaller-(System-API)) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getBundleInstaller-(System-API)) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getPermissionDef-(System-API)) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getPermissionDef-(System-API)) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setAbilityEnabled-(System-API)) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setAbilityEnabled-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
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
