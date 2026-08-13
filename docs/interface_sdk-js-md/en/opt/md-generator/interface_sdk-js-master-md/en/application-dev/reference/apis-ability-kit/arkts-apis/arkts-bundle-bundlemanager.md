# @ohos.bundle.bundleManager

The module provides APIs for obtaining application information, including bundle information, application information, ability information (information about a UIAbility), and [ExtensionAbility information](arkts-ability-extensionabilityinfo-i.md#ExtensionAbilityInfo).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [canOpenLink](arkts-ability-bundlemanager-canopenlink-f.md#canOpenLink) |
| [cleanBundleCacheFilesForSelf](arkts-ability-bundlemanager-cleanbundlecachefilesforself-f.md#cleanBundleCacheFilesForSelf) |
| [getAbilityInfo](arkts-ability-bundlemanager-getabilityinfo-f.md#getAbilityInfo) |
| [getAlternateIcons](arkts-ability-bundlemanager-getalternateicons-f.md#getAlternateIcons) |
| [getAppCloneIdentity](arkts-ability-bundlemanager-getappcloneidentity-f.md#getAppCloneIdentity) |
| [getApplicationLabel](arkts-ability-bundlemanager-getapplicationlabel-f.md#getApplicationLabel) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getBundleInfo) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getBundleInfo) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getBundleInfo) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf) |
| [getBundleInfoForSelfSync](arkts-ability-bundlemanager-getbundleinfoforselfsync-f.md#getBundleInfoForSelfSync) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getBundleInfoSync) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getBundleInfoSync) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md#getBundleNameByUid) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md#getBundleNameByUid) |
| [getBundleNameByUidSync](arkts-ability-bundlemanager-getbundlenamebyuidsync-f.md#getBundleNameByUidSync) |
| [getInstalledBundleList](arkts-ability-bundlemanager-getinstalledbundlelist-f.md#getInstalledBundleList) |
| [getLaunchWant](arkts-ability-bundlemanager-getlaunchwant-f.md#getLaunchWant) |
| [getPluginBundlePathForSelf](arkts-ability-bundlemanager-getpluginbundlepathforself-f.md#getPluginBundlePathForSelf) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md#getProfileByAbility) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md#getProfileByAbility) |
| [getProfileByAbilitySync](arkts-ability-bundlemanager-getprofilebyabilitysync-f.md#getProfileByAbilitySync) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md#getProfileByExtensionAbility) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md#getProfileByExtensionAbility) |
| [getProfileByExtensionAbilitySync](arkts-ability-bundlemanager-getprofilebyextensionabilitysync-f.md#getProfileByExtensionAbilitySync) |
| [getSignatureInfo](arkts-ability-bundlemanager-getsignatureinfo-f.md#getSignatureInfo) |
| [setAlternateIcon](arkts-ability-bundlemanager-setalternateicon-f.md#setAlternateIcon) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cleanAllBundleCache](arkts-ability-bundlemanager-cleanallbundlecache-f-sys.md#cleanAllBundleCache-(System-API)) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles-(System-API)) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles-(System-API)) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles-(System-API)) |
| [deleteAbc](arkts-ability-bundlemanager-deleteabc-f-sys.md#deleteAbc-(System-API)) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disableDynamicIcon-(System-API)) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disableDynamicIcon-(System-API)) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enableDynamicIcon-(System-API)) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enableDynamicIcon-(System-API)) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getAbilityIcon-(System-API)) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getAbilityIcon-(System-API)) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getAbilityLabel-(System-API)) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getAbilityLabel-(System-API)) |
| [getAbilityLabelSync](arkts-ability-bundlemanager-getabilitylabelsync-f-sys.md#getAbilityLabelSync-(System-API)) |
| [getAdditionalInfo](arkts-ability-bundlemanager-getadditionalinfo-f-sys.md#getAdditionalInfo-(System-API)) |
| [getAllAppCloneBundleInfo](arkts-ability-bundlemanager-getallappclonebundleinfo-f-sys.md#getAllAppCloneBundleInfo-(System-API)) |
| [getAllAppProvisionInfo](arkts-ability-bundlemanager-getallappprovisioninfo-f-sys.md#getAllAppProvisionInfo-(System-API)) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo-(System-API)) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo-(System-API)) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo-(System-API)) |
| [getAllBundleCacheSize](arkts-ability-bundlemanager-getallbundlecachesize-f-sys.md#getAllBundleCacheSize-(System-API)) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo-(System-API)) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo-(System-API)) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo-(System-API)) |
| [getAllBundleInfoByDeveloperId](arkts-ability-bundlemanager-getallbundleinfobydeveloperid-f-sys.md#getAllBundleInfoByDeveloperId-(System-API)) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md#getAllBundleInstallInfo-(System-API)) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md#getAllBundleInstallInfo-(System-API)) |
| [getAllDynamicIconInfo](arkts-ability-bundlemanager-getalldynamiciconinfo-f-sys.md#getAllDynamicIconInfo-(System-API)) |
| [getAllNewPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallnewpreinstalledapplicationinfo-f-sys.md#getAllNewPreinstalledApplicationInfo-(System-API)) |
| [getAllPluginInfo](arkts-ability-bundlemanager-getallplugininfo-f-sys.md#getAllPluginInfo-(System-API)) |
| [getAllPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallpreinstalledapplicationinfo-f-sys.md#getAllPreinstalledApplicationInfo-(System-API)) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getAllSharedBundleInfo-(System-API)) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getAllSharedBundleInfo-(System-API)) |
| [getAppCloneBundleInfo](arkts-ability-bundlemanager-getappclonebundleinfo-f-sys.md#getAppCloneBundleInfo-(System-API)) |
| [getAppCloneIdentityBySandboxDataDir](arkts-ability-bundlemanager-getappcloneidentitybysandboxdatadir-f-sys.md#getAppCloneIdentityBySandboxDataDir-(System-API)) |
| [getAppClonePreference](arkts-ability-bundlemanager-getappclonepreference-f-sys.md#getAppClonePreference-(System-API)) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo-(System-API)) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo-(System-API)) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo-(System-API)) |
| [getAppProvisionInfoSync](arkts-ability-bundlemanager-getappprovisioninfosync-f-sys.md#getAppProvisionInfoSync-(System-API)) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo-(System-API)) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo-(System-API)) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo-(System-API)) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getApplicationInfoSync-(System-API)) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getApplicationInfoSync-(System-API)) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getBundleArchiveInfo-(System-API)) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getBundleArchiveInfo-(System-API)) |
| [getBundleArchiveInfoSync](arkts-ability-bundlemanager-getbundlearchiveinfosync-f-sys.md#getBundleArchiveInfoSync-(System-API)) |
| [getBundleInstallStatus](arkts-ability-bundlemanager-getbundleinstallstatus-f-sys.md#getBundleInstallStatus-(System-API)) |
| [getDeveloperIds](arkts-ability-bundlemanager-getdeveloperids-f-sys.md#getDeveloperIds-(System-API)) |
| [getDynamicIcon](arkts-ability-bundlemanager-getdynamicicon-f-sys.md#getDynamicIcon-(System-API)) |
| [getDynamicIconInfo](arkts-ability-bundlemanager-getdynamiciconinfo-f-sys.md#getDynamicIconInfo-(System-API)) |
| [getExtResource](arkts-ability-bundlemanager-getextresource-f-sys.md#getExtResource-(System-API)) |
| [getJsonProfile](arkts-ability-bundlemanager-getjsonprofile-f-sys.md#getJsonProfile-(System-API)) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle-(System-API)) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle-(System-API)) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle-(System-API)) |
| [getLaunchWantForBundleSync](arkts-ability-bundlemanager-getlaunchwantforbundlesync-f-sys.md#getLaunchWantForBundleSync-(System-API)) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getPermissionDef-(System-API)) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getPermissionDef-(System-API)) |
| [getPermissionDefSync](arkts-ability-bundlemanager-getpermissiondefsync-f-sys.md#getPermissionDefSync-(System-API)) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getRecoverableApplicationInfo-(System-API)) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getRecoverableApplicationInfo-(System-API)) |
| [getSandboxDataDir](arkts-ability-bundlemanager-getsandboxdatadir-f-sys.md#getSandboxDataDir-(System-API)) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getSharedBundleInfo-(System-API)) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getSharedBundleInfo-(System-API)) |
| [getSpecifiedDistributionType](arkts-ability-bundlemanager-getspecifieddistributiontype-f-sys.md#getSpecifiedDistributionType-(System-API)) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled-(System-API)) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled-(System-API)) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled-(System-API)) |
| [isAbilityEnabledSync](arkts-ability-bundlemanager-isabilityenabledsync-f-sys.md#isAbilityEnabledSync-(System-API)) |
| [isApplicationDisableForbidden](arkts-ability-bundlemanager-isapplicationdisableforbidden-f-sys.md#isApplicationDisableForbidden-(System-API)) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled-(System-API)) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled-(System-API)) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled-(System-API)) |
| [isApplicationEnabledSync](arkts-ability-bundlemanager-isapplicationenabledsync-f-sys.md#isApplicationEnabledSync-(System-API)) |
| [migrateData](arkts-ability-bundlemanager-migratedata-f-sys.md#migrateData-(System-API)) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo-(System-API)) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo-(System-API)) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo-(System-API)) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo-(System-API)) |
| [queryAbilityInfoSync](arkts-ability-bundlemanager-queryabilityinfosync-f-sys.md#queryAbilityInfoSync-(System-API)) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo-(System-API)) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo-(System-API)) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo-(System-API)) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync-(System-API)) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync-(System-API)) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync-(System-API)) |
| [recoverBackupBundleData](arkts-ability-bundlemanager-recoverbackupbundledata-f-sys.md#recoverBackupBundleData-(System-API)) |
| [removeBackupBundleData](arkts-ability-bundlemanager-removebackupbundledata-f-sys.md#removeBackupBundleData-(System-API)) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled-(System-API)) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled-(System-API)) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled-(System-API)) |
| [setAbilityEnabledSync](arkts-ability-bundlemanager-setabilityenabledsync-f-sys.md#setAbilityEnabledSync-(System-API)) |
| [setAbilityFileTypesForSelf](arkts-ability-bundlemanager-setabilityfiletypesforself-f-sys.md#setAbilityFileTypesForSelf-(System-API)) |
| [setAdditionalInfo](arkts-ability-bundlemanager-setadditionalinfo-f-sys.md#setAdditionalInfo-(System-API)) |
| [setAppClonePreference](arkts-ability-bundlemanager-setappclonepreference-f-sys.md#setAppClonePreference-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled-(System-API)) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setApplicationEnabledSync-(System-API)) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setApplicationEnabledSync-(System-API)) |
| [switchUninstallState](arkts-ability-bundlemanager-switchuninstallstate-f-sys.md#switchUninstallState-(System-API)) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyAbc-(System-API)) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyAbc-(System-API)) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityType](arkts-ability-bundlemanager-abilitytype-e.md) |
| [BundleFlag](arkts-ability-bundlemanager-bundleflag-e.md) |
| [BundleType](arkts-ability-bundlemanager-bundletype-e.md) |
| [CompatiblePolicy](arkts-ability-bundlemanager-compatiblepolicy-e.md) |
| [DisplayOrientation](arkts-ability-bundlemanager-displayorientation-e.md) |
| [ExtensionAbilityType](arkts-ability-bundlemanager-extensionabilitytype-e.md) |
| [LaunchType](arkts-ability-bundlemanager-launchtype-e.md) |
| [ModuleType](arkts-ability-bundlemanager-moduletype-e.md) |
| [MultiAppModeType](arkts-ability-bundlemanager-multiappmodetype-e.md) |
| [PermissionGrantState](arkts-ability-bundlemanager-permissiongrantstate-e.md) |
| [SupportWindowMode](arkts-ability-bundlemanager-supportwindowmode-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityFlag](arkts-ability-bundlemanager-abilityflag-e-sys.md) |
| [AppClonePreferenceMode](arkts-ability-bundlemanager-appclonepreferencemode-e-sys.md) |
| [AppDistributionType](arkts-ability-bundlemanager-appdistributiontype-e-sys.md) |
| [ApplicationFlag](arkts-ability-bundlemanager-applicationflag-e-sys.md) |
| [ApplicationInfoFlag](arkts-ability-bundlemanager-applicationinfoflag-e-sys.md) |
| [BundleFlag](arkts-ability-bundlemanager-bundleflag-e-sys.md) |
| [BundleInstallStatus](arkts-ability-bundlemanager-bundleinstallstatus-e-sys.md) |
| [ExtensionAbilityFlag](arkts-ability-bundlemanager-extensionabilityflag-e-sys.md) |
| [ProfileType](arkts-ability-bundlemanager-profiletype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityInfo](arkts-ability-bundlemanager-abilityinfo-t.md) |
| [AlternateIconInfo](arkts-ability-bundlemanager-alternateiconinfo-t.md) |
| [AppCloneIdentity](arkts-ability-bundlemanager-appcloneidentity-t.md) |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) |
| [BundleInfo](arkts-ability-bundlemanager-bundleinfo-t.md) |
| [DataItem](arkts-ability-bundlemanager-dataitem-t.md) |
| [Dependency](arkts-ability-bundlemanager-dependency-t.md) |
| [ElementName](arkts-ability-bundlemanager-elementname-t.md) |
| [ExtensionAbilityInfo](arkts-ability-bundlemanager-extensionabilityinfo-t.md) |
| [HapModuleInfo](arkts-ability-bundlemanager-hapmoduleinfo-t.md) |
| [Metadata](arkts-ability-bundlemanager-metadata-t.md) |
| [ModuleMetadata](arkts-ability-bundlemanager-modulemetadata-t.md) |
| [PreloadItem](arkts-ability-bundlemanager-preloaditem-t.md) |
| [ReqPermissionDetail](arkts-ability-bundlemanager-reqpermissiondetail-t.md) |
| [RouterItem](arkts-ability-bundlemanager-routeritem-t.md) |
| [SignatureInfo](arkts-ability-bundlemanager-signatureinfo-t.md) |
| [Skill](arkts-ability-bundlemanager-skill-t.md) |
| [SkillUrl](arkts-ability-bundlemanager-skillurl-t.md) |
| [UsedScene](arkts-ability-bundlemanager-usedscene-t.md) |
| [WindowSize](arkts-ability-bundlemanager-windowsize-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppClonePreference](arkts-ability-bundlemanager-appclonepreference-t-sys.md) |
| [AppProvisionInfo](arkts-ability-bundlemanager-appprovisioninfo-t-sys.md) |
| [BundleOptions](arkts-ability-bundlemanager-bundleoptions-t-sys.md) |
| [DynamicIconInfo](arkts-ability-bundlemanager-dynamiciconinfo-t-sys.md) |
| [PermissionDef](arkts-ability-bundlemanager-permissiondef-t-sys.md) |
| [PluginBundleInfo](arkts-ability-bundlemanager-pluginbundleinfo-t-sys.md) |
| [PluginModuleInfo](arkts-ability-bundlemanager-pluginmoduleinfo-t-sys.md) |
| [PreinstalledApplicationInfo](arkts-ability-bundlemanager-preinstalledapplicationinfo-t-sys.md) |
| [RecoverableApplicationInfo](arkts-ability-bundlemanager-recoverableapplicationinfo-t-sys.md) |
| [SharedBundleInfo](arkts-ability-bundlemanager-sharedbundleinfo-t-sys.md) |
| [Validity](arkts-ability-bundlemanager-validity-t-sys.md) |
<!--DelEnd-->
