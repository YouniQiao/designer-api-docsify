# WebNativeMessagingExtensionAbility

class of web native messaging extension ability.

**Inheritance/Implementation:** WebNativeMessagingExtensionAbility extends ExtensionAbility

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare class WebNativeMessagingExtensionAbility--><!--Device-unnamed-declare class WebNativeMessagingExtensionAbility-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## onConnectNative

```TypeScript
onConnectNative(info: ConnectionInfo): void
```

Called when a web native messaging connection is established.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionAbility-onConnectNative(info: ConnectionInfo): void--><!--Device-WebNativeMessagingExtensionAbility-onConnectNative(info: ConnectionInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [ConnectionInfo](arkts-web-webnativemessagingextensionability-connectioninfo-i.md) | Yes | Indicates connection information about new native connection. |

## onDestroy

```TypeScript
onDestroy(): void
```

Called when the WebNativeMessagingExtensionAbility is destroyed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionAbility-onDestroy(): void--><!--Device-WebNativeMessagingExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onDisconnectNative

```TypeScript
onDisconnectNative(info: ConnectionInfo): void
```

Called when a web native messaging connection is disconnected.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionAbility-onDisconnectNative(info: ConnectionInfo): void--><!--Device-WebNativeMessagingExtensionAbility-onDisconnectNative(info: ConnectionInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [ConnectionInfo](arkts-web-webnativemessagingextensionability-connectioninfo-i.md) | Yes | Indicates connection information about new native connection. |

## context

```TypeScript
context: WebNativeMessagingExtensionContext
```

Context of web native messaging.

**Type:** [WebNativeMessagingExtensionContext](../../apis-arkweb/arkts-apis/arkts-arkweb-web-webnativemessagingextensioncontext-webnativemessagingextensioncontext-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionAbility-context: WebNativeMessagingExtensionContext--><!--Device-WebNativeMessagingExtensionAbility-context: WebNativeMessagingExtensionContext-End-->

**System capability:** SystemCapability.Web.Webview.Core

