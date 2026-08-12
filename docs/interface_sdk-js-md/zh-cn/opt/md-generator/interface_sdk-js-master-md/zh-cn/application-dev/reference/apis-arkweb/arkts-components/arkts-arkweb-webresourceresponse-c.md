# WebResourceResponse

Web组件资源响应对象。

**起始版本：** 8

<!--Device-unnamed-declare class WebResourceResponse--><!--Device-unnamed-declare class WebResourceResponse-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-constructor()--><!--Device-WebResourceResponse-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getReasonMessage

```TypeScript
getReasonMessage(): string
```

获取资源响应的状态码描述。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getReasonMessage(): string--><!--Device-WebResourceResponse-getReasonMessage(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getResponseCode

```TypeScript
getResponseCode(): number
```

获取资源响应的状态码。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getResponseCode(): number--><!--Device-WebResourceResponse-getResponseCode(): number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

## getResponseData

```TypeScript
getResponseData(): string
```

获取资源响应数据。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getResponseData(): string--><!--Device-WebResourceResponse-getResponseData(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getResponseDataEx

```TypeScript
getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined
```

获取资源响应数据，支持多种数据类型。

**起始版本：** 13

<!--Device-WebResourceResponse-getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined--><!--Device-WebResourceResponse-getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getResponseEncoding

```TypeScript
getResponseEncoding(): string
```

获取资源响应的编码。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getResponseEncoding(): string--><!--Device-WebResourceResponse-getResponseEncoding(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getResponseHeader

```TypeScript
getResponseHeader(): Array<Header>
```

获取资源响应头。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getResponseHeader(): Array<Header>--><!--Device-WebResourceResponse-getResponseHeader(): Array<Header>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Array&lt;[Header](arkts-arkweb-header-i.md)&gt; |

## getResponseIsReady

```TypeScript
getResponseIsReady(): boolean
```

获取响应数据是否已准备就绪。

**起始版本：** 13

<!--Device-WebResourceResponse-getResponseIsReady(): boolean--><!--Device-WebResourceResponse-getResponseIsReady(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## getResponseMimeType

```TypeScript
getResponseMimeType(): string
```

获取资源响应的媒体（MIME）类型。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-getResponseMimeType(): string--><!--Device-WebResourceResponse-getResponseMimeType(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## setReasonMessage

```TypeScript
setReasonMessage(reason: string): void
```

设置资源响应的状态码描述。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setReasonMessage(reason: string): void--><!--Device-WebResourceResponse-setReasonMessage(reason: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reason | string | 是 |

## setResponseCode

```TypeScript
setResponseCode(code: number): void
```

设置资源响应的状态码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseCode(code: number): void--><!--Device-WebResourceResponse-setResponseCode(code: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

## setResponseData

```TypeScript
setResponseData(data: string | number | Resource | ArrayBuffer): void
```

设置资源响应数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseData(data: string | number | Resource | ArrayBuffer): void--><!--Device-WebResourceResponse-setResponseData(data: string | number | Resource | ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string \| number \| Resource \| ArrayBuffer | 是 |

## setResponseEncoding

```TypeScript
setResponseEncoding(encoding: string): void
```

设置资源响应的编码。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseEncoding(encoding: string): void--><!--Device-WebResourceResponse-setResponseEncoding(encoding: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 是 |

## setResponseHeader

```TypeScript
setResponseHeader(header: Array<Header>): void
```

设置资源响应头。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseHeader(header: Array<Header>): void--><!--Device-WebResourceResponse-setResponseHeader(header: Array<Header>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| header | Array&lt;[Header](arkts-arkweb-header-i.md)&gt; | 是 |

## setResponseIsReady

```TypeScript
setResponseIsReady(IsReady: boolean): void
```

设置资源响应数据是否已经就绪。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseIsReady(IsReady: boolean): void--><!--Device-WebResourceResponse-setResponseIsReady(IsReady: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| IsReady | boolean | 是 |

## setResponseMimeType

```TypeScript
setResponseMimeType(mimeType: string): void
```

设置资源响应的媒体（MIME）类型。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebResourceResponse-setResponseMimeType(mimeType: string): void--><!--Device-WebResourceResponse-setResponseMimeType(mimeType: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mimeType | string | 是 |
