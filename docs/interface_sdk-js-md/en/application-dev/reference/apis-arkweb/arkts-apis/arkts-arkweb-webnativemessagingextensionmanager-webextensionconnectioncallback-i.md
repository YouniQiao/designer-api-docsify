# WebExtensionConnectionCallback

作为连接网络原生消息扩展时的输入参数，它用于接收连接期间的状态变化。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webNativeMessagingExtensionManager-interface WebExtensionConnectionCallback--><!--Device-webNativeMessagingExtensionManager-interface WebExtensionConnectionCallback-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## onConnect

```TypeScript
onConnect(connection: ConnectionNativeInfo): void
```

建立连接时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onConnect(connection: ConnectionNativeInfo): void--><!--Device-WebExtensionConnectionCallback-onConnect(connection: ConnectionNativeInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes | 连接信息，包含连接ID、扩展应用包名、浏览器扩展源URL和扩展进程ID等信息。 |

## onDisconnect

```TypeScript
onDisconnect(connection: ConnectionNativeInfo): void
```

断开连接时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onDisconnect(connection: ConnectionNativeInfo): void--><!--Device-WebExtensionConnectionCallback-onDisconnect(connection: ConnectionNativeInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes | 连接信息，包含连接ID、扩展应用包名、浏览器扩展源URL和扩展进程ID等信息。 |

## onFailed

```TypeScript
onFailed(code: NmErrorCode, errMsg: string): void
```

连接失败时的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onFailed(code: NmErrorCode, errMsg: string): void--><!--Device-WebExtensionConnectionCallback-onFailed(code: NmErrorCode, errMsg: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) | Yes | 错误码。 |
| errMsg | string | Yes | 错误码对应信息。 |

