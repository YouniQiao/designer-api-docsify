# ScreenCaptureHandler

Defines the onScreenCapture callback, related to {@link onScreenCapture} method.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ScreenCaptureHandler--><!--Device-unnamed-export declare class ScreenCaptureHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

WebKeyboardController的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScreenCaptureHandler-constructor()--><!--Device-ScreenCaptureHandler-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

Reject the request.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScreenCaptureHandler-deny(): void--><!--Device-ScreenCaptureHandler-deny(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getOrigin

```TypeScript
getOrigin(): string
```

Gets the source of the webpage that attempted to access the restricted resource.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScreenCaptureHandler-getOrigin(): string--><!--Device-ScreenCaptureHandler-getOrigin(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## grant

```TypeScript
grant(config: ScreenCaptureConfig): void
```

Grant origin access to a given resource.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-ScreenCaptureHandler-grant(config: ScreenCaptureConfig): void--><!--Device-ScreenCaptureHandler-grant(config: ScreenCaptureConfig): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ScreenCaptureConfig](../arkts-components/arkts-arkweb-screencaptureconfig-i.md) | Yes | The screen capture configuration. |

