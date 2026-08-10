# BundleInfo

> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [bundleInfo:BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)

<!--Device-unnamed-export interface BundleInfo--><!--Device-unnamed-export interface BundleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## abilityInfos

```TypeScript
readonly abilityInfos: Array<AbilityInfo>
```

Ability的配置信息

通过调用  
[bundle.getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo)接口时，传入GET_BUNDLE_WITH_ABILITIES获取。

**Type:** Array&lt;[AbilityInfo](arkts-ability-abilityinfo-abilityinfo-depr-i.md)&gt;

**Default:** Obtains configuration information about an ability

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#abilitiesInfo

<!--Device-BundleInfo-readonly abilityInfos: Array<AbilityInfo>--><!--Device-BundleInfo-readonly abilityInfos: Array<AbilityInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## appId

```TypeScript
readonly appId: string
```

应用包里应用程序的id。

**Type:** string

**Default:** Indicates the ID of the application to which this bundle belongs The application ID uniquely identifies an application. It is determined by the bundle name and signature

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.SignatureInfo#appId

<!--Device-BundleInfo-readonly appId: string--><!--Device-BundleInfo-readonly appId: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## appInfo

```TypeScript
readonly appInfo: ApplicationInfo
```

应用程序的配置信息。

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)

**Default:** Obtains configuration information about an application

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#appInfo

<!--Device-BundleInfo-readonly appInfo: ApplicationInfo--><!--Device-BundleInfo-readonly appInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## compatibleVersion

```TypeScript
readonly compatibleVersion: number
```

运行应用包所需要最低的SDK版本号。

**Type:** number

**Default:** Indicates the compatible version number of the bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly compatibleVersion: number--><!--Device-BundleInfo-readonly compatibleVersion: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## cpuAbi

```TypeScript
readonly cpuAbi: string
```

应用包的cpuAbi信息。

**Type:** string

**Default:** Indicates the cpuAbi information of this bundle.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly cpuAbi: string--><!--Device-BundleInfo-readonly cpuAbi: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## entryInstallationFree

```TypeScript
readonly entryInstallationFree: boolean
```

Entry是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。

**Type:** boolean

**Default:** Indicates whether free installation of the entry is supported

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly entryInstallationFree: boolean--><!--Device-BundleInfo-readonly entryInstallationFree: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## entryModuleName

```TypeScript
readonly entryModuleName: string
```

Entry的模块名称。

**Type:** string

**Default:** Indicates entry module name

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly entryModuleName: string--><!--Device-BundleInfo-readonly entryModuleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## hapModuleInfos

```TypeScript
readonly hapModuleInfos: Array<HapModuleInfo>
```

模块的配置信息。

**Type:** Array&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-hapmoduleinfo-depr-i.md)&gt;

**Default:** Obtains configuration information about a module

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#hapModulesInfo

<!--Device-BundleInfo-readonly hapModuleInfos: Array<HapModuleInfo>--><!--Device-BundleInfo-readonly hapModuleInfos: Array<HapModuleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## installTime

```TypeScript
readonly installTime: number
```

HAP安装时间，单位：毫秒。

**Type:** number

**Default:** Indicates the hap install time

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#installTime

<!--Device-BundleInfo-readonly installTime: number--><!--Device-BundleInfo-readonly installTime: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## isCompressNativeLibs

```TypeScript
readonly isCompressNativeLibs: boolean
```

是否压缩应用包的本地库，取值为true表示压缩应用包的本地库，取值为false表示不压缩应用包的本地库。

**Type:** boolean

**Default:** Indicates is compress native libs

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly isCompressNativeLibs: boolean--><!--Device-BundleInfo-readonly isCompressNativeLibs: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## isSilentInstallation

```TypeScript
readonly isSilentInstallation: string
```

是否通过静默安装。

**Type:** string

**Default:** Indicates is silent installation

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-BundleInfo-readonly isSilentInstallation: string--><!--Device-BundleInfo-readonly isSilentInstallation: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## minCompatibleVersionCode

```TypeScript
readonly minCompatibleVersionCode: number
```

分布式场景下的应用包兼容的最低版本。

**Type:** number

**Default:** Indicates the earliest historical version compatible with the bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#minCompatibleVersionCode

