# addDisallowedRunningBundlesSync

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## addDisallowedRunningBundlesSync

```TypeScript
function addDisallowedRunningBundlesSync(
    admin: Want,
    appIds: Array<string>,
    accountId?: number
  ): void
```

添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。从API version 21开始，如果应用运行允许名单  
[addAllowedRunningBundles](arkts-mdm-applicationmanager-addallowedrunningbundles-f.md#addallowedrunningbundles)非空，就不能再通过本接口添加应用运行禁止名单，否则会报9200010冲突错误码。

> **说明：**
> 
> 若指定应用正在运行，将其加入禁止名单后，系统将立即终止该应用进程。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addDisallowedRunningBundlesSync(    admin: Want,    appIds: Array<string>,    accountId?: number  ): void--><!--Device-applicationManager-function addDisallowedRunningBundlesSync(    admin: Want,    appIds: Array<string>,    accountId?: number  ): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array&lt;string&gt; | Yes | 应用ID数组，指定具体应用。&lt;br/&gt;**说明：** 从API version 21版本开始，支持传入应用的 [appId](../../../quick-start/common-problem-of-application.md#什么是appid)和 [appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)，推荐使用 [appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)。API version 20及之前版本，仅支 持[appId](../../../quick-start/common-problem-of-application.md#什么是appid)。 &lt;br&gt;取值范围： &lt;br&gt; 单个用户下该名单总数不能超过200。例如100用户下已经设置了50个、101用户未设置，则100用户还能再设置150个，101用户还能再设置200个。 |
| accountId | number | No | 用户ID，取值范围：大于等于0。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 &lt;br&gt; - 调用接口时，若传入accountId，表示指定用户。 &lt;br&gt; - 调用接口时，若未传入accountId，表示当前用户。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9200010 | A conflict policy has been configured.<br>**Applicable version:** 21 and later |
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
let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

try {
  applicationManager.addDisallowedRunningBundlesSync(wantTemp, appIds);
  console.info('Succeeded in adding disallowed running bundles.');
} catch (err) {
  console.error(`Failed to add disallowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```

