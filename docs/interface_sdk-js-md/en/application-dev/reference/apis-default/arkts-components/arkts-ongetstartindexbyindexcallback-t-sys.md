# OnGetStartIndexByIndexCallback (System API)

```TypeScript
export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo
```

Defines the callback type used in onGetStartIndexByIndex of GridLayoutOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo--><!--Device-unnamed-export type OnGetStartIndexByIndexCallback = (targetIndex: int) => StartLineInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetIndex | int | Yes | The target index to scroll to. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [StartLineInfo](arkts-grid-startlineinfo-i-sys.md) | - |

