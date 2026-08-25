# DlpConnManager

Calls **registerPlugin** and **unregisterPlugin** to register or unregister callback capabilities in the SA.

> **NOTE：**&gt;
> **registerPlugin** registers callback capabilities in the SA, and **unregisterPlugin** unregisters callback
> capabilities from the SA.

**Since:** 21

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## constructor

```TypeScript
constructor()
```

Represents a constructor for instantiating [DlpConnManager](#dlpconnmanager).

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## registerPlugin

```TypeScript
static registerPlugin(plugin: DlpConnPlugin): number
```

Registers a callback with the SA.

> **NOTE：**&gt;
> **registerPlugin** registers the callback with the SA.

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plugin | [DlpConnPlugin](arkts-dataprotection-dlppermission-dlpconnplugin-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |

## unregisterPlugin

```TypeScript
static unregisterPlugin(): void
```

Unregisters a callback from the SA.This API unregisters a callback and releases resources when an application exits, ensuring that the callback capability is correctly released.

> **NOTE：**&gt;
> **unregisterPlugin** unregisters a plug-in from the SA.

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
