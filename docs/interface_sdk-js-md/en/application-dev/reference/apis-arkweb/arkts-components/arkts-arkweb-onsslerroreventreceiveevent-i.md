# OnSslErrorEventReceiveEvent

定义网页收到SSL错误时触发。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface OnSslErrorEventReceiveEvent--><!--Device-unnamed-declare interface OnSslErrorEventReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## certChainData

```TypeScript
certChainData?: Array<Uint8Array>
```

证书链数据。

**Type:** Array&lt;Uint8Array&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>--><!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>-End-->

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

<!--Device-OnSslErrorEventReceiveEvent-error: SslError--><!--Device-OnSslErrorEventReceiveEvent-error: SslError-End-->

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

<!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler--><!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

