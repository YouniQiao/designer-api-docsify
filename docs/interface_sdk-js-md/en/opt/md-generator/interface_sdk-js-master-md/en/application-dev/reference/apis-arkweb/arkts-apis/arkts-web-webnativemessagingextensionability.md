# @ohos.web.WebNativeMessagingExtensionAbility

WebNativeMessagingExtensionAbility is a base class for web native message communication extension provided by ArkWeb,
 inherited from ExtensionAbility. It allows web pages to establish a secure, bidirectional pipe communication channel
 with system native services through the Native Messaging mechanism. By inheriting this class and implementing its
 lifecycle callbacks (such as [onConnectNative](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#onConnectNative),
 [onDisconnectNative](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#onDisconnectNative), and
 [onDestroy](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#onDestroy)), developers can detect connection establishment when
 a web page initiates a connection request, obtain the caller identity and bidirectional pipe file descriptors (see
 [ConnectionInfo](arkts-arkweb-web-webnativemessagingextensionability-connectioninfo-i.md#ConnectionInfo)), and release resources when the connection is disconnected or the extension
 is destroyed. This capability is primarily used in scenarios where browser extensions communicate with apps, enabling
 efficient message passing and data exchange to enhance extension integration and functionality. The app side must
 manage pipe read/write operations, permission verification, and the Ability lifecycle on its own.


## Modules to Import

```TypeScript
import { ConnectionInfo } from '@kit.ArkWeb';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionInfo](arkts-arkweb-web-webnativemessagingextensionability-connectioninfo-i.md) |
