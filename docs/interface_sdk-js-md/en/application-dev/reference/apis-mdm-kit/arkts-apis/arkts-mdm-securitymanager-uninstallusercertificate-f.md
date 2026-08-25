# uninstallUserCertificate

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## uninstallUserCertificate

```TypeScript
function uninstallUserCertificate(admin: Want, certUri: string): Promise<void>
```

Uninstalls a user certificate. This API uses a promise to return the result. This API is applicable to enterprise certificate management scenarios, such as replacing an expired certificate and revoking an employee's access to enterprise resources. Enterprises can call this API to uninstall a certificate when the certificate expires, is replaced, or is no longer needed, ensuring the flexibility and security of device certificate management.

**Since:** 12

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| certUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9201001](../errorcode-enterpriseDeviceManager.md#9201001-failed-to-manage-the-certificate) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
