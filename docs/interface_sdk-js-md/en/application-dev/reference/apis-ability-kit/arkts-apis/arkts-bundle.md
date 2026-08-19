# @ohos.bundle

The module provides APIs for obtaining information about an application, including bundle information, [application information](arkts-ability-applicationinfo-applicationinfo-depr-i.md#applicationinfo), and [ability information](arkts-ability-abilityinfo-abilityinfo-depr-i.md#abilityinfo). It also provides APIs to obtain and set the application disabling state. &gt; **NOTE：**&gt; &gt; The APIs of this module have been deprecated since API version 9. You are advised to use &gt; [@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [bundleManager](arkts-bundle-bundlemanager.md)

<!--Device-unnamed-declare namespace bundle--><!--Device-unnamed-declare namespace bundle-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { bundleMonitor } from '@kit.AbilityKit';
import { bundleResourceManager } from '@kit.AbilityKit';
import { bundle } from '@kit.AbilityKit';
import { defaultAppManager } from '@kit.AbilityKit';
import { distributedBundleManager } from '@kit.AbilityKit';
import { freeInstall } from '@kit.AbilityKit';
import { innerBundleManager, BundleStatusCallback } from '@kit.AbilityKit';
import { installer } from '@kit.AbilityKit';
import { launcherBundleManager } from '@kit.AbilityKit';
import { overlay } from '@kit.AbilityKit';
import { shortcutManager } from '@kit.AbilityKit';
import { skillManager } from '@kit.AbilityKit';
import { appDomainVerify } from '@kit.AbilityKit';
import { pluginBundleManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md) | Obtains the [PixelMap](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) of the icon corresponding to a given bundle name and ability name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md) | Obtains the [PixelMap](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) of the icon corresponding to a given bundle name and ability name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md) | Obtains the ability information based on a given bundle name and ability name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md) | Obtains the ability information based on a given bundle name and ability name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md) | Obtains the application name based on a given bundle name and ability name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md) | Obtains the application name based on a given bundle name and ability name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) | Obtains the information about all applications. This API uses an asynchronous callback to return the result. |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) | Obtains the information about all applications of the current user. This API uses an asynchronous callback to return the result. |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md) | Obtains the information about all applications of the specified user. This API uses a promise to return the result. |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) | Obtains the information of all bundles of the specified user. This API uses an asynchronous callback to return the result. |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) | Obtains the information of all bundles of the current user. This API uses an asynchronous callback to return the result. |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md) | Obtains the information of all bundles of the specified user. This API uses a promise to return the result. |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) | Obtains the application information of the specified user based on a given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) | Obtains the application information based on a given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md) | Obtains the application information based on a given bundle name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md) | Obtains information about the bundles contained in a HAP file. This API uses an asynchronous callback to return the result. |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md) | Obtains information about the bundles contained in a HAP file. This API uses a promise to return the result. |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) | Obtains the bundle information based on a given bundle name and bundle options. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) | Obtains the bundle information based on a given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md) | Obtains the bundle information based on a given bundle name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md) | Obtains the Want object that launches the specified application. This API uses an asynchronous callback to return the result. |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md) | Obtains the Want object that launches the specified application. This API uses a promise to return the result. |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md) | Obtains bundle name by the given uid. |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md) | Obtains the bundle name based on a UID. This API uses a promise to return the result. |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md) | Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses an asynchronous callback to return the result. |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md) | Checks whether the ability that matches a given AbilityInfo object is enabled. This API uses a promise to return the result. |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md) | Checks whether an application is enabled based on a given bundle name. This API uses an asynchronous callback to return the result. |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md) | Checks whether an application is enabled based on a given bundle name. This API uses a promise to return the result. |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) | Obtains the ability information of the specified user based on given Want. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) | Obtains the ability information based on given Want. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information. |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md) | Obtains the ability information based on given Want. This API uses a promise to return the result. No permission is required for obtaining the caller's own information. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) | Clears the cache data of an application. This API uses an asynchronous callback to return the result. |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) | Clears the cache data of an application. This API uses a promise to return the result. |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) | Obtains information about all installed apps for a specified user. This API uses an asynchronous callback to return the result. |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) | Obtains information about installed apps for the user to which the caller belongs. This API uses an asynchronous callback to return the result. |
| [getApplicationInfos](arkts-ability-bundle-getapplicationinfos-f-sys.md) | Obtains information about all installed apps for a specified user. This API uses a promise to return the result. |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) | Obtains all BundleInfo for a specified user in the system. This API uses an asynchronous callback to return the result. |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) | Obtains all BundleInfo for the current user. This API uses an asynchronous callback to return the result. |
| [getBundleInfos](arkts-ability-bundle-getbundleinfos-f-sys.md) | Obtains all BundleInfo for a specified user. This API uses a promise to return the result. |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) | Obtains the installation package. This API uses an asynchronous callback to return the result. |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) | Obtains the installation package. This API uses a promise to return the result. |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) | Obtains the permission details by permission name. This API uses an asynchronous callback to return the result. |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) | Obtains the permission details by permission name. This API uses a promise to return the result. |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) | Sets whether to enable an ability. This API uses an asynchronous callback to return the result. |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) | Sets whether to enable an ability. This API uses a promise to return the result. |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) | Sets whether to enable an application. This API uses an asynchronous callback to return the result. |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) | Sets whether to enable an application. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided. Options that contain the user ID. |

