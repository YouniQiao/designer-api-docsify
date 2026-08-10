# DepthComponent (System API)

## DepthComponent

```TypeScript
export declare function DepthComponent(
    background: ResourceStr | PixelMap,
    options?: DepthComponentOptions,
    content_?: CustomBuilder,
): DepthComponentAttribute
```

创建景深组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DepthComponent(    background: ResourceStr | PixelMap,    options?: DepthComponentOptions,    content_?: CustomBuilder,): DepthComponentAttribute--><!--Device-unnamed-export declare function DepthComponent(    background: ResourceStr | PixelMap,    options?: DepthComponentOptions,    content_?: CustomBuilder,): DepthComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| background | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap | Yes | 背景资源。支持静态图片或3D模型。  静态图支持加载PixelMap和ResourceStr的数据源，引用方式请参考[加载图片资源](../../../ui/arkts-graphics-display.md#加载图片资源)。  3D模型仅支持加载ResourceStr的数据源，仅支持glTF和glb的3D模型格式。ResourceStr包含Resource和string格式。其中string格式可用于加载本地3D模型，支持绝对路径或file://前缀的沙箱 URI，不支持网络资源的加载；Resource格式可以跨包/跨模块访问模型资源文件，推荐以该方式加载本地3D模型。 |
| options | [DepthComponentOptions](arkts-arkui-depthcomponent-depthcomponentoptions-i-sys.md) | No | 景深组件配置项。默认值：`{ depthSpace: DepthSpaceType.INSTANCE }`。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Subcomponents of DepthComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| [DepthComponentAttribute](../arkts-components/arkts-arkui-depthcomponent-attribute.md) | 景深组件属性配置项 |

