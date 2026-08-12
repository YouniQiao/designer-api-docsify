# WebResourceResponse

Defines the Web resource response.

**Since:** 8

<!--Device-unnamed-declare class WebResourceResponse--><!--Device-unnamed-declare class WebResourceResponse-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-constructor()--><!--Device-WebResourceResponse-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getReasonMessage

```TypeScript
getReasonMessage(): string
```

Gets the reason message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getReasonMessage(): string--><!--Device-WebResourceResponse-getReasonMessage(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseCode

```TypeScript
getResponseCode(): number
```

Gets the response code.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getResponseCode(): number--><!--Device-WebResourceResponse-getResponseCode(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getResponseData

```TypeScript
getResponseData(): string
```

Gets the response data.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getResponseData(): string--><!--Device-WebResourceResponse-getResponseData(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseDataEx

```TypeScript
getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined
```

Gets the response data.

**Since:** 13

<!--Device-WebResourceResponse-getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined--><!--Device-WebResourceResponse-getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseEncoding

```TypeScript
getResponseEncoding(): string
```

Gets the response encoding.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getResponseEncoding(): string--><!--Device-WebResourceResponse-getResponseEncoding(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getResponseHeader

```TypeScript
getResponseHeader(): Array<Header>
```

Gets the response headers.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getResponseHeader(): Array<Header>--><!--Device-WebResourceResponse-getResponseHeader(): Array<Header>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Header](arkts-arkweb-header-i.md)&gt; |

## getResponseIsReady

```TypeScript
getResponseIsReady(): boolean
```

Gets whether the response is ready.

**Since:** 13

<!--Device-WebResourceResponse-getResponseIsReady(): boolean--><!--Device-WebResourceResponse-getResponseIsReady(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getResponseMimeType

```TypeScript
getResponseMimeType(): string
```

Gets the response MIME type.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-getResponseMimeType(): string--><!--Device-WebResourceResponse-getResponseMimeType(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setReasonMessage

```TypeScript
setReasonMessage(reason: string): void
```

Sets the reason message.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setReasonMessage(reason: string): void--><!--Device-WebResourceResponse-setReasonMessage(reason: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | string | Yes |

## setResponseCode

```TypeScript
setResponseCode(code: number): void
```

Sets the response code.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseCode(code: number): void--><!--Device-WebResourceResponse-setResponseCode(code: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

## setResponseData

```TypeScript
setResponseData(data: string | number | Resource | ArrayBuffer): void
```

Sets the response data.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseData(data: string | number | Resource | ArrayBuffer): void--><!--Device-WebResourceResponse-setResponseData(data: string | number | Resource | ArrayBuffer): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | string \| number \| Resource \| ArrayBuffer | Yes |

## setResponseEncoding

```TypeScript
setResponseEncoding(encoding: string): void
```

Sets the response encoding.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseEncoding(encoding: string): void--><!--Device-WebResourceResponse-setResponseEncoding(encoding: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | Yes |

## setResponseHeader

```TypeScript
setResponseHeader(header: Array<Header>): void
```

Sets the response headers.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseHeader(header: Array<Header>): void--><!--Device-WebResourceResponse-setResponseHeader(header: Array<Header>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| header | Array&lt;[Header](arkts-arkweb-header-i.md)&gt; | Yes |

## setResponseIsReady

```TypeScript
setResponseIsReady(IsReady: boolean): void
```

Sets the response is ready or not.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseIsReady(IsReady: boolean): void--><!--Device-WebResourceResponse-setResponseIsReady(IsReady: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| IsReady | boolean | Yes |

## setResponseMimeType

```TypeScript
setResponseMimeType(mimeType: string): void
```

Sets the response MIME type.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebResourceResponse-setResponseMimeType(mimeType: string): void--><!--Device-WebResourceResponse-setResponseMimeType(mimeType: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mimeType | string | Yes |
