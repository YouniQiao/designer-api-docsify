# WebMessagePort

Define html web message port.

**Since:** 9

**Deprecated since:** -1

<!--Device-webview-interface WebMessagePort--><!--Device-webview-interface WebMessagePort-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## close

```TypeScript
close(): void
```

Close port.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-close(): void--><!--Device-WebMessagePort-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## onMessageEvent

```TypeScript
onMessageEvent(callback: (result: WebMessage) => void): void
```

Receive message from other port.

**Since:** 9

**Deprecated since:** -1

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

Receive message from other port.

**Since:** 10

**Deprecated since:** -1

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

Post a message to other port.

**Since:** 9

**Deprecated since:** -1

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

Post a message to other port.

**Since:** 10

**Deprecated since:** -1

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

The flag indicates whether more formats are supported than string and array buffers.

**Type:** boolean

**Since:** 10

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebMessagePort-isExtentionType?: boolean--><!--Device-WebMessagePort-isExtentionType?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core
