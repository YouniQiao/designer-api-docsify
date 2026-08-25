# WebResourceResponse

WebResourceResponse is a class in the Web component that represents HTTP responses and allows custom web page resource responses. In events such as onHttpErrorReceive, it provides the app with information including the status code, status code description, response header, response data, encoding, and MIME type of the server response. In resource request interception scenarios, it allows the app to customize the status code, status code description, response header, response data, encoding, MIME type, and data readiness state of the response, so that the app takes over the return content of specific resources. For sample code, see [onHttpErrorReceive event](arkts-arkweb-web-attribute.md#onhttperrorreceive).

**Since:** 8

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor of WebResourceResponse. It is used to create an HTTP response object, commonly used for customizing response content in resource request interception scenarios.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## getReasonMessage

```TypeScript
getReasonMessage(): string
```

Obtains the status code description of the resource response.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseCode

```TypeScript
getResponseCode(): number
```

Obtains the status code of the resource response.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getResponseData

```TypeScript
getResponseData(): string
```

Obtains the data in the resource response.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseDataEx

```TypeScript
getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined
```

Obtains resource response data, supporting multiple data types. Compared with getResponseData, this method supports returning various types such as number (file handle), ArrayBuffer (binary data), and Resource (\$rawfile resource). It is recommended to use this method when flexible data type support is needed.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string \| number \| ArrayBuffer \| Resource \| undefined |

## getResponseEncoding

```TypeScript
getResponseEncoding(): string
```

Obtains the encoding string of the resource response.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseHeader

```TypeScript
getResponseHeader(): Array<Header>
```

Obtains the resource response header.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Header](arkts-arkweb-header-i.md)&gt; |

## getResponseIsReady

```TypeScript
getResponseIsReady(): boolean
```

Obtains whether the response data is ready.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getResponseMimeType

```TypeScript
getResponseMimeType(): string
```

Obtains the MIME type of the resource response.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setReasonMessage

```TypeScript
setReasonMessage(reason: string): void
```

Sets the status code description of the resource response.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

## setResponseCode

```TypeScript
setResponseCode(code: number): void
```

Sets the status code of the resource response.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

## setResponseData

```TypeScript
setResponseData(data: string | number | Resource | ArrayBuffer): void
```

Sets the data in the resource response.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string \| number \| Resource \| ArrayBuffer | Yes |

## setResponseEncoding

```TypeScript
setResponseEncoding(encoding: string): void
```

Sets the encoding string of the resource response.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | Yes |

## setResponseHeader

```TypeScript
setResponseHeader(header: Array<Header>): void
```

Sets the resource response header.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| header | Array&lt;[Header](arkts-arkweb-header-i.md)&gt; | Yes |

## setResponseIsReady

```TypeScript
setResponseIsReady(IsReady: boolean): void
```

Sets whether the resource response data is ready.

> **NOTE：**&gt;
> - In resource request interception scenarios, call setResponseData(), setResponseEncoding(), setResponseMimeType(
> ), setResponseHeader(), setResponseCode(), setReasonMessage(), and other methods first to set the response
> attributes. Finally, call setResponseIsReady(true) to trigger resource return.&gt;
> - Asynchronous data scenario: Call setResponseIsReady(false) first. After the data is ready, call setResponseData
> () and other setting methods, and finally call setResponseIsReady(true) to trigger resource return.&gt;
> - If the calling sequence is incorrect, XMLHttpRequest synchronous requests may be blocked.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| IsReady | boolean | Yes |

## setResponseMimeType

```TypeScript
setResponseMimeType(mimeType: string): void
```

Sets the MIME type of the resource response.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
