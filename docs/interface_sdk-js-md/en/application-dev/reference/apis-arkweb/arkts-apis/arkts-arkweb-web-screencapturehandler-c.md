# ScreenCaptureHandler

Implements the **ScreenCaptureHandler** object for accepting or rejecting a screen capture request. For details about the sample code, see [onScreenCaptureRequest](./arkts-basic-components-web-events.md#onscreencapturerequest10).

> **NOTE：**&gt;
> - The initial APIs of this component are supported since API version 8.
> Updates will be marked with a superscript to indicate their earliest API version.&gt;
> - The initial APIs of this class are supported since API version 10.&gt;
> - The sample effect is subject to the actual device.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructs a **ScreenCaptureHandler** object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## deny

```TypeScript
deny(): void
```

Rejects this screen capture request.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## getOrigin

```TypeScript
getOrigin(): string
```

Obtains the origin of this web page.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## grant

```TypeScript
grant(config: ScreenCaptureConfig): void
```

Grants the screen capture permission.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [ScreenCaptureConfig](arkts-arkweb-web-screencaptureconfig-i.md) | Yes |
