# PageTransitionCallback

```TypeScript
export type PageTransitionCallback = (type: RouteType, progress: double) => void
```

页面转场事件回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type PageTransitionCallback = (type: RouteType, progress: double) => void--><!--Device-unnamed-export type PageTransitionCallback = (type: RouteType, progress: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [RouteType](../arkts-components/arkts-arkui-routetype-e.md) | Yes | transition route type |
| progress | double | Yes | transition progess |

