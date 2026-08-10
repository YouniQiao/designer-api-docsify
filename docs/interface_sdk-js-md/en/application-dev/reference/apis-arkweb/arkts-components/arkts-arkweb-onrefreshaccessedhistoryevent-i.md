# OnRefreshAccessedHistoryEvent

定义导航完成时触发。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnRefreshAccessedHistoryEvent--><!--Device-unnamed-declare interface OnRefreshAccessedHistoryEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isMainFrame

```TypeScript
isMainFrame?: boolean
```

是否是主文档触发。true表示是主文档触发，false表示不是主文档触发。

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-OnRefreshAccessedHistoryEvent-isMainFrame?: boolean--><!--Device-OnRefreshAccessedHistoryEvent-isMainFrame?: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isRefreshed

```TypeScript
isRefreshed: boolean
```

true表示该页面是被重新加载的（调用[refresh](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md/arkts-arkweb-webview-webviewcontroller-c.md#refresh)接口），false表示该页面是新加载的。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnRefreshAccessedHistoryEvent-isRefreshed: boolean--><!--Device-OnRefreshAccessedHistoryEvent-isRefreshed: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

访问的url。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnRefreshAccessedHistoryEvent-url: string--><!--Device-OnRefreshAccessedHistoryEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

