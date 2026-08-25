# WebResourceHandler

WebResourceHandler is a handler used to return the result of an intercepted request to the **Web** component in custom scheme interception scenarios. After **WebSchemeHandler** decides to intercept a request, the developer uses **WebResourceHandler** to provide a custom response header (**didReceiveResponse**) and response body data (**didReceiveResponseBody**) to the **Web** component, and notifies the request of completion (**didFinish**) or failure (**didFail**). **didFail** supports an overloaded method (API version 20 and later) to simplify the error handling process. This API enables the app layer to fully customize the response to network requests.  
**WebResourceHandler** works with [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) and [WebSchemeHandlerResponse](arkts-arkweb-webview-webschemehandlerresponse-c.md): the **onRequestStart** callback of **WebSchemeHandler** receives a **WebResourceHandler** instance, the developer constructs a **WebSchemeHandlerResponse** object, passes the response header and response body data through **didReceiveResponse** and **didReceiveResponseBody** of **WebResourceHandler**, and finally calls **didFinish** or **didFail** to end the request.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## didFail

```TypeScript
didFail(code: WebNetErrorList): void
```

Notifies the ArkWeb kernel that the intercepted request will fail and ends the network request. Before calling this API, call [didReceiveResponse](#didreceiveresponse) to pass in the response header.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |

## didFail

```TypeScript
didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void
```

Notifies the ArkWeb kernel that the intercepted request will fail. If **completeIfNoResponse** is set to **false**, call [didReceiveResponse](#didreceiveresponse) first to pass in the response header. If **completeIfNoResponse** is set to **true** and [didReceiveResponse](#didreceiveresponse) is not called beforehand, a response header is automatically generated with the network error code -104. For details, see [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Yes |
| completeIfNoResponse | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100101](../errorcode-webview.md#17100101-incorrect-network-error-code) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |

## didFail

```TypeScript
didFail(code: WebNetErrorList, completeIfNoResponse: boolean, customErrorCode: number): void
```

Notify that this request should be failed.

**Since:** 26.1.0

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | [WebNetErrorList](arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Yes |
| completeIfNoResponse | boolean | Yes |
| customErrorCode | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |

## didFinish

```TypeScript
didFinish(): void
```

Notifies the **Web** component that the intercepted request is complete and no more data is available. Before calling this API, call [didReceiveResponse](#didreceiveresponse) to pass in the response header.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Error codes:**

| Error Code ID |
| --- |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |

## didReceiveResponse

```TypeScript
didReceiveResponse(response: WebSchemeHandlerResponse): void
```

Passes the constructed response header to the intercepted request. This API must be called before **didFinish** or **didFail**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| response | [WebSchemeHandlerResponse](arkts-arkweb-webview-webschemehandlerresponse-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |

## didReceiveResponseBody

```TypeScript
didReceiveResponseBody(data: ArrayBuffer): void
```

Passes the constructed response body to the intercepted request. This API must be called before **didFinish** or **didFail**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100021](../errorcode-webview.md#17100021-webresourcehandler-is-invalid) |
