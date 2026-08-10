# SizeChangeCallback

```TypeScript
declare type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void
```

组件区域变化时的回调类型。

oldValue表示目标元素变化之前的宽高。

newValue表示目标元素变化之后的宽高。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-unnamed-declare type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void--><!--Device-unnamed-declare type SizeChangeCallback = (oldValue: SizeOptions, newValue: SizeOptions) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| oldValue | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | Yes |  |
| newValue | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | Yes |  |

