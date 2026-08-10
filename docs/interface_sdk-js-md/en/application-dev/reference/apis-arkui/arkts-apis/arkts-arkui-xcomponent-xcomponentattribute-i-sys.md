# XComponentAttribute

定义XComponent属性。

**Inheritance/Implementation:** XComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableTransparentLayer

```TypeScript
default enableTransparentLayer(enabled: boolean | undefined): this
```

当背景颜色设置半透明的XComponent需要开启独立图层（即将该组件的内容置于单独的合成图层上进行渲染，以避免半透明区域与下方内容混合时出现渲染异常）时，使用本接口。

使用本接口，并不代表一定会被设置为独立图层。出于硬件规格（如硬件不支持独立图层进行硬件合成）、软件规格（如独立图层与带有模糊效果的UI组件相交）等原因，将导致半透明XComponent无法设置为独立图层。

**说明：**仅type为SURFACE时有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default enableTransparentLayer(enabled: boolean | undefined): this--><!--Device-XComponentAttribute-default enableTransparentLayer(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | 是否开启组件背景半透明状态下的独立图层。&lt;br&gt;true：开启独立图层；false：关闭独立图层。 设置为true时，由于硬件规格或软件规格等原因，可能无法实际生效。&lt;br&gt;默认值：false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

