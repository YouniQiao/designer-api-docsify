# WebExtensionConnectionCallback

As an input parameter when connecting a web native messaging extension, it is used to receive state changes during the connection.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webNativeMessagingExtensionManager-interface WebExtensionConnectionCallback--><!--Device-webNativeMessagingExtensionManager-interface WebExtensionConnectionCallback-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## onConnect

```TypeScript
onConnect(connection: ConnectionNativeInfo): void
```

Called when a connection is set up.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onConnect(connection: ConnectionNativeInfo): void--><!--Device-WebExtensionConnectionCallback-onConnect(connection: ConnectionNativeInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-na-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes | The remote connection info |

## onDisconnect

```TypeScript
onDisconnect(connection: ConnectionNativeInfo): void
```

Called when a connection is interrupted.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onDisconnect(connection: ConnectionNativeInfo): void--><!--Device-WebExtensionConnectionCallback-onDisconnect(connection: ConnectionNativeInfo): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | [ConnectionNativeInfo](arkts-na-webnativemessagingextensionmanager-connectionnativeinfo-i.md) | Yes | The remote connection info |

## onFailed

```TypeScript
onFailed(code: NmErrorCode, errMsg: string): void
```

Called when the connection fails.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebExtensionConnectionCallback-onFailed(code: NmErrorCode, errMsg: string): void--><!--Device-WebExtensionConnectionCallback-onFailed(code: NmErrorCode, errMsg: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | [NmErrorCode](arkts-na-webnativemessagingextensionmanager-nmerrorcode-e.md) | Yes | The error code of the failure. |
| errMsg | string | Yes | The error message of the failure. |

