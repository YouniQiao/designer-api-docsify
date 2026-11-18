# WebSiteConfigResult

```TypeScript
interface WebSiteConfigResult
```

[setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback)回调返回的结果。

**起始版本：** 26.1.0

<!--Device-webview-interface WebSiteConfigResult--><!--Device-webview-interface WebSiteConfigResult-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## userAgent

```TypeScript
userAgent: string
```

完整的 User-Agent 字符串。空字符串表示使用 ArkWeb 默认 User-Agent。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigResult-userAgent: string--><!--Device-WebSiteConfigResult-userAgent: string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## viewportWidth

```TypeScript
viewportWidth: number
```

视口宽度，单位 px。值为 0 表示使用默认视口宽度。单位：px。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WebSiteConfigResult-viewportWidth: number--><!--Device-WebSiteConfigResult-viewportWidth: number-End-->

**系统能力：** SystemCapability.Web.Webview.Core
