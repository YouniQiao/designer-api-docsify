# WebSchemeHandlerResponse

WebSchemeHandlerResponse is a class used to construct HTTP response data in custom scheme interception scenarios. Developers use this class to create a Response object, set properties such as HTTP status code, status text, MIME type, character set, custom response headers, network error code, and redirection URL, and then return the custom response to the Web component through WebResourceHandler. This class is the core data carrier for custom resource interception. WebSchemeHandlerResponse is used together with WebResourceHandler: the developer constructs a WebSchemeHandlerResponse object and fills in the response properties, and then sends the response header to the intercepted request through the didReceiveResponse method of WebResourceHandler.

**Since:** 12

<!--Device-webview-class WebSchemeHandlerResponse--><!--Device-webview-class WebSchemeHandlerResponse-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a **Response** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-constructor()--><!--Device-WebSchemeHandlerResponse-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getCustomErrorCode

```TypeScript
getCustomErrorCode(): number
```

Get the custom error code of the Web response.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSchemeHandlerResponse-getCustomErrorCode(): number--><!--Device-WebSchemeHandlerResponse-getCustomErrorCode(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getEncoding

```TypeScript
getEncoding(): string
```

Obtains the character encoding format of the response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getEncoding(): string--><!--Device-WebSchemeHandlerResponse-getEncoding(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getHeaderByName

```TypeScript
getHeaderByName(name: string): string
```

Obtains the value of a response header field by name.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string--><!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMimeType

```TypeScript
getMimeType(): string
```

Obtains the MIME type of this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getMimeType(): string--><!--Device-WebSchemeHandlerResponse-getMimeType(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getNetErrorCode

```TypeScript
getNetErrorCode(): WebNetErrorList
```

Obtains the network error code of the response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList--><!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) |

## getStatus

```TypeScript
getStatus(): number
```

Obtains the HTTP status code of the response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getStatus(): number--><!--Device-WebSchemeHandlerResponse-getStatus(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getStatusText

```TypeScript
getStatusText(): string
```

Obtains the status text of this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getStatusText(): string--><!--Device-WebSchemeHandlerResponse-getStatusText(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getUrl

```TypeScript
getUrl(): string
```

Obtains the redirection URL or the URL changed due to HSTS. Risk warning: To obtain a URL for JavaScriptProxy communication API authentication, use [getLastJavascriptProxyCallingFrameUrl&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkweb-webview-webviewcontroller-c.md#getlastjavascriptproxycallingframeurl).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-getUrl(): string--><!--Device-WebSchemeHandlerResponse-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## setCustomErrorCode

```TypeScript
setCustomErrorCode(customErrorCode: number): void
```

Set the custom error code for the Web response.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSchemeHandlerResponse-setCustomErrorCode(customErrorCode: number): void--><!--Device-WebSchemeHandlerResponse-setCustomErrorCode(customErrorCode: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| customErrorCode | number | Yes |

## setEncoding

```TypeScript
setEncoding(encoding: string): void
```

Sets the character encoding format for the current response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void--><!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setHeaderByName

```TypeScript
setHeaderByName(name: string, value: string, overwrite: boolean): void
```

Sets the header information for this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void--><!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |
| [overwrite](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setMimeType

```TypeScript
setMimeType(type: string): void
```

Sets the MIME type for the current response. For example, set it to text/html when injecting HTML content, and set it to application/json when injecting JSON data.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void--><!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setNetErrorCode

```TypeScript
setNetErrorCode(code: WebNetErrorList): void
```

Sets the network error code for this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void--><!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setStatus

```TypeScript
setStatus(code: number): void
```

Sets the HTTP status code for this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setStatus(code: number): void--><!--Device-WebSchemeHandlerResponse-setStatus(code: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setStatusText

```TypeScript
setStatusText(text: string): void
```

Sets the status text for this response.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void--><!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## setUrl

```TypeScript
setUrl(url: string): void
```

Sets the redirection URL or the URL changed due to HSTS for this response. After the URL is set, a redirection to the new URL is triggered.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebSchemeHandlerResponse-setUrl(url: string): void--><!--Device-WebSchemeHandlerResponse-setUrl(url: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
