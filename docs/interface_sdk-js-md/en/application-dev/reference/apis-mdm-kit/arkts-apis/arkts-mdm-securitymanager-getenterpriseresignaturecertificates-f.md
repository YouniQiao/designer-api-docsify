# getEnterpriseReSignatureCertificates

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getEnterpriseReSignatureCertificates

```TypeScript
function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>
```

Obtains enterprise re-signature certificate information based on the account ID. This API returns the information synchronously. Enterprises can use this API to query enterprise re-signature certificate details for certificate management and validity monitoring.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>--><!--Device-securityManager-function getEnterpriseReSignatureCertificates(accountId: number): Array<ReSignatureCertificateInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[ReSignatureCertificateInfo](arkts-mdm-securitymanager-resignaturecertificateinfo-i.md)&gt; | Enterprise re-signature certificate information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-invalid-user-id) | The specified account ID is invalid. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
