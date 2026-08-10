# WebKeyboardController

Define the controller to interact with a custom keyboard, related to the {@link onInterceptKeyboardAttach} event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class WebKeyboardController--><!--Device-unnamed-export declare class WebKeyboardController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## close

```TypeScript
close(): void
```

Close the custom keyboard.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-close(): void--><!--Device-WebKeyboardController-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-constructor()--><!--Device-WebKeyboardController-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deleteBackward

```TypeScript
deleteBackward(length: int): void
```

Delete the specified length of characters in the Web input field from the beginning to the end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-deleteBackward(length: int): void--><!--Device-WebKeyboardController-deleteBackward(length: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | length of text, which will be deleted from front to back. |

## deleteForward

```TypeScript
deleteForward(length: int): void
```

Deletes the specified length of characters from the back to the front in the Web input field.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-deleteForward(length: int): void--><!--Device-WebKeyboardController-deleteForward(length: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | int | Yes | length of text, which will be deleted from back to front. |

## insertText

```TypeScript
insertText(text: string): void
```

Insert characters in the Web input field.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-insertText(text: string): void--><!--Device-WebKeyboardController-insertText(text: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | text which will be inserted. |

## sendFunctionKey

```TypeScript
sendFunctionKey(key: int): void
```

Send the function of the key.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardController-sendFunctionKey(key: int): void--><!--Device-WebKeyboardController-sendFunctionKey(key: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | int | Yes | action indicates the "enter" key related to the {@link inputMethodEngine} |

