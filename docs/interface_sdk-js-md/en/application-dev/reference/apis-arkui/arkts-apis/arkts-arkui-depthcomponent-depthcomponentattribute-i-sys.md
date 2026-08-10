# DepthComponentAttribute (System API)

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性：

**Inheritance/Implementation:** DepthComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface DepthComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface DepthComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## camera

```TypeScript
default camera(camera: DepthCameraParams): this
```

设置景深渲染使用的相机参数。

> **说明：**
> 
> 以图片作为背景时，相机参数更新不会引起背景的变化。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default camera(camera: DepthCameraParams): this--><!--Device-DepthComponentAttribute-default camera(camera: DepthCameraParams): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [DepthCameraParams](arkts-arkui-depthcomponent-depthcameraparams-i-sys.md) | Yes | 相机参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## depthMap

```TypeScript
default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this
```

设置用于景深计算和渲染的深度图。使用callback异步回调。

> **说明：**
> 
> - 深度图是用于描述在3D空间中，背景中每个像素点与相机距离的二维矩阵图像。
> 
> - 其数据格式为灰阶图，灰度值越大（颜色越白）的像素点距离相机越近。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this--><!--Device-DepthComponentAttribute-default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| depthMap | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap | Yes | 深度图资源或PixelMap对象，引用方式与静态背景图一致。仅背景为静态图时需要设置深度图。深度图需要与背景图的分辨率保持一致。 |
| callback | [DepthMapCallback](arkts-arkui-depthmapcallback-t-sys.md) | No | 深度图加载完成时的回调函数。加载成功时error.code为0，加载失败时error中包含错误码和错误信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## light

```TypeScript
default light(light: DepthLightParams): this
```

设置景深渲染使用的光照参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default light(light: DepthLightParams): this--><!--Device-DepthComponentAttribute-default light(light: DepthLightParams): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| light | [DepthLightParams](../arkts-components/arkts-arkui-depthlightparams-i-sys.md) | Yes | 光照参数，包含方向、颜色和强度。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onComplete

```TypeScript
default onComplete(callback: DepthComponentCompleteCallback): this
```

背景资源加载成功时触发该回调。使用callback异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default onComplete(callback: DepthComponentCompleteCallback): this--><!--Device-DepthComponentAttribute-default onComplete(callback: DepthComponentCompleteCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentCompleteCallback](../arkts-components/arkts-arkui-depthcomponentcompletecallback-t-sys.md) | Yes | 背景资源加载成功的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onError

```TypeScript
default onError(callback: DepthComponentErrorCallback): this
```

背景资源加载出现错误时触发该回调。使用callback异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default onError(callback: DepthComponentErrorCallback): this--><!--Device-DepthComponentAttribute-default onError(callback: DepthComponentErrorCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentErrorCallback](arkts-arkui-depthcomponenterrorcallback-t-sys.md) | Yes | 背景资源加载失败的回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setDepthComponentOptions

```TypeScript
default setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this
```

Set DepthComponent options.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this--><!--Device-DepthComponentAttribute-default setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| background | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap | Yes | Background resource (required). |
| options | [DepthComponentOptions](arkts-arkui-depthcomponent-depthcomponentoptions-i-sys.md) | No | DepthComponent options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of DepthComponentAttribute. |

