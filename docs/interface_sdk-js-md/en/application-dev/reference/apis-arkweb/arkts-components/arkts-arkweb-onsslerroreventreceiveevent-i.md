# OnSslErrorEventReceiveEvent

Defines the triggered callback when the Web page receives an ssl Error.

**Since:** 12

<!--Device-unnamed-declare interface OnSslErrorEventReceiveEvent--><!--Device-unnamed-declare interface OnSslErrorEventReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## certChainData

```TypeScript
certChainData?: Array<Uint8Array>
```

Certificate chain data in DER format.

**Type:** Array&lt;Uint8Array&gt;

**Since:** 15

<!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>--><!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## error

```TypeScript
error: SslError
```

Error codes.

**Type:** SslError

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSslErrorEventReceiveEvent-error: SslError--><!--Device-OnSslErrorEventReceiveEvent-error: SslError-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: SslErrorHandler
```

Notifies the user of the operation behavior of the web component.

**Type:** SslErrorHandler

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler--><!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

