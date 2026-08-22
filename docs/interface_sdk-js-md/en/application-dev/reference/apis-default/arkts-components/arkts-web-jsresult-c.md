# JsResult

Defines the js result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class JsResult--><!--Device-unnamed-export declare class JsResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-JsResult-constructor()--><!--Device-JsResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleCancel

```TypeScript
handleCancel(): void
```

Handle the user's JavaScript result if cancel the dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-JsResult-handleCancel(): void--><!--Device-JsResult-handleCancel(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleConfirm

```TypeScript
handleConfirm(): void
```

Handle the user's JavaScript result if confirm the dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-JsResult-handleConfirm(): void--><!--Device-JsResult-handleConfirm(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handlePromptConfirm

```TypeScript
handlePromptConfirm(result: string): void
```

Handle the user's JavaScript result if confirm the prompt dialog.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-JsResult-handlePromptConfirm(result: string): void--><!--Device-JsResult-handlePromptConfirm(result: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | string | Yes | The content of the dialog box entered by the user. |

