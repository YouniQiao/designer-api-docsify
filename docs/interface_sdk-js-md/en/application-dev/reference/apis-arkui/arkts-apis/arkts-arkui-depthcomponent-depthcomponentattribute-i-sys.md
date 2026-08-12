# DepthComponentAttribute (System API)

Style the DepthComponent.

**Inheritance/Implementation:** DepthComponentAttribute extends [CommonMethod](CommonMethod)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface DepthComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface DepthComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## camera

```TypeScript
default camera(camera: DepthCameraParams): this
```

Camera parameters for depth rendering.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default camera(camera: DepthCameraParams): this--><!--Device-DepthComponentAttribute-default camera(camera: DepthCameraParams): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [DepthCameraParams](arkts-arkui-depthcomponent-depthcameraparams-i-sys.md) | Yes | Camera parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## depthMap

```TypeScript
default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this
```

Depth map for depth calculation and rendering.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this--><!--Device-DepthComponentAttribute-default depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| depthMap | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | Yes | Depth map path or PixelMap. |
| callback | [DepthMapCallback](arkts-arkui-depthmapcallback-t-sys.md) | No | Callback invoked when the depth map resource is loaded. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## light

```TypeScript
default light(light: DepthLightParams): this
```

Lighting parameters for depth rendering.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default light(light: DepthLightParams): this--><!--Device-DepthComponentAttribute-default light(light: DepthLightParams): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| light | [DepthLightParams](arkts-arkui-depthcomponent-depthlightparams-i-sys.md) | Yes | Lighting parameters including direction, color and intensity. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onComplete

```TypeScript
default onComplete(callback: DepthComponentCompleteCallback): this
```

Triggered when the background resource is loaded successfully.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default onComplete(callback: DepthComponentCompleteCallback): this--><!--Device-DepthComponentAttribute-default onComplete(callback: DepthComponentCompleteCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentCompleteCallback](arkts-arkui-depthcomponentcompletecallback-t-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onError

```TypeScript
default onError(callback: DepthComponentErrorCallback): this
```

Triggered when an error occurs during background resource loading.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DepthComponentAttribute-default onError(callback: DepthComponentErrorCallback): this--><!--Device-DepthComponentAttribute-default onError(callback: DepthComponentErrorCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentErrorCallback](arkts-arkui-depthcomponenterrorcallback-t-sys.md) | Yes |  |

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
| background | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | Yes | Background resource (required). |
| options | [DepthComponentOptions](arkts-arkui-depthcomponent-depthcomponentoptions-i-sys.md) | No | DepthComponent options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of DepthComponentAttribute. |

