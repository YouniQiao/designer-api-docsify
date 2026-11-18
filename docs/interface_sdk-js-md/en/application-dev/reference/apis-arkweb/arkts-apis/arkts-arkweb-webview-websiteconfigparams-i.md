# WebSiteConfigParams

```TypeScript
interface WebSiteConfigParams
```

Represents the parameters passed to the website configuration query callback registered by [setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback) or [setGlobalWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setglobalwebsiteconfigcallback).

The `url` and `source` fields are always present. The optional fields are populated only when the instance-level callback is invoked; they are not provided when the static global callback is invoked.

**Since:** 26.1.0

<!--Device-webview-interface WebSiteConfigParams--><!--Device-webview-interface WebSiteConfigParams-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## isMainFrame

```TypeScript
isMainFrame?: boolean
```

Whether the navigation is for the main frame. The value `true` means a main frame navigation, and `false` means a subframe. This field is optional and is set only when the instance-level callback is invoked.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-isMainFrame?: boolean--><!--Device-WebSiteConfigParams-isMainFrame?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## pageTransition

```TypeScript
pageTransition?: number
```

Page transition value, formed by OR'ing a core type with qualifier flags defined in [PageTransition](arkts-arkweb-webview-pagetransition-e.md). Use the mask constants (`CORE_MASK`, `QUALIFIER_MASK`, `IS_REDIRECT_MASK`) to decompose it. This field is optional and is set only when the instance-level callback is invoked.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-pageTransition?: number--><!--Device-WebSiteConfigParams-pageTransition?: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## redirectChain

```TypeScript
redirectChain?: Array<string>
```

Redirect chain. Each element is a URL string. This field is optional and is set only when the instance-level callback is invoked.

**Type:** Array&lt;string&gt;

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-redirectChain?: Array<string>--><!--Device-WebSiteConfigParams-redirectChain?: Array<string>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## referrer

```TypeScript
referrer?: string
```

Source page URL (referrer). This field is optional and is set only when the instance-level callback is invoked.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-referrer?: string--><!--Device-WebSiteConfigParams-referrer?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## source

```TypeScript
source: WebSiteSource
```

Source that triggers the website configuration query. See [WebSiteSource](arkts-arkweb-webview-websitesource-e.md).

**Type:** [WebSiteSource](arkts-arkweb-webview-websitesource-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-source: WebSiteSource--><!--Device-WebSiteConfigParams-source: WebSiteSource-End-->

**System capability:** SystemCapability.Web.Webview.Core

## topFrameUrl

```TypeScript
topFrameUrl?: string
```

Top-level frame URL. For main-frame navigations, this is the same as `url`; for subframe navigations, this is the URL of the top-level page that contains the subframe. This field is optional and is set only when the instance-level callback is invoked.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-topFrameUrl?: string--><!--Device-WebSiteConfigParams-topFrameUrl?: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

Complete request URL.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSiteConfigParams-url: string--><!--Device-WebSiteConfigParams-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core
