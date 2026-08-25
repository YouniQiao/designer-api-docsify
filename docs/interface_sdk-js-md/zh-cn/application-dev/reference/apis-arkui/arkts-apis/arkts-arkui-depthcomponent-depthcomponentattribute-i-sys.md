# DepthComponentAttribute（系统接口）

除支持通用属性外，还支持以下属性：

**继承/实现关系：** DepthComponentAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## camera

```TypeScript
default camera(camera: DepthCameraParams): this
```

设置景深渲染使用的相机参数。

> **说明：**&gt;
> 以图片作为背景时，相机参数更新不会引起背景的变化。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [camera](#camera) | [DepthCameraParams](arkts-arkui-depthcomponent-depthcameraparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## depthMap

```TypeScript
default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this
```

设置用于景深计算和渲染的深度图。使用callback异步回调。

> **说明：**&gt;
> - 深度图是用于描述在3D空间中，背景中每个像素点与相机距离的二维矩阵图像。&gt;
> - 其数据格式为灰阶图，灰度值越大（颜色越白）的像素点距离相机越近。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [depthMap](#depthmap) | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |
| callback | [DepthMapCallback](arkts-arkui-depthmapcallback-t-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## light

```TypeScript
default light(light: DepthLightParams): this
```

设置景深渲染使用的光照参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [light](#light) | [DepthLightParams](arkts-arkui-depthcomponent-depthlightparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onComplete

```TypeScript
default onComplete(callback: DepthComponentCompleteCallback): this
```

背景资源加载成功时触发该回调。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [DepthComponentCompleteCallback](arkts-arkui-depthcomponentcompletecallback-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onError

```TypeScript
default onError(callback: DepthComponentErrorCallback): this
```

背景资源加载出现错误时触发该回调。使用callback异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [DepthComponentErrorCallback](arkts-arkui-depthcomponenterrorcallback-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setDepthComponentOptions

```TypeScript
default setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this
```

Set DepthComponent options.

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| background | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |
| options | [DepthComponentOptions](arkts-arkui-depthcomponent-depthcomponentoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |
