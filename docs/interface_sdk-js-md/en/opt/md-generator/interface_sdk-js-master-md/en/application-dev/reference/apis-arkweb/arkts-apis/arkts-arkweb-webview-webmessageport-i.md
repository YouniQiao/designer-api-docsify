# WebMessagePort

WebMessagePort is a message port interface in the Web component used for bidirectional communication between the app side (ArkTS) and the HTML5 side (JavaScript). A pair of associated ports is created through createWebMessagePorts, with one port sent to the HTML5 side and the other retained on the app side, enabling cross- runtime message passing. WebMessagePort supports two message protocols: the basic protocol uses WebMessage as the message carrier (postMessageEvent/onMessageEvent), and the extended protocol uses WebMessageExt to support richer data types (postMessageEventExt/onMessageEventExt).

**Since:** 9

<!--Device-webview-interface WebMessagePort--><!--Device-webview-interface WebMessagePort-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes this message port when messages do not need to be sent. Before calling this method, call [createWebMessagePorts](arkts-arkweb-webview-webviewcontroller-c.md#createwebmessageports) to create a message port.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-close(): void--><!--Device-WebMessagePort-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onMessageEvent

```TypeScript
onMessageEvent(callback: (result: WebMessage) => void): void
```

Registers a callback on the application message port to receive messages of the [WebMessage](arkts-arkweb-webview-webmessage-t.md#webmessage) type from the HTML5 side. For details about the sample code, see [postMessage](arkts-arkweb-webview-webviewcontroller-c.md#postmessage).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-onMessageEvent(callback: (result: WebMessage) => void): void--><!--Device-WebMessagePort-onMessageEvent(callback: (result: WebMessage) => void): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (result: WebMessage) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100006](../errorcode-webview.md#17100006-message-port-callback-cannot-be-registered) |

## onMessageEventExt

```TypeScript
onMessageEventExt(callback: (result: WebMessageExt) => void): void
```

Registers a callback on the application message port to receive messages of the [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md#webmessagetype) type from the HTML5 side.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-onMessageEventExt(callback: (result: WebMessageExt) => void): void--><!--Device-WebMessagePort-onMessageEventExt(callback: (result: WebMessageExt) => void): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (result: WebMessageExt) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100006](../errorcode-webview.md#17100006-message-port-callback-cannot-be-registered) |

## postMessageEvent

```TypeScript
postMessageEvent(message: WebMessage): void
```

Sends a message of the [WebMessage](arkts-arkweb-webview-webmessage-t.md#webmessage) type to the HTML5 side. The onMessageEvent API must be invoked first. Otherwise, the message fails to be sent. For details about the sample code, see [postMessage](arkts-arkweb-webview-webviewcontroller-c.md#postmessage).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-postMessageEvent(message: WebMessage): void--><!--Device-WebMessagePort-postMessageEvent(message: WebMessage): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [WebMessage](arkts-arkweb-webview-webmessage-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100010](../errorcode-webview.md#17100010-failure-to-send-messages-through-a-port) |

## postMessageEventExt

```TypeScript
postMessageEventExt(message: WebMessageExt): void
```

Sends a message of the [WebMessageType](arkts-arkweb-webview-webmessagetype-e.md#webmessagetype) type to the HTML5 side. You must call onMessageEventExt first. Otherwise, the message fails to be sent. For the complete sample code, see onMessageEventExt.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-postMessageEventExt(message: WebMessageExt): void--><!--Device-WebMessagePort-postMessageEventExt(message: WebMessageExt): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [WebMessageExt](arkts-arkweb-webview-webmessageext-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100010](../errorcode-webview.md#17100010-failure-to-send-messages-through-a-port) |

## isExtentionType

```TypeScript
isExtentionType?: boolean
```

Whether to use the extended interface such as postMessageEventExt and onMessageEventExt when creating a WebMessagePort. The value true means to use the extended interface, and false means the opposite. Default value: false.

**Type:** boolean

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-isExtentionType?: boolean--><!--Device-WebMessagePort-isExtentionType?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core
