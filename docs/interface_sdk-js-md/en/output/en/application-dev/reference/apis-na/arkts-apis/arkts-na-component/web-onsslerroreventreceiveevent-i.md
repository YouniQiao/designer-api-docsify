# OnSslErrorEventReceiveEvent

Defines the triggered callback when the Web page receives an ssl Error.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface OnSslErrorEventReceiveEvent--><!--Device-unnamed-export declare interface OnSslErrorEventReceiveEvent-End-->

**System capability:** SystemCapability.Web.Webview.Core

## certChainData

```TypeScript
certChainData?: Array<Uint8Array>
```

Certificate chain data in DER format.

**Type:** Array&lt;Uint8Array&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>--><!--Device-OnSslErrorEventReceiveEvent-certChainData?: Array<Uint8Array>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## error

```TypeScript
error: SslError
```

Error codes.

**Type:** SslError

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSslErrorEventReceiveEvent-error: SslError--><!--Device-OnSslErrorEventReceiveEvent-error: SslError-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: SslErrorHandler
```

Notifies the user of the operation behavior of the web component.

**Type:** SslErrorHandler

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler--><!--Device-OnSslErrorEventReceiveEvent-handler: SslErrorHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

