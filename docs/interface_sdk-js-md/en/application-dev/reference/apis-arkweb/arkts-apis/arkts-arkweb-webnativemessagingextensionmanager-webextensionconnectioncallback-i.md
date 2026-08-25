# WebExtensionConnectionCallback

As an input parameter when connecting a web native messaging extension, it is used to receive state changes during the connection.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## onConnect

```TypeScript
onConnect(connection: ConnectionNativeInfo): void
```

Called when a connection is set up.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes |

## onDisconnect

```TypeScript
onDisconnect(connection: ConnectionNativeInfo): void
```

Called when a connection is interrupted.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes |

## onFailed

```TypeScript
onFailed(code: NmErrorCode, errMsg: string): void
```

Called when the connection fails.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) | Yes |
| errMsg | string | Yes |
