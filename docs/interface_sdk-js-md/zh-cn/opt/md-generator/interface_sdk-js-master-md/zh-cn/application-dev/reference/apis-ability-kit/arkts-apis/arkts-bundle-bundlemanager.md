# @ohos.bundle.bundleManager

本模块提供应用信息的查询能力，支持应用包信息BundleInfo、应用程序信息 ApplicationInfo、UIAbility组件信息 AbilityInfo、ExtensionAbility组件信息 [ExtensionAbilityInfo](arkts-ability-extensionabilityinfo-i.md#ExtensionAbilityInfo)等信息的查询。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [cleanAllBundleCache](arkts-ability-bundlemanager-cleanallbundlecache-f-sys.md#cleanAllBundleCache（系统接口）) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles（系统接口）) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles（系统接口）) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanBundleCacheFiles（系统接口）) |
| [deleteAbc](arkts-ability-bundlemanager-deleteabc-f-sys.md#deleteAbc（系统接口）) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disableDynamicIcon（系统接口）) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disableDynamicIcon（系统接口）) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enableDynamicIcon（系统接口）) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enableDynamicIcon（系统接口）) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getAbilityIcon（系统接口）) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getAbilityIcon（系统接口）) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getAbilityLabel（系统接口）) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getAbilityLabel（系统接口）) |
| [getAbilityLabelSync](arkts-ability-bundlemanager-getabilitylabelsync-f-sys.md#getAbilityLabelSync（系统接口）) |
| [getAdditionalInfo](arkts-ability-bundlemanager-getadditionalinfo-f-sys.md#getAdditionalInfo（系统接口）) |
| [getAllAppCloneBundleInfo](arkts-ability-bundlemanager-getallappclonebundleinfo-f-sys.md#getAllAppCloneBundleInfo（系统接口）) |
| [getAllAppProvisionInfo](arkts-ability-bundlemanager-getallappprovisioninfo-f-sys.md#getAllAppProvisionInfo（系统接口）) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo（系统接口）) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo（系统接口）) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getAllApplicationInfo（系统接口）) |
| [getAllBundleCacheSize](arkts-ability-bundlemanager-getallbundlecachesize-f-sys.md#getAllBundleCacheSize（系统接口）) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo（系统接口）) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo（系统接口）) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getAllBundleInfo（系统接口）) |
| [getAllBundleInfoByDeveloperId](arkts-ability-bundlemanager-getallbundleinfobydeveloperid-f-sys.md#getAllBundleInfoByDeveloperId（系统接口）) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md#getAllBundleInstallInfo（系统接口）) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md#getAllBundleInstallInfo（系统接口）) |
| [getAllDynamicIconInfo](arkts-ability-bundlemanager-getalldynamiciconinfo-f-sys.md#getAllDynamicIconInfo（系统接口）) |
| [getAllNewPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallnewpreinstalledapplicationinfo-f-sys.md#getAllNewPreinstalledApplicationInfo（系统接口）) |
| [getAllPluginInfo](arkts-ability-bundlemanager-getallplugininfo-f-sys.md#getAllPluginInfo（系统接口）) |
| [getAllPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallpreinstalledapplicationinfo-f-sys.md#getAllPreinstalledApplicationInfo（系统接口）) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getAllSharedBundleInfo（系统接口）) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getAllSharedBundleInfo（系统接口）) |
| [getAppCloneBundleInfo](arkts-ability-bundlemanager-getappclonebundleinfo-f-sys.md#getAppCloneBundleInfo（系统接口）) |
| [getAppCloneIdentityBySandboxDataDir](arkts-ability-bundlemanager-getappcloneidentitybysandboxdatadir-f-sys.md#getAppCloneIdentityBySandboxDataDir（系统接口）) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo（系统接口）) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo（系统接口）) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getAppProvisionInfo（系统接口）) |
| [getAppProvisionInfoSync](arkts-ability-bundlemanager-getappprovisioninfosync-f-sys.md#getAppProvisionInfoSync（系统接口）) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo（系统接口）) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo（系统接口）) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getApplicationInfo（系统接口）) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getApplicationInfoSync（系统接口）) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getApplicationInfoSync（系统接口）) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getBundleArchiveInfo（系统接口）) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getBundleArchiveInfo（系统接口）) |
| [getBundleArchiveInfoSync](arkts-ability-bundlemanager-getbundlearchiveinfosync-f-sys.md#getBundleArchiveInfoSync（系统接口）) |
| [getBundleInstallStatus](arkts-ability-bundlemanager-getbundleinstallstatus-f-sys.md#getBundleInstallStatus（系统接口）) |
| [getDeveloperIds](arkts-ability-bundlemanager-getdeveloperids-f-sys.md#getDeveloperIds（系统接口）) |
| [getDynamicIcon](arkts-ability-bundlemanager-getdynamicicon-f-sys.md#getDynamicIcon（系统接口）) |
| [getDynamicIconInfo](arkts-ability-bundlemanager-getdynamiciconinfo-f-sys.md#getDynamicIconInfo（系统接口）) |
| [getExtResource](arkts-ability-bundlemanager-getextresource-f-sys.md#getExtResource（系统接口）) |
| [getJsonProfile](arkts-ability-bundlemanager-getjsonprofile-f-sys.md#getJsonProfile（系统接口）) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle（系统接口）) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle（系统接口）) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getLaunchWantForBundle（系统接口）) |
| [getLaunchWantForBundleSync](arkts-ability-bundlemanager-getlaunchwantforbundlesync-f-sys.md#getLaunchWantForBundleSync（系统接口）) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getPermissionDef（系统接口）) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getPermissionDef（系统接口）) |
| [getPermissionDefSync](arkts-ability-bundlemanager-getpermissiondefsync-f-sys.md#getPermissionDefSync（系统接口）) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getRecoverableApplicationInfo（系统接口）) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getRecoverableApplicationInfo（系统接口）) |
| [getSandboxDataDir](arkts-ability-bundlemanager-getsandboxdatadir-f-sys.md#getSandboxDataDir（系统接口）) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getSharedBundleInfo（系统接口）) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getSharedBundleInfo（系统接口）) |
| [getSpecifiedDistributionType](arkts-ability-bundlemanager-getspecifieddistributiontype-f-sys.md#getSpecifiedDistributionType（系统接口）) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled（系统接口）) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled（系统接口）) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isAbilityEnabled（系统接口）) |
| [isAbilityEnabledSync](arkts-ability-bundlemanager-isabilityenabledsync-f-sys.md#isAbilityEnabledSync（系统接口）) |
| [isApplicationDisableForbidden](arkts-ability-bundlemanager-isapplicationdisableforbidden-f-sys.md#isApplicationDisableForbidden（系统接口）) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled（系统接口）) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled（系统接口）) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isApplicationEnabled（系统接口）) |
| [isApplicationEnabledSync](arkts-ability-bundlemanager-isapplicationenabledsync-f-sys.md#isApplicationEnabledSync（系统接口）) |
| [migrateData](arkts-ability-bundlemanager-migratedata-f-sys.md#migrateData（系统接口）) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo（系统接口）) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo（系统接口）) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo（系统接口）) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryAbilityInfo（系统接口）) |
| [queryAbilityInfoSync](arkts-ability-bundlemanager-queryabilityinfosync-f-sys.md#queryAbilityInfoSync（系统接口）) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo（系统接口）) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo（系统接口）) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryExtensionAbilityInfo（系统接口）) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync（系统接口）) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync（系统接口）) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryExtensionAbilityInfoSync（系统接口）) |
| [recoverBackupBundleData](arkts-ability-bundlemanager-recoverbackupbundledata-f-sys.md#recoverBackupBundleData（系统接口）) |
| [removeBackupBundleData](arkts-ability-bundlemanager-removebackupbundledata-f-sys.md#removeBackupBundleData（系统接口）) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled（系统接口）) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled（系统接口）) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setAbilityEnabled（系统接口）) |
| [setAbilityEnabledSync](arkts-ability-bundlemanager-setabilityenabledsync-f-sys.md#setAbilityEnabledSync（系统接口）) |
| [setAbilityFileTypesForSelf](arkts-ability-bundlemanager-setabilityfiletypesforself-f-sys.md#setAbilityFileTypesForSelf（系统接口）) |
| [setAdditionalInfo](arkts-ability-bundlemanager-setadditionalinfo-f-sys.md#setAdditionalInfo（系统接口）) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled（系统接口）) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled（系统接口）) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled（系统接口）) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setApplicationEnabled（系统接口）) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setApplicationEnabledSync（系统接口）) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setApplicationEnabledSync（系统接口）) |
| [switchUninstallState](arkts-ability-bundlemanager-switchuninstallstate-f-sys.md#switchUninstallState（系统接口）) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyAbc（系统接口）) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyAbc（系统接口）) |
<!--DelEnd-->

### 枚举

| 名称 |
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
### 枚举（系统接口）

| 名称 |
| --- |
| [AbilityFlag](arkts-ability-bundlemanager-abilityflag-e-sys.md) |
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
