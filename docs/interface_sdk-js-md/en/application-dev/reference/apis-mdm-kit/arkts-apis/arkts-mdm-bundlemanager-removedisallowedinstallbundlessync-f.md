# removeDisallowedInstallBundlesSync

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedInstallBundlesSync

```TypeScript
function removeDisallowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void
```

在应用程序包安装禁止名单中移除应用，在禁止名单存在的情况下，在应用程序包安装禁止名单中的应用不允许在当前/指定用户下安装。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function removeDisallowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void--><!--Device-bundleManager-function removeDisallowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array&lt;string&gt; | Yes | 应用ID数组。&lt;br/&gt;**说明：** 从API version 21版本开始，数组中的元素支持使用 [appId](../../../quick-start/common-problem-of-application.md#什么是appid)和 [appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)，仅移除传入的 [appId](../../../quick-start/common-problem-of-application.md#什么是appid)（或 [appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)），不会移除同一应用的 [appIdentifier](../../../quick-start/common-problem-of-application.md#什么是appidentifier)（或 [appId](../../../quick-start/common-problem-of-application.md#什么是appid)）。API version 20及之前版本，数组中的元素只支持使用 [appId](../../../quick-start/common-problem-of-application.md#什么是appid)。 |
| accountId | number | No | 用户ID，取值范围：大于等于0。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 &lt;br&gt; - 调用接口时，若传入accountId，表示指定用户。 &lt;br&gt; - 调用接口时，若未传入accountId，表示当前用户。*@ohos.account.osAccount** to obtain the user ID. &lt;br&gt; - If **accountId** is passed in, this API applies to the specified user. &lt;br&gt; - If **accountId** is not passed in, this API applies to the current user. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { bundleManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

try {
  bundleManager.removeDisallowedInstallBundlesSync(wantTemp, appIds, 100)
  console.info('Succeeded in removing disallowed install bundles.');
} catch (err) {
  console.error(`Failed to remove disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
}
```

