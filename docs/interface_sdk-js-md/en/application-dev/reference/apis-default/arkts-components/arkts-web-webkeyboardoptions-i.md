# WebKeyboardOptions

Defines the web keyboard options when onInterceptKeyboardAttach event return.@interface WebKeyboardOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface WebKeyboardOptions--><!--Device-unnamed-export declare interface WebKeyboardOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

## customKeyboard

```TypeScript
customKeyboard?: CustomBuilder
```

Set the custom keyboard builder when the custom keyboard is used.

**Type:** [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebKeyboardOptions-customKeyboard?: CustomBuilder--><!--Device-WebKeyboardOptions-customKeyboard?: CustomBuilder-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enterKeyType

```TypeScript
enterKeyType?: int
```

Set the enter key type when the system keyboard is used, the "enter" key related to the [inputMethodEngine](../../apis-ime-kit/arkts-apis/arkts-inputmethodengine.md).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebKeyboardOptions-enterKeyType?: int--><!--Device-WebKeyboardOptions-enterKeyType?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## useSystemKeyboard

```TypeScript
useSystemKeyboard: boolean
```

Whether the system keyboard is used.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebKeyboardOptions-useSystemKeyboard: boolean--><!--Device-WebKeyboardOptions-useSystemKeyboard: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

