# WebKeyboardController

Define the controller to interact with a custom keyboard, related to the [onInterceptKeyboardAttach](onInterceptKeyboardAttach) event.

**Since:** 12

<!--Device-unnamed-declare class WebKeyboardController--><!--Device-unnamed-declare class WebKeyboardController-End-->

**System capability:** SystemCapability.Web.Webview.Core

## close

```TypeScript
close(): void
```

Closes this custom keyboard.

**Since:** 12

<!--Device-WebKeyboardController-close(): void--><!--Device-WebKeyboardController-close(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructs a **WebKeyboardController** API.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebKeyboardController-constructor()--><!--Device-WebKeyboardController-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## deleteBackward

```TypeScript
deleteBackward(length: number): void
```

Deletes a specified number of characters backward in a **Web** component text box.

**Since:** 12

<!--Device-WebKeyboardController-deleteBackward(length: number): void--><!--Device-WebKeyboardController-deleteBackward(length: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

## deleteForward

```TypeScript
deleteForward(length: number): void
```

Deletes a specified number of characters forward in a **Web** component text box.

**Since:** 12

<!--Device-WebKeyboardController-deleteForward(length: number): void--><!--Device-WebKeyboardController-deleteForward(length: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

## insertText

```TypeScript
insertText(text: string): void
```

Inserts characters into the **Web** component text box.

**Since:** 12

<!--Device-WebKeyboardController-insertText(text: string): void--><!--Device-WebKeyboardController-insertText(text: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

## sendFunctionKey

```TypeScript
sendFunctionKey(key: number): void
```

Inserts a function key. Currently, only the Enter key type is supported.For details about the value, see  
[EnterKeyType](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-enterkeytype-e.md#EnterKeyType).

**Since:** 12

<!--Device-WebKeyboardController-sendFunctionKey(key: number): void--><!--Device-WebKeyboardController-sendFunctionKey(key: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | number | Yes |
