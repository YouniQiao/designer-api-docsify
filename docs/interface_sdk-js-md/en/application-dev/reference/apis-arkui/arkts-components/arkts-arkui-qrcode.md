# QRCode

QRCode组件用于显示单个二维码，支持自定义二维码颜色、背景颜色及内容不透明度，适用于需要展示二维码以供扫描获取字符串信息的场景。

> **说明：**
>
> - 二维码组件的像素点数量与内容有关，组件尺寸过小可能导致内容无法展示，此时需要适当调整组件尺寸。

## 子组件

无

## QRCode

```TypeScript
QRCode(value: ResourceStr)
```

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-QRCodeInterface-(value: ResourceStr): QRCodeAttribute--><!--Device-QRCodeInterface-(value: ResourceStr): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | 二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。 <br>从API version 20开始，支持Resource类型。 <br>**说明：** <br>设置为null时与设置字符串"null"效果一致；设置为undefined时与设置字符串"undefined"效果一致；当传入空字符串时，将生成无效二维码。 |

## Summary