<!--Device-BundleInfo-readonly minCompatibleVersionCode: number--><!--Device-BundleInfo-readonly minCompatibleVersionCode: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## name

```TypeScript
readonly name: string
```

应用包的名称。

**Type:** string

**Default:** Indicates the name of this bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#name

<!--Device-BundleInfo-readonly name: string--><!--Device-BundleInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## reqPermissionDetails

```TypeScript
readonly reqPermissionDetails: Array<ReqPermissionDetail>
```

应用运行时需向系统申请的权限集合的详细信息

通过调用  
[bundle.getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo)接口时，传入GET_BUNDLE_WITH_REQUESTED_PERMISSION获取。

**Type:** Array&lt;ReqPermissionDetail&gt;

**Default:** Indicates the required permissions details defined in file config.json

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#reqPermissionDetails

<!--Device-BundleInfo-readonly reqPermissionDetails: Array<ReqPermissionDetail>--><!--Device-BundleInfo-readonly reqPermissionDetails: Array<ReqPermissionDetail>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## reqPermissionStates

```TypeScript
readonly reqPermissionStates: Array<number>
```

申请权限的授予状态。0表示申请成功，-1表示申请失败。

**Type:** Array&lt;number&gt;

**Default:** Indicates the grant status of required permissions

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#permissionGrantStates

<!--Device-BundleInfo-readonly reqPermissionStates: Array<number>--><!--Device-BundleInfo-readonly reqPermissionStates: Array<number>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## reqPermissions

```TypeScript
readonly reqPermissions: Array<string>
```

应用运行时需向系统申请的权限集合

通过调用  
[bundle.getBundleInfo](arkts-ability-bundle-getbundleinfo-f.md#getbundleinfo)接口时，传入GET_BUNDLE_WITH_REQUESTED_PERMISSION获取。

**Type:** Array&lt;string&gt;

**Default:** Indicates the required permissions name defined in file config.json

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#permissions

<!--Device-BundleInfo-readonly reqPermissions: Array<string>--><!--Device-BundleInfo-readonly reqPermissions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## targetVersion

```TypeScript
readonly targetVersion: number
```

运行应用包所需要最高SDK版本号。

**Type:** number

**Default:** Indicates the target version number of the bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#targetVersion

<!--Device-BundleInfo-readonly targetVersion: number--><!--Device-BundleInfo-readonly targetVersion: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## type

```TypeScript
readonly type: string
```

应用包类型。

**Type:** string

**Default:** Indicates the name of this original bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#bundleType

<!--Device-BundleInfo-readonly type: string--><!--Device-BundleInfo-readonly type: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## uid

```TypeScript
readonly uid: number
```

应用包里应用程序的uid。

**Type:** number

**Default:** Indicates the UID of the application to which this bundle belongs The UID uniquely identifies an application. It is determined by the process and user IDs of the application After an application is installed, its UID remains unchanged unless it is uninstalled and then reinstalled

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.ApplicationInfo#uid

<!--Device-BundleInfo-readonly uid: number--><!--Device-BundleInfo-readonly uid: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## updateTime

```TypeScript
readonly updateTime: number
```

HAP更新时间，单位：毫秒。

**Type:** number

**Default:** Indicates the hap update time

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#updateTime

<!--Device-BundleInfo-readonly updateTime: number--><!--Device-BundleInfo-readonly updateTime: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## vendor

```TypeScript
readonly vendor: string
```

应用包的供应商。

**Type:** string

**Default:** Describes the bundle vendor

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#vendor

<!--Device-BundleInfo-readonly vendor: string--><!--Device-BundleInfo-readonly vendor: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## versionCode

```TypeScript
readonly versionCode: number
```

应用包的版本号。

**Type:** number

**Default:** Indicates the version number of the bundle

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#versionCode

<!--Device-BundleInfo-readonly versionCode: number--><!--Device-BundleInfo-readonly versionCode: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## versionName

```TypeScript
readonly versionName: string
```

应用包的版本文本描述信息。

**Type:** string

**Default:** Indicates the text description of the bundle version

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.BundleInfo#versionName

<!--Device-BundleInfo-readonly versionName: string--><!--Device-BundleInfo-readonly versionName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

