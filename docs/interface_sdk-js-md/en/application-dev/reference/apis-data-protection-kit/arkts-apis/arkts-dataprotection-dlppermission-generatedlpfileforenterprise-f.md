# generateDlpFileForEnterprise

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## generateDlpFileForEnterprise

```TypeScript
function generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>
```

Encrypts a plaintext file to generate a DLP file for an enterprise account. This API can be called only by enterprise accounts. This API uses a promise to return the result.This API encrypts a plaintext file to generate a DLP file that can be accessed only by enterprise accounts, implementing enterprise-level file permission management.

> **NOTE：**&gt;
> This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account
> servers. This API generates a DLP file, which is an encrypted file that can be accessed only by accounts
> authorized by the enterprise server.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |
| dlpFd | number | Yes |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | Yes |
| [customProperty](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [19100014](../errorcode-dlp.md#19100014-account-not-logged-in) |
