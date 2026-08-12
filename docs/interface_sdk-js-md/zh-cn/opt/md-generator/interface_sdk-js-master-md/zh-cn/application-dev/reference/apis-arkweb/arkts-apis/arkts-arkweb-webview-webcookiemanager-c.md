# WebCookieManager

提供了用于管理网页Cookie的方法。

**起始版本：** 9

<!--Device-webview-class WebCookieManager--><!--Device-webview-class WebCookieManager-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## clearAllCookies

```TypeScript
static clearAllCookies(): Promise<void>
```

清除所有cookie。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearAllCookies(): Promise<void>--><!--Device-WebCookieManager-static clearAllCookies(): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## clearAllCookies

```TypeScript
static clearAllCookies(callback: AsyncCallback<void>): void
```

异步callback方式清除所有cookie。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearAllCookies(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## clearAllCookiesSync

```TypeScript
static clearAllCookiesSync(incognito?: boolean): void
```

清除所有cookie。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void--><!--Device-WebCookieManager-static clearAllCookiesSync(incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| incognito | boolean | 否 |

## clearSessionCookie

```TypeScript
static clearSessionCookie(): Promise<void>
```

清除所有会话cookie。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>--><!--Device-WebCookieManager-static clearSessionCookie(): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## clearSessionCookie

```TypeScript
static clearSessionCookie(callback: AsyncCallback<void>): void
```

异步callback方式清除所有会话cookie。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static clearSessionCookie(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## clearSessionCookieSync

```TypeScript
static clearSessionCookieSync(): void
```

清除所有会话cookie。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static clearSessionCookieSync(): void--><!--Device-WebCookieManager-static clearSessionCookieSync(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## configCookie

```TypeScript
static configCookie(url: string, value: string): Promise<void>
```

指定url设置单个cookie的值。使用Promise异步回调。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>
```

指定url设置单个cookie的值。使用Promise异步回调。

**起始版本：** 14

<!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>--><!--Device-WebCookieManager-static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |
| incognito | boolean | 是 |
| includeHttpOnly | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## configCookie

```TypeScript
static configCookie(url: string, value: string, callback: AsyncCallback<void>): void
```

异步callback方式为指定url设置单个cookie的值。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static configCookie(url: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito?: boolean): void
```

为指定url设置单个cookie的值。

> **说明：**
> 
> - configCookieSync中的url，可以指定域名的方式来使得页面内请求也附带上cookie。
> 
> - 同步cookie的时机建议在Web组件加载之前完成。
> 
> - cookie每30s周期性保存到磁盘中，也可以使用接口saveCookieAsync进行强制落盘。
> 
> - value参数必须遵循Set-Cookie HTTP响应头的格式。形式为"key=value"的键值对，后面可跟随以分号分隔的cookie属性列表（例如"key=value;Max-Age=100"）。
> 
> - 若存在相同host、path和名称的cookie，将被新cookie替换。若设置的cookie已过期，则不会存储该cookie。如需设置多个cookie，应多次调用此方法。
> 
> - 若通过configCookieSync进行两次或多次设置cookie，则每次设置的cookie之间会通过"; "进行分隔。
> 
> - 如果指定的值包含"Secure"属性，则url必须使用"https://"协议。
> 
> - 如果要覆盖HttpOnly的cookies，需要在value中指定HttpOnly属性。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |
| incognito | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## configCookieSync

```TypeScript
static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void
```

为指定url设置cookie的值。

> **说明：**
> 
> - configCookieSync中的url，可以指定域名的方式来使得页面内请求也附带上cookie。
> 
> - 同步cookie的时机建议在Web组件加载之前完成。
> 
> - cookie每30s周期性保存到磁盘中，也可以使用接口saveCookieAsync进行强制落盘。
> 
> - value参数必须遵循Set-Cookie HTTP响应头的格式。形式为"key=value"的键值对，后面可跟随以分号分隔的cookie属性列表（例如"key=value;Max-Age=100"）。
> 
> - 若存在相同host、path和名称的cookie，将被新cookie替换。若设置的cookie已过期，则不会存储该cookie。如需设置多个cookie，应多次调用此方法。
> 
> - 若通过configCookieSync进行两次或多次设置cookie，则每次设置的cookie之间会通过"; "进行分隔。
> 
> - 如果指定的值包含"Secure"属性，则url必须使用"https://"协议。

**起始版本：** 14

<!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void--><!--Device-WebCookieManager-static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |
| incognito | boolean | 是 |
| includeHttpOnly | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## deleteEntireCookie

```TypeScript
static deleteEntireCookie(): void
```

清除所有cookie。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [clearAllCookiesSync](#clearAllCookiesSync)

<!--Device-WebCookieManager-static deleteEntireCookie(): void--><!--Device-WebCookieManager-static deleteEntireCookie(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## deleteSessionCookie

```TypeScript
static deleteSessionCookie(): void
```

清除所有会话cookie。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [clearSessionCookieSync](#clearSessionCookieSync)

<!--Device-WebCookieManager-static deleteSessionCookie(): void--><!--Device-WebCookieManager-static deleteSessionCookie(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## existCookie

```TypeScript
static existCookie(incognito?: boolean): boolean
```

获取是否存在cookie。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean--><!--Device-WebCookieManager-static existCookie(incognito?: boolean): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| incognito | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| boolean |

## fetchAllCookies

```TypeScript
static fetchAllCookies(incognito: boolean):  Promise<Array<WebHttpCookie>>
```

异步获取所有cookie。

**起始版本：** 23

<!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean):  Promise<Array<WebHttpCookie>>--><!--Device-WebCookieManager-static fetchAllCookies(incognito: boolean):  Promise<Array<WebHttpCookie>>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| incognito | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[WebHttpCookie](arkts-arkweb-webview-webhttpcookie-i.md)&gt;&gt; |

## fetchCookie

```TypeScript
static fetchCookie(url: string): Promise<string>
```

以Promise方式异步获取指定url对应cookie的值。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## fetchCookie

```TypeScript
static fetchCookie(url: string, incognito: boolean): Promise<string>
```

以Promise方式异步获取指定url对应cookie的值。

**起始版本：** 14

<!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>--><!--Device-WebCookieManager-static fetchCookie(url: string, incognito: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| incognito | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## fetchCookie

```TypeScript
static fetchCookie(url: string, callback: AsyncCallback<string>): void
```

异步callback方式获取指定url对应cookie的值。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void--><!--Device-WebCookieManager-static fetchCookie(url: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## fetchCookieSync

```TypeScript
static fetchCookieSync(url: string, incognito?: boolean): string
```

获取指定url对应cookie的值。

> **说明：**
> 
> - 系统会自动清理过期的cookie，对于同名key的数据，新数据将会覆盖前一个数据。
> 
> - 为了获取可正常使用的cookie值，fetchCookieSync需传入完整链接。
> 
> - fetchCookieSync用于获取所有的cookie值，每条cookie值之间会通过"; "进行分隔，但无法单独获取某一条特定的cookie值。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string--><!--Device-WebCookieManager-static fetchCookieSync(url: string, incognito?: boolean): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| incognito | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## getCookie

```TypeScript
static getCookie(url: string): string
```

获取指定url对应cookie的值。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [fetchCookieSync](#fetchCookieSync)

<!--Device-WebCookieManager-static getCookie(url: string): string--><!--Device-WebCookieManager-static getCookie(url: string): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## isCookieAllowed

```TypeScript
static isCookieAllowed(): boolean
```

获取WebCookieManager实例是否拥有发送和接收cookie的权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static isCookieAllowed(): boolean--><!--Device-WebCookieManager-static isCookieAllowed(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isThirdPartyCookieAllowed

```TypeScript
static isThirdPartyCookieAllowed(): boolean
```

获取WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean--><!--Device-WebCookieManager-static isThirdPartyCookieAllowed(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## putAcceptCookieEnabled

```TypeScript
static putAcceptCookieEnabled(accept: boolean): void
```

设置WebCookieManager实例是否拥有发送和接收cookie的权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptCookieEnabled(accept: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accept | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## putAcceptThirdPartyCookieEnabled

```TypeScript
static putAcceptThirdPartyCookieEnabled(accept: boolean): void
```

设置WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void--><!--Device-WebCookieManager-static putAcceptThirdPartyCookieEnabled(accept: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accept | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## saveCookieAsync

```TypeScript
static saveCookieAsync(): Promise<void>
```

将当前可通过fetchCookie获取到的所有需要持久化的cookie以Promise方法异步保存到磁盘中。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>--><!--Device-WebCookieManager-static saveCookieAsync(): Promise<void>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## saveCookieAsync

```TypeScript
static saveCookieAsync(callback: AsyncCallback<void>): void
```

将当前可通过fetchCookie获取到的所有需要持久化的cookie异步保存到磁盘中。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void--><!--Device-WebCookieManager-static saveCookieAsync(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## saveCookieSync

```TypeScript
static saveCookieSync(): void
```

将当前可通过fetchCookie获取到的所有需要持久化的cookie同步保存到磁盘中。

> **说明：**
> 
> - saveCookieSync用于强制将需要持久化的cookies写入磁盘。PC/2in1和Tablet设备不会持久化session cookie，即使调用saveCookieSync，也不会将session
> cookie写入磁盘。
> 
> - saveCookieSync将阻塞调用者直到操作完成，期间可能会执行I/O操作。

**起始版本：** 15

<!--Device-WebCookieManager-static saveCookieSync(): void--><!--Device-WebCookieManager-static saveCookieSync(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## setCookie

```TypeScript
static setCookie(url: string, value: string): void
```

为指定url设置单个cookie的值。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [configCookieSync](#configCookieSync)

<!--Device-WebCookieManager-static setCookie(url: string, value: string): void--><!--Device-WebCookieManager-static setCookie(url: string, value: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100005-cookie-value格式错误) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## setLazyInitializeWebEngine

```TypeScript
static setLazyInitializeWebEngine(lazy: boolean): void
```

Delays the initialization of the web engine. By default, the web engine is initialized when the CookieManager interface is called. By setting the 'lazy' parameter to true, the web engine will not be initialized when the CookieManager interface is called. Instead, the web engine will be initialized either when the web component is created or when initializeWebEngine is called.

**起始版本：** 22

<!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void--><!--Device-WebCookieManager-static setLazyInitializeWebEngine(lazy: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lazy | boolean | 是 |
