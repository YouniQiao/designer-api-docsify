# WebHttpBodyStream

The http body stream of the request.

**Since:** 12

**Deprecated since:** -1

<!--Device-webview-class WebHttpBodyStream--><!--Device-webview-class WebHttpBodyStream-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getPosition

```TypeScript
getPosition(): number
```

Get the current position of the data stream. Unit: bytes.

**Since:** 12

**Deprecated since:** -1

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

Get the total size of the data stream. When data is chunked, always return zero. Unit: bytes.

**Since:** 12

**Deprecated since:** -1

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

Initialize data stream.

**Since:** 12

**Deprecated since:** -1

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

Whether data stream is chunked.

**Since:** 12

**Deprecated since:** -1

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

Whether all data stream has been consumed. For chunked uploads, returns false until the first read attempt.

**Since:** 12

**Deprecated since:** -1

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

Returns true if the upload data in the stream is entirely in memory, and all read requests will succeed synchronously. Expected to return false for chunked requests.

**Since:** 12

**Deprecated since:** -1

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

Read the data stream to the buffer. Unit: bytes.

**Since:** 12

**Deprecated since:** -1

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
