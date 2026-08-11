# createNormalOsAccount

## Modules to Import

```TypeScript
import { accountManager } from 'kits/@kit.MDMKit';
```

## createNormalOsAccount

```TypeScript
function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>
```

Creates a normal system account. A maximum of two normal system accounts (  
[osAccount.OsAccountType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccounttype-e.md/arkts-basicservices-osaccount-osaccounttype-e.md)) can be created.

> **NOTE：**
> 
> The account creation process is time-consuming. Subsequent calls to other synchronous APIs in the application
> main thread must wait for the asynchronous return of this API.
> 
> Creating a system account has a significant impact on device performance. This API is supported only on phones
> and tablets with 12 GB or more of RAM.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>--><!--Device-accountManager-function createNormalOsAccount(admin: Want, name: string): Promise<osAccount.OsAccountInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;osAccount.OsAccountInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [9201003](../errorcode-enterpriseDeviceManager.md#9201003-failed-to-add-an-account) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9201040](../errorcode-enterpriseDeviceManager.md#9201040-system-account-count-has-reached-the-upper-limit) |
| [204](../../errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { osAccount } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Create a normal system account. The account name needs to be passed.
accountManager.createNormalOsAccount(wantTemp, "TestAccountName").then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('Succeeded in creating normal os account, accountInfo: ' + JSON.stringify(accountInfo));
}).catch((err: BusinessError) => {
  console.error(`Failed to create normal os account: code is ${err.code}, message is ${err.message}`);
});
```
