# @ohos.web.webNativeMessagingExtensionManager

The webNativeMessagingExtensionManager module is a Web native message extension management module provided by ArkWeb. It is used to initiate and manage connections from the app side (caller) to [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md). Developers can call [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md) to specify the target extension Ability and establish a connection, use the returned connection ID and [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md) to listen for connection establishment, disconnection, and failure events, and call [disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md) to actively release the connection. This module is suitable for scenarios where browser extensions communicate with apps. Before using it, you need to request the [ohos.permission.WEB_NATIVE_MESSAGING](../../../security/AccessToken/restricted-permissions.md#ohospermissionweb_native_messaging) permission, and it is available only under the Stage model.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webNativeMessagingExtensionManager } from 'kits/@kit.ArkWeb';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [connectNative](arkts-arkweb-webnativemessagingextensionmanager-connectnative-f.md) |
| [disconnectNative](arkts-arkweb-webnativemessagingextensionmanager-disconnectnative-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionNativeInfo](arkts-arkweb-webnativemessagingextensionmanager-connectionnativeinfo-i.md) |
| [WebExtensionConnectionCallback](arkts-arkweb-webnativemessagingextensionmanager-webextensionconnectioncallback-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NmErrorCode](arkts-arkweb-webnativemessagingextensionmanager-nmerrorcode-e.md) |