### Enums

| Name | Description |
| --- | --- |
| [AbilitySubType](arkts-ability-bundle-abilitysubtype-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided. Enumerates the ability subtypes. |
| [AbilityType](arkts-ability-bundle-abilitytype-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [bundleManager.AbilityType](arkts-ability-bundlemanager-abilitytype-e.md) instead. Enumerates the ability types. |
| [BundleFlag](arkts-ability-bundle-bundleflag-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [bundleManager.BundleFlag](arkts-ability-bundlemanager-bundleflag-e.md) instead. Enumerates the bundle flags, which indicate the type of bundle information to obtain. If an API does not match the flag, the flag is ignored. For example, using **GET_ABILITY_INFO_WITH_PERMISSION** to obtain the application information does not affect the result. Flags can be used together. For example, you can use the combination of **GET_APPLICATION_INFO_WITH_PERMISSION** and **GET_APPLICATION_INFO_WITH_DISABLE** to obtain the result that contains both application permission information and disabled application information. |
| [ColorMode](arkts-ability-bundle-colormode-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided. Enumerates the color modes of applications and widgets. |
| [DisplayOrientation](arkts-ability-bundle-displayorientation-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [bundleManager.DisplayOrientation](arkts-ability-bundlemanager-displayorientation-e.md) instead. Enumerates display orientations. |
| [GrantStatus](arkts-ability-bundle-grantstatus-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [bundleManager.PermissionGrantState](arkts-ability-bundlemanager-permissiongrantstate-e.md) &gt; instead. Enumerates the permission grant states. |
| [InstallErrorCode](arkts-ability-bundle-installerrorcode-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [errorcode-bundle](../errorcode-bundle.md) instead. |
| [LaunchMode](arkts-ability-bundle-launchmode-e.md) | > **NOTE：**&gt; &gt; This API has been supported since API version 7 and deprecated since API version 9. You are advised to use &gt; [bundleManager.LaunchType](arkts-ability-bundlemanager-launchtype-e.md) instead. Enumerates the ability launch modes. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ModuleRemoveFlag](arkts-ability-bundle-moduleremoveflag-e-sys.md) | Flag indicating whether a module is associated with a widget or shortcut when it is removed. |
| [QueryShortCutFlag](arkts-ability-bundle-queryshortcutflag-e-sys.md) | Flag used to specify the query scope for shortcuts. |
| [ShortcutExistence](arkts-ability-bundle-shortcutexistence-e-sys.md) | Result returned when querying whether a shortcut exists. |
| [SignatureCompareResult](arkts-ability-bundle-signaturecompareresult-e-sys.md) | Signature verification result. |
<!--DelEnd-->

