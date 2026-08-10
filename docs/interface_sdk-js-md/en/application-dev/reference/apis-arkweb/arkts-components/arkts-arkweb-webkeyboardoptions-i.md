# WebKeyboardOptions

Defines the web keyboard options when onInterceptKeyboardAttach event return.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface WebKeyboardOptions--><!--Device-unnamed-declare interface WebKeyboardOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## customKeyboard

```TypeScript
customKeyboard?: CustomBuilder
```

Set the custom keyboard builder when the custom keyboard is used.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebKeyboardOptions-customKeyboard?: CustomBuilder--><!--Device-WebKeyboardOptions-customKeyboard?: CustomBuilder-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enterKeyType

```TypeScript
enterKeyType?: number
```

Set the enter key type when the system keyboard is used, the "enter" key related to the {@link inputMethodEngine}.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebKeyboardOptions-enterKeyType?: number--><!--Device-WebKeyboardOptions-enterKeyType?: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## useSystemKeyboard

```TypeScript
useSystemKeyboard: boolean
```

Whether the system keyboard is used.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WebKeyboardOptions-useSystemKeyboard: boolean--><!--Device-WebKeyboardOptions-useSystemKeyboard: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

