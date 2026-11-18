# WebSiteConfigResult

```TypeScript
interface WebSiteConfigResult
```

Represents the result returned by the [setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback) callback.

**Since:** 26.1.0

<!--Device-webview-interface WebSiteConfigResult--><!--Device-webview-interface WebSiteConfigResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## userAgent

```TypeScript
userAgent: string
```

Complete User-Agent string. An empty string indicates that the ArkWeb default User-Agent is used.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigResult-userAgent: string--><!--Device-WebSiteConfigResult-userAgent: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## viewportWidth

```TypeScript
viewportWidth: number
```

Viewport width, in px. The value 0 indicates that the default viewport width is used. Unit: px.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigResult-viewportWidth: number--><!--Device-WebSiteConfigResult-viewportWidth: number-End-->

**System capability:** SystemCapability.Web.Webview.Core
