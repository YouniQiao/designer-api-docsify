# ButtonTriggerClickCallback

```TypeScript
declare type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void
```

定义ButtonConfiguration中使用的回调类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void--><!--Device-unnamed-declare type ButtonTriggerClickCallback = (xPos: number, yPos: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xPos | number | Yes | 点击位置x的坐标。<br/>单位：vp |
| yPos | number | Yes | 点击位置y的坐标。<br/>单位：vp |

