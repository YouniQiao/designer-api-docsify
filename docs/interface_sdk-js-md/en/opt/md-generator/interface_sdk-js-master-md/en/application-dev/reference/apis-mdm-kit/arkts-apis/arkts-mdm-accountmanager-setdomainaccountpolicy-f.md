# setDomainAccountPolicy

## Modules to Import

```TypeScript
import { accountManager } from '@kit.MDMKit';
```

## setDomainAccountPolicy

```TypeScript
function setDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo, policy: DomainAccountPolicy): void
```

Sets the domain account policy.

**Since:** 19

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

**Model restriction:** This API can be used only in the stage model.

<!--Device-accountManager-function setDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo, policy: DomainAccountPolicy): void--><!--Device-accountManager-function setDomainAccountPolicy(admin: Want, domainAccountInfo: osAccount.DomainAccountInfo, policy: DomainAccountPolicy): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| [domainAccountInfo](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | osAccount.DomainAccountInfo | Yes |
| policy | [DomainAccountPolicy](arkts-mdm-accountmanager-domainaccountpolicy-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { accountManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

async function setDomainAccountPolicy() {
  let wantTemp: Want = {
    // Replace with actual values.
    bundleName: 'com.example.myapplication',
    abilityName: 'EnterpriseAdminAbility'
  };
  let policy: accountManager.DomainAccountPolicy = {
    // Replace with actual values.
    authenticationValidityPeriod: 300,
    passwordValidityPeriod: 420,
    passwordExpirationNotification: 60
  };
  // Set the global domain account policy.
  let accountInfo: osAccount.DomainAccountInfo = {
    domain: '',
    accountName: '',
    serverConfigId: ''
  };
  try {
    accountManager.setDomainAccountPolicy(wantTemp, accountInfo, policy);
    console.info('Succeeded in setting global domainAccount policy.');
  } catch (err) {
    console.error(`Failed to set domainAccount policy. Code: ${err.code}, message: ${err.message}`);
  }
  // Set the policy for a specified domain account.
  let accountInfo2: osAccount.DomainAccountInfo = {
    domain: '',
    accountName: '',
    serverConfigId: ''
  };
  // Replace with actual values.
  let userId: number = 100;
  await osAccount.getAccountManager().getOsAccountDomainInfo(userId)
    .then((domainAccountInfo: osAccount.DomainAccountInfo) => {
      accountInfo2 = domainAccountInfo;
    }).catch((err: BusinessError) => {
      console.error(`Failed to get account domain info. Code: ${err.code}, message: ${err.message}`);
    })
  try {
    accountManager.setDomainAccountPolicy(wantTemp, accountInfo2, policy);
    console.info('Succeeded in setting domain account policy.');
  } catch (err) {
    console.error(`Failed to set domain account policy. Code: ${err.code}, message: ${err.message}`);
  }
}
```
