# SwiperController

Implements the controller for the **Swiper** component. Bind this object to a **Swiper** component to control page turning and other functionalities.

**Since:** 7

<!--Device-unnamed-declare class SwiperController--><!--Device-unnamed-declare class SwiperController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeIndex

```TypeScript
changeIndex(index: number, useAnimation?: boolean)
```

Goes to a specified page.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SwiperController-changeIndex(index: number, useAnimation?: boolean)--><!--Device-SwiperController-changeIndex(index: number, useAnimation?: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| useAnimation | boolean | No |

## changeIndex

```TypeScript
changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean)
```

Moves to a specific page.

> **NOTE：**
> 
> This API itself supports jumping without animation (set **animationMode** to **false** or
> **SwiperAnimationMode.NO_ANIMATION**). Avoid starting an animation with **changeIndex** and then interrupt it
> with **finishAnimation** to achieve animation-free jumping.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-SwiperController-changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean)--><!--Device-SwiperController-changeIndex(index: number, animationMode?: SwiperAnimationMode | boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| animationMode | [SwiperAnimationMode](arkts-arkui-swiperanimationmode-e.md) \| boolean | No |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **SwiperController** object.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-SwiperController-constructor()--><!--Device-SwiperController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fakeDragBy

```TypeScript
fakeDragBy(offset: number): boolean
```

Sets the drag distance of drag simulation.

> **NOTE：**
> 
> - The drag distance of drag simulation depends on the layout. You are advised to call this API before the layout,
> so that the drag effect can be displayed after the current frame layout. If this API is called multiple times
> before the layout, only the drag distance passed in the last call takes effect during the current frame layout.
> 
> - In the loop scenario where [loop](SwiperAttribute#loop) is set to **true**, if the drag distance of drag
> simulation is greater than the total layout length, the drag distance will be adjusted to the distance required
> to drag just far enough to display the first child node (when dragging toward the start of the layout) or the
> last child node (when dragging toward the end of the layout).
> 
> - The [onGestureSwipe](SwiperAttribute#onGestureSwipe) and
> [onContentWillScroll](SwiperAttribute#onContentWillScroll) events are not triggered during the drag. The
> [customContentTransition](SwiperAttribute#customContentTransition) event is triggered before the layout.
> Since the actual drag distance may be adjusted during the layout, if the passed drag distance is too large, the
> returned node display information may be inconsistent with the layout result when the event is triggered.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SwiperController-fakeDragBy(offset: number): boolean--><!--Device-SwiperController-fakeDragBy(offset: number): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## finishAnimation

```TypeScript
finishAnimation(callback?: VoidCallback)
```

Stops an animation.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-SwiperController-finishAnimation(callback?: VoidCallback)--><!--Device-SwiperController-finishAnimation(callback?: VoidCallback)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | No |

## isFakeDragging

```TypeScript
isFakeDragging(): boolean
```

Obtains whether drag simulation is enabled.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SwiperController-isFakeDragging(): boolean--><!--Device-SwiperController-isFakeDragging(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## preloadItems

```TypeScript
preloadItems(indices: Optional<Array<number>>): Promise<void>
```

Preloads child nodes for **Swiper**. After this API is called, all specified child nodes will be loaded at once.Therefore, for performance considerations, it is recommended that you load child nodes in batches. This API uses a promise to return the result.

If the **SwiperController** object is not bound to any **Swiper** component, any attempt to call APIs on it will result in a JavaScript exception, together with the error code 100004. Therefore, you are advised to use  
**try-catch** to handle potential exceptions when calling APIs on **SwiperController**.

When combining with [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md) and custom components, be aware that [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md) only retains custom components within the cache range. Components outside this range are removed. Therefore, make sure the indexes of nodes to be preloaded via this API are within the cache range to avoid issues.

> **NOTE：**
> 
> **preloadItems** of **Swiper** needs to be called after **Swiper** is created. You are advised to control the
> first preloading in the [onAppear](arkts-arkui-commonmethod-c.md#onappear) lifecycle of **Swiper**.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-SwiperController-preloadItems(indices: Optional<Array<number>>): Promise<void>--><!--Device-SwiperController-preloadItems(indices: Optional<Array<number>>): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| indices | [Optional](arkts-arkui-optional-t.md)&lt;Array&lt;number&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## showNext

```TypeScript
showNext()
```

Turns to the next page. The page turning includes a transition animation, with the duration set by the  
[duration](SwiperAttribute#duration) attribute of the **Swiper** component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-SwiperController-showNext()--><!--Device-SwiperController-showNext()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showPrevious

```TypeScript
showPrevious()
```

Turns to the previous page. The page turning includes a transition animation, with the duration set by the  
[duration](SwiperAttribute#duration) attribute of the **Swiper** component.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

<!--Device-SwiperController-showPrevious()--><!--Device-SwiperController-showPrevious()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startFakeDrag

```TypeScript
startFakeDrag(): boolean
```

Enables drag simulation.

> **NOTE：**
> 
> - If the **Swiper** component is dragged using real gestures or the drag simulation is enabled, the API returns
> **false**, indicating that the operation fails.
> 
> - Simulated drag cannot trigger nested scrolling.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SwiperController-startFakeDrag(): boolean--><!--Device-SwiperController-startFakeDrag(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## stopFakeDrag

```TypeScript
stopFakeDrag(): boolean
```

Disables drag simulation.

> **NOTE：**
> 
> After drag simulation is enabled, it will end if a real drag gesture is received.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-SwiperController-stopFakeDrag(): boolean--><!--Device-SwiperController-stopFakeDrag(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
