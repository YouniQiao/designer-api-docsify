# @ohos.bundle.bundleResourceManager

The module provides APIs for obtaining resource information, including [BundleResourceInfo](arkts-ability-bundleresourceinfo-i-sys.md#BundleResourceInfo-(System-API)) and [LauncherAbilityResourceInfo](arkts-ability-launcherabilityresourceinfo-i-sys.md#LauncherAbilityResourceInfo-(System-API)). > **NOTE：**> > Starting from API version 12, this module supports query of icons and names of disabled applications and > applications installed by all users. > > The APIs provided by this module are system APIs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace bundleResourceManager--><!--Device-unnamed-declare namespace bundleResourceManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { bundleResourceManager } from 'bundleResourceManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getAllBundleResourceInfo](arkts-ability-bundleresourcemanager-getallbundleresourceinfo-f-sys.md#getAllBundleResourceInfo) | Obtains the bundle resource information of all applications based on the given resource flags. This API uses an asynchronous callback to return the result. |
| [getAllBundleResourceInfo](arkts-ability-bundleresourcemanager-getallbundleresourceinfo-f-sys.md#getAllBundleResourceInfo-(System-API)) | Obtains the bundle resource information of all applications based on the given resource flags. This API uses a promise to return the result. |
| [getAllLauncherAbilityResourceInfo](arkts-ability-bundleresourcemanager-getalllauncherabilityresourceinfo-f-sys.md#getAllLauncherAbilityResourceInfo) | Obtains the resource information of the entry abilities of the current application based on the given resource flags. This API uses an asynchronous callback to return the result. |
| [getAllLauncherAbilityResourceInfo](arkts-ability-bundleresourcemanager-getalllauncherabilityresourceinfo-f-sys.md#getAllLauncherAbilityResourceInfo-(System-API)) | Obtains the resource information of the entry abilities of the current application based on the given resource flags. This API uses a promise to return the result. |
| [getAllUninstalledBundleResourceInfo](arkts-ability-bundleresourcemanager-getalluninstalledbundleresourceinfo-f-sys.md#getAllUninstalledBundleResourceInfo) | Obtains the bundle resource information of all uninstalled applications that have retained data based on the given resource flags. This API uses a promise to return the result. |
| [getBundleResourceInfo](arkts-ability-bundleresourcemanager-getbundleresourceinfo-f-sys.md#getBundleResourceInfo) | Obtains the resource information of an application based on the given bundle name and resource flags. This API returns the result synchronously. |
| [getBundleResourceInfo](arkts-ability-bundleresourcemanager-getbundleresourceinfo-f-sys.md#getBundleResourceInfo-(System-API)) | Obtains the resource information of an application based on the given bundle name, resource flags, and app index. This API returns the result synchronously. |
| [getExtensionAbilityResourceInfo](arkts-ability-bundleresourcemanager-getextensionabilityresourceinfo-f-sys.md#getExtensionAbilityResourceInfo) | Obtains the ExtensionAbility resource information of an application based on the bundle name, ExtensionAbility type , resource flags, and clone ID. This API returns the result synchronously. |
| [getLauncherAbilityResourceInfo](arkts-ability-bundleresourcemanager-getlauncherabilityresourceinfo-f-sys.md#getLauncherAbilityResourceInfo) | Obtains the bundle information of the entry ability of an application based on the given bundle name and resource flags. This API returns the result synchronously. |
| [getLauncherAbilityResourceInfo](arkts-ability-bundleresourcemanager-getlauncherabilityresourceinfo-f-sys.md#getLauncherAbilityResourceInfo-(System-API)) | Obtains the launcher ability resource information of an application based on the given bundle name, resource flags, and app index. This API returns the result synchronously. |
| [getLauncherAbilityResourceInfoList](arkts-ability-bundleresourcemanager-getlauncherabilityresourceinfolist-f-sys.md#getLauncherAbilityResourceInfoList) | Obtains the launcher ability resource information of each application corresponding to the **BundleOptions** element in **optionsList**. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ResourceFlag](arkts-ability-bundleresourcemanager-resourceflag-e-sys.md) | Enumerates the resource information flags, which indicate the type of resource information to obtain. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [BundleResourceInfo](arkts-ability-bundleresourcemanager-bundleresourceinfo-t-sys.md) | Defines the icon and name of an application. |
| [LauncherAbilityResourceInfo](arkts-ability-bundleresourcemanager-launcherabilityresourceinfo-t-sys.md) | Defines the entry icon and name of an application. &lt;!--no_check--&gt; |
<!--DelEnd-->

