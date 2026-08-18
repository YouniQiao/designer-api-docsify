# WebMessagePort

Define html web message port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-interface WebMessagePort--><!--Device-webview-interface WebMessagePort-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Close port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-close(): void--><!--Device-WebMessagePort-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onMessageEvent

```TypeScript
onMessageEvent(callback: (result: WebMessage) => void): void
```

Receive message from other port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-onMessageEvent(callback: (result: WebMessage) => void): void--><!--Device-WebMessagePort-onMessageEvent(callback: (result: WebMessage) => void): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (result: WebMessage) =&gt; void | Yes | Callback function for receiving messages. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100006](../../apis-arkweb/errorcode-webview.md#17100006-message-port-callback-cannot-be-registered) | Failed to register a message event for the port. |

## onMessageEventExt

```TypeScript
onMessageEventExt(callback: (result: WebMessageExt) => void): void
```

Receive message from other port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-onMessageEventExt(callback: (result: WebMessageExt) => void): void--><!--Device-WebMessagePort-onMessageEventExt(callback: (result: WebMessageExt) => void): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (result: WebMessageExt) =&gt; void | Yes | Callback function for receiving messages. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100006](../../apis-arkweb/errorcode-webview.md#17100006-message-port-callback-cannot-be-registered) | Failed to register a message event for the port. |

## postMessageEvent

```TypeScript
postMessageEvent(message: WebMessage): void
```

Post a message to other port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-postMessageEvent(message: WebMessage): void--><!--Device-WebMessagePort-postMessageEvent(message: WebMessage): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [WebMessage](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webmessage-t.md) | Yes | Message to send. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100010](../../apis-arkweb/errorcode-webview.md#17100010-failure-to-send-messages-through-a-port) | Failed to post messages through the port. |

## postMessageEventExt

```TypeScript
postMessageEventExt(message: WebMessageExt): void
```

Post a message to other port.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-postMessageEventExt(message: WebMessageExt): void--><!--Device-WebMessagePort-postMessageEventExt(message: WebMessageExt): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [WebMessageExt](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webmessageext-c.md) | Yes | Message to send. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. 3.Parameter verification failed. |
| [17100010](../../apis-arkweb/errorcode-webview.md#17100010-failure-to-send-messages-through-a-port) | Failed to post messages through the port. |

## isExtentionType

```TypeScript
isExtentionType?: boolean
```

The flag indicates whether more formats are supported than string and array buffers.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-WebMessagePort-isExtentionType?: boolean--><!--Device-WebMessagePort-isExtentionType?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

