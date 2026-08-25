# @ohos.bundle

本模块提供应用信息查询能力，支持包信息、[应用信息](arkts-ability-applicationinfo-applicationinfo-depr-i.md#applicationinfo)、 [Ability组件信息](arkts-ability-abilityinfo-abilityinfo-depr-i.md#abilityinfo)等信息的查询，以及应用禁用状态的查询、设置等。

> **说明：**&gt;
> 从API version 9开始，该模块不再维护，建议使用[@ohos.bundle.bundleManager](arkts-bundle-bundlemanager.md)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [bundleManager](arkts-bundle-bundlemanager.md)

**系统能力：** SystemCapability.BundleManager.BundleFramework

## 导入模块

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) |
| [cleanBundleCacheFiles](arkts-ability-bundle-cleanbundlecachefiles-f-sys.md) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) |
| [getBundleInstaller](arkts-ability-bundle-getbundleinstaller-f-sys.md) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) |
| [getPermissionDef](arkts-ability-bundle-getpermissiondef-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) |
| [setAbilityEnabled](arkts-ability-bundle-setabilityenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) |
| [setApplicationEnabled](arkts-ability-bundle-setapplicationenabled-f-sys.md) |
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
