# DlpConnManager

Calls **registerPlugin** and **unregisterPlugin** to register or unregister callback capabilities in the SA.

> **NOTE：**
> 
> **registerPlugin** registers callback capabilities in the SA, and **unregisterPlugin** unregisters callback
> capabilities from the SA.

**Since:** 21

<!--Device-dlpPermission-export class DlpConnManager--><!--Device-dlpPermission-export class DlpConnManager-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## constructor

```TypeScript
constructor()
```

Represents a constructor for instantiating [DlpConnManager](arkts-dataprotection-dlppermission-dlpconnmanager-c.md).

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-DlpConnManager-constructor()--><!--Device-DlpConnManager-constructor()-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

let dlpConnManager: dlpPermission.DlpConnManager = new dlpPermission.DlpConnManager();
```

## registerPlugin

```TypeScript
static registerPlugin(plugin: DlpConnPlugin): number
```

Registers a callback with the SA.

> **NOTE：**
> 
> **registerPlugin** registers the callback with the SA.

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-DlpConnManager-static registerPlugin(plugin: DlpConnPlugin): number--><!--Device-DlpConnManager-static registerPlugin(plugin: DlpConnPlugin): number-End-->

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
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { Callback } from '@kit.BasicServicesKit';

export default class DataCapsulePlugin implements dlpPermission.DlpConnPlugin {
  private accountId: string;
  private accountName: string;
  constructor() {
    this.accountId = 'accountId'; // Initialize account information.
    this.accountName = 'accountName';
  }

  connectServer(requestId: string, requestData: string, callback: Callback<string>): void {
    let callbackJson = JSON.stringify({
      'requestId': requestId,
    });
    callback(callbackJson);
  }
}
  
let pluginId: number = dlpPermission.DlpConnManager.registerPlugin(new DataCapsulePlugin());
```

## unregisterPlugin

```TypeScript
static unregisterPlugin(): void
```

Unregisters a callback from the SA.

This API unregisters a callback and releases resources when an application exits, ensuring that the callback capability is correctly released.

> **NOTE：**
> 
> **unregisterPlugin** unregisters a plug-in from the SA.

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-DlpConnManager-static unregisterPlugin(): void--><!--Device-DlpConnManager-static unregisterPlugin(): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Error codes:**

| Error Code ID |
| --- |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.DlpConnManager.unregisterPlugin();
```
