# addOsAccountAsync

## Modules to Import

```TypeScript
import { accountManager } from '@kit.MDMKit';
```

## addOsAccountAsync

```TypeScript
function addOsAccountAsync(admin: Want, name: string, type: osAccount.OsAccountType): Promise<osAccount.OsAccountInfo>
```

Adds an account in the background. This API uses a promise to return the result. This API is applicable to scenarios where enterprises need to create accounts in batches or remotely manage accounts. Accounts can be created without user interaction, improving management efficiency. > **NOTE：**> > This API is time-consuming. Subsequent calls to other synchronous APIs in the application main thread must wait > for the asynchronous return of this API.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function addOsAccountAsync(admin: Want, name: string, type: osAccount.OsAccountType): Promise<osAccount.OsAccountInfo>--><!--Device-accountManager-function addOsAccountAsync(admin: Want, name: string, type: osAccount.OsAccountType): Promise<osAccount.OsAccountInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| name | string | Yes |
| type | osAccount.OsAccountType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;osAccount.OsAccountInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [9201003](../errorcode-enterpriseDeviceManager.md#9201003-failed-to-add-an-account) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace parameters with actual values.
accountManager.addOsAccountAsync(wantTemp, "TestAccountName", osAccount.OsAccountType.NORMAL).then((info) => {
  console.info(`Succeeded in creating os account: ${JSON.stringify(info)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create os account. Code: ${err.code}, message: ${err.message}`);
});
```
