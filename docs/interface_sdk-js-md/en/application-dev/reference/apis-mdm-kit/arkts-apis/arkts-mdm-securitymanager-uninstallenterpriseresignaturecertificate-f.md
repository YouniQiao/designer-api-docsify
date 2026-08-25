# uninstallEnterpriseReSignatureCertificate

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## uninstallEnterpriseReSignatureCertificate

```TypeScript
function uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void
```

Uninstalls the enterprise application re-signing certificate. After the enterprise re-signing certificate is uninstalled, the applications signed using this certificate can run properly before the device is restarted, but cannot run after the device is restarted.Usage scenarios:
1. Installing a new certificate: After a new certificate is installed via the  
[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md) API, applications re-signed using the new certificate can run properly. If the application corresponding to the old signing certificate is a super device administrator application, the application must be deactivated before the certificate can be uninstalled. Otherwise, after the certificate is uninstalled, the application cannot be uninstalled or run.
2. Restoring a mistakenly deleted certificate: After a mistakenly deleted certificate is re-installed via the  
[installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md) API, re-signed applications can run normally without being affected.

> **NOTE：**&gt;
> Certificate deletion is typically performed in scenarios such as certificate expiration or certificate leakage.
> You are advised to implement this feature with a strong prompt to administrators, advising them to delete
> certificates with caution. Before deleting a certificate, ensure that a new re-signing certificate has been
> loaded and that all applications have been updated and switched to the new re-signing certificate. Otherwise,
> historically installed applications will fail to run after a device restart.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

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
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9201008](../errorcode-enterpriseDeviceManager.md#9201008-enterprise-re-signing-certificate-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
