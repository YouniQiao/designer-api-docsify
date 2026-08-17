# DepthComponentAttribute (System API)

Style the DepthComponent.

**Inheritance/Implementation:** DepthComponentAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface DepthComponentAttribute--><!--Device-unnamed-export declare interface DepthComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## camera

```TypeScript
camera(camera: DepthCameraParams): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-camera(camera: DepthCameraParams): this--><!--Device-DepthComponentAttribute-camera(camera: DepthCameraParams): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| camera | [DepthCameraParams](arkts-na-depthcomponent-depthcameraparams-i-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## depthMap

```TypeScript
depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this--><!--Device-DepthComponentAttribute-depthMap(depthMap: ResourceStr | PixelMap, callback?: DepthMapCallback): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| depthMap | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) | Yes |  |
| callback | [DepthMapCallback](arkts-na-depthmapcallback-t-sys.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## light

```TypeScript
light(light: DepthLightParams): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-light(light: DepthLightParams): this--><!--Device-DepthComponentAttribute-light(light: DepthLightParams): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| light | [DepthLightParams](arkts-na-depthcomponent-depthlightparams-i-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onComplete

```TypeScript
onComplete(callback: DepthComponentCompleteCallback): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-onComplete(callback: DepthComponentCompleteCallback): this--><!--Device-DepthComponentAttribute-onComplete(callback: DepthComponentCompleteCallback): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentCompleteCallback](arkts-na-depthcomponentcompletecallback-t-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onError

```TypeScript
onError(callback: DepthComponentErrorCallback): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-onError(callback: DepthComponentErrorCallback): this--><!--Device-DepthComponentAttribute-onError(callback: DepthComponentErrorCallback): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [DepthComponentErrorCallback](arkts-na-depthcomponenterrorcallback-t-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setDepthComponentOptions

```TypeScript
setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DepthComponentAttribute-setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this--><!--Device-DepthComponentAttribute-setDepthComponentOptions(background: ResourceStr | PixelMap, options?: DepthComponentOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| background | [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) | Yes |  |
| options | [DepthComponentOptions](arkts-na-depthcomponent-depthcomponentoptions-i-sys.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

