# WebCookieManager

WebCookieManager is the cookie manager for Web components, providing global management capabilities for cookies in Web components. With this class, developers can obtain, set, save, and clear cookies, as well as control cookie permissions. All methods of this class are static, and all Web components in an app share a single WebCookieManager instance. The cookie format complies with the [RFC6265](https://www.rfc-editor.org/info/rfc6265/) standard.When browsing web pages in Privacy Mode, data such as cookies and caches are not written to local persistent storage. After the Web component in Privacy Mode is destroyed, this data is cleared and not retained.

> **NOTE：**&gt;
> - Static methods must be used on the user interface (UI) thread.

**Since:** 9

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## clearAllCookies

```TypeScript
static clearAllCookies(): Promise<void>
```

Clears all cookies, including session cookies and persistent cookies. This API uses a promise to return the result. To clear only session cookies, use [clearSessionCookie](#clearsessioncookie).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Clears all cookies, including session cookies and persistent cookies. This API uses an asynchronous callback to return the result. To clear only session cookies, use [clearSessionCookie](#clearsessioncookie).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearAllCookiesSync

```TypeScript
static clearAllCookiesSync(incognito?: boolean): void
```

Clears all cookies, including session cookies and persistent cookies. To clear only session cookies, use [clearSessionCookieSync](#clearsessioncookiesync).

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| incognito | boolean | No |

## clearSessionCookie

```TypeScript
static clearSessionCookie(): Promise<void>
```

Clears all session cookies. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Clears all session cookies. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## clearSessionCookieSync

```TypeScript
static clearSessionCookieSync(): void
```

Deletes all session cookies.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## configCookie

```TypeScript
static configCookie(url: string, value: string): Promise<void>
```

Sets a single cookie value for a specified URL. This API uses a promise to return the result.

> **NOTE：**&gt;
> - In configCookie, you can specify a domain name in the URL so that in-page requests also carry the cookie.&gt;
> - Cookies are periodically saved to the disk every 30 seconds. You can also use
> [saveCookieAsync](#savecookieasync) for force
> storage.&gt;
> - The value parameter must follow the format of the Set-Cookie HTTP response header. It is a key-value pair in
> the form of "key=value", optionally followed by a cookie property list separated by "; " (for example, "key=
> value; Max-Age=100").&gt;
> - If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie
> to set has expired, it will not be stored. To set multiple cookies, call this method multiple times.&gt;
> - If configCookie is called twice or more to set cookies, each cookie set is separated by "; ".&gt;
> - If the specified value contains the "Secure" attribute, the URL must use the "https://" protocol.&gt;
> - To overwrite HttpOnly cookies, specify the HttpOnly attribute in the value.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>
```

Sets a single cookie value for a specified URL. This API uses a promise to return the result.

> **NOTE：**&gt;
> - In configCookie, you can specify a domain name in the URL so that in-page requests also carry the cookie.&gt;
> - Cookies are periodically saved to the disk every 30 seconds. You can also use
> [saveCookieAsync](#savecookieasync) for force
> storage.&gt;
> - The value parameter must follow the format of the Set-Cookie HTTP response header. It is a key-value pair in
> the form of "key=value", optionally followed by a cookie property list separated by "; " (for example, "key=
> value; Max-Age=100").&gt;
> - If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie
> to set has expired, it will not be stored. To set multiple cookies, call this method multiple times.&gt;
> - If configCookie is called twice or more to set cookies, each cookie set is separated by "; ".&gt;
> - If the specified value contains the "Secure" attribute, the URL must use the "https://" protocol.

**Since:** 14

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
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, callback: AsyncCallback<void>): void
```

Sets a single cookie value for a specified URL. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - In configCookie, you can specify a domain name in the URL so that in-page requests also carry the cookie.&gt;
> - Cookies are periodically saved to the disk every 30 seconds. You can also use
> [saveCookieAsync](#savecookieasync) for force
> storage.&gt;
> - The value parameter must follow the format of the Set-Cookie HTTP response header. It is a key-value pair in
> the form of "key=value", optionally followed by a cookie property list separated by "; " (for example, "key=
> value; Max-Age=100").&gt;
> - If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie
> to set has expired, it will not be stored. To set multiple cookies, call this method multiple times.&gt;
> - If configCookie is called twice or more to set cookies, each cookie set is separated by "; ".&gt;
> - If the specified value contains the "Secure" attribute, the URL must use the "https://" protocol.&gt;
> - To overwrite HttpOnly cookies, specify the HttpOnly attribute in the value.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito?: boolean): void
```

Sets a cookie for the specified URL.

> **NOTE：**&gt;
> - In configCookieSync, you can specify a domain name in the URL so that in-page requests also carry the cookie.&gt;
> - Cookies are periodically saved to the disk every 30 seconds. You can also use
> [saveCookieAsync](#savecookieasync) for force
> storage.&gt;
> - The value parameter must follow the format of the Set-Cookie HTTP response header. It is a key-value pair in
> the form of "key=value", optionally followed by a cookie property list separated by "; " (for example, "key=
> value; Max-Age=100").&gt;
> - If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie
> to set has expired, it will not be stored. To set multiple cookies, call this method multiple times.&gt;
> - If configCookieSync is called twice or more to set cookies, each cookie set is separated by "; ".&gt;
> - If the specified value contains the "Secure" attribute, the URL must use the "https://" protocol.&gt;
> - To overwrite HttpOnly cookies, specify the HttpOnly attribute in the value.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void
```

Sets a single cookie value for a specified URL.

> **NOTE：**&gt;
> - In configCookieSync, you can specify a domain name in the URL so that in-page requests also carry the cookie.&gt;
> - Cookies are periodically saved to the disk every 30 seconds. You can also use
> [saveCookieAsync](#savecookieasync) for force
> storage.&gt;
> - The value parameter must follow the format of the Set-Cookie HTTP response header. It is a key-value pair in
> the form of "key=value", optionally followed by a cookie property list separated by "; " (for example, "key=
> value; Max-Age=100").&gt;
> - If a cookie with the same host, path, and name exists, it will be replaced by the new cookie. If the cookie
> to set has expired, it will not be stored. To set multiple cookies, call this method multiple times.&gt;
> - If configCookieSync is called twice or more to set cookies, each cookie set is separated by "; ".&gt;
> - If the specified value contains the "Secure" attribute, the URL must use the "https://" protocol.

**Since:** 14

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
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## deleteEntireCookie

```TypeScript
static deleteEntireCookie(): void
```

Deletes all cookies.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [clearAllCookiesSync](#clearallcookiessync)

**System capability:** SystemCapability.Web.Webview.Core

## deleteSessionCookie

```TypeScript
static deleteSessionCookie(): void
```

Deletes all session cookies.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [clearSessionCookieSync](#clearsessioncookiesync)

**System capability:** SystemCapability.Web.Webview.Core

## existCookie

```TypeScript
static existCookie(incognito?: boolean): boolean
```

Checks whether cookies exist.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Obtains all cookies. This API uses a promise to return the result.

**Since:** 23

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

Obtains the cookie value of a specified URL. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Obtains the cookie value of a specified URL. This API uses a promise to return the result.

**Since:** 14

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
static fetchCookie(url: string, incognito: boolean, includePartitionedCookies: boolean): Promise<string>
```

Obtains the cookies corresponding to a specified URL. The parameter incognito specifies whether to obtain cookies in Privacy Mode, and the parameter includePartitionedCookies specifies whether to obtain first-party partitioned cookies. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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

## fetchCookie

```TypeScript
static fetchCookie(url: string, callback: AsyncCallback<string>): void
```

Obtains the cookie value of a specified URL. This API uses an asynchronous callback to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean): string
```

Obtains the cookie value of the specified URL.

> **NOTE：**&gt;
> - The system automatically deletes expired cookies. For data with the same key name, the new data overwrites
> the previous data.&gt;
> - To obtain a usable cookie value, you are advised to pass a complete URL to fetchCookieSync.&gt;
> - fetchCookieSync is used to obtain all cookie values. Each cookie value is separated by "; ", but a specific
> cookie value cannot be obtained individually.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Obtains the cookies corresponding to a specified URL. The optional parameter incognito specifies whether to obtain cookies in Privacy Mode, and the optional parameter includePartitionedCookies specifies whether to obtain first-party partitioned cookies.

> **NOTE：**&gt;
> - The system automatically deletes expired cookies. For data with the same key name, the new data overwrites
> the previous data.&gt;
> - To obtain a usable cookie value, you are advised to pass a complete URL to fetchCookieSync.&gt;
> - fetchCookieSync is used to obtain all cookie values. Each cookie value is separated by "; ", but a specific
> cookie value cannot be obtained individually.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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

Obtains the cookie value of the specified URL.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [fetchCookieSync](#fetchcookiesync)

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

Checks whether the **WebCookieManager** instance has the permission to send and receive cookies.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isThirdPartyCookieAllowed

```TypeScript
static isThirdPartyCookieAllowed(): boolean
```

Checks whether the **WebCookieManager** instance has the permission to send and receive third-party cookies.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## putAcceptCookieEnabled

```TypeScript
static putAcceptCookieEnabled(accept: boolean): void
```

Sets whether the **WebCookieManager** instance has the permission to send and receive cookies.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Sets whether the **WebCookieManager** instance has the permission to send and receive third-party cookies.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Saves all cookies that can be obtained through fetchCookie and need to be persisted to the disk. This API uses a promise to return the result.

> **NOTE：**&gt;
> - saveCookieAsync is used to forcibly write cookies that need to be persisted to the disk. Session cookies are
> not persisted on PC/2-in-1 and tablet devices. Even if saveCookieAsync is called, session cookies are not
> written to the disk.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

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

Asynchronously saves all cookies (that can be obtained through **fetchCookie** and need to be persisted) to the disk.

> **NOTE：**&gt;
> - saveCookieAsync is used to forcibly write cookies that need to be persisted to the disk. Session cookies are
> not persisted on PC/2-in-1 and tablet devices. Even if saveCookieAsync is called, session cookies are not
> written to the disk.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## saveCookieSync

```TypeScript
static saveCookieSync(): void
```

Synchronously saves all cookies (that can be obtained through **fetchCookie** and need to be persisted) to the disk.

> **NOTE：**&gt;
> - saveCookieSync is used to forcibly write cookies that need to be persisted to the disk. Session cookies are
> not persisted on PC/2-in-1 and tablet devices. Even if saveCookieSync is called, session cookies are not
> written to the disk.&gt;
> - saveCookieSync blocks the caller until the operation is complete, during which I/O operations may be
> performed.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

## setCookie

```TypeScript
static setCookie(url: string, value: string): void
```

Sets a cookie for the specified URL.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [configCookieSync](#configcookiesync)

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
| [17100002](../errorcode-webview.md#17100002-incorrect-url-format) |
| [17100005](../errorcode-webview.md#17100005-invalid-cookie-value) |

## setLazyInitializeWebEngine

```TypeScript
static setLazyInitializeWebEngine(lazy: boolean): void
```

Sets whether to delay the initialization of the ArkWeb kernel. If this method is not called, the ArkWeb kernel is not delayed by default.

> **NOTE：**&gt;
> - This API is a global static method. It must be called before using ArkWeb components and initializing the
> ArkWeb kernel. Otherwise, the setting does not take effect.&gt;
> - This API applies only to APIs that initialize CookieManager when called, such as other APIs of this class
> WebCookieManager. After this API is called and set to **true**, calling applicable APIs skips the
> initialization of the ArkWeb kernel when initializing CookieManager. You need to initialize the ArkWeb kernel
> separately afterwards.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lazy | boolean | Yes |
