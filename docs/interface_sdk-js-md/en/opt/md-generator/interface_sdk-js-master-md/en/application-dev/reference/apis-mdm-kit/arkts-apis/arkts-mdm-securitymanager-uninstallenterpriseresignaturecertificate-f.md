# uninstallEnterpriseReSignatureCertificate

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## uninstallEnterpriseReSignatureCertificate

```TypeScript
function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void
```

Uninstalls the enterprise application re-signing certificate. After the enterprise re-signing certificate is uninstalled, the applications signed using this certificate can run properly before the device is restarted, but cannot run after the device is restarted.

Usage scenarios:

1. Installing a new certificate: After a new certificate is installed via the  
[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installEnterpriseReSignatureCertificate) API,applications re-signed using the new certificate can run properly. If the application corresponding to the old signing certificate is a super device administrator application, the application must be deactivated before the certificate can be uninstalled. Otherwise, after the certificate is uninstalled, the application cannot be uninstalled or run.2. Restoring a mistakenly deleted certificate: After a mistakenly deleted certificate is re-installed via the  
[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installEnterpriseReSignatureCertificate) API,re-signed applications can run normally without being affected.

> **NOTE：**
> 
> Certificate deletion is typically performed in scenarios such as certificate expiration or certificate leakage.
> You are advised to implement this feature with a strong prompt to administrators, advising them to delete
> certificates with caution. Before deleting a certificate, ensure that a new re-signing certificate has been
> loaded and that all applications have been updated and switched to the new re-signing certificate. Otherwise,
> historically installed applications will fail to run after a device restart.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: int): void--><!--Device-securityManager-function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: int): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| certificateAlias | string | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [9201008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9201008-enterprise-resigning-certificate-not-exist) |
| [9200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let certificateAlias: string = 'test.cer';
// Replace with actual values.
let accountId: number = 100;
try {
  securityManager.uninstallEnterpriseReSignatureCertificate(
    wantTemp, certificateAlias, accountId);
  console.info('Success to uninstall enterprise re signature certificate.');
} catch (err) {
  console.error(`Failed to uninstall enterprise re signature certificate.
    Code: ${err.code}, message: ${err.message}`);
};
```
