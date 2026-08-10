# OnDidStopDraggingCallback

```TypeScript
declare type OnDidStopDraggingCallback = (willFling: boolean) => void
```

滚动组件在结束拖拽时触发的回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-unnamed-declare type OnDidStopDraggingCallback = (willFling: boolean) => void--><!--Device-unnamed-declare type OnDidStopDraggingCallback = (willFling: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| willFling | boolean | Yes | 结束拖拽后是否会有惯性动效。返回true代表拖拽结束后有惯性动效，返回false代表没有惯性动效。 |

