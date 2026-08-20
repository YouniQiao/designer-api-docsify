# AreaChangeCallback

```TypeScript
export declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void
```

Defines the options for the AreaChangeEvent.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void--><!--Device-unnamed-export declare type AreaChangeCallback = (oldValue: Area, newValue: Area) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldValue | [Area](../../apis-arkui/arkts-apis/arkts-arkui-area-i.md) | Yes | Component area information before the change. |
| newValue | [Area](../../apis-arkui/arkts-apis/arkts-arkui-area-i.md) | Yes | Component area information after the change. |

