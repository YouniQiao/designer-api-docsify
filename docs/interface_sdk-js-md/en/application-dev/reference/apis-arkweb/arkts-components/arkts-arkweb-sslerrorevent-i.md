# SslErrorEvent

Defines the ssl error event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface SslErrorEvent--><!--Device-unnamed-declare interface SslErrorEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## certChainData

```TypeScript
certChainData?: Array<Uint8Array>
```

证书链数据。

**Type:** Array&lt;Uint8Array&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SslErrorEvent-certChainData?: Array<Uint8Array>--><!--Device-SslErrorEvent-certChainData?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## error

```TypeScript
error: SslError
```

错误码。

**Type:** [SslError](arkts-arkweb-sslerror-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-error: SslError--><!--Device-SslErrorEvent-error: SslError-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: SslErrorHandler
```

通知Web组件用户操作行为。

**Type:** [SslErrorHandler](arkts-arkweb-sslerrorhandler-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-handler: SslErrorHandler--><!--Device-SslErrorEvent-handler: SslErrorHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isFatalError

```TypeScript
isFatalError: boolean
```

是否是致命错误。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-isFatalError: boolean--><!--Device-SslErrorEvent-isFatalError: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## isMainFrame

```TypeScript
isMainFrame: boolean
```

是否是主资源。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-isMainFrame: boolean--><!--Device-SslErrorEvent-isMainFrame: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## originalUrl

```TypeScript
originalUrl: string
```

请求的原始url地址。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-originalUrl: string--><!--Device-SslErrorEvent-originalUrl: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## referrer

```TypeScript
referrer: string
```

referrer url地址。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-referrer: string--><!--Device-SslErrorEvent-referrer: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

## url

```TypeScript
url: string
```

url地址。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SslErrorEvent-url: string--><!--Device-SslErrorEvent-url: string-End-->

**System capability:** SystemCapability.Web.Webview.Core

