# WebKeyboardController

Define the controller to interact with a custom keyboard, related to the {@link onInterceptKeyboardAttach} event.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class WebKeyboardController--><!--Device-unnamed-declare class WebKeyboardController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## close

```TypeScript
close(): void
```

Close the custom keyboard.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebKeyboardController-close(): void--><!--Device-WebKeyboardController-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebKeyboardController-constructor()--><!--Device-WebKeyboardController-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deleteBackward

```TypeScript
deleteBackward(length: number): void
```

Delete text from front to back.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebKeyboardController-deleteBackward(length: number): void--><!--Device-WebKeyboardController-deleteBackward(length: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes | length of text, which will be deleted from front to back. |

## deleteForward

```TypeScript
deleteForward(length: number): void
```

Delete text from back to front.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebKeyboardController-deleteForward(length: number): void--><!--Device-WebKeyboardController-deleteForward(length: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes | length of text, which will be deleted from back to front. |

## insertText

```TypeScript
insertText(text: string): void
```

Insert text into Editor.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebKeyboardController-insertText(text: string): void--><!--Device-WebKeyboardController-insertText(text: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text which will be inserted. |

## sendFunctionKey

```TypeScript
sendFunctionKey(key: number): void
```

Send the function of the key.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WebKeyboardController-sendFunctionKey(key: number): void--><!--Device-WebKeyboardController-sendFunctionKey(key: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | number | Yes | action indicates the "enter" key related to the {@link inputMethodEngine} |

