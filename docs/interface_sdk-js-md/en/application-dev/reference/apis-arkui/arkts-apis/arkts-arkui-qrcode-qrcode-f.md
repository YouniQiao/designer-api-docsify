# QRCode

## QRCode

```TypeScript
export declare function QRCode(
    value: ResourceStr
): QRCodeAttribute
```

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function QRCode(    value: ResourceStr): QRCodeAttribute--><!--Device-unnamed-export declare function QRCode(    value: ResourceStr): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。 &lt;br/&gt;**说明：** &lt;br/&gt;设置为null时与设置字符串“null”效果一致；设置为 undefined时与设置字符串“undefined”效果一致；当传入空字符串时，将生成无效二维码。 |

**Return value:**

| Type | Description |
| --- | --- |
| [QRCodeAttribute](../arkts-components/arkts-arkui-qrcode-attribute.md) |  |


## QRCode

```TypeScript
export declare function QRCode(
    style: CustomBuilderT<QRCodeAttribute>,
): QRCodeAttribute
```

定义QRCode组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute--><!--Device-unnamed-export declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;QRCodeAttribute&gt; | Yes | QRCode属性实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| [QRCodeAttribute](../arkts-components/arkts-arkui-qrcode-attribute.md) |  |

