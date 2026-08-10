# SizeChangeCallback

```TypeScript
export type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void
```

Defines the callback type used in onSizeChange.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void--><!--Device-unnamed-export type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldValue | [SizeOptions](arkts-arkui-sizeoptions-i.md) | Yes | the width and height of the component before the change. |
| newValue | [SizeOptions](arkts-arkui-sizeoptions-i.md) | Yes | the width and height of the component after the change. |

