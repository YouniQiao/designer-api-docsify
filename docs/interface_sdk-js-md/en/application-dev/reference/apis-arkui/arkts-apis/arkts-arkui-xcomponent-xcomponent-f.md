# XComponent

## XComponent

```TypeScript
export declare function XComponent(
    params: XComponentParameters | XComponentOptions | NativeXComponentParameters
): XComponentAttribute
```

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。同时支持AI图像分析、HDR视频亮度调节、防截屏录屏隐私保护、画布自绘制等能力，适用于视频播放、相机预览、游戏渲染、图像AI识别等需要高性能自绘制和媒体内容展示的场景。创建XComponent组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function XComponent(    params: XComponentParameters | XComponentOptions | NativeXComponentParameters): XComponentAttribute--><!--Device-unnamed-export declare function XComponent(    params: XComponentParameters | XComponentOptions | NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) \| XComponentOptions \| NativeXComponentParameters | Yes | 用于 创建XComponent的选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) | XComponent的属性。 |


## XComponent

```TypeScript
export declare function XComponent(
    style: CustomBuilderT<XComponentAttribute>
): XComponentAttribute
```

定义XComponent组件。要求在组件属性设置开始时调用setXComponentOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function XComponent(    style: CustomBuilderT<XComponentAttribute>): XComponentAttribute--><!--Device-unnamed-export declare function XComponent(    style: CustomBuilderT<XComponentAttribute>): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;XComponentAttribute&gt; | Yes | 用于设置XComponent属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) | XComponent的属性。 |

