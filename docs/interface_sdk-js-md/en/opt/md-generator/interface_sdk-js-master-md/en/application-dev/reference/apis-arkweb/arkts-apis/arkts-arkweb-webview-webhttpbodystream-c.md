# WebHttpBodyStream

WebHttpBodyStream is an HTTP request body data stream object used to read the request body data of POST, PUT, and other requests in custom scheme interception scenarios. This object is obtained through the getHttpBodyStream method of WebSchemeHandlerRequest and supports data of the BYTES, FILE, BLOB, and CHUNKED types. Developers can use this API to read uplink data in a custom protocol interceptor, enabling inspection or forwarding of the request body. Note: Other APIs in this class can be called only after [initialize](#initialize) succeeds. WebHttpBodyStream works in conjunction with [WebSchemeHandlerRequest](arkts-arkweb-webview-webschemehandlerrequest-c.md#webschemehandlerrequest): WebSchemeHandlerRequest represents the intercepted request, and WebHttpBodyStream represents the HTTP body data stream of that request. By reading data from the stream, developers can obtain the complete request body content.

**Since:** 12

<!--Device-webview-class WebHttpBodyStream--><!--Device-webview-class WebHttpBodyStream-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## getPosition

```TypeScript
getPosition(): number
```

Reads the current read position in this **WebHttpBodyStream** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-getPosition(): number--><!--Device-WebHttpBodyStream-getPosition(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

Obtains the size of data in this **WebHttpBodyStream** instance. This API always returns zero when chunked transfer is used.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-getSize(): number--><!--Device-WebHttpBodyStream-getSize(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## initialize

```TypeScript
initialize(): Promise<void>
```

Initializes this **WebHttpBodyStream** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-initialize(): Promise<void>--><!--Device-WebHttpBodyStream-initialize(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100022](../errorcode-webview.md#17100022-failed-to-initialize-webhttpbodystream) |

## isChunked

```TypeScript
isChunked(): boolean
```

Checks whether this **WebHttpBodyStream** instance is transmitted by chunk.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-isChunked(): boolean--><!--Device-WebHttpBodyStream-isChunked(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEof

```TypeScript
isEof(): boolean
```

Checks whether all data in this **WebHttpBodyStream** instance has been read.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-isEof(): boolean--><!--Device-WebHttpBodyStream-isEof(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInMemory

```TypeScript
isInMemory(): boolean
```

Checks whether the uploaded data in this **WebHttpBodyStream** instance is in memory.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-isInMemory(): boolean--><!--Device-WebHttpBodyStream-isInMemory(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## read

```TypeScript
read(size: number): Promise<ArrayBuffer>
```

Reads data from this **WebHttpBodyStream** instance.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebHttpBodyStream-read(size: number): Promise<ArrayBuffer>--><!--Device-WebHttpBodyStream-read(size: number): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
