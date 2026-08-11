# DepthComponent

Defines DepthComponent Component.

## DepthComponent

```TypeScript
DepthComponent(background: ResourceStr | PixelMap, options?: DepthComponentOptions)
```

创建景深组件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-DepthComponentInterface-(background: ResourceStr | PixelMap, options?: DepthComponentOptions): DepthComponentAttribute--><!--Device-DepthComponentInterface-(background: ResourceStr | PixelMap, options?: DepthComponentOptions): DepthComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| background | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-apis/arkts-arkui-pixelmap-t.md) | 是 |
| options | [DepthComponentOptions](arkts-arkui-depthcomponentoptions-i-sys.md) | 否 |

## 汇总

- [CameraBufferCrop](arkts-arkui-depthcomponent-camerabuffercrop-i-sys.md)
- [CropOffset](arkts-arkui-depthcomponent-cropoffset-i-sys.md)
- [DepthCameraParams](arkts-arkui-depthcomponent-depthcameraparams-i-sys.md)
- [DepthComponentCompleteEvent](arkts-arkui-depthcomponent-depthcomponentcompleteevent-i-sys.md)
- [DepthComponentErrorEvent](arkts-arkui-depthcomponent-depthcomponenterrorevent-i-sys.md)
- [DepthComponentOptions](arkts-arkui-depthcomponent-depthcomponentoptions-i-sys.md)
- [DepthLightParams](arkts-arkui-depthcomponent-depthlightparams-i-sys.md)
- [DepthComponentCompleteCallback](arkts-arkui-depthcomponent-depthcomponentcompletecallback-t-sys.md)
- [DepthComponentErrorCallback](arkts-arkui-depthcomponent-depthcomponenterrorcallback-t-sys.md)
- [DepthMapCallback](arkts-arkui-depthcomponent-depthmapcallback-t-sys.md)
- [DepthSpaceType](arkts-arkui-depthcomponent-depthspacetype-e-sys.md)
