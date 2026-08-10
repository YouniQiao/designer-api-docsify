# XComponentController

定义XComponent的控制器。您可以将该控制器绑定到XComponent，以通过控制器调用组件接口。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class XComponentController--><!--Device-unnamed-declare class XComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

用于创建XComponentController实例的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-constructor()--><!--Device-XComponentController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getXComponentContext

```TypeScript
getXComponentContext(): Object
```

获取XComponent对象的context。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-getXComponentContext(): Object--><!--Device-XComponentController-getXComponentContext(): Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Object | XComponent对象的context。 context中包含的接口由开发者定义。 context作为onLoad回调的第一个参数传入。 |

## getXComponentSurfaceId

```TypeScript
getXComponentSurfaceId(): string
```

获取XComponent所持有的surface的ID，可用于@ohos相关接口。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-getXComponentSurfaceId(): string--><!--Device-XComponentController-getXComponentSurfaceId(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | XComponent所持有的surface的ID。 |

## getXComponentSurfaceRect

```TypeScript
getXComponentSurfaceRect(): SurfaceRect
```

获取XComponent所持有的surface的矩形。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-getXComponentSurfaceRect(): SurfaceRect--><!--Device-XComponentController-getXComponentSurfaceRect(): SurfaceRect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SurfaceRect](../arkts-apis/arkts-arkui-xcomponent-surfacerect-i.md) | XComponent所持有的surface的矩形。 |

## getXComponentSurfaceRotation

```TypeScript
getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>
```

获取屏幕旋转时此XComponent所持有的surface的方向是否锁定。该接口仅在XComponent的type设置为SURFACE("surface")时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>--><!--Device-XComponentController-getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Required](../../apis-default/arkts-apis/arkts-required-t.md)&lt;SurfaceRotationOptions&gt; | surface旋转选项的结果。 |

## lockCanvas

```TypeScript
lockCanvas(): DrawingCanvas | null
```

获取用于在XComponent创建的surface上绘制的Canvas。有关绘制方法的详细信息，请参见[Canvas](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-canvas-c.md/arkts-arkgraphics2d-drawing-canvas-c.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-XComponentController-lockCanvas(): DrawingCanvas | null--><!--Device-XComponentController-lockCanvas(): DrawingCanvas | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [DrawingCanvas](../arkts-apis/arkts-arkui-drawingcanvas-t.md) | 返回用于在XComponent创建的surface上绘制的Canvas。 如果surface不可用，则返回null。 |

## onSurfaceChanged

```TypeScript
onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void
```

当XComponent所持有的surface大小发生变化时触发（包括XComponent以指定大小创建时）。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**说明：**仅当XComponent组件未设置libraryname参数时，会进行该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void--><!--Device-XComponentController-onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | XComponent所持有的surface的ID。 |
| rect | [SurfaceRect](../arkts-apis/arkts-arkui-xcomponent-surfacerect-i.md) | Yes | 用于显示XComponent所持有的surface的矩形。 |

## onSurfaceCreated

```TypeScript
onSurfaceCreated(surfaceId: string): void
```

当XComponent所持有的surface创建完成时触发。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**说明：**仅当XComponent组件未设置libraryname参数时，会进行该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-onSurfaceCreated(surfaceId: string): void--><!--Device-XComponentController-onSurfaceCreated(surfaceId: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | XComponent所持有的surface的ID。 |

## onSurfaceDestroyed

```TypeScript
onSurfaceDestroyed(surfaceId: string): void
```

当XComponent所持有的surface销毁时触发。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**说明：**仅当XComponent组件未设置libraryname参数时，会进行该回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-onSurfaceDestroyed(surfaceId: string): void--><!--Device-XComponentController-onSurfaceDestroyed(surfaceId: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| surfaceId | string | Yes | XComponent所持有的surface的ID。 |

## setXComponentSurfaceConfig

```TypeScript
setXComponentSurfaceConfig(config: SurfaceConfig):void
```

设置XComponent创建的surface的配置。

> **说明：**
> 
> 此接口仅在XComponent的type为TEXTURE或SURFACE时生效。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-XComponentController-setXComponentSurfaceConfig(config: SurfaceConfig):void--><!--Device-XComponentController-setXComponentSurfaceConfig(config: SurfaceConfig):void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [SurfaceConfig](../arkts-apis/arkts-arkui-xcomponent-surfaceconfig-i.md) | Yes | surface配置 |

## setXComponentSurfaceRect

```TypeScript
setXComponentSurfaceRect(rect: SurfaceRect): void
```

设置XComponent所持有的surface的矩形。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-setXComponentSurfaceRect(rect: SurfaceRect): void--><!--Device-XComponentController-setXComponentSurfaceRect(rect: SurfaceRect): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rect | [SurfaceRect](../arkts-apis/arkts-arkui-xcomponent-surfacerect-i.md) | Yes | XComponent所持有的surface的矩形。 |

## setXComponentSurfaceRotation

```TypeScript
setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void
```

设置屏幕旋转时是否锁定此XComponent所持有的surface的方向。该接口仅在XComponent的type设置为SURFACE("surface")时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void--><!--Device-XComponentController-setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rotationOptions | [SurfaceRotationOptions](../arkts-apis/arkts-arkui-xcomponent-surfacerotationoptions-i.md) | Yes | 屏幕旋转时是否锁定当前XComponent所持有的surface的方向。 |

## setXComponentSurfaceSize

```TypeScript
setXComponentSurfaceSize(value: {
    surfaceWidth: number;
    surfaceHeight: number;
  }): void
```

设置XComponent所持有的surface的宽度和高度。该接口仅在XComponent的type设置为SURFACE("surface")或TEXTURE时生效。

单位：px。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** [setXComponentSurfaceRect](arkts-arkui-xcomponentcontroller-c.md#setxcomponentsurfacerect)

<!--Device-XComponentController-setXComponentSurfaceSize(value: {    surfaceWidth: number;    surfaceHeight: number;  }): void--><!--Device-XComponentController-setXComponentSurfaceSize(value: {    surfaceWidth: number;    surfaceHeight: number;  }): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | {     surfaceWidth: number;     surfaceHeight: number;   } | Yes | XComponent所持有的surface的宽度和高度。 |

## startImageAnalyzer

```TypeScript
startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>
```

配置AI分析并启动AI分析功能，使用前需先启用图像AI分析能力[enableAnalyzer](XComponentAttribute#enableAnalyzer)，仅type为SURFACE或TEXTURE时有效。使用Promise异步回调来返回结果。

由于用于分析的图像帧是调用此接口时捕获的帧，因此请注意此接口的调用时机。

如果在执行完成之前重复调用此接口，将触发错误回调。

> **说明：**

> 图像分析类型无法动态修改。
> 
> 此接口依赖于设备能力。在不兼容的设备上调用将返回错误码。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>--><!--Device-XComponentController-startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](../arkts-apis/arkts-arkui-imageanalyzerconfig-i.md) | Yes | AI图像分析器的设置。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 用于返回结果的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 110001 | 不支持图像分析特性。 |
| 110003 | 图像分析已停止。 |
| 110002 | 图像分析正在执行中。 |

## stopImageAnalyzer

```TypeScript
stopImageAnalyzer(): void
```

停止AI分析功能，AI分析展示的内容将被销毁。仅type为SURFACE或TEXTURE时有效。

> **说明：**

> 如果在startImageAnalyzer接口尚未返回任何结果时调用此接口，将触发错误回调。
> 
> 此特性依赖于设备能力。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-XComponentController-stopImageAnalyzer(): void--><!--Device-XComponentController-stopImageAnalyzer(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unlockCanvasAndPost

```TypeScript
unlockCanvasAndPost(canvas: DrawingCanvas):void
```

将Canvas的新内容发布到XComponent创建的surface，并释放该Canvas。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-XComponentController-unlockCanvasAndPost(canvas: DrawingCanvas):void--><!--Device-XComponentController-unlockCanvasAndPost(canvas: DrawingCanvas):void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | [DrawingCanvas](../arkts-apis/arkts-arkui-drawingcanvas-t.md) | Yes | 之前通过lockCanvas获取的canvas。 |

