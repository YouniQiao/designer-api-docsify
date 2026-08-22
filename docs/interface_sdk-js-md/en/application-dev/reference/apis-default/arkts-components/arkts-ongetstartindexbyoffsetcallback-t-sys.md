# OnGetStartIndexByOffsetCallback (System API)

```TypeScript
export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo
```

Defines the callback type used in onGetStartIndexByOffset of GridLayoutOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo--><!--Device-unnamed-export type OnGetStartIndexByOffsetCallback = (totalOffset: double) => StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| totalOffset | double | Yes | The total offset to scroll to. |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](arkts-grid-startlineinfo-i-sys.md) | - |

