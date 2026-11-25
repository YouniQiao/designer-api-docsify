# getCredentialId

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## getCredentialId

```TypeScript
function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>
```

Obtains the credential ID based on the authentication token. This API uses a promise to return the result. Enterprises can use this API to parse and query user credential IDs (such as facial or fingerprint IDs) for scenarios such as enterprise device security audit and identity verification.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>--><!--Device-securityManager-function getCredentialId(authToken: Uint8Array, allowableDuration: number): Promise<bigint>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authToken | Uint8Array | Yes | Authentication token, which is issued after successful authentication. The maximum length is 1024 bytes. |
| allowableDuration | number | Yes | Allowable duration for parsing the authentication token, in milliseconds. and less than or equal to 86400000. <br>The value must be greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;bigint&gt; | Promise used to return the credential ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| 9201057 | Invalid authentication token. |
| 9201058 | The authentication token parsing duration is out of the allowed range. |
