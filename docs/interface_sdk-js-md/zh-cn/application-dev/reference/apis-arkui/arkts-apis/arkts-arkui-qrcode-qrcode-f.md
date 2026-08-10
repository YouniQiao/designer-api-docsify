# QRCode

## QRCode

```TypeScript
export declare function QRCode(
    value: ResourceStr
): QRCodeAttribute
```

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function QRCode(    value: ResourceStr): QRCodeAttribute--><!--Device-unnamed-export declare function QRCode(    value: ResourceStr): QRCodeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 | 二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。 &lt;br/&gt;**说明：** &lt;br/&gt;设置为null时与设置字符串“null”效果一致；设置为 undefined时与设置字符串“undefined”效果一致；当传入空字符串时，将生成无效二维码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [QRCodeAttribute](../arkts-components/arkts-arkui-qrcode-attribute.md) |  |


## QRCode

```TypeScript
export declare function QRCode(
    style: CustomBuilderT<QRCodeAttribute>,
): QRCodeAttribute
```

定义QRCode组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute--><!--Device-unnamed-export declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;QRCodeAttribute&gt; | 是 | QRCode属性实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [QRCodeAttribute](../arkts-components/arkts-arkui-qrcode-attribute.md) |  |

