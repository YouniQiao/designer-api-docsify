# QRCode

## QRCode

```TypeScript
export declare function QRCode(
    value: ResourceStr
): QRCodeAttribute
```

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [QRCodeAttribute](arkts-arkui-qrcode-qrcodeattribute-i.md) |


## QRCode

```TypeScript
export declare function QRCode(
    style: CustomBuilderT<QRCodeAttribute>,
): QRCodeAttribute
```

定义QRCode组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[QRCodeAttribute](arkts-arkui-qrcode-qrcodeattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [QRCodeAttribute](arkts-arkui-qrcode-qrcodeattribute-i.md) |
