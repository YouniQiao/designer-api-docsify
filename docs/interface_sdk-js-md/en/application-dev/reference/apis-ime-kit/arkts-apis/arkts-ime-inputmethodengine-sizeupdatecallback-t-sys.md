# SizeUpdateCallback (System API)

```TypeScript
export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void
```

Callback triggered when the size of the input method panel changes.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void--><!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | window.Size | Yes | Panel size. |
| keyboardArea | [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | Yes | Size of the keyboard area. |

