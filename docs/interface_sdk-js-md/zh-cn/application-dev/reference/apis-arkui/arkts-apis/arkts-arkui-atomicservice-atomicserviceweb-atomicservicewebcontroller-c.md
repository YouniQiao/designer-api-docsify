# AtomicServiceWebController

通过AtomicServiceWebController可以控制AtomicServiceWeb组件各种行为。一个AtomicServiceWebController对象只能控制一个AtomicServiceWeb组件，且必须在 AtomicServiceWeb组件和AtomicServiceWebController绑定后，才能调用AtomicServiceWebController上的方法。

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnErrorReceiveEvent, OnHttpErrorReceiveEvent, OnPageBeginEvent, OnPageEndEvent, AtomicServiceWebController, OnLoadInterceptEvent, OnProgressChangeEvent, OnLoadInterceptCallback, WebHeader } from 'kits/@kit.ArkUI';
```

## accessBackward

```TypeScript
accessBackward(): boolean
```

当前页面是否可后退，即当前页面是否有返回历史记录。可结合[backward](#backward)一起使用，先通过此方法判断是否可后退，再调用backward执行后退 操作。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessForward

```TypeScript
accessForward(): boolean
```

当前页面是否可前进，即当前页面是否有前进历史记录。可结合[forward](#forward)一起使用，先通过此方法判断是否可前进，再调用forward执行前进操作。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## accessStep

```TypeScript
accessStep(step: number): boolean
```

当前页面是否可前进或者后退给定的step步。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

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
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## backward

```TypeScript
backward(): void
```

按照历史栈，后退一个页面。可结合[accessBackward](#accessbackward)一起使用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## forward

```TypeScript
forward(): void
```

按照历史栈，前进一个页面。可结合[accessForward](#accessforward)一起使用。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getCustomUserAgent

```TypeScript
getCustomUserAgent(): string
```

获取自定义用户代理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## getUserAgent

```TypeScript
getUserAgent(): string
```

获取当前默认用户代理。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## loadUrl

```TypeScript
loadUrl(url: string | Resource, headers?: Array<WebHeader>): void
```

加载指定的URL。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| headers | Array&lt;[WebHeader](arkts-arkui-atomicservice-atomicserviceweb-webheader-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
| [17100002](../../apis-arkweb/errorcode-webview.md#17100002-url格式错误) |
| [17100003](../../apis-arkweb/errorcode-webview.md#17100003-resource路径错误) |

## refresh

```TypeScript
refresh(): void
```

通知AtomicServiceWeb组件刷新网页。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**错误码：**

| 错误码ID |
| --- |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |

## setCustomUserAgent

```TypeScript
setCustomUserAgent(userAgent: string): void
```

设置自定义用户代理，会覆盖系统的用户代理。建议在onControllerAttached回调事件中设置User-Agent，设置方式请参考示例。不建议将User-Agent设置在onLoadIntercept回调事件中，在部分场景下可能出现设置失败。

> **说明：**&gt;
> 当Web组件src设置了url，且未在onControllerAttached回调事件中设置User-Agent，再调用setCustomUserAgent方法时，可能会出现加载的页面与实际设置User-Agent不符的异常现
> 象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAgent | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17100001](../../apis-arkweb/errorcode-webview.md#17100001-webviewcontroller没有和具体的web组件关联) |
