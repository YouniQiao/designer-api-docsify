# SwiperController

Provides methods for switching components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class SwiperController--><!--Device-unnamed-export declare class SwiperController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(index: int | undefined, animationMode?: SwiperAnimationMode | boolean): void
```

Controlling Swiper to change to the specified subcomponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-changeIndex(index: int | undefined, animationMode?: SwiperAnimationMode | boolean): void--><!--Device-SwiperController-changeIndex(index: int | undefined, animationMode?: SwiperAnimationMode | boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes | the index of item to be redirected, default value is 0, undefined means setting to default value. |
| animationMode | [SwiperAnimationMode](arkts-na-swiper-swiperanimationmode-e.md) \| boolean | No | animation mode for changeIndex, true is equivalent to SwiperAnimationMode.DEFAULT_ANIMATION, false is equivalent to SwiperAnimationMode.NO_ANIMATION |

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-constructor()--><!--Device-SwiperController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fakeDragBy

```TypeScript
fakeDragBy(offset: float): boolean
```

Fake drag by an offset. The 'startFakeDrag' must be called first.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-fakeDragBy(offset: float): boolean--><!--Device-SwiperController-fakeDragBy(offset: float): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | float | Yes | Indicate the offset that needs to be scrolled. The unit is vp. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If not in a fake drag progress, or no offset is consumed, return false. If any offset is consumed, return true. |

## finishAnimation

```TypeScript
finishAnimation(callback?: VoidCallback): void
```

Called when need to stop the swiper animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-finishAnimation(callback?: VoidCallback): void--><!--Device-SwiperController-finishAnimation(callback?: VoidCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) | No |  |

## isFakeDragging

```TypeScript
isFakeDragging(): boolean
```

Get the fake drag state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-isFakeDragging(): boolean--><!--Device-SwiperController-isFakeDragging(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If a fake drag is in progress return true, otherwise return false. |

## preloadItems

```TypeScript
preloadItems(indices: Array<int> | undefined): Promise<void>
```

Called when need to preload specified child.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-preloadItems(indices: Array<int> | undefined): Promise<void>--><!--Device-SwiperController-preloadItems(indices: Array<int> | undefined): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indices | Array&lt;int&gt; \| undefined | Yes | Indices of swiper child to be preloaded, default value is no swiper child to be preloaded, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter invalid. Possible causes: &lt;br&gt; 1. The parameter type is not Array&lt;int&gt;. &lt;br&gt; 2. The parameter is an empty array. &lt;br&gt; 3. The parameter contains an invalid index. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to component. |

## showNext

```TypeScript
showNext(): void
```

Called when the next child component is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-showNext(): void--><!--Device-SwiperController-showNext(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious(): void
```

Called when the previous subcomponent is displayed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-showPrevious(): void--><!--Device-SwiperController-showPrevious(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startFakeDrag

```TypeScript
startFakeDrag(): boolean
```

Start a fake drag. Call 'fakeDragBy' to simulate the drag motion. Call 'stopFakeDrag' to complete the fake drag. A fake drag can be interrupted by a real drag. If you need to ignore touch events and other user input during a fake drag, use 'disableSwipe(true)'.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-startFakeDrag(): boolean--><!--Device-SwiperController-startFakeDrag(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the fake drag started successfully, return true. If the Swiper is not ready to start the fake drag, or a real or fake drag is already in progress, return false. |

## stopFakeDrag

```TypeScript
stopFakeDrag(): boolean
```

Stop a fake drag.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperController-stopFakeDrag(): boolean--><!--Device-SwiperController-stopFakeDrag(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If the fake drag stopped successfully, return true. If the Swiper is not ready to stop a fake drag, or no fake drag is in progress, return false. |

