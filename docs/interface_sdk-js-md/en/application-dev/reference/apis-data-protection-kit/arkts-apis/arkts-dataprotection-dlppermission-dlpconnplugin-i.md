# DlpConnPlugin

被用于registerPlugin接口中，将回调能力注册到SA（System Ability）中。

> **说明：**
> 
> [registerPlugin](arkts-dataprotection-dlppermission-dlpconnmanager-c.md#registerplugin)接口的参数需要继承该接口，
> [connectServer](arkts-dataprotection-dlppermission-dlpconnplugin-i.md#connectserver)由SA（System Ability）侧调用，通过callback进行回传参数。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-dlpPermission-export interface DlpConnPlugin--><!--Device-dlpPermission-export interface DlpConnPlugin-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## connectServer

```TypeScript
connectServer(requestId: string, requestData: string, callback: Callback<string>): void
```

该函数提供给SA（System Ability）侧调用，处理完连接云端服务的请求后，通过callback将结果返回给SA（System Ability）。

该接口可用于企业账号认证、云端权限验证等场景，实现SA与云服务器的通信能力，完成权限校验或账号验证流程。

> **说明：**
> 
> connectServer接口代表系统能力侧向前端通信的一次调用。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE or ohos.permission.ACCESS_DLP_SERVICE
- API version 21 - 24: ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-DlpConnPlugin-connectServer(requestId: string, requestData: string, callback: Callback<string>): void--><!--Device-DlpConnPlugin-connectServer(requestId: string, requestData: string, callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| requestId | string | Yes | SA（System Ability）侧传递的本次请求的标识。无范围限制。 |
| requestData | string | Yes | SA（System Ability）侧传递的数据。无范围限制。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | SA（System Ability）侧传递的接口，用于回调。无范围限制。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19100011 | The system ability works abnormally. |
| 201 | Permission denied. |

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

