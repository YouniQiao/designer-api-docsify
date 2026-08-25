# XComponent

## XComponent

```TypeScript
export declare function XComponent(
    params: XComponentParameters | XComponentOptions | NativeXComponentParameters
): XComponentAttribute
```

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。 同时支持AI图像分析、HDR视频亮度调节、防截屏录屏隐私保护、画布自绘制等能力， 适用于视频播放、相机预览、游戏渲染、图像AI识别等需要高性能自绘制和媒体内容展示的场景。 创建XComponent组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) \| [XComponentOptions](arkts-arkui-xcomponent-xcomponentoptions-i.md) \| [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |


## XComponent

```TypeScript
export declare function XComponent(
    style: CustomBuilderT<XComponentAttribute>
): XComponentAttribute
```

定义XComponent组件。要求在组件属性设置开始时调用setXComponentOptions， 并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md) |
