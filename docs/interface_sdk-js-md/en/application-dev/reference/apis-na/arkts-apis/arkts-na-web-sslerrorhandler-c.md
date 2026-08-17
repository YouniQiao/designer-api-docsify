# SslErrorHandler

Defines the ssl error request result, related to onSslErrorEventReceive method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class SslErrorHandler--><!--Device-unnamed-export declare class SslErrorHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SslErrorHandler-constructor()--><!--Device-SslErrorHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleCancel

```TypeScript
handleCancel(): void
```

Cancel this request.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SslErrorHandler-handleCancel(): void--><!--Device-SslErrorHandler-handleCancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleCancel

```TypeScript
handleCancel(abortLoading: boolean): void
```

ArkWeb has encountered an SSL certificate error, and this interface indicates whether to terminate or continue displaying the error to users.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SslErrorHandler-handleCancel(abortLoading: boolean): void--><!--Device-SslErrorHandler-handleCancel(abortLoading: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| abortLoading | boolean | Yes | If abortLoading is true, the current request will be canceled and the user will remain on the current page. If it is false, the SSL error will not be ignored, and a blank page will be displayed. If a default error page is enabled, the default error page will be shown instead. The default value is false. |

## handleConfirm

```TypeScript
handleConfirm(): void
```

Confirm to use the SSL certificate.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SslErrorHandler-handleConfirm(): void--><!--Device-SslErrorHandler-handleConfirm(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

