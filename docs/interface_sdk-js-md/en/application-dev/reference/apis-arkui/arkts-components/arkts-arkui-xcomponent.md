# XComponent

**XComponent**提供用于图形绘制和媒体数据写入的[surface](docroot://ui/napi-xcomponent-guidelines.md#overview)，XComponent负责将其嵌入到视图中，支持应用自定义surface的位置和大小。同时支持AI图像分析、HDR视频亮度调节、防截屏录屏隐私保护、画布自绘制等能力，适用于视频播放、相机预览、游戏渲染、图像AI识别等需要高性能自绘制和媒体内容展示的场景。具体指南请参考[自定义渲染（XComponent）文档](docroot://ui/napi-xcomponent-guidelines.md)。

> **说明：**

## 子组件

不支持

## XComponent

```TypeScript
XComponent(value: { id: string; type: string; libraryname?: string; controller?: XComponentController })
```

构造参数

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 12

**Substitutes:** <!--SUBSTITUTE_API-->(value:<!--/SUBSTITUTE_API-->

<!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: string; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { id: string; type: string; libraryname?: string; controller?: XComponentController } | Yes | 表示XComponent的选项。 |

## XComponent

```TypeScript
XComponent(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController })
```

创建**XComponent**组件，其生命周期回调可以从native侧触发。

从API版本12开始，该接口不再维护。建议使用[XComponent(options: XComponentOptions)](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-xcomponent.md#xcomponent12)替代。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute--><!--Device-XComponentInterface-(value: { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController }): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { id: string; type: XComponentType; libraryname?: string; controller?: XComponentController } | Yes | 表示XComponent的选项。 |

## XComponent

```TypeScript
XComponent(options: XComponentOptions)
```

创建**XComponent**组件，允许您在ArkTS侧获取**SurfaceId**值，注册**XComponent**所持有的surface的生命周期回调以及触摸、鼠标、按键等组件事件的回调，并配置AI分析器功能。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute--><!--Device-XComponentInterface-(options: XComponentOptions): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [XComponentOptions](arkts-arkui-xcomponentoptions-i.md) | Yes | 表示XComponent的选项。 |

## XComponent

```TypeScript
XComponent(params: NativeXComponentParameters)
```

在native侧获取**XComponent**节点实例，并注册**XComponent**所持有的surface的生命周期回调以及触摸、鼠标、按键等组件事件的回调。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute--><!--Device-XComponentInterface-(params: NativeXComponentParameters): XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [NativeXComponentParameters](../arkts-apis/arkts-arkui-xcomponent-nativexcomponentparameters-i.md) | Yes | 表示用于native开发的XComponent构造参数。 |

## Summary

- [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md)
- [SurfaceConfig](arkts-arkui-xcomponent-surfaceconfig-i.md)
- [SurfaceRect](arkts-arkui-xcomponent-surfacerect-i.md)
- [SurfaceRotationOptions](arkts-arkui-xcomponent-surfacerotationoptions-i.md)
- [XComponentOptions](arkts-arkui-xcomponent-xcomponentoptions-i.md)
- [OnNativeLoadCallback](arkts-arkui-xcomponent-onnativeloadcallback-t.md)
- [HdrType](arkts-arkui-xcomponent-hdrtype-e.md)
