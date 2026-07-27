# OnLoadInterceptEvent

当资源加载被拦截时，加载拦截事件。

**起始版本：** 12

<!--Device-unnamed-export declare interface OnLoadInterceptEvent--><!--Device-unnamed-export declare interface OnLoadInterceptEvent-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { AtomicServiceWeb, OnMessageEvent, OnPageEndEvent, OnHttpErrorReceiveEvent, OnLoadInterceptEvent, WebHeader, OnProgressChangeEvent, OnErrorReceiveEvent, OnPageBeginEvent, OnLoadInterceptCallback, AtomicServiceWebController } from '@kit.ArkUI';
```

## data

```TypeScript
data: WebResourceRequest
```

Web resource request of event.

**类型：** WebResourceRequest

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-OnLoadInterceptEvent-data: WebResourceRequest--><!--Device-OnLoadInterceptEvent-data: WebResourceRequest-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

