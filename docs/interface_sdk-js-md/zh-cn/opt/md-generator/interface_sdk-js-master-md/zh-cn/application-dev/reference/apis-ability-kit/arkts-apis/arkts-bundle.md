# @ohos.bundle

本模块提供应用信息查询能力，支持包信息、[应用信息](arkts-ability-applicationinfo-applicationinfo-depr-i.md#applicationinfo)、 [Ability组件信息](arkts-ability-abilityinfo-abilityinfo-depr-i.md#abilityinfo)等信息的查询，以及应用禁用状态的查询、设置等。 > **说明：** > > 从API version 9开始，该模块不再维护，建议使用[@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md#ohosbundlebundlemanager)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [bundleManager](arkts-bundle-bundlemanager.md#ohosbundlebundlemanager)

<!--Device-unnamed-declare namespace bundle--><!--Device-unnamed-declare namespace bundle-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getabilityicon) |
| [getAbilityIcon](arkts-ability-bundle-getabilityicon-f.md#getabilityicon) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo) |
| [getAbilityInfo](arkts-ability-bundle-getabilityinfo-f.md#getabilityinfo) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getabilitylabel) |
| [getAbilityLabel](arkts-ability-bundle-getabilitylabel-f.md#getabilitylabel) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo) |
| [getAllApplicationInfo](arkts-ability-bundle-getallapplicationinfo-f.md#getallapplicationinfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo) |
| [getAllBundleInfo](arkts-ability-bundle-getallbundleinfo-f.md#getallbundleinfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo) |
| [getApplicationInfo](arkts-ability-bundle-getapplicationinfo-f.md#getapplicationinfo) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getbundlearchiveinfo) |
| [getBundleArchiveInfo](arkts-ability-bundle-getbundlearchiveinfo-f.md#getbundlearchiveinfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo) |
| [getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getlaunchwantforbundle) |
| [getLaunchWantForBundle](arkts-ability-bundle-getlaunchwantforbundle-f.md#getlaunchwantforbundle) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getnameforuid) |
| [getNameForUid](arkts-ability-bundle-getnameforuid-f.md#getnameforuid) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isabilityenabled) |
| [isAbilityEnabled](arkts-ability-bundle-isabilityenabled-f.md#isabilityenabled) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isapplicationenabled) |
| [isApplicationEnabled](arkts-ability-bundle-isapplicationenabled-f.md#isapplicationenabled) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant) |
| [queryAbilityByWant](arkts-ability-bundle-queryabilitybywant-f.md#queryabilitybywant) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles系统接口) |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md#cleanbundlecachefiles系统接口) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getbundleinstaller系统接口) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md#getbundleinstaller系统接口) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getpermissiondef系统接口) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md#getpermissiondef系统接口) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setabilityenabled系统接口) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md#setabilityenabled系统接口) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setapplicationenabled系统接口) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md#setapplicationenabled系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BundleOptions](arkts-ability-bundle-bundleoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [AbilitySubType](arkts-ability-bundle-abilitysubtype-e.md) |
| [AbilityType](arkts-ability-bundle-abilitytype-e.md) |
| [BundleFlag](arkts-ability-bundle-bundleflag-e.md) |
| [ColorMode](arkts-ability-bundle-colormode-e.md) |
| [DisplayOrientation](arkts-ability-bundle-displayorientation-e.md) |
| [GrantStatus](arkts-ability-bundle-grantstatus-e.md) |
| [InstallErrorCode](arkts-ability-bundle-installerrorcode-e.md) |
| [LaunchMode](arkts-ability-bundle-launchmode-e.md) |
