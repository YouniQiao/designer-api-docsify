# getAllowedDistributeAbilityConnBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getAllowedDistributeAbilityConnBundles

```TypeScript
function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>
```

Gets the applications that are allowed to distribute ability connection.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>--><!--Device-applicationManager-function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) \| null | Yes | admin indicates the enterprise admin extension ability information. |
| serviceType | [ServiceType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-servicetype-e.md) | Yes | serviceType indicates the type of distribute ability. |
| accountId | number | Yes | accountId indicates the ID of OS account.<br>The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | returns the list of application appIdentifiers. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace it as required.
  let accountId: number = 100;
  let result: Array<string> = applicationManager.getAllowedDistributeAbilityConnBundles(wantTemp, applicationManager.ServiceType.COLLABORATION_SERVICE, accountId);
  console.info(`Succeeded in getting allowed distribute ability conn bundles: ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get allowed distribute ability conn bundles. Code: ${err.code}, message: ${err.message}`);
}

```

