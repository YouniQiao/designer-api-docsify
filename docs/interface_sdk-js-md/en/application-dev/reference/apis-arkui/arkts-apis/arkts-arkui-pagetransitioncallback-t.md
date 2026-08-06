# PageTransitionCallback

```TypeScript
export type PageTransitionCallback = (type: RouteType, progress: double) => void
```

Callback used to report page trasition events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type PageTransitionCallback = (type: RouteType, progress: double) => void--><!--Device-unnamed-export type PageTransitionCallback = (type: RouteType, progress: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | transition route type  |
| progress | double | Yes | transition progess  |

