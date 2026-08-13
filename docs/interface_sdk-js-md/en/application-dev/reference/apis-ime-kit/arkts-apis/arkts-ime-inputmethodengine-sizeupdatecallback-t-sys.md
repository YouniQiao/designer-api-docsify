# SizeUpdateCallback (System API)

```TypeScript
export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void
```

Callback triggered when the size of the input method panel changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void--><!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | window.Size | Yes | Panel size. |
| keyboardArea | [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | Yes | Size of the keyboard area. |

