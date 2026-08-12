# DlpConnPlugin

Registers the callback capability with the system ability (SA). This API is used in the **registerPlugin** API.

> **NOTE：**
> 
> [registerPlugin](arkts-dataprotection-dlppermission-dlpconnmanager-c.md#registerPlugin) requires identical parameters to this API.
> [connectServer](#connectServer) is called by the SA and the parameters are
> returned through the callback.

**Since:** 21

<!--Device-dlpPermission-export interface DlpConnPlugin--><!--Device-dlpPermission-export interface DlpConnPlugin-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## connectServer

```TypeScript
connectServer(requestId: string, requestData: string, callback: Callback<string>): void
```

This API is called by the SA. After the request of connecting to the cloud server is processed, the result is returned the SA using a callback.

This API can be used in enterprise account authentication and cloud permission verification to enable communication between the SA and the cloud server.

> **NOTE：**
> 
> **connectServer** indicates a call from the system capability side to the frontend.

**Since:** 21

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-DlpConnPlugin-connectServer(requestId: string, requestData: string, callback: Callback<string>): void--><!--Device-DlpConnPlugin-connectServer(requestId: string, requestData: string, callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestId | string | Yes |
| requestData | string | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { Callback } from '@kit.BasicServicesKit';

export default class DataCapsulePlugin implements dlpPermission.DlpConnPlugin {
  constructor() {
  }

  connectServer(requestId: string, requestData: string, callback: Callback<string>): void {
    let callbackJson = JSON.stringify({
      'requestId': requestId,
    }); // Construct callback JSON data.
    callback(callbackJson);  // Use a callback to return the result.
  }
}

let plugin: dlpPermission.DlpConnPlugin = new DataCapsulePlugin();
```
