# BundleInfo

The module defines the bundle information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface BundleInfo--><!--Device-unnamed-export interface BundleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## appIndex

```TypeScript
readonly appIndex: int
```

Index of an application clone. It takes effect only for application clones.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-BundleInfo-readonly appIndex: int--><!--Device-BundleInfo-readonly appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## appInfo

```TypeScript
readonly appInfo: ApplicationInfo
```

Application information. The information can be obtained by passing in **GET_BUNDLE_INFO_WITH_APPLICATION** to the  
**bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly appInfo: ApplicationInfo--><!--Device-BundleInfo-readonly appInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## buildVersion

```TypeScript
readonly buildVersion?: string
```

Build version number of the application package, which identifies different build version packages under the same release version. It corresponds to the buildVersion field in the app.json5 file.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-BundleInfo-readonly buildVersion?: string--><!--Device-BundleInfo-readonly buildVersion?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## firstInstallTime

```TypeScript
readonly firstInstallTime?: long
```

Timestamp for the initial installation of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds. For preinstalled applications, the initial installation timestamp is 1533657660000.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-BundleInfo-readonly firstInstallTime?: long--><!--Device-BundleInfo-readonly firstInstallTime?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## hapModulesInfo

```TypeScript
readonly hapModulesInfo: Array<HapModuleInfo>
```

Module configuration information. The information can be obtained by passing in **GET_BUNDLE_INFO_WITH_HAP_MODULE**to the **bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).

**Type:** Array&lt;[HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly hapModulesInfo: Array<HapModuleInfo>--><!--Device-BundleInfo-readonly hapModulesInfo: Array<HapModuleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## installTime

```TypeScript
readonly installTime: long
```

Timestamp for the installation of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds.

**NOTE：**

If the current time is not obtained when the device is powered on for the first time from the factory, the Unix epoch (1970-01-01 08:00:00 UTC+8) is used as the start time of the current system. For example, if the time is not obtained after startup and the installation succeeds after a 32-second wait, the application package installation timestamp is 32000.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly installTime: long--><!--Device-BundleInfo-readonly installTime: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## minCompatibleVersionCode

```TypeScript
readonly minCompatibleVersionCode: int
```

Minimum compatible version of the application package in the distributed scenario. It corresponds to the  
**minCompatibleVersionCode** field in the [app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly minCompatibleVersionCode: int--><!--Device-BundleInfo-readonly minCompatibleVersionCode: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## name

```TypeScript
readonly name: string
```

Name of the application package. It corresponds to the **bundleName** field in the  
[app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly name: string--><!--Device-BundleInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## permissionGrantStates

```TypeScript
readonly permissionGrantStates: Array<bundleManager.PermissionGrantState>
```

Permission grant state. The information can be obtained by passing in **GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION**to the **bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).The indices of the **reqPermissionDetails** array and the **permissionGrantStates** array are in one-to-one correspondence, meaning that the authorization status of **reqPermissionDetails[2]** is  
**permissionGrantStates[2]**.

**Type:** Array&lt;bundleManager.PermissionGrantState&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly permissionGrantStates: Array<bundleManager.PermissionGrantState>--><!--Device-BundleInfo-readonly permissionGrantStates: Array<bundleManager.PermissionGrantState>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## reqPermissionDetails

```TypeScript
readonly reqPermissionDetails: Array<ReqPermissionDetail>
```

Detailed information of the permissions to request from the system. The information can be obtained by passing in  
**GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION** to the **bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).The indices of the **reqPermissionDetails** array and the **permissionGrantStates** array are in one-to-one correspondence, meaning that the authorization status of **reqPermissionDetails[2]** is  
**permissionGrantStates[2]**.

**Type:** Array&lt;[ReqPermissionDetail](arkts-ability-bundleinfo-reqpermissiondetail-i.md)&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly reqPermissionDetails: Array<ReqPermissionDetail>--><!--Device-BundleInfo-readonly reqPermissionDetails: Array<ReqPermissionDetail>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## routerMap

```TypeScript
readonly routerMap: Array<RouterItem>
```

Router table of the application. The table is obtained by deduplicating and combining the **routerMap** information under **hapModulesInfo** based on the **name** field in **RouterItem**. The information can be obtained by passing in **GET_BUNDLE_INFO_WITH_HAP_MODULE** and **GET_BUNDLE_INFO_WITH_ROUTER_MAP** to the **bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).

**Type:** Array&lt;[RouterItem](arkts-ability-hapmoduleinfo-routeritem-i.md)&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BundleInfo-readonly routerMap: Array<RouterItem>--><!--Device-BundleInfo-readonly routerMap: Array<RouterItem>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## signatureInfo

```TypeScript
readonly signatureInfo: SignatureInfo
```

Signature information of the bundle. The information can be obtained by passing in  
**GET_BUNDLE_INFO_WITH_SIGNATURE_INFO** to the **bundleFlags** parameter of  
[getBundleInfoForSelf](arkts-ability-bundlemanager-getbundleinfoforself-f.md#getBundleInfoForSelf).

**Type:** [SignatureInfo](arkts-ability-bundleinfo-signatureinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly signatureInfo: SignatureInfo--><!--Device-BundleInfo-readonly signatureInfo: SignatureInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## targetVersion

```TypeScript
readonly targetVersion: int
```

Target version of the application. It corresponds to the **targetAPIVersion** field in the  
[app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly targetVersion: int--><!--Device-BundleInfo-readonly targetVersion: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## updateTime

```TypeScript
readonly updateTime: long
```

Timestamp for the last update of the application package. It measures the milliseconds that have passed since the Unix epoch (January 1, 1970, 08:00:00 UTC+8), in milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly updateTime: long--><!--Device-BundleInfo-readonly updateTime: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## vendor

```TypeScript
readonly vendor: string
```

Vendor of the application package. It corresponds to the **vendor** field in the  
[app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly vendor: string--><!--Device-BundleInfo-readonly vendor: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## versionCode

```TypeScript
readonly versionCode: long
```

Version code of the application package. It corresponds to the **versionCode** field in the  
[app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly versionCode: long--><!--Device-BundleInfo-readonly versionCode: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## versionName

```TypeScript
readonly versionName: string
```

Version description of the application package. It corresponds to the **versionName** field in the  
[app.json5](../../../quick-start/app-configuration-file.md) file.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BundleInfo-readonly versionName: string--><!--Device-BundleInfo-readonly versionName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

