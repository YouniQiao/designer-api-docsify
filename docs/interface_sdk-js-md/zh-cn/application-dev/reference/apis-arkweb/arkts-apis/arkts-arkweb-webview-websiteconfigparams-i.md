# WebSiteConfigParams

```TypeScript
interface WebSiteConfigParams
```

传递给[setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback)或[setGlobalWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setglobalwebsiteconfigcallback)回调的参数。

`url`和`source`字段始终存在。可选字段仅在实例级回调触发时填充；静态全局回调触发时不带这些可选字段。

**起始版本：** 26.1.0

<!--Device-webview-interface WebSiteConfigParams--><!--Device-webview-interface WebSiteConfigParams-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## isMainFrame

```TypeScript
isMainFrame?: boolean
```

是否为主帧导航。值为`true`表示主帧导航，值为`false`表示子帧导航。此字段为可选字段，仅在实例级回调触发时设置。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-isMainFrame?: boolean--><!--Device-WebSiteConfigParams-isMainFrame?: boolean-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## pageTransition

```TypeScript
pageTransition?: number
```

页面跳转值，由[PageTransition](arkts-arkweb-webview-pagetransition-e.md)中定义的核心类型与修饰标志按位或得到。可使用掩码常量（`CORE_MASK`、`QUALIFIER_MASK`、`IS_REDIRECT_MASK`）进行拆解。此字段为可选字段，仅在实例级回调触发时设置。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-pageTransition?: number--><!--Device-WebSiteConfigParams-pageTransition?: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## redirectChain

```TypeScript
redirectChain?: Array<string>
```

重定向链。每个元素为一个 URL 字符串。此字段为可选字段，仅在实例级回调触发时设置。

**类型：** Array&lt;string&gt;

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-redirectChain?: Array<string>--><!--Device-WebSiteConfigParams-redirectChain?: Array<string>-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## referrer

```TypeScript
referrer?: string
```

来源页面 URL（referrer）。此字段为可选字段，仅在实例级回调触发时设置。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-referrer?: string--><!--Device-WebSiteConfigParams-referrer?: string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## source

```TypeScript
source: WebSiteSource
```

网站配置查询的触发来源。参见[WebSiteSource](arkts-arkweb-webview-websitesource-e.md)。

**类型：** [WebSiteSource](arkts-arkweb-webview-websitesource-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-source: WebSiteSource--><!--Device-WebSiteConfigParams-source: WebSiteSource-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## topFrameUrl

```TypeScript
topFrameUrl?: string
```

顶层帧 URL。主帧导航时与`url`相同；子帧导航时为包含该子帧的顶层页面 URL。此字段为可选字段，仅在实例级回调触发时设置。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-topFrameUrl?: string--><!--Device-WebSiteConfigParams-topFrameUrl?: string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

完整的请求 URL。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigParams-url: string--><!--Device-WebSiteConfigParams-url: string-End-->

**系统能力：** SystemCapability.Web.Webview.Core
