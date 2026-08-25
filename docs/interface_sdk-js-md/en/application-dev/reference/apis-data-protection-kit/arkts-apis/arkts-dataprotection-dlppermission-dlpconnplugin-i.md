# DlpConnPlugin

Registers the callback capability with the system ability (SA). This API is used in the **registerPlugin** API.

> **NOTE：**&gt;
> [registerPlugin](arkts-dataprotection-dlppermission-dlpconnmanager-c.md#registerplugin) requires identical parameters to this API.
> [connectServer](#connectserver) is called by the SA and the parameters are
> returned through the callback.

**Since:** 21

**ArkTS mode:** Supports only ArkTS-Dyn, since version 21.

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## connectServer

```TypeScript
connectServer(requestId: string, requestData: string, callback: Callback<string>): void
```

This API is called by the SA. After the request of connecting to the cloud server is processed, the result is returned the SA using a callback.This API can be used in enterprise account authentication and cloud permission verification to enable communication between the SA and the cloud server.

> **NOTE：**&gt;
> **connectServer** indicates a call from the system capability side to the frontend.

**Since:** 21

**ArkTS mode:** Supports only ArkTS-Dyn, since version 21.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestId | string | Yes |
| requestData | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
