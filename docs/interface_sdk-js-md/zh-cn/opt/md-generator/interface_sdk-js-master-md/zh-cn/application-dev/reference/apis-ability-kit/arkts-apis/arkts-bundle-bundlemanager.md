# @ohos.bundle.bundleManager

本模块提供应用信息的查询能力，支持应用包信息[BundleInfo](bundleManager/BundleInfo)、应用程序信息  
[ApplicationInfo](bundleManager/ApplicationInfo)、UIAbility组件信息  
[AbilityInfo](bundleManager/AbilityInfo)、ExtensionAbility组件信息  
[ExtensionAbilityInfo](arkts-ability-extensionabilityinfo-i.md#ExtensionAbilityInfo)等信息的查询。

**起始版本：** 9

<!--Device-unnamed-declare namespace bundleManager--><!--Device-unnamed-declare namespace bundleManager-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

## 汇总

### 函数

| 名称 |
| --- |
| [canOpenLink](arkts-ability-bundlemanager-canopenlink-f.md#canopenlink) |
| [cleanBundleCacheFilesForSelf](arkts-ability-bundlemanager-cleanbundlecachefilesforself-f.md#cleanbundlecachefilesforself) |
| [getAbilityInfo](arkts-ability-bundlemanager-getabilityinfo-f.md#getabilityinfo) |
| [getAlternateIcons](arkts-ability-bundlemanager-getalternateicons-f.md#getalternateicons) |
| [getAppCloneIdentity](arkts-ability-bundlemanager-getappcloneidentity-f.md#getappcloneidentity) |
| [getApplicationLabel](arkts-ability-bundlemanager-getapplicationlabel-f.md#getapplicationlabel) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getbundleinfo) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getbundleinfo-1) |
| [getBundleInfo](arkts-ability-bundlemanager-getbundleinfo-f.md#getbundleinfo-2) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself) |
| [getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself-1) |
| [getBundleInfoForSelfSync](arkts-ability-bundlemanager-getbundleinfoforselfsync-f.md#getbundleinfoforselfsync) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync) |
| [getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync-1) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md#getbundlenamebyuid) |
| [getBundleNameByUid](arkts-ability-bundlemanager-getbundlenamebyuid-f.md#getbundlenamebyuid-1) |
| [getBundleNameByUidSync](arkts-ability-bundlemanager-getbundlenamebyuidsync-f.md#getbundlenamebyuidsync) |
| [getInstalledBundleList](arkts-ability-bundlemanager-getinstalledbundlelist-f.md#getinstalledbundlelist) |
| [getLaunchWant](arkts-ability-bundlemanager-getlaunchwant-f.md#getlaunchwant) |
| [getLaunchWantForBundleSync](arkts-ability-bundlemanager-getlaunchwantforbundlesync-f.md#getlaunchwantforbundlesync) |
| [getPluginBundlePathForSelf](arkts-ability-bundlemanager-getpluginbundlepathforself-f.md#getpluginbundlepathforself) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md#getprofilebyability) |
| [getProfileByAbility](arkts-ability-bundlemanager-getprofilebyability-f.md#getprofilebyability-1) |
| [getProfileByAbilitySync](arkts-ability-bundlemanager-getprofilebyabilitysync-f.md#getprofilebyabilitysync) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md#getprofilebyextensionability) |
| [getProfileByExtensionAbility](arkts-ability-bundlemanager-getprofilebyextensionability-f.md#getprofilebyextensionability-1) |
| [getProfileByExtensionAbilitySync](arkts-ability-bundlemanager-getprofilebyextensionabilitysync-f.md#getprofilebyextensionabilitysync) |
| [getSignatureInfo](arkts-ability-bundlemanager-getsignatureinfo-f.md#getsignatureinfo) |
| [setAlternateIcon](arkts-ability-bundlemanager-setalternateicon-f.md#setalternateicon) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [cleanAllBundleCache](arkts-ability-bundlemanager-cleanallbundlecache-f-sys.md#cleanallbundlecache) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles-1) |
| [cleanBundleCacheFiles](arkts-ability-bundlemanager-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles-2) |
| [deleteAbc](arkts-ability-bundlemanager-deleteabc-f-sys.md#deleteabc) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disabledynamicicon) |
| [disableDynamicIcon](arkts-ability-bundlemanager-disabledynamicicon-f-sys.md#disabledynamicicon-1) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enabledynamicicon) |
| [enableDynamicIcon](arkts-ability-bundlemanager-enabledynamicicon-f-sys.md#enabledynamicicon-1) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getabilityicon) |
| [getAbilityIcon](arkts-ability-bundlemanager-getabilityicon-f-sys.md#getabilityicon-1) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getabilitylabel) |
| [getAbilityLabel](arkts-ability-bundlemanager-getabilitylabel-f-sys.md#getabilitylabel-1) |
| [getAbilityLabelSync](arkts-ability-bundlemanager-getabilitylabelsync-f-sys.md#getabilitylabelsync) |
| [getAdditionalInfo](arkts-ability-bundlemanager-getadditionalinfo-f-sys.md#getadditionalinfo) |
| [getAllAppCloneBundleInfo](arkts-ability-bundlemanager-getallappclonebundleinfo-f-sys.md#getallappclonebundleinfo) |
| [getAllAppProvisionInfo](arkts-ability-bundlemanager-getallappprovisioninfo-f-sys.md#getallappprovisioninfo) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getallapplicationinfo) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getallapplicationinfo-1) |
| [getAllApplicationInfo](arkts-ability-bundlemanager-getallapplicationinfo-f-sys.md#getallapplicationinfo-2) |
| [getAllBundleCacheSize](arkts-ability-bundlemanager-getallbundlecachesize-f-sys.md#getallbundlecachesize) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getallbundleinfo) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getallbundleinfo-1) |
| [getAllBundleInfo](arkts-ability-bundlemanager-getallbundleinfo-f-sys.md#getallbundleinfo-2) |
| [getAllBundleInfoByDeveloperId](arkts-ability-bundlemanager-getallbundleinfobydeveloperid-f-sys.md#getallbundleinfobydeveloperid) |
| [getAllBundleInstallInfo](arkts-ability-bundlemanager-getallbundleinstallinfo-f-sys.md#getallbundleinstallinfo) |
| [getAllDynamicIconInfo](arkts-ability-bundlemanager-getalldynamiciconinfo-f-sys.md#getalldynamiciconinfo) |
| [getAllNewPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallnewpreinstalledapplicationinfo-f-sys.md#getallnewpreinstalledapplicationinfo) |
| [getAllPluginInfo](arkts-ability-bundlemanager-getallplugininfo-f-sys.md#getallplugininfo) |
| [getAllPreinstalledApplicationInfo](arkts-ability-bundlemanager-getallpreinstalledapplicationinfo-f-sys.md#getallpreinstalledapplicationinfo) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getallsharedbundleinfo) |
| [getAllSharedBundleInfo](arkts-ability-bundlemanager-getallsharedbundleinfo-f-sys.md#getallsharedbundleinfo-1) |
| [getAppCloneBundleInfo](arkts-ability-bundlemanager-getappclonebundleinfo-f-sys.md#getappclonebundleinfo) |
| [getAppCloneIdentityBySandboxDataDir](arkts-ability-bundlemanager-getappcloneidentitybysandboxdatadir-f-sys.md#getappcloneidentitybysandboxdatadir) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getappprovisioninfo) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getappprovisioninfo-1) |
| [getAppProvisionInfo](arkts-ability-bundlemanager-getappprovisioninfo-f-sys.md#getappprovisioninfo-2) |
| [getAppProvisionInfoSync](arkts-ability-bundlemanager-getappprovisioninfosync-f-sys.md#getappprovisioninfosync) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getapplicationinfo) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getapplicationinfo-1) |
| [getApplicationInfo](arkts-ability-bundlemanager-getapplicationinfo-f-sys.md#getapplicationinfo-2) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getapplicationinfosync) |
| [getApplicationInfoSync](arkts-ability-bundlemanager-getapplicationinfosync-f-sys.md#getapplicationinfosync-1) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getbundlearchiveinfo) |
| [getBundleArchiveInfo](arkts-ability-bundlemanager-getbundlearchiveinfo-f-sys.md#getbundlearchiveinfo-1) |
| [getBundleArchiveInfoSync](arkts-ability-bundlemanager-getbundlearchiveinfosync-f-sys.md#getbundlearchiveinfosync) |
| [getBundleInstallStatus](arkts-ability-bundlemanager-getbundleinstallstatus-f-sys.md#getbundleinstallstatus) |
| [getDeveloperIds](arkts-ability-bundlemanager-getdeveloperids-f-sys.md#getdeveloperids) |
| [getDynamicIcon](arkts-ability-bundlemanager-getdynamicicon-f-sys.md#getdynamicicon) |
| [getDynamicIconInfo](arkts-ability-bundlemanager-getdynamiciconinfo-f-sys.md#getdynamiciconinfo) |
| [getExtResource](arkts-ability-bundlemanager-getextresource-f-sys.md#getextresource) |
| [getJsonProfile](arkts-ability-bundlemanager-getjsonprofile-f-sys.md#getjsonprofile) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getlaunchwantforbundle) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getlaunchwantforbundle-1) |
| [getLaunchWantForBundle](arkts-ability-bundlemanager-getlaunchwantforbundle-f-sys.md#getlaunchwantforbundle-2) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getpermissiondef) |
| [getPermissionDef](arkts-ability-bundlemanager-getpermissiondef-f-sys.md#getpermissiondef-1) |
| [getPermissionDefSync](arkts-ability-bundlemanager-getpermissiondefsync-f-sys.md#getpermissiondefsync) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getrecoverableapplicationinfo) |
| [getRecoverableApplicationInfo](arkts-ability-bundlemanager-getrecoverableapplicationinfo-f-sys.md#getrecoverableapplicationinfo-1) |
| [getSandboxDataDir](arkts-ability-bundlemanager-getsandboxdatadir-f-sys.md#getsandboxdatadir) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getsharedbundleinfo) |
| [getSharedBundleInfo](arkts-ability-bundlemanager-getsharedbundleinfo-f-sys.md#getsharedbundleinfo-1) |
| [getSpecifiedDistributionType](arkts-ability-bundlemanager-getspecifieddistributiontype-f-sys.md#getspecifieddistributiontype) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isabilityenabled) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isabilityenabled-1) |
| [isAbilityEnabled](arkts-ability-bundlemanager-isabilityenabled-f-sys.md#isabilityenabled-2) |
| [isAbilityEnabledSync](arkts-ability-bundlemanager-isabilityenabledsync-f-sys.md#isabilityenabledsync) |
| [isApplicationDisableForbidden](arkts-ability-bundlemanager-isapplicationdisableforbidden-f-sys.md#isapplicationdisableforbidden) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isapplicationenabled) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isapplicationenabled-1) |
| [isApplicationEnabled](arkts-ability-bundlemanager-isapplicationenabled-f-sys.md#isapplicationenabled-2) |
| [isApplicationEnabledSync](arkts-ability-bundlemanager-isapplicationenabledsync-f-sys.md#isapplicationenabledsync) |
| [migrateData](arkts-ability-bundlemanager-migratedata-f-sys.md#migratedata) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryabilityinfo) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryabilityinfo-1) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryabilityinfo-2) |
| [queryAbilityInfo](arkts-ability-bundlemanager-queryabilityinfo-f-sys.md#queryabilityinfo-3) |
| [queryAbilityInfoSync](arkts-ability-bundlemanager-queryabilityinfosync-f-sys.md#queryabilityinfosync) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryextensionabilityinfo) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryextensionabilityinfo-1) |
| [queryExtensionAbilityInfo](arkts-ability-bundlemanager-queryextensionabilityinfo-f-sys.md#queryextensionabilityinfo-2) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryextensionabilityinfosync) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryextensionabilityinfosync-1) |
| [queryExtensionAbilityInfoSync](arkts-ability-bundlemanager-queryextensionabilityinfosync-f-sys.md#queryextensionabilityinfosync-2) |
| [recoverBackupBundleData](arkts-ability-bundlemanager-recoverbackupbundledata-f-sys.md#recoverbackupbundledata) |
| [removeBackupBundleData](arkts-ability-bundlemanager-removebackupbundledata-f-sys.md#removebackupbundledata) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setabilityenabled) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setabilityenabled-1) |
| [setAbilityEnabled](arkts-ability-bundlemanager-setabilityenabled-f-sys.md#setabilityenabled-2) |
| [setAbilityEnabledSync](arkts-ability-bundlemanager-setabilityenabledsync-f-sys.md#setabilityenabledsync) |
| [setAbilityFileTypesForSelf](arkts-ability-bundlemanager-setabilityfiletypesforself-f-sys.md#setabilityfiletypesforself) |
| [setAdditionalInfo](arkts-ability-bundlemanager-setadditionalinfo-f-sys.md#setadditionalinfo) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setapplicationenabled) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setapplicationenabled-1) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setapplicationenabled-2) |
| [setApplicationEnabled](arkts-ability-bundlemanager-setapplicationenabled-f-sys.md#setapplicationenabled-3) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setapplicationenabledsync) |
| [setApplicationEnabledSync](arkts-ability-bundlemanager-setapplicationenabledsync-f-sys.md#setapplicationenabledsync-1) |
| [switchUninstallState](arkts-ability-bundlemanager-switchuninstallstate-f-sys.md#switchuninstallstate) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyabc) |
| [verifyAbc](arkts-ability-bundlemanager-verifyabc-f-sys.md#verifyabc-1) |
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
