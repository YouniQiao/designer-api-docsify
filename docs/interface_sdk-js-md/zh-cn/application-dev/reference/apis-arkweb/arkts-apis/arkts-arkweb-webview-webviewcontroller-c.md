# WebviewController

WebviewController是Web组件各种行为的核心控制器，提供网页加载与导航控制、JavaScript交互、生命周期、滚动控制、页面缩放与内容查找、消息端口通信、缓存与证书管理等广泛功能。一个 WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，才能调用WebviewController上的方法（静态方法除外）。

**起始版本：** 9

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

当前页面是否可后退，即当前页面是否有返回历史记录。可以结合使用[getBackForwardEntries](#getbackforwardentries)来获取当前WebView的历史信息列表，以及使用 [accessStep](#accessstep)来判断是否可以按照给定的步数前进或后退。

> **说明：**&gt;
> 在Web组件首次加载过程中调用[setCustomUserAgent](#setcustomuseragent)，可能会导致在当前存在多个历史节点的情况下，获取
> 的accessBackward实际为false，即没有后退节点。建议先调用setCustomUserAgent方法设置UserAgent，再通过loadUrl加载具体页面。&gt;
> 该现象是由于在Web组件首次加载时，调用[setCustomUserAgent](#setcustomuseragent)会导致组件重新加载并保持初始历史节点的
> 状态。随后新增的节点将替换初始历史节点，不会生成新的历史节点，导致accessBackward为false。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessForward

```TypeScript
accessForward(): boolean
```

当前页面是否可前进，即当前页面是否有前进历史记录。可以结合使用[getBackForwardEntries](#getbackforwardentries)来获取当前WebView的历史信息列表，以及使用 [accessStep](#accessstep)来判断是否可以按照给定的步数前进或后退。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

当前页面是否可前进或者后退给定的step步。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## addIntelligentTrackingPreventionBypassingList

```TypeScript
static addIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

添加智能防跟踪功能绕过的域名列表。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## avoidVisibleViewportBottom

```TypeScript
avoidVisibleViewportBottom(avoidHeight: number): void
```

设置Web网页可视视口底部避让高度。

> **说明：**&gt;
> - avoidHeight有效值区间为[0, Web组件高度]，超出有效值区间时取边界值。&gt;
> - 该接口高度设置为非0时，Web组件位置和尺寸不变，可视视口向上避让avoidHeight，表现为Web网页内容抬升avoidHeight。该接口一般用于应用自定义网页底部避让区，不建议和点击web网页可编辑区拉起键盘的
> 场景同时使用。同时使用时，键盘弹起避让模式将使用OVERLAYS_CONTENT。&gt;
> - 该接口高度设置为0时，Web网页内容可恢复，键盘弹起避让模式将使用keyboardAvoidMode()声明的模式。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| avoidHeight | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## backOrForward

```TypeScript
backOrForward(step: number): void
```

按照历史栈，前进或者后退指定步长的页面，当历史栈中不存在对应步长的页面时，不会进行页面跳转。前进或者后退页面时，直接使用已加载过的网页，无需重新加载网页。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| step | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## backward

```TypeScript
backward(): void
```

按照历史栈，后退一个页面。一般结合[accessBackward](#accessbackward)一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearBlanklessLoadingCache

```TypeScript
static clearBlanklessLoadingCache(keys?: Array<string>) : void
```

清除指定key值页面无白屏优化缓存，本接口只清除缓存。在小程序或Web应用场景中，当页面加载时内容变化显著，可能会出现一次明显的跳变。若对此跳变有所顾虑，可使用该接口清除页面缓存。

> **说明：**&gt;
> - 清除之后的页面，需在第三次加载页面时才会产生优化效果。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keys | Array & lt;string & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## clearClientAuthenticationCache

```TypeScript
clearClientAuthenticationCache(): void
```

清除Web组件记录的客户端证书请求事件对应的用户操作行为。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearHistory

```TypeScript
clearHistory(): void
```

删除所有前进后退记录，不建议在onErrorReceive与onPageBegin中调用clearHistory，会造成异常退出。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearHostIP

```TypeScript
static clearHostIP(hostName: string): void
```

清除指定主机域名解析后的IP地址。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostName | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## clearIntelligentTrackingPreventionBypassingList

```TypeScript
static clearIntelligentTrackingPreventionBypassingList(): void
```

删除通过addIntelligentTrackingPreventionBypassingList接口添加的所有域名。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## clearMatches

```TypeScript
clearMatches(): void
```

清除所有通过[searchAllAsync](#searchallasync)匹配到的高亮字符查找结果。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearPrefetchedResource

```TypeScript
static clearPrefetchedResource(cacheKeyList: Array<string>): void
```

根据指定的缓存key列表清除对应的预获取资源缓存。入参中的缓存key必须是[prefetchResource](#prefetchresource)指定预获取到的资 源缓存key。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cacheKeyList | Array & lt;string & gt; | 是 |

## clearServiceWorkerWebSchemeHandler

```TypeScript
static clearServiceWorkerWebSchemeHandler(): void
```

清除应用中设置的所有用于拦截ServiceWorker的WebSchemeHandler。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## clearSslCache

```TypeScript
clearSslCache(): void
```

清除Web组件记录的SSL证书错误事件对应的用户操作行为。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## clearWebSchemeHandler

```TypeScript
clearWebSchemeHandler(): void
```

清除Web组件设置的所有WebSchemeHandler。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## closeAllMediaPresentations

```TypeScript
closeAllMediaPresentations(): void
```

控制网页所有全屏视频关闭。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## closeCamera

```TypeScript
closeCamera(): void
```

关闭当前网页摄像头捕获。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## constructor

```TypeScript
constructor(webTag?: string)
```

用于创建 WebviewController 对象的构造函数。

> **说明：**&gt;
> 不传参：new webview.WebviewController()表示构造函数为空，不使用C API时不需要传参。&gt;
> 传参且参数是合法字符串：new webview.WebviewController("xxx")，用于开发者区分多实例，并调用对应实例下的方法。&gt;
> 传入参数为空：new webview.WebviewController("")或new webview.WebviewController(undefined)，该场景下参数无意义，无法区分多个实例，直接返回
> undefined，需要开发者判断返回值是否正常。&gt;
> Web组件销毁后会解绑WebViewController，之后调用WebviewController的非静态方法会抛出
> [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联)异常，应注意调
> 用时机和捕获异常，防止进程异常退出。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webTag | string | 否 |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void
```

异步callback方式获取指定网页的数据流。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configuration | [PdfConfiguration](arkts-arkweb-webview-pdfconfiguration-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PdfData](arkts-arkweb-webview-pdfdata-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## createPdf

```TypeScript
createPdf(configuration: PdfConfiguration): Promise<PdfData>
```

以Promise方式异步获取指定网页的数据流。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## createWebMessagePorts

```TypeScript
createWebMessagePorts(isExtentionType?: boolean): Array<WebMessagePort>
```

创建Web消息端口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createWebPrintDocumentAdapter

```TypeScript
createWebPrintDocumentAdapter(jobName: string): print.PrintDocumentAdapter
```

创建web相关打印功能。

**起始版本：** 11

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [jobName](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-print-printjobdata-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| print.PrintDocumentAdapter |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>): void
```

对Web内核赋予自定义协议URL的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议URL时，该fetch请求可被 [onInterceptRequest](../arkts-components/arkts-arkweb-web-attribute.md#oninterceptrequest)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100020](../errorcode-webview.md#17100020-注册自定义协议失败) |

## customizeSchemes

```TypeScript
static customizeSchemes(schemes: Array<WebCustomScheme>, lazyInitWebEngine: boolean): void
```

对Web内核赋予自定义协议URL的跨域请求与fetch请求的权限。当Web在跨域fetch自定义协议URL时，该fetch请求可被 [onInterceptRequest](../arkts-components/arkts-arkweb-web-attribute.md#oninterceptrequest)事件接口所拦截，从而开发者可以进一步处理该请求。建议在任何Web组件初始化之前调用该接口。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| schemes | Array&lt;[WebCustomScheme](arkts-arkweb-webview-webcustomscheme-i.md)&gt; | 是 |
| lazyInitWebEngine | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100020](../errorcode-webview.md#17100020-注册自定义协议失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## deleteJavaScriptRegister

```TypeScript
deleteJavaScriptRegister(name: string): void
```

删除通过[registerJavaScriptProxy](#registerjavascriptproxy)或者 [javaScriptProxy](../arkts-components/arkts-arkweb-web-attribute.md#javascriptproxy)注册到window上的指定name的应用侧JavaScript对象。删除操作在页面下次（重新）加载后生效。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100008](../errorcode-webview.md#17100008-删除不存在的javascriptproxy) |

## enableAdsBlock

```TypeScript
enableAdsBlock(enable: boolean): void
```

启用广告过滤功能。

> **说明：**&gt;
> - 广告过滤功能需要release包，使用debug包不生效。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## enableAdvancedSecurityMode

```TypeScript
static enableAdvancedSecurityMode(securityParams: SecurityParams): void
```

通过配置安全特性选项禁用特定的Web引擎能力，以降低攻击面。典型使用场景包括：高安全要求的应用（如金融、政务类应用）应启用高级安全模式以禁用不必要的Web引擎能力。

> **说明：**&gt;
> - 该接口为全局静态API，在整个APP生命周期中调用一次即可，不需要重复调用。&gt;
> - 必须在[initializeWebEngine()](#initializewebengine)之前调用，否则设置无效。
> 26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| securityParams | [SecurityParams](arkts-arkweb-webview-securityparams-i.md) | 是 |

## enableBackForwardCache

```TypeScript
static enableBackForwardCache(features: BackForwardCacheSupportedFeatures): void
```

开启Web组件前进后退缓存功能，通过参数指定是否允许使用特定的页面进入前进后退缓存。需要在[initializeWebEngine()](#initializewebengine)初始化内核之前调用。

**起始版本：** 12

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

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## enablePrivateNetworkAccess

```TypeScript
static enablePrivateNetworkAccess(enable: boolean): void
```

设置私有网络访问检查功能（Private Network Access）的启用状态。启用后，Web组件将对私有网络请求（如访问本地服务器或内网资源）进行CORS预检。它会先发送OPTIONS预检请求，获取目标服务器的显式授权，然后传输实际数据。禁用此功能将跳过安全检查。

> **说明：**&gt;
> 当前私有网络访问检查功能主要针对Web Worker场景生效。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## enableSafeBrowsing

```TypeScript
enableSafeBrowsing(enable: boolean): void
```

启用检查网站安全风险的功能，非法和欺诈网站是强制启用的，不能通过此功能禁用。本功能默认不生效，OpenHarmony只提供恶意网址拦截页WebUI，网址风险检测以及显示WebUI的功能由Vendor实现。推荐在WebContentsObserver中监听跳转 [DidStartNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) 、 [DidRedirectNavigation](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/content/public/browser/web_contents_observer.h) 进行检测。

> **说明：**&gt;
> 该接口不生效，调用不会产生任何实际效果。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## enableWholeWebPageDrawing

```TypeScript
static enableWholeWebPageDrawing(): void
```

设置开启网页全量绘制能力。仅在web初始化时设置。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## executeAIPageCommand

```TypeScript
executeAIPageCommand(command: string): Promise<string>
```

异步执行`AIPageCommand`。该接口通过JSON字符串形式的`command`参数指定命令类型和命令参数，使用Promise异步回调。

> **说明：**&gt;
> - 不同命令的返回格式不同，详细说明请参见[AIPageCommand](../../../reference/apis-arkweb/arkts-apis-webview-AIPageCommand.md)和
> [AIPageInteraction](../../../reference/apis-arkweb/arkts-apis-webview-AIPageInteraction.md)。&gt;
> - 当命令无法分发或无结果返回时，Promise可能返回空字符串。&gt;
> - 返回值非空时为JSON字符串，应用可通过`JSON.parse`解析后使用。
> 26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| command | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100024](../errorcode-webview.md#17100024-aipagecommand格式错误) |

## forward

```TypeScript
forward(): void
```

按照历史栈，前进一个页面。一般结合[accessForward](#accessforward)一起使用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getActiveWebEngineVersion

```TypeScript
static getActiveWebEngineVersion(): ArkWebEngineVersion
```

获取当前ArkWeb内核版本。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) |

## getAttachState

```TypeScript
getAttachState(): ControllerAttachState
```

查询当前WebViewController是否绑定一个Web组件。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md) |

## getBackForwardEntries

```TypeScript
getBackForwardEntries(): BackForwardList
```

获取当前WebView的历史信息列表。

> **说明：**&gt;
> onLoadIntercept在加载开始的时候触发，该时刻还未生成历史节点，所以在onLoadIntercept中调用
> getBackForwardEntries拿到的历史栈不包括当前正在加载中的跳转。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [BackForwardList](arkts-arkweb-webview-backforwardlist-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getBlanklessInfoWithKey

```TypeScript
getBlanklessInfoWithKey(key: string) : BlanklessInfo
```

获取页面首屏加载预测信息（详细说明见[BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md)），并开始本次加载过渡帧生成，应用根据此信息确定是否需要启用无白屏加载。 必须与[setBlanklessLoadingWithKey](#setblanklessloadingwithkey)接口配套使用，并且必须在触发加载页面的接口之前或在`onLoadIntercept`中调用。 需在`WebViewController`与Web组件绑定后才能使用。

> **说明：**&gt;
> - 持久缓存容量：默认大小为30MB（约30页），可以通过接口[setBlanklessLoadingCacheCapacity](#setblanklessloadingcachecapacity)设置缓存容量，具体见该接口说明。
> 超过容量时根据LRU（Least Recently Used，淘汰不常用缓存的策略）机制更新缓存。自动清理超过7天的持久缓存数据，缓存清除后第三次加载页面开始有优化效果。&gt;
> - 如果发现快照相似度（即[BlanklessInfo](arkts-arkweb-webview-blanklessinfo-i.md)极低，请确认key值是否传递正确。&gt;
> - 调用本接口后，将启用页面加载快照检测及生成过渡帧计算，会产生一定的资源开销。&gt;
> - 启用无白屏加载的页面会带来一定的资源开销，开销的大小与Web组件的分辨率相关。假设分辨率的宽度和高度分别为：w, h。页面在打开阶段会增加峰值内存，增加约12 * w * h B，页面打开后内存回收，不影响稳态内存。
> 增加固态应用缓存的大小，每个页面增加的缓存约w * h / 10 B，缓存位于应用缓存的位置。&gt;
> - 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，
> 具体权限的添加方法请参考[在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 20

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getCertificate

```TypeScript
getCertificate(): Promise<Array<cert.X509Cert>>
```

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过Promise异步返回当前网站的X509格式证书（X509Cert证书类型定义见 [X509Cert](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-x509cert-i.md)定义），便于开发者展示网站证书信息。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;cert.X509Cert & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getCertificate

```TypeScript
getCertificate(callback: AsyncCallback<Array<cert.X509Cert>>): void
```

获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会通过AsyncCallback异步返回当前网站的X509格式证书（X509Cert证书类型定义见 [X509Cert](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-x509cert-i.md)），便于开发者展示网站证书信息。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;cert.X509Cert&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

获取自定义用户代理。默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getDefaultUserAgent

```TypeScript
static getDefaultUserAgent(): string
```

获取默认用户代理。此接口只允许在UI线程调用。默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)

**起始版本：** 14

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getErrorPageEnabled

```TypeScript
getErrorPageEnabled(): boolean
```

查询是否启用了默认错误页功能。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getFavicon

```TypeScript
getFavicon(): image.PixelMap
```

获取页面的favicon图标。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getHitTest

```TypeScript
getHitTest(): WebHitTestType
```

获取当前被点击区域的元素类型。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getLastHitTest](#getlasthittest)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [WebHitTestType](arkts-arkweb-webview-webhittesttype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getHitTestValue

```TypeScript
getHitTestValue(): HitTestValue
```

获取当前被点击区域的元素信息。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [getLastHitTest](#getlasthittest)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getLastHitTest

```TypeScript
getLastHitTest(): HitTestValue
```

获取上一次被点击区域的元素信息。

**起始版本：** 18

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [HitTestValue](arkts-arkweb-webview-hittestvalue-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getLastJavascriptProxyCallingFrameUrl

```TypeScript
getLastJavascriptProxyCallingFrameUrl(): string
```

通过[registerJavaScriptProxy](#registerjavascriptproxy)或者 [javaScriptProxy](../arkts-components/arkts-arkweb-web-attribute.md#javascriptproxy)注入JavaScript对象到window对象中。该接口可以获取最后一次调用注入的对象的frame的URL。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getMediaPlaybackState

```TypeScript
getMediaPlaybackState(): MediaPlaybackState
```

查询当前网页音视频播放状态。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [MediaPlaybackState](arkts-arkweb-webview-mediaplaybackstate-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getOriginalUrl

```TypeScript
getOriginalUrl(): string
```

获取当前页面的原始URL地址。风险提示：如果想获取URL来做JavascriptProxy通信接口认证，请使用 [getLastJavascriptProxyCallingFrameUrl&lt;sup&gt;12+&lt;/sup&gt;](#getlastjavascriptproxycallingframeurl)

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getPageHeight

```TypeScript
getPageHeight(): number
```

获取当前网页的页面高度。具体使用详情请参考[获取网页内容高度](../../../web/web-getpage-height.md)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getPageOffset

```TypeScript
getPageOffset(): ScrollOffset
```

获取网页当前的滚动偏移量（不包含过滚动偏移量）。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ScrollOffset](arkts-arkweb-webview-scrolloffset-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getPrintBackground

```TypeScript
getPrintBackground(): boolean
```

查询webview是否打印网页背景。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getProgress

```TypeScript
getProgress() : number
```

获取当前网页加载进度。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## getRenderProcessMode

```TypeScript
static getRenderProcessMode(): RenderProcessMode
```

查询ArkWeb的渲染子进程模式。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) |

## getScrollable

```TypeScript
getScrollable(): boolean
```

获取当前网页是否允许滚动。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getScrollOffset

```TypeScript
getScrollOffset(): ScrollOffset
```

获取网页当前的滚动偏移量（包含过滚动偏移量）。

**起始版本：** 13

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ScrollOffset](arkts-arkweb-webview-scrolloffset-i.md) |

## getSecurityLevel

```TypeScript
getSecurityLevel(): SecurityLevel
```

获取当前网页的安全级别。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [SecurityLevel](../../apis-arkdata/arkts-apis/arkts-arkdata-distributedkvstore-securitylevel-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getSiteIsolationMode

```TypeScript
static getSiteIsolationMode(): SiteIsolationMode
```

查询当前生效的站点隔离模式。

**起始版本：** 21

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) |

## getSubframeErrorPageEnabled

```TypeScript
getSubframeErrorPageEnabled(): boolean
```

查询是否启用了subframe错误页功能。
26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getSurfaceId

```TypeScript
getSurfaceId(): string
```

获取ArkWeb对应Surface的ID，此ID可用于网页截图。

> **说明：**&gt;
> 仅Web组件渲染模式是ASYNC_RENDER时有效。getSurfaceId需要在Web组件初始化之后才能获取到值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUrl

```TypeScript
getUrl(): string
```

获取当前页面的URL地址。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUserAgent

```TypeScript
getUserAgent(): string
```

获取当前默认用户代理。默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUserAgentClientHintsEnabled

```TypeScript
static getUserAgentClientHintsEnabled(): boolean
```

查询User-Agent Client Hints功能当前是否开启。

**起始版本：** 24

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## getUserAgentMetadata

```TypeScript
getUserAgentMetadata(userAgent: string): UserAgentMetadata
```

查询userAgent对应的UserAgent Metadata信息。

**起始版本：** 24

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

获取Web组件的索引值，用于多个Web组件的管理。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## hasImage

```TypeScript
hasImage(): Promise<boolean>
```

通过Promise方式异步查找当前页面是否存在图像。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## hasImage

```TypeScript
hasImage(callback: AsyncCallback<boolean>): void
```

通过Callback方式异步查找当前页面是否存在图像。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## initializeWebEngine

```TypeScript
static initializeWebEngine(): void
```

在Web组件初始化之前，通过此接口加载Web引擎的动态库文件，以提高启动性能。自动预连接历史访问过的高频网站。

> **说明：**&gt;
> - initializeWebEngine不支持在异步线程中调用，否则会造成崩溃。&gt;
> - initializeWebEngine全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## injectOfflineResources

```TypeScript
injectOfflineResources(resourceMaps: Array<OfflineResourceMap>): void
```

将本地离线资源注入到内存缓存中，以提升页面首次启动速度。内存缓存中的资源由内核自动管理，当注入的资源过多导致内存压力过大，内核自动释放未使用的资源，应避免注入大量资源到内存缓存中。正常情况下，资源的有效期由提供的Cache-Control或Expires响应头控制其有效期，默认的有效期为86400秒，即1天。资源的MIMEType通过提供的Content-Type响应头配置，Content-Type需符合标准，否则无法正常使用，MODULE_JS必须提供有效的MIMEType，其他类型可不提供。以此方式注入的资源，仅支持通过HTML中的标签加载。如果业务网页中的script标签使用了crossorigin属性，则必须在接口的responseHeaders参数中设置Cross-Origin响应头的值为anonymous 或use-credentials。当调用`webview.WebviewController.SetRenderProcessMode(webview.RenderProcessMode.MULTIPLE)`接口后，应用会启动多渲染进程模式，此接口在此场景下不 会生效。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| resourceMaps | Array&lt;[OfflineResourceMap](arkts-arkweb-webview-offlineresourcemap-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## isActiveWebEngineEvergreen

```TypeScript
static isActiveWebEngineEvergreen(): boolean
```

判断当前系统是否正在使用常青内核，即系统的最新内核。

**起始版本：** 23

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

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isAdsBlockEnabledForCurPage

```TypeScript
isAdsBlockEnabledForCurPage(): boolean
```

查询当前网页是否开启广告过滤功能。当Web组件使能广告过滤功能后，默认所有页面都是开启广告过滤的，支持通过 [addAdsBlockDisallowedList](arkts-arkweb-webview-adsblockmanager-c.md#addadsblockdisallowedlist)指定域名禁用广告过滤。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isAutoPreconnectEnabled

```TypeScript
static isAutoPreconnectEnabled(): boolean
```

查询Web内核的自动预连接状态。如果没有使用[setAutoPreconnect](#setautopreconnect)设置Web内核自动预连接的状态，则默认启用自动预连接，返回true。

**起始版本：** 21

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

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## isIntelligentTrackingPreventionEnabled

```TypeScript
isIntelligentTrackingPreventionEnabled(): boolean
```

获取Web组件是否启用了智能防跟踪功能。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## isPrivateNetworkAccessEnabled

```TypeScript
static isPrivateNetworkAccessEnabled(): boolean
```

获取Web组件是否启用了私有网络访问检查功能。

> **说明：**&gt;
> 当前私有网络访问检查功能主要针对Web Worker场景生效。

**起始版本：** 20

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

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## loadData

```TypeScript
loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void
```

加载指定的数据。baseUrl与historyUrl同时为空的情况下：encoding如果为非base64（包括空值），则假定数据对安全URL字符范围内的八位字节使用ASCII编码，对该范围外的八位字节使用URL的标准%xx十六进制编码。data数据必须使用base64编码或将内容中的任何#字符编码为%23。否则#将被视为内容的结尾而剩余的文本将被用作文档片段标识符。

> **说明：**&gt;
> - 若加载本地图片，可以给baseUrl或historyUrl任一参数赋值空格，详情请参考示例代码。&gt;
> - 加载本地图片场景，baseUrl和historyUrl不能同时为空，否则图片无法成功加载。&gt;
> - 若html中的富文本中带有注入#等特殊字符，建议将baseUrl和historyUrl两个参数的值设置为"空格"。&gt;
> - 加载文字场景，需主动设置`&lt;meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8"&gt;`避免文本字体大小不
> 一致。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

加载指定的URL。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| headers | Array & lt;WebHeader & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |
| [17100003](../errorcode-webview.md#17100003-resource路径错误) |

## off('controllerAttachStateChange')

```TypeScript
off(type: 'controllerAttachStateChange', callback?: Callback<ControllerAttachState>): void
```

取消WebViewController绑定状态事件的注册，取消后将不再接收Callback通知。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 否 |

## on('controllerAttachStateChange')

```TypeScript
on(type: 'controllerAttachStateChange', callback: Callback<ControllerAttachState>): void
```

注册WebViewController绑定状态事件，通过Callback方式获取WebViewController绑定状态的变化通知。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'controllerAttachStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)&gt; | 是 |

## onActive

```TypeScript
onActive(): void
```

调用此接口通知Web组件进入前台激活状态。激活状态是应用与用户互动的状态。应用会保持这种状态，直到发生某些事件（例如收到来电或设备屏幕关闭）时将焦点从应用移开。若页面此前处于未激活状态，H5页面中通过document.addEventListener('visibilitychange',...)注册的事件监听器将被触发，document.visibilityState 从"hidden"变为"visible"。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## onCreateNativeMediaPlayer

```TypeScript
onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback): void
```

注册回调函数，使用[enableNativeMediaPlayer](../arkts-components/arkts-arkweb-web-attribute.md#enablenativemediaplayer)开启应用接管网页媒体播放功能后，当网页中有播放媒体时，触发注册的回调函 数。如果应用接管网页媒体播放功能未开启，则注册的回调函数不会被触发。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md) | 是 |

## onInactive

```TypeScript
onInactive(): void
```

调用此接口通知Web组件进入未激活状态。开发者可以在此回调中实现应用失去焦点时应表现的恰当行为。此状态下会尽可能的暂停任何可以安全暂停的内容，例如动画和地理位置。但不会暂停JavaScript，要全局暂停JavaScript，请使用 [pauseAllTimers](#pausealltimers)。要重新激活Web组件，请调用 [onActive](#onactive)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pageDown

```TypeScript
pageDown(bottom: boolean): void
```

将Webview的内容向下滚动半个视框大小或者跳转到页面最底部，通过bottom入参控制。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bottom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pageUp

```TypeScript
pageUp(top: boolean): void
```

将Webview的内容向上滚动半个视框大小或者跳转到页面最顶部，通过top入参控制。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| top | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseAllMedia

```TypeScript
pauseAllMedia(): void
```

控制网页所有音视频暂停。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseAllTimers

```TypeScript
static pauseAllTimers(): void
```

暂停所有WebView的定时器，定时器暂停期间，网页中的setInterval、setTimeout等定时操作将被挂起。建议在应用进入后台等场景暂停，前台时恢复，以节省资源，可以与 [resumeAllTimers](#resumealltimers)()成对使用，避免定时器状态混乱。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## pauseMicrophone

```TypeScript
pauseMicrophone(): void
```

暂停当前网页麦克风捕获。

> **说明：**&gt;
> 与 resumeMicrophone 和 stopMicrophone 的区别：&gt;
> pauseMicrophone 仅暂停麦克风捕获，可通过 resumeMicrophone 恢复；stopMicrophone 会停止捕获并释放资源。

**起始版本：** 23

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## postMessage

```TypeScript
postMessage(name: string, ports: Array<WebMessagePort>, uri: string): void
```

发送Web消息端口到HTML。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## postUrl

```TypeScript
postUrl(url: string, postData: ArrayBuffer): void
```

使用"POST"方法加载带有postData的URL。如果URL不是网络URL，则会使用[loadUrl](#loadurl)方法加载URL，忽略postData参 数。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| postData | ArrayBuffer | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## precompileJavaScript

```TypeScript
precompileJavaScript(url: string, script: string | Uint8Array, cacheOptions: CacheOptions): Promise<number>
```

预编译JavaScript生成字节码缓存或根据提供的参数更新已有的字节码缓存。接口通过提供的文件信息、E-Tag响应头和Last-Modified响应头判断是否需要更新已有的字节码缓存。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>): void
```

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

> **说明：**&gt;
> - 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。&gt;
> - prefetchPage对302重定向页面同样正常预取。&gt;
> - 先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。&gt;
> - 连续prefetchPage多个URL只有第一个生效。&gt;
> - prefetchPage有时间限制，500ms内不能多次预取。&gt;
> - prefetchPage会缓存所有资源，但具有Cache-Control: no-store标头的资源除外。如果存在Vary响应标头、Cache-Control: no-store标头，或者下载的页面资源已超过五分钟，
> 则在使用之前会重新验证资源。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| additionalHeaders | Array & lt;WebHeader & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## prefetchPage

```TypeScript
prefetchPage(url: string, additionalHeaders?: Array<WebHeader>, prefetchOptions?: PrefetchOptions): void
```

在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度。

> **说明：**&gt;
> - 下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。&gt;
> - prefetchPage对302重定向页面同样正常预取。&gt;
> - 先执行prefetchPage再加载页面时，已预取的资源将直接从缓存中加载。&gt;
> - prefetchPage会缓存所有资源，但具有Cache-Control: no-store标头的资源除外。如果存在Vary响应标头、Cache-Control: no-store标头，或者下载的页面资源已超过五分钟，
> 则在使用之前会重新验证资源。

**起始版本：** 21

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
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## prefetchResource

```TypeScript
static prefetchResource(request: RequestInfo, additionalHeaders?: Array<WebHeader>, cacheKey?: string,
                            cacheValidTime?: number): void
```

根据指定的请求信息和附加的HTTP请求头去预获取资源请求，存入内存缓存，并指定其缓存key和有效期，以加快加载速度。目前仅支持Content-Type为application/x-www-form-urlencoded的 POST请求。最多可以预获取6个POST请求。如果要预获取第7个，请通过 [clearPrefetchedResource](#clearprefetchedresource)清除不需要的POST请求缓存，否则会自动清除最早预获取的 POST缓存。如果要使用预获取的资源缓存，开发者需要在正式发起的POST请求的请求头中增加键值“ArkWebPostCacheKey”，其内容为对应缓存的cacheKey。内存缓存中的资源由内核自动管理。当注入的资源过多，导致内存压力过大时，内核会自动释放未使用的资源，但仍应避免向内存缓存中注入大量资源。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## prepareForPageLoad

```TypeScript
static prepareForPageLoad(url: string, preconnectable: boolean, numSockets: number): void
```

预连接URL，在加载URL之前调用此API，对URL只进行DNS解析，socket建链操作，并不获取主资源子资源。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [17100002](../errorcode-webview.md#17100002-url格式错误) |
| [17100013](../errorcode-webview.md#17100013-预连接时输入socket数目无效) |

## refresh

```TypeScript
refresh(): void
```

调用此接口通知Web组件刷新网页。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## refresh

```TypeScript
refresh(ignoreCache: boolean): void
```

通知Web组件刷新网页，可以选择是否忽略缓存刷新。

**起始版本：** 24

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ignoreCache | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## registerJavaScriptProxy

```TypeScript
registerJavaScriptProxy(jsObject: object, name: string, methodList: Array<string>,
        asyncMethodList?: Array<string>, permission?: string): void
```

registerJavaScriptProxy提供了应用与Web组件加载的网页之间强大的交互能力。注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。示例请参考[前端页面调用应用侧函数](../../../web/web-in-page-app-function-invoking.md)。

> **说明：**&gt;
> - registerJavaScriptProxy需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏。&gt;
> - 请尽可能只在可信的URL及安全通信HTTPS场景下进行registerJavaScriptProxy注册。在非可信的Web组件中注入JavaScript对象，可能会导致应用被恶意攻击。&gt;
> - 在注册registerJavaScriptProxy后，应用会将JavaScript对象暴露给所有的页面frames。&gt;
> - 同一方法在同步与异步列表中重复注册，将默认异步调用。&gt;
> - 同步函数列表和异步函数列表不可同时为空，否则此次调用接口注册失败。&gt;
> - 异步的作用在于：H5线程将异步JavaScript任务提交给ETS主线程后，无需等待任务执行完成并返回结果，H5线程即可继续执行后续任务。这在执行耗时较长的JavaScript任务或ETS线程较为拥堵的情况下，可以有效
> 减少H5线程因JavaScript任务而被阻塞的情况。然而，异步JavaScript任务无法返回值，且任务执行的顺序无法保证，因此需要根据具体情境判断是否使用同步或异步方式。&gt;
> - 注入的对象在页面下一次（重新）加载前不会出现在JavaScript中。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jsObject | object | 是 |
| name | string | 是 |
| [methodList](../arkts-components/arkts-arkweb-javascriptproxy-i.md) | Array & lt;string & gt; | 是 |
| [asyncMethodList](../arkts-components/arkts-arkweb-javascriptproxy-i.md) | Array & lt;string & gt; | 否 |
| permission | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## removeAllCache

```TypeScript
static removeAllCache(clearRom: boolean): void
```

清除应用内所有Webview(含隐私模式)产生的资源缓存。

> **说明：**&gt;
> 可以通过在data/app/el2/100/base/\&lt;applicationPackageName\&gt;/cache/web/目录下查看Webview的缓存。

**起始版本：** 18

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| clearRom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## removeCache

```TypeScript
removeCache(clearRom: boolean): void
```

清除与当前WebView上下文相关的资源缓存。

> **说明：**&gt;
> 可以通过在data/storage/el2/base/cache/web/Cache目录下查看Webview的缓存。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| clearRom | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## removeIntelligentTrackingPreventionBypassingList

```TypeScript
static removeIntelligentTrackingPreventionBypassingList(hostList: Array<string>): void
```

删除通过addIntelligentTrackingPreventionBypassingList接口添加的部分域名列表。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## requestFocus

```TypeScript
requestFocus(): void
```

使指定组件获取焦点。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## restoreWebState

```TypeScript
restoreWebState(state: Uint8Array) : void
```

当前WebView从序列化数据中恢复页面状态历史记录。如果state过大，可能会导致异常。建议state大于512k时，放弃恢复页面状态历史记录。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | Uint8Array | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeAllMedia

```TypeScript
resumeAllMedia(): void
```

控制网页被pauseAllMedia接口暂停的音视频继续播放。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeAllTimers

```TypeScript
static resumeAllTimers(): void
```

恢复从pauseAllTimers()接口中被暂停的所有的定时器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## resumeMicrophone

```TypeScript
resumeMicrophone(): void
```

恢复当前网页麦克风捕获。使用麦克风功能前请在module.json5中添加权限: ohos.permission.MICROPHONE，具体权限的添加方法请参考 [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 23

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## runJavaScript

```TypeScript
runJavaScript(script: string): Promise<string>
```

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

> **说明：**&gt;
> - 跨导航操作（如loadUrl）时，JavaScript状态 将不再保留，例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。&gt;
> - 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。&gt;
> - 目前不支持传递对象，支持传递结构体。&gt;
> - 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。&gt;
> - 前端页面传到应用侧的string数据类型会被视为JSON格式的数据，需要调用JSON.parse反序列化。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../errorcode-webview.md#17100003-resource路径错误) |

## runJavaScript

```TypeScript
runJavaScript(script: string, callback: AsyncCallback<string>): void
```

在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用 ，并且回调也将在用户界面（UI）线程上调用。

> **说明：**&gt;
> - 跨导航操作（如loadUrl）时，JavaScript状态将不再保留。例如，调用loadUrl前定义的全局变量和函数在加载的页面中将不存在。&gt;
> - 建议应用程序使用registerJavaScriptProxy来确保JavaScript状态能够在页面导航间保持。&gt;
> - 目前不支持传递对象，支持传递结构体。&gt;
> - 执行异步方法无法获取返回值，需要根据具体情境判断是否使用同步或异步方式。&gt;
> - 前端页面传到应用侧的string数据类型会被视为JSON格式的数据，需要调用JSON.parse反序列化。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../errorcode-webview.md#17100003-resource路径错误) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer): Promise<JsMessageExt>
```

异步执行JavaScript脚本，并通过Promise方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中 调用。

> **说明：**&gt;
> - 前端页面传到应用侧的string数据类型会被视为JSON格式的数据，需要调用JSON.parse反序列化。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## runJavaScriptExt

```TypeScript
runJavaScriptExt(script: string | ArrayBuffer, callback: AsyncCallback<JsMessageExt>): void
```

异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。

> **说明：**&gt;
> - 前端页面传到应用侧的string数据类型会被视为JSON格式的数据，需要调用JSON.parse反序列化。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| script | string \| ArrayBuffer | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[JsMessageExt](arkts-arkweb-webview-jsmessageext-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollBy

```TypeScript
scrollBy(deltaX: number, deltaY: number, duration?: number): void
```

在指定时间内将页面滚动指定的偏移量。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollByWithResult

```TypeScript
scrollByWithResult(deltaX: number, deltaY: number): boolean
```

将页面滚动指定的偏移量，返回值表示此次滚动是否执行成功。

**起始版本：** 12

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## scrollTo

```TypeScript
scrollTo(x: number, y: number, duration?: number): void
```

在指定时间内，将页面滚动到指定的绝对位置。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## searchAllAsync

```TypeScript
searchAllAsync(searchString: string): void
```

异步查找网页中所有匹配关键字'searchString'的内容并高亮，结果通过[onSearchResultReceive](../arkts-components/arkts-arkweb-web-attribute.md#onsearchresultreceive)异步返回。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchString | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## searchNext

```TypeScript
searchNext(forward: boolean): void
```

滚动到下一个匹配的查找结果并高亮。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [forward](#forward) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## serializeWebState

```TypeScript
serializeWebState() : Uint8Array
```

将当前WebView的页面状态历史记录信息序列化。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setActiveWebEngineVersion

```TypeScript
static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void
```

设置ArkWeb内核版本。若系统不支持指定版本，则设置无效，使用系统默认内核（可参考[约束与限制](../../../web/web-component-overview.md#约束与限制)）。该接口为全局静态API，须在调 用initializeWebEngine前执行，若已加载任何Web组件，则该设置无效。典型使用场景：使用特定内核版本的特性或兼容性需求时，可切换到对应内核版本。

> **说明：**&gt;
> - setActiveWebEngineVersion不支持在异步线程中调用。&gt;
> - setActiveWebEngineVersion全局生效，在整个APP生命周期中调用一次即可，不需要重复调用。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| engineVersion | [ArkWebEngineVersion](arkts-arkweb-webview-arkwebengineversion-e.md) | 是 |

## setAppCustomUserAgent

```TypeScript
static setAppCustomUserAgent(userAgent: string) : void
```

设置应用级自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。当需要设置应用级自定义用户代理时，建议在Web组件创建前调用setAppCustomUserAgent方法设置User-Agent，再创建指定src的Web组件或通过 [loadUrl](#loadurl)加载具体页面。默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

## setAudioMuted

```TypeScript
setAudioMuted(mute: boolean): void
```

设置网页静音。典型使用场景包括：应用需要控制网页音量（如提供静音开关）、后台播放时需要静音等。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mute | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setAutoPreconnect

```TypeScript
static setAutoPreconnect(enabled: boolean): void
```

设置Web内核的自动预连接状态。若未设置，默认启用自动预连接。需要在[initializeWebEngine()](#initializewebengine)初始化内核或者创建Web组件之前调用。若已加载任何Web组件，则该设 置无效。

**起始版本：** 21

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

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [BackForwardCacheOptions](arkts-arkweb-webview-backforwardcacheoptions-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setBlanklessLoadingCacheCapacity

```TypeScript
static setBlanklessLoadingCacheCapacity(capacity: number) : number
```

设置无白屏加载方案的持久化缓存容量，返回实际生效值。当接口没有显式调用时，默认缓存容量为30MB。当实际缓存超过容量时，将采用淘汰不常用的过渡帧的方式清理。

**起始版本：** 20

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## setBlanklessLoadingWithKey

```TypeScript
setBlanklessLoadingWithKey(key: string, is_start: boolean) : WebBlanklessErrorCode
```

设置无白屏加载是否启用，本接口必须与[getBlanklessInfoWithKey](#getblanklessinfowithkey)接口配套使用。

> **说明：**&gt;
> - 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](#getblanklessinfowithkey)。&gt;
> - 页面加载必须在调用本接口的组件中进行。&gt;
> - 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。&gt;
> - 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，
> 具体权限的添加方法请参考[在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 20

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## setBlanklessLoadingWithParams

```TypeScript
setBlanklessLoadingWithParams(key: string,
      param: BlanklessLoadingParam) : WebBlanklessErrorCode
```

设置白屏插帧的配置参数，本接口必须与[getBlanklessInfoWithKey](#getblanklessinfowithkey)接口配套使用。相比于 [setBlanklessLoadingWithKey](#setblanklessloadingwithkey)，本接口支持白屏插帧更多的参数设置，包括插帧持续时 间，缓存数据有效时间，插帧完成后的自定义回调。

> **说明：**&gt;
> - 需在触发页面加载的接口之后调用，其他约束同[getBlanklessInfoWithKey](#getblanklessinfowithkey)。&gt;
> - 页面加载必须在调用本接口的组件中进行。&gt;
> - 当相似度较低时，系统将判定为跳变过大，启用插帧会失败。&gt;
> - 请在module.json5中添加权限: ohos.permission.INTERNET和ohos.permission.GET_NETWORK_INFO，具体权限的添加方法请参考
> [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## setConnectionTimeout

```TypeScript
static setConnectionTimeout(timeout: number): void
```

设置网络连接超时时间，使用者可通过Web组件中的onErrorReceive方法获取超时错误码。若未调用该接口则默认超时时间为30秒。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

设置自定义用户代理，会覆盖系统的用户代理。

> **说明：**&gt;
> - 当Web组件src设置了URL时，建议在onControllerAttached回调中设置User-Agent。不要在
> onLoadIntercept回调中设置，否则可能会设置失败或导致不可预期的后果。&gt;
> - 若未在onControllerAttached回调中设置User-Agent，再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现象。&gt;
> - 当Web组件src未设置URL时，建议先调用setCustomUserAgent方法设置User-Agent，再通过loadUrl加载具体页面。&gt;
> - 默认User-Agent定义与使用场景请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setDownloadDelegate

```TypeScript
setDownloadDelegate(delegate: WebDownloadDelegate): void
```

为当前的Web组件设置一个WebDownloadDelegate，该delegate用来接收页面内触发的下载进度的委托。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delegate | [WebDownloadDelegate](arkts-arkweb-webview-webdownloaddelegate-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean): void
```

设置是否启用默认错误页。在当前接口设置为true时如果页面加载发生错误将触发[onOverrideErrorPage](../arkts-components/arkts-arkweb-web-attribute.md#onoverrideerrorpage)回调，可在该回调接口中设置自定义的错误展示页面。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setErrorPageEnabled

```TypeScript
setErrorPageEnabled(enable: boolean, includeSubframe: boolean): void
```

设置是否启用mainframe错误页功能，并可控制是否同时启用subframe错误页功能。当enable设置为true时，mainframe加载发生错误将展示错误页：若设置了[onOverrideErrorPage](../arkts-components/arkts-arkweb-web-attribute.md#onoverrideerrorpage)回调，则展示用户自定 义的错误页；若未设置，则展示ArkWeb提供的默认错误页。当enable和includeSubframe同时设置为true时，subframe加载发生错误也会展示错误页，onOverrideErrorPage回调对 subframe同样生效。

> **说明：**&gt;
> - 当enable设置为false时，无论includeSubframe取何值，mainframe和subframe的错误页功能均不启用。&gt;
> - 当includeSubframe设置为false时，本接口行为与
> [setErrorPageEnabled](#seterrorpageenabled)一致，即仅启用mainframe错误页功
> 能，不启用subframe错误页功能。&gt;
> - 可通过errorPageEvent.request.isMainFrame()判断错误来源是mainframe还是subframe，以便在
> onOverrideErrorPage回调中分别设置对应的自定义错误页。
> 26.0.0

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| includeSubframe | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setHostIP

```TypeScript
static setHostIP(hostName: string, address: string, aliveTime: number): void
```

设置主机域名解析后的IP地址。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setHttpDns

```TypeScript
static setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: string): void
```

设置Web组件是否使用HTTPDNS解析DNS。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| secureDnsMode | [SecureDnsMode](arkts-arkweb-webview-securednsmode-e.md) | 是 |
| secureDnsConfig | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setNetworkAvailable

```TypeScript
setNetworkAvailable(enable: boolean): void
```

设置JavaScript中的`window.navigator.onLine`属性。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setPathAllowingUniversalAccess

```TypeScript
setPathAllowingUniversalAccess(pathList: Array<string>): void
```

设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件，也允许跨域访问其他在线资源。此外，当设置了路径列表时，file协议仅允许访问路径列表中的资源。典型使用场景：用于需要允许Web组件跨域访问本地资源 文件，同时限制访问范围以保证安全的场景。（fileAccess的行为将会被此接口行为覆盖）。setPathAllowingUniversalAccess放开目录的跨域访问限制是一个高风险操作。基于最小权限原则，当前el1，el2放开的路径是固定的，路径列表中的路径应符合以下任一路径格式：
1.应用文件目录的子目录（应用文件目录通过Ability Kit中的 [Context.filesDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：
* /data/storage/el2/base/files/example  
* /data/storage/el2/base/haps/entry/files/example
2.应用资源目录及其子目录（应用资源目录通过Ability Kit中的 [Context.resourceDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：
* /data/storage/el1/bundle/entry/resources/resfile  
* /data/storage/el1/bundle/entry/resources/resfile/example
3.从API version 21开始，还包括了应用缓存目录及其子目录（应用缓存目录通过Ability Kit中的 [Context.cacheDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：
* /data/storage/el2/base/cache  
* /data/storage/el2/base/haps/entry/cache/example  
* 设置的目录路径中，不允许包含cache/web，否则会抛出异常码401。如果设置目录路径是cache，cache/web也不允许访问。
4.从API version 21开始，还包括了应用临时目录及其子目录（应用临时目录通过Ability Kit中的 [Context.tempDir](../../../reference/apis-ability-kit/js-apis-inner-application-context.md#属性)获取），例如：
* /data/storage/el2/base/temp  
* /data/storage/el2/base/haps/entry/temp/example当路径列表中有其中一个路径不满足以上条件之一，则会抛出异常码401，并且设置路径列表失败。当设置的路径列表为空，则file协议可访问范围以fileAccess的 行为为准。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pathList | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setPrintBackground

```TypeScript
setPrintBackground(enable: boolean): void
```

设置是否打印网页背景，该接口与[PrintAttributes](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-print-printattributes-i.md)打印参数配置不一致时，本接口设置优先级高于打印参数。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setRenderProcessMode

```TypeScript
static setRenderProcessMode(mode: RenderProcessMode): void
```

设置ArkWeb渲染子进程模式，可根据应用对内存占用与渲染进程隔离的需求选择对应的模式。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [RenderProcessMode](arkts-arkweb-webview-renderprocessmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setScrollable

```TypeScript
setScrollable(enable: boolean, type?: ScrollType): void
```

设置网页是否允许滚动。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
| type | [ScrollType](arkts-arkweb-webview-scrolltype-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setScrollbarMode

```TypeScript
static setScrollbarMode(scrollbarMode: ScrollbarMode): void
```

在Web页面场景，设置全局滚动条模式。不显式调用时，默认为[ScrollbarMode.OVERLAY_LAYOUT_SCROLLBAR](arkts-arkweb-webview-scrollbarmode-e.md)（非常驻滚动条）。

> **说明：**&gt;
> - 根据滚动条模式，改变当前应用所有web滚动条模式为常驻滚动条或非常驻滚动条。&gt;
> - 若[forceDisplayScrollBar](../arkts-components/arkts-arkweb-web-attribute.md#forcedisplayscrollbar)接口与当前接口同时设置，forceDisplayScrollBar接口设置不生效。&gt;
> - 该接口需要在WebViewController绑定Web组件之前调用。

**起始版本：** 23

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scrollbarMode | [ScrollbarMode](arkts-arkweb-webview-scrollbarmode-e.md) | 是 |

## setServiceWorkerWebSchemeHandler

```TypeScript
static setServiceWorkerWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

为当前应用的所有Web组件设置用于拦截ServiceWorker的WebSchemeHandler。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scheme | string | 是 |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSiteIsolationMode

```TypeScript
static setSiteIsolationMode(mode: SiteIsolationMode): void
```

设置站点隔离模式。站点隔离机制将不同源的网站隔离在不同的渲染进程中，减少跨域攻击面。例如：PC等设备上，在未启用站点隔离模式时，原有进程模型是每一个Tab对应一个渲染进程，开启站点隔离后，一个Tab下不同源的Iframe可在独 立的渲染进程中运行。对于仅加载可信网页的第三方应用，可以关闭此功能，以提升性能并减少内存占用，同时减少跨域访问的拦截。默认值根据不同的设备而定，PC/Table采用严格站点隔离 [SiteIsolationMode.STRICT](arkts-arkweb-webview-siteisolationmode-e.md)，Phone默认部分站点隔离 [SiteIsolationMode.PARTIAL](arkts-arkweb-webview-siteisolationmode-e.md)。[坚盾守护模式](../../../web/web-secure-shield-mode.md)下采用 严格站点隔离。

> **说明：**&gt;
> 不能在单子进程模式下设置严格站点隔离。&gt;
> 接口只能在初始化时调用一次，不支持反复修改。

**起始版本：** 21

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [SiteIsolationMode](arkts-arkweb-webview-siteisolationmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setSocketIdleTimeout

```TypeScript
static setSocketIdleTimeout(timeout: number): void
```

设置ArkWeb中已使用过的空闲socket的超时时间，即已使用过的socket可以处于空闲状态的最大时长。如果设置的值与已存在的空闲socket超时时间不同，则根据新的值对已存在的空闲socket进行清理。未使用该接口设置空闲socket的超时时间时，ArkWeb的默认值为300s。

**起始版本：** 21

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

## setSoftKeyboardBehaviorMode

```TypeScript
setSoftKeyboardBehaviorMode(mode: WebSoftKeyboardBehaviorMode): void
```

设置软键盘自动控制模式，当接口没有显式调用时，Web组件失去焦点或获得焦点、状态切换为inactive或active时，系统均会尝试触发软键盘自动隐藏或拉起。典型使用场景：不希望Web组件在inactive或active状态切 换时自动隐藏或重新拉起软键盘时，可使用DISABLE_AUTO_KEYBOARD_ON_ACTIVE；需要保留默认自动管理行为时，可使用DEFAULT。

**起始版本：** 22

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebSoftKeyboardBehaviorMode](arkts-arkweb-webview-websoftkeyboardbehaviormode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string): void
```

设置Web的URL白名单，只有白名单内的URL才能允许加载/跳转，否则将拦截并弹出告警页。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| urlTrustList | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setUrlTrustList

```TypeScript
setUrlTrustList(urlTrustList: string, allowOpaqueOrigin: boolean, supportWildcard: boolean): void
```

设置Web的URL白名单，只有白名单内的URL才能允许加载/跳转，否则将拦截并弹出告警页。扩展了对Opaque Origin URL以及通配符规则的控制能力。

**起始版本：** 24

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
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setUserAgentClientHintsEnabled

```TypeScript
static setUserAgentClientHintsEnabled(enabled: boolean): void
```

设置是否开启User-Agent Client Hints功能。

> **说明：**&gt;
> User-Agent Client Hints（UA-CH）是一种替代传统User-Agent字符串的隐私保护机制，通过按需请求和结构化数据传递客户端信息，减少过度追踪风险。&gt;
> 不使用该方法时，默认不开启User-Agent Client Hints功能。

**起始版本：** 24

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## setUserAgentForHosts

```TypeScript
static setUserAgentForHosts(userAgent: string, hosts : Array<string>) : void
```

针对特定网站设置自定义用户代理，会覆盖系统的用户代理，应用内所有Web组件生效。当需要对特定网站设置自定义用户代理时，建议在Web组件创建前调用setUserAgentForHosts方法设置User-Agent，再创建指定src的Web组件或通过 [loadUrl](#loadurl)加载具体页面。默认User-Agent定义与使用场景，及相关User-Agent接口定义优先级请参考[User-Agent开发指导](../../../web/web-default-userAgent.md)。

**起始版本：** 20

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

设置与User-Agent相对应的UserAgent Metadata数据。

> **说明：**&gt;
> User-Agent Metadata将用于填充用户代理客户端提示，它们可以提供客户端的品牌和版本信息、底层操作系统的品牌和主要版本，以及底层设备的详细信息。&gt;
> 用户代理可以通过setCustomUserAgent、setAppCustomUserAgent或setUserAgentForHosts来设置。&gt;
> 如果根据覆盖后的User-Agent未找到UserAgentMetadata，且覆盖后的User-Agent包含系统默认的User-Agent，则将使用系统默认值。&gt;
> 如果根据覆盖后的User-Agent未找到UserAgentMetadata，但覆盖后的 User-Agent 不包含系统默认用户代理，则只会生成低级用户代理客户端提示。

**起始版本：** 24

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

设置是否启用网页调试功能。详情请参考[DevTools工具](../../../web/web-debugging-with-devtools.md)。安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webDebuggingAccess | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setWebDebuggingAccess

```TypeScript
static setWebDebuggingAccess(webDebuggingAccess: boolean, port: number): void
```

设置是否启用无线网页调试功能，默认不开启。  
* 当没有指定端口port时，该接口等同于  
[setWebDebuggingAccess](#setwebdebuggingaccess)接口， ArkWeb会启动一个本地domain socket监听。  
* 当指定了端口port时，ArkWeb会启动一个tcp socket监听。这时可以无线调试网页。详情请参考[无线调试](../../../web/web-debugging-with-devtools.md#无线调试)。由于小于1024的端口号作为熟知或系统端口，在操作系统上需要特权才能开启，因此port的取值必须大于1024，否则该接口会抛出异常。安全提示：启用网页调试功能可以让用户检查修改Web页面内部状态，存在安全隐患，不建议在应用正式发布版本中启用。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webDebuggingAccess | boolean | 是 |
| port | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100023](../errorcode-webview.md#17100023-使用了不被允许的端口号) |

## setWebDestroyMode

```TypeScript
static setWebDestroyMode(mode: WebDestroyMode): void
```

设置Web组件的销毁模式。当Web组件销毁时，销毁模式会影响Web内核资源释放的时机，例如JavaScript运行上下文、渲染上下文等。默认值： [WebDestroyMode.NORMAL_MODE](arkts-arkweb-webview-webdestroymode-e.md)（普通模式），由系统决定销毁时机。应用可设置 [WebDestroyMode.FAST_MODE](arkts-arkweb-webview-webdestroymode-e.md)（快速模式），以立即销毁资源，从而提升特定场景的性能。

> **说明：**&gt;
> [WebDestroyMode.FAST_MODE](arkts-arkweb-webview-webdestroymode-e.md)（快速模式）会改变Web组件销毁时机，应用需关注依赖Web组件销毁时机的错误实现，例如：Web组件销毁后仍调用
> WebviewController的未定义行为，与[WebDestroyMode.NORMAL_MODE](arkts-arkweb-webview-webdestroymode-e.md)（普通模式）相比，销毁时机提前，有更高的几率触发未关联绑
> 定的异常（17100001），建议应用捕捉异常，或者通过[getAttachState](#getattachstate)方法查询是否绑定状态，来避免稳定性问
> 题。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebDestroyMode](arkts-arkweb-webview-webdestroymode-e.md) | 是 |

## setWebSchemeHandler

```TypeScript
setWebSchemeHandler(scheme: string, handler: WebSchemeHandler): void
```

为Web组件设置[WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md), [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md)类用于 拦截指定scheme的请求。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scheme | string | 是 |
| handler | [WebSchemeHandler](arkts-arkweb-webview-webschemehandler-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## slideScroll

```TypeScript
slideScroll(vx: number, vy: number): void
```

按照指定速度模拟对页面的轻扫滚动动作。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| vx | number | 是 |
| vy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## startCamera

```TypeScript
startCamera(): void
```

开启当前网页摄像头捕获。使用摄像头功能前请在module.json5中添加权限: ohos.permission.CAMERA，具体权限的添加方法请参考 [在配置文件中声明权限](../../../security/AccessToken/declare-permissions.md#在配置文件中声明权限)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## startDownload

```TypeScript
startDownload(url: string): void
```

使用Web组件的下载能力来下载指定的URL，比如下载网页中指定的图片。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## stop

```TypeScript
stop(): void
```

停止页面加载。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopAllMedia

```TypeScript
stopAllMedia(): void
```

控制网页所有音视频停止。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopCamera

```TypeScript
stopCamera(): void
```

停止当前网页摄像头捕获。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## stopMicrophone

```TypeScript
stopMicrophone(): void
```

停止当前网页麦克风捕获。

**起始版本：** 23

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean): Promise<string>
```

以Promise方式异步保存当前页面。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../errorcode-webview.md#17100003-resource路径错误) |

## storeWebArchive

```TypeScript
storeWebArchive(baseName: string, autoName: boolean, callback: AsyncCallback<string>): void
```

以回调方式异步保存当前页面。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| baseName | string | 是 |
| autoName | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100003](../errorcode-webview.md#17100003-resource路径错误) |

## terminateRenderProcess

```TypeScript
terminateRenderProcess(): boolean
```

销毁渲染进程。调用该接口将会主动销毁相关联的渲染进程。如果渲染进程尚未启动，或者已销毁则没有任何影响。此外销毁渲染进程会同时影响所有与该渲染进程关联的其他实例。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## trimMemoryByPressureLevel

```TypeScript
static trimMemoryByPressureLevel(level: PressureLevel): void
```

根据指定的内存压力等级，主动清理Web组件占用的缓存。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| level | [PressureLevel](arkts-arkweb-webview-pressurelevel-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## waitForAttached

```TypeScript
waitForAttached(timeout: number): Promise<ControllerAttachState>
```

异步等待WebViewController与Web组件绑定完成，绑定完成或超时触发回调，通过Promise方式返回当前 [ControllerAttachState](arkts-arkweb-webview-controllerattachstate-e.md)状态。

**起始版本：** 20

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

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17100002](../errorcode-webview.md#17100002-url格式错误) |

## webPageSnapshot

```TypeScript
webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): void
```

获取网页全量绘制结果。

> **说明：**&gt;
> 此接口不支持并发调用。&gt;
> 仅支持对渲染进程上的资源进行截图：静态图片和文本。&gt;
> 如果页面有视频则截图时会显示该视频的占位图片，没有占位图片则显示空白。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [SnapshotInfo](arkts-arkweb-webview-snapshotinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SnapshotResult](arkts-arkweb-webview-snapshotresult-i.md)&gt; | 是 |

## zoom

```TypeScript
zoom(factor: number): void
```

调整当前网页的缩放比例，[zoomAccess](../arkts-components/arkts-arkweb-web-attribute.md#zoomaccess)需为true。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [factor](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-materialproperty-i.md) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100004](../errorcode-webview.md#17100004-功能开关未打开) |

## zoomIn

```TypeScript
zoomIn(): void
```

调用此接口将当前网页进行放大，比例为25%。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100004](../errorcode-webview.md#17100004-功能开关未打开) |

## zoomOut

```TypeScript
zoomOut(): void
```

调用此接口将当前网页进行缩小，比例为20%。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

| 错误码ID |
| --- |
| [17100001](../errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100004](../errorcode-webview.md#17100004-功能开关未打开) |
