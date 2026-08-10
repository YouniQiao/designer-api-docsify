# disconnectNative

## Modules to Import

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## disconnectNative

```TypeScript
function disconnectNative(connectionId: int): Promise<void>
```

断开指定Web原生消息扩展连接。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.WEB_NATIVE_MESSAGING

**Model restriction:** This API can be used only in the stage model.

<!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>--><!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connectionId | int | Yes | 连接的标识ID，用于标识一次Web原生消息扩展连接，由 [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md#connectnative)方法返回。建立连接后需要通过disconnectNative释放。需使用由 connectNative返回的有效连接ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| 201 | Permission verification failed. |
| 16000011 | The context does not exist. |

