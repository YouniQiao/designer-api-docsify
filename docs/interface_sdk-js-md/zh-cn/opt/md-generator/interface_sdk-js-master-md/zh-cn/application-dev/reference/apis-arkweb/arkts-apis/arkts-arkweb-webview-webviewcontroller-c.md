# WebviewController

Provides methods for controlling the web controller.

**起始版本：** 11

<!--Device-webview-class WebviewController--><!--Device-webview-class WebviewController-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## accessBackward

```TypeScript
accessBackward(): boolean
```

当前页面是否可后退，即当前页面是否有返回历史记录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-accessBackward(): boolean--><!--Device-WebviewController-accessBackward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessForward

```TypeScript
accessForward(): boolean
```

当前页面是否可前进，即当前页面是否有前进历史记录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-accessForward(): boolean--><!--Device-WebviewController-accessForward(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

当前页面是否可前进或者后退给定的step步。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-accessStep(step: number): boolean--><!--Device-WebviewController-accessStep(step: number): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| step | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## addIntelligentTrackingPreventionBypassingList

```TypeScript
static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

添加智能防跟踪功能绕过的域名列表。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## avoidVisibleViewportBottom

```TypeScript
avoidVisibleViewportBottom(avoidHeight: number): void
```

设置Web网页可视视口底部避让高度。

> **说明：**
> 
> - avoidHeight有效值区间为[0, Web组件高度]，超出有效值区间时取边界值。
> 
> - 该接口高度设置为非0时，Web组件位置和尺寸不变，可视视口向上避让avoidHeight，表现为Web网页内容抬升avoidHeight。该接口一般用于应用自定义网页底部避让区，不建议和点击web网页可编辑区拉起键盘的
> 场景同时使用。同时使用时，键盘弹起避让模式将使用OVERLAYS_CONTENT。
> 
> - 该接口高度设置为0时，Web网页内容可恢复，键盘弹起避让模式将使用
> [keyboardAvoidMode()](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#keyboardavoidmode12)
> 声明的模式。

**起始版本：** 20

<!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: number): void--><!--Device-WebviewController-avoidVisibleViewportBottom(avoidHeight: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| avoidHeight | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## backOrForward

```TypeScript
backOrForward(step: number): void
```

按照历史栈，前进或者后退指定步长的页面，当历史栈中不存在对应步长的页面时，不会进行页面跳转。

前进或者后退页面时，直接使用已加载过的网页，无需重新加载网页。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-backOrForward(step: number): void--><!--Device-WebviewController-backOrForward(step: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| step | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## backward

```TypeScript
backward(): void
```

按照历史栈，后退一个页面。一般结合[accessBackward](#accessBackward)一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-backward(): void--><!--Device-WebviewController-backward(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearBlanklessLoadingCache

```TypeScript
static clearBlanklessLoadingCache(keys?: Array<string>) : void
```

清除指定key值页面无白屏优化缓存，本接口只清除缓存。在小程序或Web应用场景中，当页面加载时内容变化显著，可能会出现一次明显的跳变。若对此跳变有所顾虑，可使用该接口清除页面缓存。

> **说明：**
> 
> - 清除之后的页面，需在第三次加载页面时才会产生优化效果。

**起始版本：** 20

<!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void--><!--Device-WebviewController-static clearBlanklessLoadingCache(keys?: Array<string>) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | Array & lt;string & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## clearClientAuthenticationCache

```TypeScript
clearClientAuthenticationCache(): void
```

清除Web组件记录的客户端证书请求事件对应的用户操作行为。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-clearClientAuthenticationCache(): void--><!--Device-WebviewController-clearClientAuthenticationCache(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearHistory

```TypeScript
clearHistory(): void
```

删除所有前进后退记录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-clearHistory(): void--><!--Device-WebviewController-clearHistory(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearHostIP

```TypeScript
static clearHostIP(hostName: string): void
```

清除指定主机域名解析后的IP地址。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static clearHostIP(hostName: string): void--><!--Device-WebviewController-static clearHostIP(hostName: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## clearIntelligentTrackingPreventionBypassingList

```TypeScript
static clearIntelligentTrackingPreventionBypassingList(): void
```

删除通过addIntelligentTrackingPreventionBypassingList接口添加的所有域名。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void--><!--Device-WebviewController-static clearIntelligentTrackingPreventionBypassingList(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## clearMatches

```TypeScript
clearMatches(): void
```

清除所有通过[searchAllAsync](#searchAllAsync)匹配到的高亮字符查找结果。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-clearMatches(): void--><!--Device-WebviewController-clearMatches(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearPrefetchedResource

```TypeScript
static clearPrefetchedResource(cacheKeyList: Array<string>): void
```

根据指定的缓存key列表清除对应的预获取资源缓存。入参中的缓存key必须是[prefetchResource](#prefetchResource)指定预获取到的资源缓存key。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void--><!--Device-WebviewController-static clearPrefetchedResource(cacheKeyList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cacheKeyList | Array & lt;string & gt; | 是 |

## clearServiceWorkerWebSchemeHandler

```TypeScript
static clearServiceWorkerWebSchemeHandler(): void
```

Clear all web service worker scheme handlers.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void--><!--Device-WebviewController-static clearServiceWorkerWebSchemeHandler(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## clearSslCache

```TypeScript
clearSslCache(): void
```

清除Web组件记录的SSL证书错误事件对应的用户操作行为。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-clearSslCache(): void--><!--Device-WebviewController-clearSslCache(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearWebSchemeHandler

```TypeScript
clearWebSchemeHandler(): void
```

Clear all web scheme handlers for related web component.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-clearWebSchemeHandler(): void--><!--Device-WebviewController-clearWebSchemeHandler(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## closeAllMediaPresentations

```TypeScript
closeAllMediaPresentations(): void
```

控制网页所有全屏视频关闭。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-closeAllMediaPresentations(): void--><!--Device-WebviewController-closeAllMediaPresentations(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## closeCamera

```TypeScript
closeCamera(): void
```

关闭当前网页摄像头捕获。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-closeCamera(): void--><!--Device-WebviewController-closeCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## constructor

```TypeScript
constructor(webTag?: string)
```

A constructor used to create a WebviewController object.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-constructor(webTag?: string)--><!--Device-WebviewController-constructor(webTag?: string)-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webTag | string | 否 |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void
```

Rendering current Web page into Pdf data, return the result in async mode.

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PdfData](arkts-arkweb-webview-pdfdata-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration): Promise<PdfData>
```

Rendering current Web page into Pdf data, return the result in promise mode.

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>--><!--Device-WebviewController-createPdf(configuration: PdfConfiguration): Promise<PdfData>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PdfData](arkts-arkweb-webview-pdfdata-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## createWebMessagePorts

```TypeScript
createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>
```

创建Web消息端口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>--><!--Device-WebviewController-createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isExtentionType](arkts-arkweb-webview-webmessageport-i.md) | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[WebMessagePort](arkts-arkweb-webview-webmessageport-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## createWebPrintDocumentAdapter

```TypeScript
createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter
```

Creates a PrintDocumentAdapter instance to provide content for printing.

**起始版本：** 11

<!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter--><!--Device-WebviewController-createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [jobName](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-print-printjobdata-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| print.PrintDocumentAdapter |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>): void
```

