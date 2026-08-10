# addAllowedRunningBundles

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addAllowedRunningBundles

```TypeScript
function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void
```

添加应用至应用运行允许名单，添加至允许名单的应用允许在指定用户下运行，不在允许名单的应用不允许在指定用户下运行。

> **说明：**
> 
> 1. 由于MDM Kit下大多数接口仅对MDM应用开放，本接口使用时，请将MDM应用同时添加至应用运行允许名单，否则会导致MDM应用不允许运行，阻塞接口调用。接口是否仅对MDM应用开放请查看对应的模块说明。
> 
> 2. 如果应用运行禁止名单非空，不支持再使用本接口添加应用运行允许名单，否则会报9200010冲突错误码。应用运行禁止名单相关接口包括
> [addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md#adddisallowedrunningbundlessync)、
> [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles)、
> [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles)、
> [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f.md#adddisallowedrunningbundles)。
> 
> 3. 本接口仅对三方应用生效，系统应用不受该名单管控，默认可以运行。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void--><!--Device-applicationManager-function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIdentifiers | Array&lt;string&gt; | Yes | 应用 [唯一标识符](../../../quick-start/common-problem-of-application.md#什么是appidentifier)的数组，可以通过接口 [bundleManager.getInstalledBundleList](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getinstalledbundlelist-f.md/arkts-ability-bundlemanager-getinstalledbundlelist-f.md#getinstalledbundlelist) 获取bundleInfo.signatureInfo.appIdentifier。 &lt;br&gt;取值范围： &lt;br&gt; - 单个用户下该名单总数不能超过200。例如100用户下已经设置了50个、101用户未设置，则100用户还能再设置150个，101用户还能再设置200个。 |
| accountId | number | Yes | 用户ID，取值范围：大于等于0。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIdentifiers: Array<string> = ['0123456789123456789'];

try {
  applicationManager.addAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in adding allowed running bundles.');
} catch (err) {
  console.error(`Failed to add allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

