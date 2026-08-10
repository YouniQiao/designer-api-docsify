# getDisallowedUninstallBundlesSync

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## getDisallowedUninstallBundlesSync

```TypeScript
function getDisallowedUninstallBundlesSync(admin: Want, accountId?: number): Array<string>
```

获取当前/指定用户下包卸载禁止名单。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getDisallowedUninstallBundlesSync(admin: Want, accountId?: number): Array<string>--><!--Device-bundleManager-function getDisallowedUninstallBundlesSync(admin: Want, accountId?: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | No | 用户ID，取值范围：大于等于0。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 &lt;br&gt; - 调用接口时，若传入accountId，表示指定用户。 &lt;br&gt; - 调用接口时，若未传入accountId，表示当前用户。*@ohos.account.osAccount** to obtain the account ID. &lt;br&gt; - If **accountId** is passed in, this API applies to the specified user. &lt;br&gt; - If **accountId** is not passed in, this API applies to the current user. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回当前/指定用户下的包卸载禁止名单。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |


## getDisallowedUninstallBundlesSync

```TypeScript
function getDisallowedUninstallBundlesSync(admin: Want | null, accountId?: number): Array<string>
```

获取当前/指定用户下包卸载禁止名单。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getDisallowedUninstallBundlesSync(admin: Want | null, accountId?: number): Array<string>--><!--Device-bundleManager-function getDisallowedUninstallBundlesSync(admin: Want | null, accountId?: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |
| accountId | number | No | 用户ID，取值范围：大于等于0。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 &lt;br&gt; - 调用接口时，若传入accountId，表示指定用户。 &lt;br&gt; - 调用接口时，若未传入accountId，表示当前用户。*@ohos.account.osAccount** to obtain the user ID. &lt;br&gt; - If **accountId** is passed in, this API applies to the specified user. &lt;br&gt; - If **accountId** is not passed in, this API applies to the current user. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 返回当前/指定用户下的包卸载禁止名单。 |

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

try {
  // Replace parameters with actual values.
  let result: Array<string> = bundleManager.getDisallowedUninstallBundlesSync(wantTemp, 100);
  console.info(`Succeeded in getting disallowed uninstall bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed uninstall bundles. Code is ${err.code}, message is ${err.message}`);
}
```

