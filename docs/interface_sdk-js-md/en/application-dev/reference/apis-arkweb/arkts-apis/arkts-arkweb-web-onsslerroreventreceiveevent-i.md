# OnSslErrorEventReceiveEvent

Defines the triggered callback when the Web page receives an ssl Error.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## certChainData

```TypeScript
certChainData?: Array<Uint8Array>
```

Certificate chain data in DER format.

**Type:** Array&lt;Uint8Array&gt;

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## error

```TypeScript
error: SslError
```

Error codes.

**Type:** [SslError](arkts-arkweb-web-sslerror-e.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## handler

```TypeScript
handler: SslErrorHandler
```

Notifies the user of the operation behavior of the web component.

**Type:** [SslErrorHandler](arkts-arkweb-web-sslerrorhandler-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
