# @ohos.bundle.bundleManager

本模块提供应用信息的查询能力，支持应用包信息BundleInfo、应用程序信息 ApplicationInfo、UIAbility组件信息 AbilityInfo、ExtensionAbility组件信息 [ExtensionAbilityInfo](arkts-ability-extensionabilityinfo-i.md)等信息的查询。

**起始版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [canOpenLink](arkts-ability-bundlemanager-canopenlink-f.md) |
| [cleanBundleCacheFilesForSelf](arkts-ability-bundlemanager-cleanbundlecachefilesforself-f.md) |
| [getAbilityInfo](arkts-ability-bundlemanager-getabilityinfo-f.md) |
| [getAlternateIcons](arkts-ability-bundlemanager-getalternateicons-f.md) |
| [getAppCloneIdentity](arkts-ability-bundlemanager-getappcloneidentity-f.md) |
| [getApplicationLabel](arkts-ability-bundlemanager-getapplicationlabel-f.md) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md) |
| [getBundleInfoForSelfSync](arkts-ability-bundlemanager-getbundleinfoforselfsync-f.md) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md) |
| [getBundleNameByUidSync](arkts-ability-bundlemanager-getbundlenamebyuidsync-f.md) |
| [getInstalledBundleList](arkts-ability-bundlemanager-getinstalledbundlelist-f.md) |
| [getLaunchWant](arkts-ability-bundlemanager-getlaunchwant-f.md) |
| [getLaunchWantForBundleSync](arkts-ability-bundlemanager-getlaunchwantforbundlesync-f.md) |
| [getPluginBundlePathForSelf](arkts-ability-bundlemanager-getpluginbundlepathforself-f.md) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md) |
| [getProfileByAbilitySync](arkts-ability-bundlemanager-getprofilebyabilitysync-f.md) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md) |
| [getProfileByExtensionAbilitySync](arkts-ability-bundlemanager-getprofilebyextensionabilitysync-f.md) |
| [getSignatureInfo](arkts-ability-bundlemanager-getsignatureinfo-f.md) |
| [setAlternateIcon](arkts-ability-bundlemanager-setalternateicon-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [cleanAllBundleCache](arkts-ability-bundlemanager-cleanallbundlecache-f-sys.md) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md) |
| [deleteAbc](arkts-ability-bundlemanager-deleteabc-f-sys.md) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md) |
| [getAbilityLabelSync](arkts-ability-bundlemanager-getabilitylabelsync-f-sys.md) |
| [getAdditionalInfo](arkts-ability-bundlemanager-getadditionalinfo-f-sys.md) |
| [getAllAppCloneBundleInfo](arkts-ability-bundlemanager-getallappclonebundleinfo-f-sys.md) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md) |
| [getAllAppProvisionInfo](arkts-ability-bundlemanager-getallappprovisioninfo-f-sys.md) |
| [getAllBundleCacheSize](arkts-ability-bundlemanager-getallbundlecachesize-f-sys.md) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md) |
| [getAllBundleInfoByDeveloperId](arkts-ability-bundlemanager-getallbundleinfobydeveloperid-f-sys.md) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md) |
| [getAllDynamicIconInfo](arkts-ability-bundlemanager-getalldynamiciconinfo-f-sys.md) |
| [getAllNewPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallnewpreinstalledapplicationinfo-f-sys.md) |
| [getAllPluginInfo](arkts-ability-bundlemanager-getallplugininfo-f-sys.md) |
| [getAllPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallpreinstalledapplicationinfo-f-sys.md) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md) |
| [getAppCloneBundleInfo](arkts-ability-bundlemanager-getappclonebundleinfo-f-sys.md) |
| [getAppCloneIdentityBySandboxDataDir](arkts-ability-bundlemanager-getappcloneidentitybysandboxdatadir-f-sys.md) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md) |
| [getAppProvisionInfoSync](arkts-ability-bundlemanager-getappprovisioninfosync-f-sys.md) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md) |
| [getBundleArchiveInfoSync](arkts-ability-bundlemanager-getbundlearchiveinfosync-f-sys.md) |
| [getBundleInstallStatus](arkts-ability-bundlemanager-getbundleinstallstatus-f-sys.md) |
| [getDeveloperIds](arkts-ability-bundlemanager-getdeveloperids-f-sys.md) |
| [getDynamicIcon](arkts-ability-bundlemanager-getdynamicicon-f-sys.md) |
| [getDynamicIconInfo](arkts-ability-bundlemanager-getdynamiciconinfo-f-sys.md) |
| [getExtResource](arkts-ability-bundlemanager-getextresource-f-sys.md) |
| [getJsonProfile](arkts-ability-bundlemanager-getjsonprofile-f-sys.md) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md) |
| [getPermissionDefSync](arkts-ability-bundlemanager-getpermissiondefsync-f-sys.md) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md) |
| [getSandboxDataDir](arkts-ability-bundlemanager-getsandboxdatadir-f-sys.md) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md) |
| [getSpecifiedDistributionType](arkts-ability-bundlemanager-getspecifieddistributiontype-f-sys.md) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md) |
| [isAbilityEnabledSync](arkts-ability-bundlemanager-isabilityenabledsync-f-sys.md) |
| [isApplicationDisableForbidden](arkts-ability-bundlemanager-isapplicationdisableforbidden-f-sys.md) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md) |
| [isApplicationEnabledSync](arkts-ability-bundlemanager-isapplicationenabledsync-f-sys.md) |
| [migrateData](arkts-ability-bundlemanager-migratedata-f-sys.md) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md) |
| [queryAbilityInfoSync](arkts-ability-bundlemanager-queryabilityinfosync-f-sys.md) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md) |
| [recoverBackupBundleData](arkts-ability-bundlemanager-recoverbackupbundledata-f-sys.md) |
| [removeBackupBundleData](arkts-ability-bundlemanager-removebackupbundledata-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md) |
| [setAbilityEnabledSync](arkts-ability-bundlemanager-setabilityenabledsync-f-sys.md) |
| [setAbilityFileTypesForSelf](arkts-ability-bundlemanager-setabilityfiletypesforself-f-sys.md) |
| [setAdditionalInfo](arkts-ability-bundlemanager-setadditionalinfo-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md) |
| [switchUninstallState](arkts-ability-bundlemanager-switchuninstallstate-f-sys.md) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AbilityFlag](arkts-ability-bundlemanager-abilityflag-e.md) |
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
### 枚举（系统接口）

| 名称 |
| --- |
| [AppDistributionType](arkts-ability-bundlemanager-appdistributiontype-e-sys.md) |
| [ApplicationFlag](arkts-ability-bundlemanager-applicationflag-e-sys.md) |
| [ApplicationInfoFlag](arkts-ability-bundlemanager-applicationinfoflag-e-sys.md) |
| [BundleFlag](arkts-ability-bundlemanager-bundleflag-e-sys.md) |
| [BundleInstallStatus](arkts-ability-bundlemanager-bundleinstallstatus-e-sys.md) |
| [ExtensionAbilityFlag](arkts-ability-bundlemanager-extensionabilityflag-e-sys.md) |
| [ProfileType](arkts-ability-bundlemanager-profiletype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
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
### 类型（系统接口）

| 名称 |
| --- |
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
