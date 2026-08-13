# WebHttpBodyStream

The http body stream of the request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-webview-class WebHttpBodyStream--><!--Device-webview-class WebHttpBodyStream-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getPosition

```TypeScript
getPosition(): long
```

Get the current position of the data stream. Unit: bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-getPosition(): long--><!--Device-WebHttpBodyStream-getPosition(): long-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| long | Return position in post data stream. |

## getSize

```TypeScript
getSize(): long
```

Get the total size of the data stream. When data is chunked, always return zero. Unit: bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-getSize(): long--><!--Device-WebHttpBodyStream-getSize(): long-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| long | Return size of data stream size. |

## initialize

```TypeScript
initialize(): Promise<void>
```

Initialize data stream.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-initialize(): Promise<void>--><!--Device-WebHttpBodyStream-initialize(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise of data stream is initialized. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100022](../../apis-arkweb/errorcode-webview.md#17100022-failed-to-initialize-webhttpbodystream) | Failed to initialize the HTTP body stream. |

## isChunked

```TypeScript
isChunked(): boolean
```

Whether data stream is chunked.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-isChunked(): boolean--><!--Device-WebHttpBodyStream-isChunked(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether data stream is chunked. |

## isEof

```TypeScript
isEof(): boolean
```

Whether all data stream has been consumed. For chunked uploads, returns false until the first read attempt.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-isEof(): boolean--><!--Device-WebHttpBodyStream-isEof(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether data stream has been consumed. |

## isInMemory

```TypeScript
isInMemory(): boolean
```

Returns true if the upload data in the stream is entirely in memory, and all read requests will succeed synchronously. Expected to return false for chunked requests.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-isInMemory(): boolean--><!--Device-WebHttpBodyStream-isInMemory(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the data stream is in memory. |

## read

```TypeScript
read(size: int): Promise<ArrayBuffer>
```

Read the data stream to the buffer. Unit: bytes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebHttpBodyStream-read(size: int): Promise<ArrayBuffer>--><!--Device-WebHttpBodyStream-read(size: int): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int | Yes | Read size. The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Read array buffer of result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

