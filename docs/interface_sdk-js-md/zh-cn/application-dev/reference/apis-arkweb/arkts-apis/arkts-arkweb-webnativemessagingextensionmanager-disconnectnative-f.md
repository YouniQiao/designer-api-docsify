# disconnectNative

## 导入模块

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## disconnectNative

```TypeScript
function disconnectNative(connectionId: int): Promise<void>
```

断开指定Web原生消息扩展连接。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.WEB_NATIVE_MESSAGING

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>--><!--Device-webNativeMessagingExtensionManager-function disconnectNative(connectionId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connectionId | int | 是 | 连接的标识ID，用于标识一次Web原生消息扩展连接，由 [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md#connectnative)方法返回。建立连接后需要通过disconnectNative释放。需使用由 connectNative返回的有效连接ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module. |
| 201 | Permission verification failed. |
| 16000011 | The context does not exist. |

