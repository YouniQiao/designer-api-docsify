# QRCode

## QRCode

```TypeScript
@ComponentBuilder
export declare function QRCode(
    value: ResourceStr
): QRCodeAttribute
```

Defines the QRCode component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function QRCode(    value: ResourceStr): QRCodeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function QRCode(    value: ResourceStr): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) | Yes | qrcode string. |

**Return value:**

| Type | Description |
| --- | --- |
| [QRCodeAttribute](arkts-qrcode-attribute.md) |  |


## QRCode

```TypeScript
@Builder
export declare function QRCode(
    style: CustomBuilderT<QRCodeAttribute>,
): QRCodeAttribute
```

Defines QRCode Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute--><!--Device-unnamed-@Builderexport declare function QRCode(    style: CustomBuilderT<QRCodeAttribute>,): QRCodeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[QRCodeAttribute](arkts-qrcode-attribute.md)&gt; | Yes | QRCode attribute instance |

**Return value:**

| Type | Description |
| --- | --- |
| [QRCodeAttribute](arkts-qrcode-attribute.md) |  |