对Web内核赋予自定义协议URL的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议URL时，该fetch请求可被onInterceptRequest事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100020-注册自定义协议失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void
```

对Web内核赋予自定义协议URL的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议URL时，该fetch请求可被onInterceptRequest事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void--><!--Device-WebviewController-static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 |
| lazyInitWebEngine | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100020](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100020-注册自定义协议失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string): void
```

删除一个已注册的、具有给定名称的JavaScript对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-deleteJavaScriptRegister(name: string): void--><!--Device-WebviewController-deleteJavaScriptRegister(name: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100008-删除不存在的javascriptproxy) |

## enableAdsBlock

```TypeScript
enableAdsBlock(enable: boolean): void
```

启用广告过滤功能。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-enableAdsBlock(enable: boolean): void--><!--Device-WebviewController-enableAdsBlock(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## enableAdvancedSecurityMode

```TypeScript
static enableAdvancedSecurityMode(securityParams: SecurityParams): void
```

启用应用程序禁用PDFViewer等一些功能，以提高Web应用程序的安全级别

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void--><!--Device-WebviewController-static enableAdvancedSecurityMode(securityParams: SecurityParams): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| securityParams | [SecurityParams](arkts-arkweb-webview-securityparams-i.md) | 是 |

## enableBackForwardCache

```TypeScript
static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void
```

开启Web组件前进后退缓存功能，通过参数指定是否允许使用特定的页面进入前进后退缓存。默认设置为禁用。

**起始版本：** 12

<!--Device-WebviewController-static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void--><!--Device-WebviewController-static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| features | [BackForwardCacheSupportedFeatures](arkts-arkweb-webview-backforwardcachesupportedfeatures-c.md) | 是 |

## enableIntelligentTrackingPrevention

```TypeScript
enableIntelligentTrackingPrevention(enable: boolean): void
```

启用智能防跟踪功能。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void--><!--Device-WebviewController-enableIntelligentTrackingPrevention(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## enablePrivateNetworkAccess

```TypeScript
static enablePrivateNetworkAccess(enable: boolean): void
```

After enable PrivateNetworkAccess feature, ArkWeb will send a CORS preflight request before issuing any sub-resource private network requests to request explicit permission from the target server. After disable PrivateNetworkAccess, ArkWeb will no longer check whether the private network request is legitimate.By default, PrivateNetworkAccess feature is enabled.

**起始版本：** 20

<!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void--><!--Device-WebviewController-static enablePrivateNetworkAccess(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## enableSafeBrowsing

```TypeScript
enableSafeBrowsing(enable: boolean): void
```

启用检查网站安全风险的功能，非法和欺诈网站是强制启用的，不能通过此功能禁用。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void--><!--Device-WebviewController-enableSafeBrowsing(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## enableWholeWebPageDrawing

```TypeScript
static enableWholeWebPageDrawing(): void
```

设置开启网页全量绘制能力。仅在web初始化时设置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static enableWholeWebPageDrawing(): void--><!--Device-WebviewController-static enableWholeWebPageDrawing(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## forward

```TypeScript
forward(): void
```

按照历史栈，前进一个页面。一般结合accessForward一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-forward(): void--><!--Device-WebviewController-forward(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getActiveWebEngineVersion

```TypeScript
static getActiveWebEngineVersion(): ArkWebEngineVersion
```

获取当前ArkWeb内核版本。

**起始版本：** 20

<!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion--><!--Device-WebviewController-static getActiveWebEngineVersion(): ArkWebEngineVersion-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) |

## getAttachState

```TypeScript
getAttachState(): ControllerAttachState
```

获取webview controller是否绑定一个web组件

**起始版本：** 20

<!--Device-WebviewController-getAttachState(): ControllerAttachState--><!--Device-WebviewController-getAttachState(): ControllerAttachState-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md) |

## getBackForwardEntries

```TypeScript
getBackForwardEntries(): BackForwardList
```

获取当前Webview的历史信息列表。

> **说明：**
> 
> onLoadIntercept在加载开始的时候触发，该时刻还未生成历史节点，所以在onLoadIntercept中调用getBackForwardEntries
> 拿到的历史栈不包括当前正在加载中的跳转。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getBackForwardEntries(): BackForwardList--><!--Device-WebviewController-getBackForwardEntries(): BackForwardList-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [BackForwardList](arkts-arkweb-webview-backforwardlist-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getBlanklessInfoWithKey

```TypeScript
getBlanklessInfoWithKey(key: string) : BlanklessInfo
```

获取页面首屏加载预测信息（详细说明见[BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md#BlanklessInfo)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。必须与[setBlanklessLoadingWithKey](#setBlanklessLoadingWithKey)接口配套使用，并且必须在触发加载页面的接口之前或在`onLoadIntercept`中调用。需在`WebViewController`与Web组件绑定后才能使用。

> **说明：**
> 
> - 持久缓存容量：默认大小为30MB（约30页），可以通过接口
> [setBlanklessLoadingCacheCapacity](#setBlanklessLoadingCacheCapacity)设置缓存容量，具体见该
> 接口说明。超过容量时根据LRU（Least Recently Used，淘汰不常用缓存的策略）机制更新缓存。自动清理超过7天的持久缓存数据，缓存清除后第三次加载页面开始有优化效果。
> 
> - 如果发现快照相似度（即[BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md#BlanklessInfo)中的similarity）极低，请确认key值是否传递正确。
> 
> - 调用本接口后，将启用页面加载快照检测及生成过渡帧计算，会产生一定的资源开销。
> 
> - 启用无白屏加载的页面会带来一定的资源开销，开销的大小与Web组件的分辨率相关。假设分辨率的宽度和高度分别为：w, h。页面在打开阶段会增加峰值内存，增加约12 * w * h B，页面打开后内存回收，不影响稳态内存。增
> 加固态应用缓存的大小，每个页面增加的缓存约w * h / 10 B，缓存位于应用缓存的位置。
> 
> - 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考
> [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 20

<!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo--><!--Device-WebviewController-getBlanklessInfoWithKey(key: string) : BlanklessInfo-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| [BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## getCertificate

```TypeScript
getCertificate(): Promise<Array<cert.X509Cert>>
```

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过Promise异步返回当前网站的X509格式证书。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>--><!--Device-WebviewController-getCertificate(): Promise<Array<cert.X509Cert>>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;cert.X509Cert & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void
```

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过AsyncCallback异步返回当前网站的X509格式证书。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void--><!--Device-WebviewController-getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;cert.X509Cert&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

获取自定义用户代理。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getCustomUserAgent(): string--><!--Device-WebviewController-getCustomUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getDefaultUserAgent

```TypeScript
static getDefaultUserAgent(): string
```

获取默认用户代理。

**起始版本：** 14

<!--Device-WebviewController-static getDefaultUserAgent(): string--><!--Device-WebviewController-static getDefaultUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getErrorPageEnabled

```TypeScript
getErrorPageEnabled(): boolean
```

Get whether default error page feature is enabled.

**起始版本：** 20

<!--Device-WebviewController-getErrorPageEnabled(): boolean--><!--Device-WebviewController-getErrorPageEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getFavicon

```TypeScript
getFavicon(): image.PixelMap
```

获取页面的favicon图标。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getFavicon(): image.PixelMap--><!--Device-WebviewController-getFavicon(): image.PixelMap-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getHitTest

```TypeScript
getHitTest(): WebHitTestType
```

获取当前被点击区域的元素类型。

> **说明：**
> 
> 从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](#getLastHitTest)替代。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getLastHitTest](#getLastHitTest)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getHitTest(): WebHitTestType--><!--Device-WebviewController-getHitTest(): WebHitTestType-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [WebHitTestType](arkts-arkweb-webview-webhittesttype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getHitTestValue

```TypeScript
getHitTestValue(): HitTestValue
```

获取当前被点击区域的元素信息。

> **说明：**
> 
> 从API version11开始支持，从API version 18开始废弃。建议使用[getLastHitTest](#getLastHitTest)替代。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getLastHitTest](#getLastHitTest)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getHitTestValue(): HitTestValue--><!--Device-WebviewController-getHitTestValue(): HitTestValue-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getLastHitTest

```TypeScript
getLastHitTest(): HitTestValue
```

获取上一次被点击区域的元素信息。

**起始版本：** 18

<!--Device-WebviewController-getLastHitTest(): HitTestValue--><!--Device-WebviewController-getLastHitTest(): HitTestValue-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getLastJavascriptProxyCallingFrameUrl

```TypeScript
getLastJavascriptProxyCallingFrameUrl(): string
```

获取最后一次调用注入的对象的frame的URL。该方法应在 UI 线程上调用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string--><!--Device-WebviewController-getLastJavascriptProxyCallingFrameUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getLastPostMessageURL

```TypeScript
getLastPostMessageURL(): string
```

获取上一次发送post message给应用的HTML的frame的url

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-getLastPostMessageURL(): string--><!--Device-WebviewController-getLastPostMessageURL(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getMediaPlaybackState

```TypeScript
getMediaPlaybackState(): MediaPlaybackState
```

查询当前网页音视频播放状态。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState--><!--Device-WebviewController-getMediaPlaybackState(): MediaPlaybackState-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [MediaPlaybackState](arkts-arkweb-webview-mediaplaybackstate-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

获取当前页面的原始URL地址。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getOriginalUrl(): string--><!--Device-WebviewController-getOriginalUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getPageHeight

```TypeScript
getPageHeight(): number
```

获取当前网页的页面高度。具体使用详情请参考[获取网页内容高度](../../../web/web-getpage-height.md)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getPageHeight(): number--><!--Device-WebviewController-getPageHeight(): number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getPageOffset

```TypeScript
getPageOffset(): ScrollOffset
```

获取网页当前的滚动偏移量（不包含过滚动偏移量）。

**起始版本：** 20

<!--Device-WebviewController-getPageOffset(): ScrollOffset--><!--Device-WebviewController-getPageOffset(): ScrollOffset-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ScrollOffset](arkts-arkweb-webview-scrolloffset-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## getPrintBackground

```TypeScript
getPrintBackground(): boolean
```

Get whether print web page background.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getPrintBackground(): boolean--><!--Device-WebviewController-getPrintBackground(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getProgress

```TypeScript
getProgress() : number
```

Gets the loading progress for the current page.

**起始版本：** 20

<!--Device-WebviewController-getProgress() : number--><!--Device-WebviewController-getProgress() : number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## getRenderProcessMode

```TypeScript
static getRenderProcessMode(): RenderProcessMode
```

Get render process mode of the ArkWeb.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode--><!--Device-WebviewController-static getRenderProcessMode(): RenderProcessMode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) |

## getScrollOffset

```TypeScript
getScrollOffset(): ScrollOffset
```

获取网页当前的滚动偏移量（包含过滚动偏移量）。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getScrollOffset(): ScrollOffset--><!--Device-WebviewController-getScrollOffset(): ScrollOffset-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ScrollOffset](arkts-arkweb-webview-scrolloffset-i.md) |

## getScrollable

```TypeScript
getScrollable(): boolean
```

获取当前网页是否允许滚动。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getScrollable(): boolean--><!--Device-WebviewController-getScrollable(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getSecurityLevel

```TypeScript
getSecurityLevel(): SecurityLevel
```

获取当前网页的安全级别。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getSecurityLevel(): SecurityLevel--><!--Device-WebviewController-getSecurityLevel(): SecurityLevel-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [SecurityLevel](../../apis-arkdata/arkts-apis/arkts-arkdata-distributedkvstore-securitylevel-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getSiteIsolationMode

```TypeScript
static getSiteIsolationMode(): SiteIsolationMode
```

Get the site isolation mode.

**起始版本：** 21

<!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode--><!--Device-WebviewController-static getSiteIsolationMode(): SiteIsolationMode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) |

## getSurfaceId

```TypeScript
getSurfaceId(): string
```

获取ArkWeb对应Surface的ID，此ID可用于网页截图。

> **说明：**
> 
> 仅Web组件渲染模式是ASYNC_RENDER时有效。getSurfaceId需要在Web组件初始化之后才能获取到值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getSurfaceId(): string--><!--Device-WebviewController-getSurfaceId(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getTitle

```TypeScript
getTitle(): string
```

获取当前网页的标题。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getTitle(): string--><!--Device-WebviewController-getTitle(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUrl

```TypeScript
getUrl(): string
```

获取当前页面的URL地址。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getUrl(): string--><!--Device-WebviewController-getUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUserAgent

```TypeScript
getUserAgent(): string
```

获取当前默认用户代理。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getUserAgent(): string--><!--Device-WebviewController-getUserAgent(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUserAgentClientHintsEnabled

```TypeScript
static getUserAgentClientHintsEnabled(): boolean
```

Get if the UserAgent Client Hints enabled.

**起始版本：** 24

<!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean--><!--Device-WebviewController-static getUserAgentClientHintsEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## getUserAgentMetadata

```TypeScript
getUserAgentMetadata(userAgent: string): UserAgentMetadata
```

Get the User-Agent metadata corresponding to the User-Agent.

**起始版本：** 24

<!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata--><!--Device-WebviewController-getUserAgentMetadata(userAgent: string): UserAgentMetadata-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

**返回值：**

| 类型 |
| --- |
| [UserAgentMetadata](arkts-arkweb-webview-useragentmetadata-c.md) |

## getWebId

```TypeScript
getWebId(): number
```

Gets the index value of the current Web component for the management of multiple Web components.

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-getWebId(): number--><!--Device-WebviewController-getWebId(): number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## hasImage

```TypeScript
hasImage(): Promise<boolean>
```

通过Promise方式异步查找当前页面是否存在图像。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-hasImage(): Promise<boolean>--><!--Device-WebviewController-hasImage(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## hasImage

```TypeScript
hasImage(callback: AsyncCallback<boolean>): void
```

通过Callback方式异步查找当前页面是否存在图像。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void--><!--Device-WebviewController-hasImage(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## initializeWebEngine

```TypeScript
static initializeWebEngine(): void
```

Initialize the web engine before loading the Web components.This is a global static API that must be called on the UI thread, and it will have no effect if any Web components are loaded.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static initializeWebEngine(): void--><!--Device-WebviewController-static initializeWebEngine(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## injectOfflineResources

```TypeScript
injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void
```

将本地离线资源注入到内存缓存中，以提升页面首次启动速度。内存缓存中的资源由内核自动管理，当注入的资源过多导致内存压力过大，内核自动释放未使用的资源，应避免注入大量资源到内存缓存中。正常情况下，资源的有效期由提供的Cache-Control或Expires响应头控制其有效期，默认的有效期为86400秒，即1天。资源的MIMEType通过提供的Content-Type响应头配置，Content-Type需符合标准，否则无法正常使用，MODULE_JS必须提供有效的MIMEType，其他类型可不提供。以此方式注入的资源，仅支持通过HTML中的标签加载。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous或use-credentials。当调用`webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)`接口后，应用会启动多渲染进程模式，此接口在此场景下不会生效。

**起始版本：** 12

<!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void--><!--Device-WebviewController-injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceMaps | Array&lt;[OfflineResourceMap](arkts-arkweb-webview-offlineresourcemap-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## isActiveWebEngineEvergreen

```TypeScript
static isActiveWebEngineEvergreen(): boolean
```

判断当前系统是否正在使用常青内核，即系统的最新内核。

**起始版本：** 23

<!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean--><!--Device-WebviewController-static isActiveWebEngineEvergreen(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isAdsBlockEnabled

```TypeScript
isAdsBlockEnabled(): boolean
```

查询广告过滤功能是否开启。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-isAdsBlockEnabled(): boolean--><!--Device-WebviewController-isAdsBlockEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## isAdsBlockEnabledForCurPage

```TypeScript
isAdsBlockEnabledForCurPage(): boolean
```

查询当前网页是否开启广告过滤功能。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean--><!--Device-WebviewController-isAdsBlockEnabledForCurPage(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## isAutoPreconnectEnabled

```TypeScript
static isAutoPreconnectEnabled(): boolean
```

?Retrieve whether the automatic pre-connection feature is enabled?.

**起始版本：** 21

<!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean--><!--Device-WebviewController-static isAutoPreconnectEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isIncognitoMode

```TypeScript
isIncognitoMode(): boolean
```

查询当前是否是隐私模式的Webview。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-isIncognitoMode(): boolean--><!--Device-WebviewController-isIncognitoMode(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## isIntelligentTrackingPreventionEnabled

```TypeScript
isIntelligentTrackingPreventionEnabled(): boolean
```

获取Web组件是否启用了智能防跟踪功能。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean--><!--Device-WebviewController-isIntelligentTrackingPreventionEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## isPrivateNetworkAccessEnabled

```TypeScript
static isPrivateNetworkAccessEnabled(): boolean
```

Get whether PrivateNetworkAccess is enabled.

**起始版本：** 20

<!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean--><!--Device-WebviewController-static isPrivateNetworkAccessEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isSafeBrowsingEnabled

```TypeScript
isSafeBrowsingEnabled(): boolean
```

获取当前网页是否启用了检查网站安全风险。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-isSafeBrowsingEnabled(): boolean--><!--Device-WebviewController-isSafeBrowsingEnabled(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## loadData

```TypeScript
loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void
```

加载指定的数据。

baseUrl与historyUrl同时为空的情况下：

encoding如果为非base64（包括空值），则假定数据对安全URL字符范围内的八位字节使用ASCII编码，对该范围外的八位字节使用URL的标准%xx十六进制编码。data数据必须使用base64编码或将内容中的任何#字符编码为%23。否则#将被视为内容的结尾而剩余的文本将被用作文档片段标识符。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void--><!--Device-WebviewController-loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | string | 是 |
| mimeType | string | 是 |
| encoding | string | 是 |
| baseUrl | string | 否 |
| [historyUrl](arkts-arkweb-webview-historyitem-i.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

加载指定的URL。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void--><!--Device-WebviewController-loadUrl(url: string | Resource, headers?: Array<WebHeader>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| headers | Array & lt;WebHeader & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |
| [17100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## off('controllerAttachStateChange')

```TypeScript
off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void
```

取消注册controller绑定状态变化的回调

**起始版本：** 20

<!--Device-WebviewController-off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void--><!--Device-WebviewController-off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 否 |

## on('controllerAttachStateChange')

```TypeScript
on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void
```

注册controller绑定状态变化的回调

**起始版本：** 20

<!--Device-WebviewController-on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void--><!--Device-WebviewController-on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 是 |

## onActive

```TypeScript
onActive(): void
```

Let the Web active.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-onActive(): void--><!--Device-WebviewController-onActive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## onCreateNativeMediaPlayer

```TypeScript
onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void
```

注册回调函数，开启  
[应用接管网页媒体播放功能](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#enablenativemediaplayer12)后，当网页中有播放媒体时，触发注册的回调函数。

如果应用接管网页媒体播放功能未开启，则注册的回调函数不会被触发。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void--><!--Device-WebviewController-onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md) | 是 |

## onInactive

```TypeScript
onInactive(): void
```

Let the Web inactive.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-onInactive(): void--><!--Device-WebviewController-onInactive(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pageDown

```TypeScript
pageDown(bottom: boolean): void
```

将Webview的内容向下滚动半个视框大小或者跳转到页面最底部，通过bottom入参控制。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-pageDown(bottom: boolean): void--><!--Device-WebviewController-pageDown(bottom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bottom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pageUp

```TypeScript
pageUp(top: boolean): void
```

将Webview的内容向上滚动半个视框大小或者跳转到页面最顶部，通过top入参控制。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-pageUp(top: boolean): void--><!--Device-WebviewController-pageUp(top: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| top | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseAllMedia

```TypeScript
pauseAllMedia(): void
```

控制网页所有音视频暂停。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-pauseAllMedia(): void--><!--Device-WebviewController-pauseAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseAllTimers

```TypeScript
static pauseAllTimers(): void
```

暂停所有WebView的定时器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static pauseAllTimers(): void--><!--Device-WebviewController-static pauseAllTimers(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseMicrophone

```TypeScript
pauseMicrophone(): void
```

暂停当前网页麦克风捕获。

**起始版本：** 23

<!--Device-WebviewController-pauseMicrophone(): void--><!--Device-WebviewController-pauseMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## postMessage

```TypeScript
postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void
```

发送Web消息端口到HTML。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void--><!--Device-WebviewController-postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| ports | Array&lt;[WebMessagePort](arkts-arkweb-webview-webmessageport-i.md)&gt; | 是 |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## postUrl

```TypeScript
postUrl(url: string, postData: ArrayBuffer): void
```

使用"POST"方法加载带有postData的URL。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void--><!--Device-WebviewController-postUrl(url: string, postData: ArrayBuffer): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| postData | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## precompileJavaScript

```TypeScript
precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>
```

预编译JavaScript生成字节码缓存或根据提供的参数更新已有的字节码缓存。接口通过提供的文件信息、E-Tag响应头和Last-Modified响应头判断是否需要更新已有的字节码缓存。

**起始版本：** 12

<!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>--><!--Device-WebviewController-precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| script | string \| Uint8Array | 是 |
| cacheOptions | [CacheOptions](arkts-arkweb-webview-cacheoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void
```

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

> **说明：**
> 
> - 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。
> 
> - prefetchPage对302重定向页面同样正常预取。
> 
> - 先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。
> 
> - 连续prefetchPage多个URL只有第一个生效。
> 
> - prefetchPage有时间限制，500ms内不能多次预取。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| additionalHeaders | Array & lt;WebHeader & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void
```

Prefetch the resources required by the page, but will not execute js or render the page.

> **说明：**
> 
> - 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。
> - prefetchPage对302重定向页面同样正常预取。
?> - prefetchPage默认不缓存Cache-Control: no-store的资源，并且只允许在500ms内进行一次预取。  
> - 可以通过prefetchOptions自定义预取行为，包括忽略Cache-Control: no-store和调整节流间隔。

**起始版本：** 21

<!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void--><!--Device-WebviewController-prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| additionalHeaders | Array & lt;WebHeader & gt; | 否 |
| prefetchOptions | [PrefetchOptions](arkts-arkweb-webview-prefetchoptions-c.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## prefetchResource

```TypeScript
static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,
                            cacheValidTime?: number): void
```

根据指定的请求信息和附加的HTTP请求头去预获取资源请求，存入内存缓存，并指定其缓存key和有效期，以加快加载速度。目前仅支持Content-Type为application/x-www-form-urlencoded的POST请求。最多可以预获取6个POST请求。如果要预获取第7个，请通过  
[clearPrefetchedResource](#clearPrefetchedResource)清除不需要的POST请求缓存，否则会自动清除最早预获取的POST缓存。如果要使用预获取的资源缓存，开发者需要在正式发起的POST请求的请求头中增加键值“ArkWebPostCacheKey”，其内容为对应缓存的cacheKey。

内存缓存中的资源由内核自动管理，当注入的资源过多导致内存压力过大，内核自动释放未使用的资源，应避免注入大量资源到内存缓存中。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,                            cacheValidTime?: number): void--><!--Device-WebviewController-static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,                            cacheValidTime?: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [RequestInfo](../../apis-ability-kit/arkts-apis/arkts-ability-dialogrequest-requestinfo-i.md) | 是 |
| additionalHeaders | Array & lt;WebHeader & gt; | 否 |
| cacheKey | string | 否 |
| cacheValidTime | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## prepareForPageLoad

```TypeScript
static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void
```

预连接URL，在加载URL之前调用此API，对URL只进行DNS解析，socket建链操作，并不获取主资源子资源。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void--><!--Device-WebviewController-static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| preconnectable | boolean | 是 |
| numSockets | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |
| [17100013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100013-预连接时输入socket数目无效) |

## refresh

```TypeScript
refresh(): void
```

调用此接口通知Web组件刷新网页。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-refresh(): void--><!--Device-WebviewController-refresh(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## refresh

```TypeScript
refresh(ignoreCache: boolean): void
```

通知Web组件刷新网页，可以选择是否忽略缓存刷新。

**起始版本：** 24

<!--Device-WebviewController-refresh(ignoreCache: boolean): void--><!--Device-WebviewController-refresh(ignoreCache: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ignoreCache | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,
        asyncMethodList?: Array<string>, permission?: string): void
```

Registers the JavaScript object and method list.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,        asyncMethodList?: Array<string>, permission?: string): void--><!--Device-WebviewController-registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,        asyncMethodList?: Array<string>, permission?: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [jsObject](arkts-arkweb-web-javascriptproxy-i.md) | object | 是 |
| name | string | 是 |
| methodList | Array & lt;string & gt; | 是 |
| asyncMethodList | Array & lt;string & gt; | 否 |
| permission | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## removeAllCache

```TypeScript
static removeAllCache(clearRom: boolean): void
```

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

**起始版本：** 18

<!--Device-WebviewController-static removeAllCache(clearRom: boolean): void--><!--Device-WebviewController-static removeAllCache(clearRom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| clearRom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## removeCache

```TypeScript
removeCache(clearRom: boolean): void
```

清除应用中的资源缓存文件，此方法将会清除同一应用中所有Webview的缓存文件。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-removeCache(clearRom: boolean): void--><!--Device-WebviewController-removeCache(clearRom: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| clearRom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## removeIntelligentTrackingPreventionBypassingList

```TypeScript
static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

删除通过addIntelligentTrackingPreventionBypassingList接口添加的部分域名列表。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void--><!--Device-WebviewController-static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## requestFocus

```TypeScript
requestFocus(): void
```

使当前Web页面获取焦点。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-requestFocus(): void--><!--Device-WebviewController-requestFocus(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## restoreWebState

```TypeScript
restoreWebState(state: Uint8Array) : void
```

当前Webview从序列化数据中恢复页面状态历史记录。如果state过大，可能会导致异常。建议state大于512k时，放弃恢复页面状态历史记录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-restoreWebState(state: Uint8Array) : void--><!--Device-WebviewController-restoreWebState(state: Uint8Array) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeAllMedia

```TypeScript
resumeAllMedia(): void
```

控制网页被pauseAllMedia接口暂停的音视频继续播放。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-resumeAllMedia(): void--><!--Device-WebviewController-resumeAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeAllTimers

```TypeScript
static resumeAllTimers(): void
```

恢复从pauseAllTimers()接口中被暂停的所有的定时器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static resumeAllTimers(): void--><!--Device-WebviewController-static resumeAllTimers(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeMicrophone

```TypeScript
resumeMicrophone(): void
```

恢复当前网页麦克风捕获。使用麦克风功能前请在module.json5中添加权限: ohos.permission.MICROPHONE，具体权限的添加方法请参考  
[在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 23

<!--Device-WebviewController-resumeMicrophone(): void--><!--Device-WebviewController-resumeMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## runJavaScript

```TypeScript
runJavaScript(script: string): Promise<string>
```

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

> **说明：**
> 
> - 跨导航操作（如loadUrl）时，JavaScript状态 将不再保留，例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
> 
> - 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-runJavaScript(script: string): Promise<string>--><!--Device-WebviewController-runJavaScript(script: string): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## runJavaScript

```TypeScript
runJavaScript(script: string, callback: AsyncCallback<string>): void
```

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

> **说明：**
> 
> - 跨导航操作（如loadUrl）时，JavaScript状态将不再保留。例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。
> 
> - 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void--><!--Device-WebviewController-runJavaScript(script: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>
```

异步执行JavaScript脚本，并通过Promise方式返回脚本执行的结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string \| ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void
```

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void--><!--Device-WebviewController-runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string \| ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollBy

```TypeScript
scrollBy(deltaX: number, deltaY: number, duration?: number): void
```

在指定时间内将页面滚动指定的偏移量。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-scrollBy(deltaX: number, deltaY: number, duration?: number): void--><!--Device-WebviewController-scrollBy(deltaX: number, deltaY: number, duration?: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deltaX | number | 是 |
| deltaY | number | 是 |
| duration | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollByWithResult

```TypeScript
scrollByWithResult(deltaX: number, deltaY: number): boolean
```

将页面滚动指定的偏移量，返回值表示此次滚动是否执行成功。

**起始版本：** 12

<!--Device-WebviewController-scrollByWithResult(deltaX: number, deltaY: number): boolean--><!--Device-WebviewController-scrollByWithResult(deltaX: number, deltaY: number): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deltaX | number | 是 |
| deltaY | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollTo

```TypeScript
scrollTo(x: number, y: number, duration?: number): void
```

Scrolls the page to the specified absolute position within a specified period.

在指定时间内，将页面滚动到指定的绝对位置。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-scrollTo(x: number, y: number, duration?: number): void--><!--Device-WebviewController-scrollTo(x: number, y: number, duration?: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| duration | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## searchAllAsync

```TypeScript
searchAllAsync(searchString: string): void
```

异步查找网页中所有匹配关键字'searchString'的内容并高亮，结果通过  
[onSearchResultReceive](@ohos.web.WebAttribute#onsearchresultreceive)异步返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-searchAllAsync(searchString: string): void--><!--Device-WebviewController-searchAllAsync(searchString: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchString | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## searchNext

```TypeScript
searchNext(forward: boolean): void
```

滚动到下一个匹配的查找结果并高亮。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-searchNext(forward: boolean): void--><!--Device-WebviewController-searchNext(forward: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [forward](#forward) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## serializeWebState

```TypeScript
serializeWebState() : Uint8Array
```

Serialize the access stack of the web, that is, the history of access.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-serializeWebState() : Uint8Array--><!--Device-WebviewController-serializeWebState() : Uint8Array-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setActiveWebEngineVersion

```TypeScript
static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void
```

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效。该接口为全局静态API，须在调用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。

> **说明：**
> 
> - setActiveWebEngineVersion不支持在异步线程中调用。
> 
> - setActiveWebEngineVersion全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**起始版本：** 20

<!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void--><!--Device-WebviewController-static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) | 是 |

## setAppCustomUserAgent

```TypeScript
static setAppCustomUserAgent(userAgent: string) : void
```

Set the default User-Agent for the application.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;Unlike setCustomUserAgent, which only takes effect in the current web context, the priority for pages loaded in the web is as follows:1. The User-Agent set by setCustomUserAgent is used first.2. If not set, it will check whether a specific User-Agent has been  assigned to the current page via setUserAgentForHosts.3. If no specific User-Agent is assigned, the application will fall back  to using the User-Agent set by setAppCustomUserAgent.4. If the app's default User-Agent is also not specified, the web's default  User-Agent will be used as the final fallback.&lt;/p&gt;

**起始版本：** 20

<!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void--><!--Device-WebviewController-static setAppCustomUserAgent(userAgent: string) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

## setAudioMuted

```TypeScript
setAudioMuted(mute: boolean): void
```

设置网页静音。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setAudioMuted(mute: boolean): void--><!--Device-WebviewController-setAudioMuted(mute: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setAutoPreconnect

```TypeScript
static setAutoPreconnect(enabled: boolean): void
```

Configure whether to enable automatic pre-connection to high-frequency URLs accessed during the application's previous lifecycle after web initialization.

**起始版本：** 21

<!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void--><!--Device-WebviewController-static setAutoPreconnect(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## setBackForwardCacheOptions

```TypeScript
setBackForwardCacheOptions(options: BackForwardCacheOptions): void
```

可以设置Web组件中前进后退缓存的相关选项。

**起始版本：** 12

<!--Device-WebviewController-setBackForwardCacheOptions(options: BackForwardCacheOptions): void--><!--Device-WebviewController-setBackForwardCacheOptions(options: BackForwardCacheOptions): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [BackForwardCacheOptions](arkts-arkweb-webview-backforwardcacheoptions-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setBlanklessLoadingCacheCapacity

```TypeScript
static setBlanklessLoadingCacheCapacity(capacity: number) : number
```

设置无白屏加载方案的持久化缓存容量，返回实际生效值。当接口没有显式调用时，默认缓存容量为30MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。

**起始版本：** 20

<!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: number) : number--><!--Device-WebviewController-static setBlanklessLoadingCacheCapacity(capacity: number) : number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capacity | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## setBlanklessLoadingWithKey

```TypeScript
setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode
```

设置无白屏加载是否启用，本接口必须与[getBlanklessInfoWithKey](#getBlanklessInfoWithKey)接口配套使用。

> **说明：**
> 
> - 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](#getBlanklessInfoWithKey)。
> 
> - 页面加载必须在调用本接口的组件中进行。
> 
> - 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。
> 
> - 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考
> [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 20

<!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| is_start | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [WebBlanklessErrorCode](arkts-arkweb-webview-webblanklesserrorcode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## setBlanklessLoadingWithParams

```TypeScript
setBlanklessLoadingWithParams(key: string,
      param: BlanklessLoadingParam) : WebBlanklessErrorCode
```

Triggers frame interpolation and sets frame interpolation parameters. This API must be used in pair with the getBlanklessInfoWithKey API.

Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,      param: BlanklessLoadingParam) : WebBlanklessErrorCode--><!--Device-WebviewController-setBlanklessLoadingWithParams(key: string,      param: BlanklessLoadingParam) : WebBlanklessErrorCode-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| param | [BlanklessLoadingParam](arkts-arkweb-webview-blanklessloadingparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [WebBlanklessErrorCode](arkts-arkweb-webview-webblanklesserrorcode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |

## setConnectionTimeout

```TypeScript
static setConnectionTimeout(timeout: number): void
```

设置网络连接超时时间，使用者可通过Web组件中的onErrorReceive方法获取超时错误码。若未调用该接口则默认超时时间为30秒。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setConnectionTimeout(timeout: number): void--><!--Device-WebviewController-static setConnectionTimeout(timeout: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

设置自定义用户代理，会覆盖系统的用户代理。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setCustomUserAgent(userAgent: string): void--><!--Device-WebviewController-setCustomUserAgent(userAgent: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setDownloadDelegate

```TypeScript
setDownloadDelegate(delegate: WebDownloadDelegate): void
```

为当前的Web组件设置一个WebDownloadDelegate，该delegate用来接收页面内触发的下载进度的委托。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void--><!--Device-WebviewController-setDownloadDelegate(delegate: WebDownloadDelegate): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean): void
```

是否开启默认错误页，开启后onOverrideErrorPage会在页面发生错误的时候进行回调

**起始版本：** 20

<!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void--><!--Device-WebviewController-setErrorPageEnabled(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setHostIP

```TypeScript
static setHostIP(hostName: string, address: string, aliveTime: number): void
```

设置主机域名解析后的IP地址。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: number): void--><!--Device-WebviewController-static setHostIP(hostName: string, address: string, aliveTime: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostName | string | 是 |
| address | string | 是 |
| aliveTime | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setHttpDns

```TypeScript
static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void
```

设置Web组件是否使用HTTPDNS解析DNS。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void--><!--Device-WebviewController-static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| secureDnsMode | [SecureDnsMode](arkts-arkweb-webview-securednsmode-e.md) | 是 |
| secureDnsConfig | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setNetworkAvailable

```TypeScript
setNetworkAvailable(enable: boolean): void
```

为网页设置网络状态。该功能用于在JavaScript中设置window.navigator.onLine属性。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setNetworkAvailable(enable: boolean): void--><!--Device-WebviewController-setNetworkAvailable(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setPathAllowingUniversalAccess

```TypeScript
setPathAllowingUniversalAccess(pathList: Array<string>): void
```

设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件，也允许跨域访问其他在线资源。此外，当设置了路径列表时，file协议仅允许访问路径列表中的资源（  
[fileAccess](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#fileaccess)的行为将会被此接口行为覆盖）。

setPathAllowingUniversalAccess放开目录的跨域访问限制是一个高风险操作。基于最小权限原则，当前el1，el2放开的路径是固定的，路径列表中的路径应符合以下任一路径格式：

1.应用文件目录的子目录（应用文件目录通过Ability Kit中的  
[Context.filesDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/files/example  
* /data/storage/el2/base/haps/entry/files/example

2.应用资源目录及其子目录（应用资源目录通过Ability Kit中的  
[Context.resourceDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el1/bundle/entry/resources/resfile  
* /data/storage/el1/bundle/entry/resources/resfile/example

3.从API version 21开始，还包括了应用缓存目录及其子目录（应用缓存目录通过Ability Kit中的  
[Context.cacheDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/cache  
* /data/storage/el2/base/haps/entry/cache/example  
* 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。

4.从API version 21开始，还包括了应用临时目录及其子目录（应用临时目录通过Ability Kit中的  
[Context.tempDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：

* /data/storage/el2/base/temp  
* /data/storage/el2/base/haps/entry/temp/example

当路径列表中有其中一个路径不满足以上条件之一，则会抛出异常码401，并且设置路径列表失败。当设置的路径列表为空，则file协议可访问范围以  
[fileAccess](../../../reference/apis-arkweb/arkts-basic-components-web-attributes.md#fileaccess)的行为为准。

**起始版本：** 12

<!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void--><!--Device-WebviewController-setPathAllowingUniversalAccess(pathList: Array<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setPrintBackground

```TypeScript
setPrintBackground(enable: boolean): void
```

Set whether print web page background.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setPrintBackground(enable: boolean): void--><!--Device-WebviewController-setPrintBackground(enable: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setRenderProcessMode

```TypeScript
static setRenderProcessMode(mode: RenderProcessMode): void
```

Set render process mode of the ArkWeb.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void--><!--Device-WebviewController-static setRenderProcessMode(mode: RenderProcessMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setScrollable

```TypeScript
setScrollable(enable: boolean, type?: ScrollType): void
```

设置网页是否允许滚动。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void--><!--Device-WebviewController-setScrollable(enable: boolean, type?: ScrollType): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| type | [ScrollType](arkts-arkweb-webview-scrolltype-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setScrollbarMode

```TypeScript
static setScrollbarMode(scrollbarMode: ScrollbarMode): void
```

在Web页面场景，设置全局滚动条模式。不显式调用时，默认为  
[ScrollbarMode.OVERLAY_LAYOUT_SCROLLBAR](arkts-arkweb-webview-scrollbarmode-e.md#ScrollbarMode)（非常驻滚动条）。

> **说明：**
> 
> - 根据滚动条模式，改变当前应用所有web滚动条模式为常驻滚动条或非常驻滚动条。
> 
> - 若[forceDisplayScrollBar](@ohos.web.WebAttribute#forcedisplayscrollbar)
> 接口与当前接口同时设置，forceDisplayScrollBar接口设置不生效。
> 
> - 该接口需要在WebViewController绑定Web组件之前调用。

**起始版本：** 23

<!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void--><!--Device-WebviewController-static setScrollbarMode(scrollbarMode: ScrollbarMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollbarMode | [ScrollbarMode](arkts-arkweb-webview-scrollbarmode-e.md) | 是 |

## setServiceWorkerWebSchemeHandler

```TypeScript
static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Set web scheme handler for specific scheme. This is used for service worker.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scheme | string | 是 |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setSiteIsolationMode

```TypeScript
static setSiteIsolationMode(mode: SiteIsolationMode): void
```

Set the site isolation mode.

**起始版本：** 21

<!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void--><!--Device-WebviewController-static setSiteIsolationMode(mode: SiteIsolationMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setSocketIdleTimeout

```TypeScript
static setSocketIdleTimeout(timeout: number): void
```

设置ArkWeb中已使用过的空闲socket的超时时间。

**起始版本：** 21

<!--Device-WebviewController-static setSocketIdleTimeout(timeout: number): void--><!--Device-WebviewController-static setSocketIdleTimeout(timeout: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

## setSoftKeyboardBehaviorMode

```TypeScript
setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void
```

Set the WebSoftKeyboardBehaviorMode to decide whether the keyboard will be shown/hidden automatically in particular situation, for example, when web is inactive or active.

**起始版本：** 22

<!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void--><!--Device-WebviewController-setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](arkts-arkweb-webview-websoftkeyboardbehaviormode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string): void
```

Set the URL trust list for the ArkWeb.When the URL trust list has been set, only the URLs in the list can be accessed.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| urlTrustList | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void
```

Sets the URL trust list for the ArkWeb.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;When the URL trust list is set, only the URLs in the list can be accessed.

Example of the urlTrustList:

{ "UrlPermissionList": [ { "scheme": "https", "host": "www.example1.com", "port": 443, "path": "pathA/pathB" }, { "scheme": "http", "host": "*.example2.com", "port": 80, "path": "test1/test2/test3" } ]}&lt;/p&gt;

**起始版本：** 24

<!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void--><!--Device-WebviewController-setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| urlTrustList | string | 是 |
| allowOpaqueOrigin | boolean | 是 |
| supportWildcard | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setUserAgentClientHintsEnabled

```TypeScript
static setUserAgentClientHintsEnabled(enabled: boolean): void
```

Enable the UserAgent Client Hints.

**起始版本：** 24

<!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void--><!--Device-WebviewController-static setUserAgentClientHintsEnabled(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## setUserAgentForHosts

```TypeScript
static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void
```

设置用于指定主机的User-Agent，最多支持20,000个主机。

为同一个 User-Agent 多次设置相同的 Host 列表，将会覆盖之前的设置。也就是说，如果您希望取消某些Host使用指定的User-Agent，您需要重新为该 User-Agent 设置 Host 列表。

**起始版本：** 20

<!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void--><!--Device-WebviewController-static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |
| hosts | Array & lt;string & gt; | 是 |

## setUserAgentMetadata

```TypeScript
setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void
```

Sets the User-Agent metadata corresponding to the User-Agent.

&lt;p&gt;&lt;strong&gt;API Note&lt;/strong&gt;:&lt;br&gt;This User-Agent metadata will be used to populate the User-Agent client hints, They can provide the client's branding and version information, the underlying operating system's branding and major version, as well as details about the underlying device.

**起始版本：** 24

<!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void--><!--Device-WebviewController-setUserAgentMetadata(userAgent: string, metaData: UserAgentMetadata): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |
| metaData | [UserAgentMetadata](arkts-arkweb-webview-useragentmetadata-c.md) | 是 |

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean): void
```

设置是否启用网页调试功能。默认情况下，网页调试功能是关闭的。详情请参考DevTools工具。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患因此，建议在应用正式发布版本时，不要开启此功能。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webDebuggingAccess | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void
```

设置是否启用无线网页调试功能，默认不开启。

当没有指定端口port时，该接口等同于  
[setWebDebuggingAccess](webview.WebviewController.static setWebDebuggingAccess(webDebuggingAccess: boolean))接口，ArkWeb会启动一个本地domain socket监听。当指定了端口port时，ArkWeb会启动一个tcp socket监听。这时可以无线调试网页。

由于小于1024的端口号作为熟知或系统端口，在操作系统上需要特权才能开启，因此port的取值必须大于1024，否则该接口会抛出异常。

安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**起始版本：** 20

<!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void--><!--Device-WebviewController-static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webDebuggingAccess | boolean | 是 |
| port | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100023](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100023-使用了不被允许的端口号) |

## setWebDestroyMode

```TypeScript
static setWebDestroyMode(mode: WebDestroyMode): void
```

设置web组件的销毁模式

**起始版本：** 20

<!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void--><!--Device-WebviewController-static setWebDestroyMode(mode: WebDestroyMode): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebDestroyMode](arkts-arkweb-webview-webdestroymode-e.md) | 是 |

## setWebSchemeHandler

```TypeScript
setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

Set web scheme handler for specific scheme. This is only used for related web component.

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void--><!--Device-WebviewController-setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scheme | string | 是 |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## slideScroll

```TypeScript
slideScroll(vx: number, vy: number): void
```

按照指定速度模拟对页面的轻扫滚动动作。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-slideScroll(vx: number, vy: number): void--><!--Device-WebviewController-slideScroll(vx: number, vy: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vx | number | 是 |
| vy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## startCamera

```TypeScript
startCamera(): void
```

开启当前网页摄像头捕获。使用摄像头功能前请在module.json5中添加权限: ohos.permission.CAMERA，具体权限的添加方法请参考  
[在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-startCamera(): void--><!--Device-WebviewController-startCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## startDownload

```TypeScript
startDownload(url: string): void
```

使用Web组件的下载能力来下载指定的URL，比如下载网页中指定的图片。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-startDownload(url: string): void--><!--Device-WebviewController-startDownload(url: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## stop

```TypeScript
stop(): void
```

停止页面加载。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-stop(): void--><!--Device-WebviewController-stop(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopAllMedia

```TypeScript
stopAllMedia(): void
```

控制网页所有音视频停止。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-stopAllMedia(): void--><!--Device-WebviewController-stopAllMedia(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopCamera

```TypeScript
stopCamera(): void
```

停止当前网页摄像头捕获。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-stopCamera(): void--><!--Device-WebviewController-stopCamera(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopMicrophone

```TypeScript
stopMicrophone(): void
```

停止当前网页麦克风捕获。

**起始版本：** 23

<!--Device-WebviewController-stopMicrophone(): void--><!--Device-WebviewController-stopMicrophone(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean): Promise<string>
```

以Promise方式异步保存当前页面。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| baseName | string | 是 |
| autoName | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void
```

以回调方式异步保存当前页面。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void--><!--Device-WebviewController-storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| baseName | string | 是 |
| autoName | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## terminateRenderProcess

```TypeScript
terminateRenderProcess(): boolean
```

Destroy the rendering process.Calling this interface will actively destroy the associated rendering process.If the rendering process has not been started or destroyed, it has no effect.In addition, destroying the rendering process will also affect all other instances associated with the rendering process.

**起始版本：** 12

<!--Device-WebviewController-terminateRenderProcess(): boolean--><!--Device-WebviewController-terminateRenderProcess(): boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## trimMemoryByPressureLevel

```TypeScript
static trimMemoryByPressureLevel(level: PressureLevel): void
```

根据指定的内存压力等级，主动清理Web组件占用的缓存。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void--><!--Device-WebviewController-static trimMemoryByPressureLevel(level: PressureLevel): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [PressureLevel](arkts-arkweb-webview-pressurelevel-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## waitForAttached

```TypeScript
waitForAttached(timeout: number): Promise<ControllerAttachState>
```

Wait for the controller to attach a web component until timeout.

**起始版本：** 20

<!--Device-WebviewController-waitForAttached(timeout: number): Promise<ControllerAttachState>--><!--Device-WebviewController-waitForAttached(timeout: number): Promise<ControllerAttachState>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; |

## warmupServiceWorker

```TypeScript
static warmupServiceWorker(url: string): void
```

预热ServiceWorker，以提升首屏页面的加载速度（仅限于会使用ServiceWorker的页面）。在加载URL之前调用此API。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-static warmupServiceWorker(url: string): void--><!--Device-WebviewController-static warmupServiceWorker(url: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100002-url格式错误) |

## webPageSnapshot

```TypeScript
webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void
```

获取网页全量绘制结果。

> **说明：**
> 
> 此接口不支持并发调用。
> 
> 仅支持对渲染进程上的资源进行截图：静态图片和文本。
> 
> 如果页面有视频则截图时会显示该视频的占位图片，没有占位图片则显示空白。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void--><!--Device-WebviewController-webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [SnapshotInfo](arkts-arkweb-webview-snapshotinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SnapshotResult](arkts-arkweb-webview-snapshotresult-i.md)&gt; | 是 |

## zoom

```TypeScript
zoom(factor: number): void
```

调整当前网页的缩放比例，[zoomAccess](@ohos.web.WebAttribute#zoomAccess)需为true.

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-zoom(factor: number): void--><!--Device-WebviewController-zoom(factor: number): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## zoomIn

```TypeScript
zoomIn(): void
```

调用此接口将当前网页进行放大，比例为25%。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-zoomIn(): void--><!--Device-WebviewController-zoomIn(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## zoomOut

```TypeScript
zoomOut(): void
```

调用此接口将当前网页进行缩小，比例为20%。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebviewController-zoomOut(): void--><!--Device-WebviewController-zoomOut(): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100004-功能开关未打开) |
| [17100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
