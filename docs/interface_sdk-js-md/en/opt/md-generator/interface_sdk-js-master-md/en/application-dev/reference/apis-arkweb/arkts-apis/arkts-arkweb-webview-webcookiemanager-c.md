# WebCookieManager

Provides methods for managing the web cookies.

**Since:** 9

**Deprecated since:** -1

<!--Device-webview-class WebCookieManager--><!--Device-webview-class WebCookieManager-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## clearAllCookies

```TypeScript
static clearAllCookies(): Promise<void>
```

Remove all cookies Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearAllCookies(): Promise<void>--><!--Device-WebCookieManager-static clearAllCookies(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearAllCookies

```TypeScript
static clearAllCookies(callback: AsyncCallback<void>): void
```

Remove all cookies Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearAllCookiesSync

```TypeScript
static clearAllCookiesSync(incognito?: boolean): void
```

Remove all cookies.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void--><!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

## clearSessionCookie

```TypeScript
static clearSessionCookie(): Promise<void>
```

Delete the session cookies Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>--><!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearSessionCookie

```TypeScript
static clearSessionCookie(callback: AsyncCallback<void>): void
```

Delete the session cookies Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearSessionCookieSync

```TypeScript
static clearSessionCookieSync(): void
```

Delete the session cookies.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static clearSessionCookieSync(): void--><!--Device-WebCookieManager-static clearSessionCookieSync(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## configCookie

```TypeScript
static configCookie(url: string, value: string): Promise<void>
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 14

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |
| incognito | boolean | Yes |
| includeHttpOnly | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, callback: AsyncCallback<void>): void
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito?: boolean): void
```

Set a single cookie (key-value pair) for the given URL. > **NOTE：**> > You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on > the page. > > Cookies are periodically saved to the disk every 30s. You can also use the > **saveCookieAsync** API to forcibly save cookies to the disk. > > The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the > format of "key=value", followed by a list of cookie attributes separated by semicolons, for example, > **"key=value;Max-Age=100"**. > > If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has > expired, it will not be stored. To set multiple cookies, call this method multiple times. > > If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated > by semicolons. > > If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol. > > To override HttpOnly cookies, the HttpOnly attribute must be specified in the value.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |
| incognito | boolean | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void
```

Set a single cookie (key-value pair) for the given URL. > **NOTE：**> > You can set **url** in **configCookieSync** to a domain name so that the cookie is attached to the requests on > the page. > > It is recommended that cookie syncing be completed before the **Web** component is loaded. > > Cookies are periodically saved to the disk every 30s. You can also use the > **saveCookieAsync** API to forcibly save cookies to the disk. > > The **value** parameter must comply with the format of the Set-Cookie HTTP response header. The value is in the > format of "key=value", followed by a list of cookie attributes separated by semicolons, for example, > **"key=value;Max-Age=100"**. > > If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie has > expired, it will not be stored. To set multiple cookies, call this method multiple times. > > If **configCookieSync()** is used to set cookies for two or more times, the cookies set each time are separated > by semicolons. > > If the specified value contains the **Secure** attribute, the URL must use the **https://** protocol.

**Since:** 14

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |
| incognito | boolean | Yes |
| includeHttpOnly | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## deleteEntireCookie

```TypeScript
static deleteEntireCookie(): void
```

Remove all cookies.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [clearAllCookiesSync](#clearAllCookiesSync)

<!--Device-WebCookieManager-static deleteEntireCookie(): void--><!--Device-WebCookieManager-static deleteEntireCookie(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deleteSessionCookie

```TypeScript
static deleteSessionCookie(): void
```

Delete the session cookies.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [clearSessionCookieSync](#clearSessionCookieSync)

<!--Device-WebCookieManager-static deleteSessionCookie(): void--><!--Device-WebCookieManager-static deleteSessionCookie(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## existCookie

```TypeScript
static existCookie(incognito?: boolean): boolean
```

Check whether exists any cookies.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean--><!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## fetchAllCookies

```TypeScript
static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>
```

Fetches all stored cookies asynchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>--><!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[WebHttpCookie](arkts-arkweb-webview-webhttpcookie-i.md)&gt;&gt; |

## fetchCookie

```TypeScript
static fetchCookie(url: string): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookie

```TypeScript
static fetchCookie(url: string, incognito: boolean): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 14

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| incognito | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookie

```TypeScript
static fetchCookie(url: string, callback: AsyncCallback<string>): void
```

Gets all cookies for the given URL Asynchronously.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void--><!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookie

```TypeScript
static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| incognito | boolean | Yes |
| includePartitionedCookies | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean): string
```

Gets all cookies for the given URL. &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; **fetchCookieSync()** is used to obtain all cookie values. Cookie values are separated by semicolons. However, a specific cookie value cannot be obtained separately. &lt;/p&gt;

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string--><!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| incognito | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string
```

Gets all cookies for the given URL. &lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; **fetchCookieSync()** is used to obtain all cookie values. Cookie values are separated by semicolons. However, a specific cookie value cannot be obtained separately.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string--><!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| incognito | boolean | No |
| includePartitionedCookies | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## getCookie

```TypeScript
static getCookie(url: string): string
```

Gets all cookies for the given URL.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [fetchCookieSync](#fetchCookieSync)

<!--Device-WebCookieManager-static getCookie(url: string): string--><!--Device-WebCookieManager-static getCookie(url: string): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## isCookieAllowed

```TypeScript
static isCookieAllowed(): boolean
```

Get whether the instance can send and accept cookies.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static isCookieAllowed(): boolean--><!--Device-WebCookieManager-static isCookieAllowed(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isThirdPartyCookieAllowed

```TypeScript
static isThirdPartyCookieAllowed(): boolean
```

Get whether the instance can send and accept thirdparty cookies.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean--><!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## putAcceptCookieEnabled

```TypeScript
static putAcceptCookieEnabled(accept: boolean): void
```

Set whether the instance should send and accept cookies. By default this is set to be true.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accept | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## putAcceptThirdPartyCookieEnabled

```TypeScript
static putAcceptThirdPartyCookieEnabled(accept: boolean): void
```

Set whether the instance should send and accept thirdparty cookies. By default this is set to be false.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accept | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## saveCookieAsync

```TypeScript
static saveCookieAsync(): Promise<void>
```

Save the cookies Asynchronously.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>--><!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## saveCookieAsync

```TypeScript
static saveCookieAsync(callback: AsyncCallback<void>): void
```

Save the cookies Asynchronously.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## saveCookieSync

```TypeScript
static saveCookieSync(): void
```

Save the cookies synchronously. &lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt; **saveCookieSync** is used to forcibly write cookies that need to be persisted to disks. Session cookies are not persisted on PCs, 2-in-1 devices, or tablets, even if **saveCookieSync** is invoked. **saveCookieSync** blocks the caller until the operation is complete. During this period, I/O operations may be performed. &lt;/p&gt;

**Since:** 15

**Deprecated since:** -1

<!--Device-WebCookieManager-static saveCookieSync(): void--><!--Device-WebCookieManager-static saveCookieSync(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setCookie

```TypeScript
static setCookie(url: string, value: string): void
```

Set a single cookie (key-value pair) for the given URL.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [configCookieSync](#configCookieSync)

<!--Device-WebCookieManager-static setCookie(url: string, value: string): void--><!--Device-WebCookieManager-static setCookie(url: string, value: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## setLazyInitializeWebEngine

```TypeScript
static setLazyInitializeWebEngine(lazy: boolean): void
```

Delays the initialization of the web engine. By default, the web engine is initialized when the CookieManager interface is called. By setting the 'lazy' parameter to true, the web engine will not be initialized when the CookieManager interface is called. Instead, the web engine will be initialized either when the web component is created or when initializeWebEngine is called.

**Since:** 22

**Deprecated since:** -1

<!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void--><!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lazy | boolean | Yes |
