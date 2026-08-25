# WebExtensionConnectionCallback

作为连接网络原生消息扩展时的输入参数，它用于接收连接期间的状态变化。

**起始版本：** 21

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## onConnect

```TypeScript
onConnect(connection: ConnectionNativeInfo): void
```

建立连接时的回调函数。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [connection](../../apis-network-kit/arkts-apis/arkts-net-connection.md) | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | 是 |

## onDisconnect

```TypeScript
onDisconnect(connection: ConnectionNativeInfo): void
```

断开连接时的回调函数。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [connection](../../apis-network-kit/arkts-apis/arkts-net-connection.md) | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | 是 |

## onFailed

```TypeScript
onFailed(code: NmErrorCode, errMsg: string): void
```

连接失败时的回调函数。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) | 是 |
| errMsg | string | 是 |
