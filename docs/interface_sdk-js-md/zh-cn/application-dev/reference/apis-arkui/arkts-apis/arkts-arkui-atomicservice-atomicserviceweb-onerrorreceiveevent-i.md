# OnErrorReceiveEvent

定义网页加载遇到错误时触发该回调。

**起始版本：** 12

<!--Device-unnamed-export declare interface OnErrorReceiveEvent--><!--Device-unnamed-export declare interface OnErrorReceiveEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from '@kit.ArkUI';
```

## error

```TypeScript
error: WebResourceError
```

Web resource error of event.

**类型：** WebResourceError

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OnErrorReceiveEvent-error: WebResourceError--><!--Device-OnErrorReceiveEvent-error: WebResourceError-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## request

```TypeScript
request: WebResourceRequest
```

Web resource request of event.

**类型：** WebResourceRequest

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OnErrorReceiveEvent-request: WebResourceRequest--><!--Device-OnErrorReceiveEvent-request: WebResourceRequest-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

