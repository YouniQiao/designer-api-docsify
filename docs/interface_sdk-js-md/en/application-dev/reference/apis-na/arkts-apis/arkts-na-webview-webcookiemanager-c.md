# WebCookieManager

Provides methods for managing the web cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-webview-class WebCookieManager--><!--Device-webview-class WebCookieManager-End-->

**System capability:** SystemCapability.Web.Webview.Core

## clearAllCookies

```TypeScript
static clearAllCookies(): Promise<void>
```

Remove all cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearAllCookies(): Promise<void>--><!--Device-WebCookieManager-static clearAllCookies(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A promise resolved after the cookies have been deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

## clearAllCookies

```TypeScript
static clearAllCookies(callback: AsyncCallback<void>): void
```

Remove all cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Called after the cookies have been deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |

## clearAllCookiesSync

```TypeScript
static clearAllCookiesSync(incognito?: boolean): void
```

Remove all cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void--><!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| incognito | boolean | No | {@code true} remove all cookies in incognito mode; {@code false} otherwise. |

## clearSessionCookie

```TypeScript
static clearSessionCookie(): Promise<void>
```

Delete the session cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>--><!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A promise resolved after the cookies have been deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

## clearSessionCookie

```TypeScript
static clearSessionCookie(callback: AsyncCallback<void>): void
```

Delete the session cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Called after the cookies have been deleted. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |

## clearSessionCookieSync

```TypeScript
static clearSessionCookieSync(): void
```

Delete the session cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static clearSessionCookieSync(): void--><!--Device-WebCookieManager-static clearSessionCookieSync(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## configCookie

```TypeScript
static configCookie(url: string, value: string): Promise<void>
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookie is to be set. |
| value | string | Yes | The cookie as a string, using the format of the 'Set-Cookie' HTTP response header. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A promise resolved after the cookies of given URL have been set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100005](../../apis-arkweb/errorcode-webview.md#17100005-invalid-cookie-value) | The provided cookie value is invalid. It must follow the format specified &lt;br&gt;in RFC 6265. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## configCookie

```TypeScript
static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookie is to be set. |
| value | string | Yes | The cookie as a string, using the format of the 'Set-Cookie' HTTP response header. |
| incognito | boolean | Yes | {@code true} set a single cookie (key-value pair) for the given URL in incognito mode; {@code false} otherwise. |
| includeHttpOnly | boolean | Yes | {@code true} HTTP-only cookies can also be overwritten; {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A promise resolved after the cookies of given URL have been set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100005](../../apis-arkweb/errorcode-webview.md#17100005-invalid-cookie-value) | The provided cookie value is invalid. It must follow the format specified &lt;br&gt;in RFC 6265. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## configCookie

```TypeScript
static configCookie(url: string, value: string, callback: AsyncCallback<void>): void
```

Set a single cookie (key-value pair) for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookie is to be set. |
| value | string | Yes | The cookie as a string, using the format of the 'Set-Cookie' HTTP response header. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Called after the cookies have been set. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100005](../../apis-arkweb/errorcode-webview.md#17100005-invalid-cookie-value) | The provided cookie value is invalid. It must follow the format specified &lt;br&gt;in RFC 6265. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito?: boolean): void
```

Set a single cookie (key-value pair) for the given URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookie is to be set. |
| value | string | Yes | The cookie as a string, using the format of the 'Set-Cookie' HTTP response header. |
| incognito | boolean | No | {@code true} set a single cookie (key-value pair) for the given URL in incognito mode; {@code false} otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100005](../../apis-arkweb/errorcode-webview.md#17100005-invalid-cookie-value) | The provided cookie value is invalid. It must follow the format specified &lt;br&gt;in RFC 6265. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void
```

Set a single cookie (key-value pair) for the given URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookie is to be set. |
| value | string | Yes | The cookie as a string, using the format of the 'Set-Cookie' HTTP response header. |
| incognito | boolean | Yes | {@code true} set a single cookie (key-value pair) for the given URL in incognito mode; {@code false} otherwise. |
| includeHttpOnly | boolean | Yes | {@code true} HTTP-only cookies can also be overwritten; {@code false} otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100005](../../apis-arkweb/errorcode-webview.md#17100005-invalid-cookie-value) | The provided cookie value is invalid. It must follow the format specified &lt;br&gt;in RFC 6265. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## existCookie

```TypeScript
static existCookie(incognito?: boolean): boolean
```

Check whether exists any cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean--><!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| incognito | boolean | No | {@code true} check whether exists any cookies. in incognito mode; {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if exists more than one cookie else false; |

## fetchAllCookies

```TypeScript
static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>
```

Fetches all stored cookies asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>--><!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| incognito | boolean | Yes | {@code true} Gets all cookies in incognito context; {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[WebHttpCookie](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webhttpcookie-i.md)&gt;&gt; | A promise resolved after the cookies gotten. |

## fetchCookie

```TypeScript
static fetchCookie(url: string): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookies are requested. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | A promise resolved after the cookies of given URL have been gotten. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## fetchCookie

```TypeScript
static fetchCookie(url: string, incognito: boolean): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookies are requested. |
| incognito | boolean | Yes | {@code true} gets all cookies for the given URL in incognito mode; {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | A promise resolved after the cookies of given URL have been gotten. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## fetchCookie

```TypeScript
static fetchCookie(url: string, callback: AsyncCallback<string>): void
```

Gets all cookies for the given URL Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void--><!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookies are requested. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Called after the cookies of given URL have been gotten. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## fetchCookie

```TypeScript
static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>
```

Gets all cookies for the given URL Asynchronously.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which to fetch cookies. |
| incognito | boolean | Yes | Whether to fetch cookies in incognito mode. |
| includePartitionedCookies | boolean | Yes | If true, allows fetching first-party partitioned cookies. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | A promise resolved with the cookie string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean): string
```

Gets all cookies for the given URL.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string--><!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookies are requested. |
| incognito | boolean | No | {@code true} gets all cookies for the given URL in incognito mode; {@code false} otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The cookie value for the given URL. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string
```

Gets all cookies for the given URL.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string--><!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean, includePartitionedCookies?: boolean): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | The URL for which the cookies are requested. |
| incognito | boolean | No | {@code true} gets all cookies for the given URL in incognito mode; {@code false} otherwise. |
| includePartitionedCookies | boolean | No | If true, allows fetching first-party partitioned cookies. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The cookie value for the given URL. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-incorrect-url-format) | URL error. No valid cookie found for the specified URL. |

## isCookieAllowed

```TypeScript
static isCookieAllowed(): boolean
```

Get whether the instance can send and accept cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static isCookieAllowed(): boolean--><!--Device-WebCookieManager-static isCookieAllowed(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the instance can send and accept cookies else false. |

## isThirdPartyCookieAllowed

```TypeScript
static isThirdPartyCookieAllowed(): boolean
```

Get whether the instance can send and accept thirdparty cookies.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean--><!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the instance can send and accept thirdparty cookies else false. |

## putAcceptCookieEnabled

```TypeScript
static putAcceptCookieEnabled(accept: boolean): void
```

Set whether the instance should send and accept cookies. By default this is set to be true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accept | boolean | Yes | Whether the instance should send and accept cookies. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

## putAcceptThirdPartyCookieEnabled

```TypeScript
static putAcceptThirdPartyCookieEnabled(accept: boolean): void
```

Set whether the instance should send and accept thirdparty cookies. By default this is set to be false.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accept | boolean | Yes | Whether the instance should send and accept thirdparty cookies. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

## saveCookieAsync

```TypeScript
static saveCookieAsync(): Promise<void>
```

Save the cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>--><!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A promise resolved after the cookies have been saved. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

## saveCookieAsync

```TypeScript
static saveCookieAsync(callback: AsyncCallback<void>): void
```

Save the cookies Asynchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Called after the cookies have been saved. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

## saveCookieSync

```TypeScript
static saveCookieSync(): void
```

Save the cookies synchronously.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static saveCookieSync(): void--><!--Device-WebCookieManager-static saveCookieSync(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setLazyInitializeWebEngine

```TypeScript
static setLazyInitializeWebEngine(lazy: boolean): void
```

Delays the initialization of the web engine. By default, the web engine is initialized when the CookieManager interface is called. By setting the 'lazy' parameter to true, the web engine will not be initialized when the CookieManager interface is called. Instead, the web engine will be initialized either when the web component is created or when initializeWebEngine is called.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void--><!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lazy | boolean | Yes | Controls whether to delay the initialization of the web engine. @static |

