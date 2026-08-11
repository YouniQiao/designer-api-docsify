# SizeChangeCallback

```TypeScript
export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void
```

Callback triggered when the size of the input method panel changes.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void--><!--Device-inputMethodEngine-export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | window.Size | Yes | Panel size. |
| keyboardArea | [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | No | Size of the keyboard area. |

