# UIObserver

Register callbacks to observe ArkUI behavior.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class UIObserver--><!--Device-unnamed-export declare class UIObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addGlobalGestureListener

```TypeScript
addGlobalGestureListener(type: GestureListenerType,
      option: GestureObserverConfigs, callback: GestureListenerCallback): void
```

Registers a callback to monitor the gesture trigger information.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-addGlobalGestureListener(type: GestureListenerType,      option: GestureObserverConfigs, callback: GestureListenerCallback): void--><!--Device-UIObserver-addGlobalGestureListener(type: GestureListenerType,      option: GestureObserverConfigs, callback: GestureListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [GestureListenerType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-gesturelistenertype-e.md) | Yes | The type of gesture to monitor. |
| option | [GestureObserverConfigs](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-gestureobserverconfigs-i.md) | Yes | The options when bind the global listener. |
| callback | [GestureListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gesturelistenercallback-t.md) | Yes | The callback function to be called when any gesture's state is updated. |

## offAfterPanEnd

```TypeScript
offAfterPanEnd(callback?: PanListenerCallback): void
```

Removes a callback function to be called after panGesture onActionEnd is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offAfterPanEnd(callback?: PanListenerCallback): void--><!--Device-UIObserver-offAfterPanEnd(callback?: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offAfterPanStart

```TypeScript
offAfterPanStart(callback?: PanListenerCallback): void
```

Removes a callback function to be called after panGesture onActionStart is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offAfterPanStart(callback?: PanListenerCallback): void--><!--Device-UIObserver-offAfterPanStart(callback?: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offBeforePanEnd

```TypeScript
offBeforePanEnd(callback?: PanListenerCallback): void
```

Removes a callback function to be called before panGesture onActionEnd is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offBeforePanEnd(callback?: PanListenerCallback): void--><!--Device-UIObserver-offBeforePanEnd(callback?: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offBeforePanStart

```TypeScript
offBeforePanStart(callback?: PanListenerCallback): void
```

Removes a callback function to be called before panGesture onActionStart is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offBeforePanStart(callback?: PanListenerCallback): void--><!--Device-UIObserver-offBeforePanStart(callback?: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offDensityUpdate

```TypeScript
offDensityUpdate(callback?: Callback<observer.DensityInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offDensityUpdate(callback?: Callback<observer.DensityInfo>): void--><!--Device-UIObserver-offDensityUpdate(callback?: Callback<observer.DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.DensityInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offDidClick

```TypeScript
offDidClick(callback?: ClickEventListenerCallback): void
```

Removes a callback function to be called after clickEvent is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offDidClick(callback?: ClickEventListenerCallback): void--><!--Device-UIObserver-offDidClick(callback?: ClickEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClickEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-clickeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offDidLayout

```TypeScript
offDidLayout(callback?: Callback<void>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offDidLayout(callback?: Callback<void>): void--><!--Device-UIObserver-offDidLayout(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offDidTap

```TypeScript
offDidTap(callback?: GestureEventListenerCallback): void
```

Removes a callback function to be called after tapGesture is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offDidTap(callback?: GestureEventListenerCallback): void--><!--Device-UIObserver-offDidTap(callback?: GestureEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gestureeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationSizeChange

```TypeScript
offNavDestinationSizeChange(callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with 'onNavDestinationSizeChange()'.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationSizeChange(callback?: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-offNavDestinationSizeChange(callback?: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationSizeChangeByUniqueId

```TypeScript
offNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with 'onNavDestinationSizeChangeByUniqueId()'.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-offNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | int | Yes | The uniqueId of the Navigation to which NavDestination belongs. <br>The value should be an integer. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationSwitch

```TypeScript
offNavDestinationSwitch(callback?: Callback<observer.NavDestinationSwitchInfo>): void
```

Removes a callback function that was previously registered with `onNavDestinationSwitch`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationSwitch(callback?: Callback<observer.NavDestinationSwitchInfo>): void--><!--Device-UIObserver-offNavDestinationSwitch(callback?: Callback<observer.NavDestinationSwitchInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationSwitchInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationSwitch

```TypeScript
offNavDestinationSwitch(
    observerOptions: observer.NavDestinationSwitchObserverOptions,
    callback?: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Removes a callback function that was previously registered with `onNavDestinationSwitch`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationSwitch(    observerOptions: observer.NavDestinationSwitchObserverOptions,    callback?: Callback<observer.NavDestinationSwitchInfo>  ): void--><!--Device-UIObserver-offNavDestinationSwitch(    observerOptions: observer.NavDestinationSwitchObserverOptions,    callback?: Callback<observer.NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerOptions | observer.NavDestinationSwitchObserverOptions | Yes | Options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationSwitchInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationUpdate

```TypeScript
offNavDestinationUpdate(
    options: observer.NavDestinationSwitchObserverOptions,
    callback?: Callback<observer.NavDestinationInfo>
    ): void
```

Removes a callback function that was previously registered with `onNavDestinationUpdate`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationUpdate(    options: observer.NavDestinationSwitchObserverOptions,    callback?: Callback<observer.NavDestinationInfo>    ): void--><!--Device-UIObserver-offNavDestinationUpdate(    options: observer.NavDestinationSwitchObserverOptions,    callback?: Callback<observer.NavDestinationInfo>    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.NavDestinationSwitchObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and navigation ID will be removed. |

## offNavDestinationUpdate

```TypeScript
offNavDestinationUpdate(callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `onNavDestinationUpdate`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationUpdate(callback?: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-offNavDestinationUpdate(callback?: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationUpdateByUniqueId

```TypeScript
offNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `onNavDestinationUpdateByUniqueId`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-offNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback?: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | int | Yes | The uniqueId of the navigation. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNodeRenderState

```TypeScript
offNodeRenderState(nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void
```

Removes a callback function for node render state monitoring.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offNodeRenderState(nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void--><!--Device-UIObserver-offNodeRenderState(nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nodeIdentity | [NodeIdentity](../../apis-arkui/arkts-apis/arkts-arkui-nodeidentity-t.md) | Yes | The identity of the target node |
| callback | [NodeRenderStateChangeCallback](../../apis-arkui/arkts-apis/arkts-arkui-noderenderstatechangecallback-t.md) | No | The callback function to remove. If not provided, all callbacks will be removed. |

## offRouterPageSizeChange

```TypeScript
offRouterPageSizeChange(callback?: Callback<observer.RouterPageInfo>): void
```

Removes a callback function that was previously registered with 'onRouterPageSizeChange()'.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offRouterPageSizeChange(callback?: Callback<observer.RouterPageInfo>): void--><!--Device-UIObserver-offRouterPageSizeChange(callback?: Callback<observer.RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.RouterPageInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offRouterPageUpdate

```TypeScript
offRouterPageUpdate(callback?: Callback<observer.RouterPageInfo>): void
```

Removes a callback function that was previously registered with `onRouterPageUpdate`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offRouterPageUpdate(callback?: Callback<observer.RouterPageInfo>): void--><!--Device-UIObserver-offRouterPageUpdate(callback?: Callback<observer.RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.RouterPageInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offScrollEvent

```TypeScript
offScrollEvent(options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offScrollEvent(options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void--><!--Device-UIObserver-offScrollEvent(options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.ObserverOptions | Yes |  |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.ScrollEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and scroll ID will be removed. |

## offScrollEvent

```TypeScript
offScrollEvent(callback?: Callback<observer.ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `onScrollEvent()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offScrollEvent(callback?: Callback<observer.ScrollEventInfo>): void--><!--Device-UIObserver-offScrollEvent(callback?: Callback<observer.ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.ScrollEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offSwiperContentUpdate

```TypeScript
offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void
```

Removes a callback function that was previously registered with `onSwiperContentUpdate`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void--><!--Device-UIObserver-offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SwiperContentInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offSwiperContentUpdate

```TypeScript
offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void
```

Removes a callback function that was previously registered with `onSwiperContentUpdate`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void--><!--Device-UIObserver-offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SwiperContentInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offTabChange

```TypeScript
offTabChange(config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `onTabChange`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTabChange(config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-offTabChange(config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## offTabChange

```TypeScript
offTabChange(callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `onTabChange`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTabChange(callback?: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-offTabChange(callback?: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offTabContentUpdate

```TypeScript
offTabContentUpdate(options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTabContentUpdate(options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-offTabContentUpdate(options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## offTabContentUpdate

```TypeScript
offTabContentUpdate(callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTabContentUpdate(callback?: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-offTabContentUpdate(callback?: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## offTextChange

```TypeScript
offTextChange(callback?: Callback<observer.TextChangeEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTextChange(callback?: Callback<observer.TextChangeEventInfo>): void--><!--Device-UIObserver-offTextChange(callback?: Callback<observer.TextChangeEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TextChangeEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offTextChange

```TypeScript
offTextChange(identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offTextChange(identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void--><!--Device-UIObserver-offTextChange(identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identity | observer.ObserverOptions | Yes | Identity options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TextChangeEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offWillClick

```TypeScript
offWillClick(callback?: ClickEventListenerCallback): void
```

Removes a callback function to be called before clickEvent is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offWillClick(callback?: ClickEventListenerCallback): void--><!--Device-UIObserver-offWillClick(callback?: ClickEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClickEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-clickeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offWillDraw

```TypeScript
offWillDraw(callback?: Callback<void>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offWillDraw(callback?: Callback<void>): void--><!--Device-UIObserver-offWillDraw(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offWillTap

```TypeScript
offWillTap(callback?: GestureEventListenerCallback): void
```

Removes a callback function to be called before tapGesture is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offWillTap(callback?: GestureEventListenerCallback): void--><!--Device-UIObserver-offWillTap(callback?: GestureEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gestureeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offWindowSizeLayoutBreakpointChange

```TypeScript
offWindowSizeLayoutBreakpointChange(callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void
```

Removes a previously registered callback function for window size layout breakpoint changes. If no callback is provided, all callbacks for the specified context will be removed.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-offWindowSizeLayoutBreakpointChange(callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void--><!--Device-UIObserver-offWindowSizeLayoutBreakpointChange(callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.WindowSizeLayoutBreakpointInfo&gt; | No | The specific callback function to remove. If not provided, all callbacks for the given event type and context will be removed. |

## onAfterPanEnd

```TypeScript
onAfterPanEnd(callback: PanListenerCallback): void
```

Registers a callback function to be called after panGesture onActionEnd is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onAfterPanEnd(callback: PanListenerCallback): void--><!--Device-UIObserver-onAfterPanEnd(callback: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | Yes | The callback function to be called when the panGesture will be trigger or after. |

## onAfterPanStart

```TypeScript
onAfterPanStart(callback: PanListenerCallback): void
```

Registers a callback function to be called after panGesture onActionStart is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onAfterPanStart(callback: PanListenerCallback): void--><!--Device-UIObserver-onAfterPanStart(callback: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | Yes | The callback function to be called when the panGesture will be trigger or after. |

## onBeforePanEnd

```TypeScript
onBeforePanEnd(callback: PanListenerCallback): void
```

Registers a callback function to be called before panGesture onActionEnd is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onBeforePanEnd(callback: PanListenerCallback): void--><!--Device-UIObserver-onBeforePanEnd(callback: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | Yes | The callback function to be called when the panGesture will be trigger or after. |

## onBeforePanStart

```TypeScript
onBeforePanStart(callback: PanListenerCallback): void
```

Registers a callback function to be called before panGesture onActionStart is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onBeforePanStart(callback: PanListenerCallback): void--><!--Device-UIObserver-onBeforePanStart(callback: PanListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [PanListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-panlistenercallback-t.md) | Yes | The callback function to be called when the panGesture will be trigger or after. |

## onDensityUpdate

```TypeScript
onDensityUpdate(callback: Callback<observer.DensityInfo>): void
```

Registers a callback function to be called when the screen density in a ui context is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onDensityUpdate(callback: Callback<observer.DensityInfo>): void--><!--Device-UIObserver-onDensityUpdate(callback: Callback<observer.DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.DensityInfo&gt; | Yes | The callback function to be called when the screen density is updated. |

## onDidClick

```TypeScript
onDidClick(callback: ClickEventListenerCallback): void
```

Registers a callback function to be called after clickEvent is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onDidClick(callback: ClickEventListenerCallback): void--><!--Device-UIObserver-onDidClick(callback: ClickEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClickEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-clickeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## onDidLayout

```TypeScript
onDidLayout(callback: Callback<void>): void
```

Registers a callback function to be called when the layout is done.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onDidLayout(callback: Callback<void>): void--><!--Device-UIObserver-onDidLayout(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | The callback function to be called when the layout is done. |

## onDidTap

```TypeScript
onDidTap(callback: GestureEventListenerCallback): void
```

Registers a callback function to be called after tapGesture is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onDidTap(callback: GestureEventListenerCallback): void--><!--Device-UIObserver-onDidTap(callback: GestureEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gestureeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## onNavDestinationSizeChange

```TypeScript
onNavDestinationSizeChange(callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback function to be called when the visible NavDestination's size is changed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationSizeChange(callback: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-onNavDestinationSizeChange(callback: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the visible NavDestination's size is changed. |

## onNavDestinationSizeChangeByUniqueId

```TypeScript
onNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback function to be called when the size of the visible NavDestination of the navigation with the specified uniqueId changes.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-onNavDestinationSizeChangeByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | int | Yes | The uniqueId of the Navigation to which NavDestination belongs. <br>The value should be an integer. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the visible NavDestination's size is changed. |

## onNavDestinationSwitch

```TypeScript
onNavDestinationSwitch(callback: Callback<observer.NavDestinationSwitchInfo>): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationSwitch(callback: Callback<observer.NavDestinationSwitchInfo>): void--><!--Device-UIObserver-onNavDestinationSwitch(callback: Callback<observer.NavDestinationSwitchInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationSwitchInfo&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |

## onNavDestinationSwitch

```TypeScript
onNavDestinationSwitch(
    observerOptions: observer.NavDestinationSwitchObserverOptions,
    callback: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationSwitch(    observerOptions: observer.NavDestinationSwitchObserverOptions,    callback: Callback<observer.NavDestinationSwitchInfo>  ): void--><!--Device-UIObserver-onNavDestinationSwitch(    observerOptions: observer.NavDestinationSwitchObserverOptions,    callback: Callback<observer.NavDestinationSwitchInfo>  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerOptions | observer.NavDestinationSwitchObserverOptions | Yes | Options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationSwitchInfo&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |

## onNavDestinationUpdate

```TypeScript
onNavDestinationUpdate(
    options: observer.NavDestinationSwitchObserverOptions,
    callback: Callback<observer.NavDestinationInfo>
    ): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationUpdate(    options: observer.NavDestinationSwitchObserverOptions,    callback: Callback<observer.NavDestinationInfo>    ): void--><!--Device-UIObserver-onNavDestinationUpdate(    options: observer.NavDestinationSwitchObserverOptions,    callback: Callback<observer.NavDestinationInfo>    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.NavDestinationSwitchObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

## onNavDestinationUpdate

```TypeScript
onNavDestinationUpdate(callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationUpdate(callback: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-onNavDestinationUpdate(callback: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

## onNavDestinationUpdateByUniqueId

```TypeScript
onNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void--><!--Device-UIObserver-onNavDestinationUpdateByUniqueId(navigationUniqueId: int, callback: Callback<observer.NavDestinationInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | int | Yes | The uniqueId of the navigation. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

## onNodeRenderState

```TypeScript
onNodeRenderState(nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void
```

Registers a callback function to be called when the specific node's render state changed. This callback will be executed once immediately when the register is successful. [Notes]: 1. Be aware of the limit on the number of nodes: For performance considerations, the system has imposed a limit on the number of nodes that can be registered for monitoring in a single UI instance, exception will be thrown if overmuch. Please use this interface with caution. 2. Understanding scenarios where notifications may not occur: In general, within container components that have view or page switching functionality, when a view or page within the screen is moved outside the screen, the components previously within the screen should be removed from the render tree and should receive a RENDER_OUT notification. However, this is not always the case, as some scenarios involve views or components being moved outside the screen's display range without triggering a RENDER_OUT notification. For example, some components with caching capabilities may affect this behavior, and swiper is one such component. The cacheCount property of the swiper component allows you to force, via its second parameter isShow, that even if the current page is moved outside the display range, it remains in the render tree. This can be useful in scenarios where multiple pages are displayed on the screen simultaneously. Another example is scrolling components like list or scroll, where their internal content remains in the render tree even if it is scrolled outside the screen's display range, provided that lazyForEach/Repeat is not used. As a result, there will be no changes to the render state. Once you understand the principles behind the triggers for render state changes, these scenarios will become easier to comprehend.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onNodeRenderState(nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void--><!--Device-UIObserver-onNodeRenderState(nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nodeIdentity | [NodeIdentity](../../apis-arkui/arkts-apis/arkts-arkui-nodeidentity-t.md) | Yes | The identity of the target node |
| callback | [NodeRenderStateChangeCallback](../../apis-arkui/arkts-apis/arkts-arkui-noderenderstatechangecallback-t.md) | Yes | The callback function executed when the rendering state of the component node changes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [161001](../../apis-arkui/errorcode-node-render-monitor.md#161001-number-of-nodes-listening-for-render-state-exceeds-the-limit) | The count of nodes monitoring render state is over the limitation. |

## onRouterPageSizeChange

```TypeScript
onRouterPageSizeChange(callback: Callback<observer.RouterPageInfo>): void
```

Registers a callback function to be called when the visible router page's size is changed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onRouterPageSizeChange(callback: Callback<observer.RouterPageInfo>): void--><!--Device-UIObserver-onRouterPageSizeChange(callback: Callback<observer.RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.RouterPageInfo&gt; | Yes | The callback function to be called when the visible router page's size is changed. |

## onRouterPageUpdate

```TypeScript
onRouterPageUpdate(callback: Callback<observer.RouterPageInfo>): void
```

Registers a callback function to be called when the router page in a ui context is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onRouterPageUpdate(callback: Callback<observer.RouterPageInfo>): void--><!--Device-UIObserver-onRouterPageUpdate(callback: Callback<observer.RouterPageInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.RouterPageInfo&gt; | Yes | The callback function to be called when the router page is updated. |

## onScrollEvent

```TypeScript
onScrollEvent(options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onScrollEvent(options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void--><!--Device-UIObserver-onScrollEvent(options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |

## onScrollEvent

```TypeScript
onScrollEvent(callback: Callback<observer.ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onScrollEvent(callback: Callback<observer.ScrollEventInfo>): void--><!--Device-UIObserver-onScrollEvent(callback: Callback<observer.ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |

## onSwiperContentUpdate

```TypeScript
onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void
```

Registers a callback function to be called when the swiper content is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void--><!--Device-UIObserver-onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SwiperContentInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | Yes | The callback function to be called when the content is updated. |

## onSwiperContentUpdate

```TypeScript
onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void
```

Registers a callback function to be called when the swiper content is updated.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void--><!--Device-UIObserver-onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[SwiperContentInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | Yes | The callback function to be called when the swiper content is updated. |

## onTabChange

```TypeScript
onTabChange(config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTabChange(config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-onTabChange(config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

## onTabChange

```TypeScript
onTabChange(callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTabChange(callback: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-onTabChange(callback: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

## onTabContentUpdate

```TypeScript
onTabContentUpdate(options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTabContentUpdate(options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-onTabContentUpdate(options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent show or hide. |

## onTabContentUpdate

```TypeScript
onTabContentUpdate(callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTabContentUpdate(callback: Callback<observer.TabContentInfo>): void--><!--Device-UIObserver-onTabContentUpdate(callback: Callback<observer.TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

## onTextChange

```TypeScript
onTextChange(callback: Callback<observer.TextChangeEventInfo>): void
```

Registers a callback function to be called when text field's content is changed.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTextChange(callback: Callback<observer.TextChangeEventInfo>): void--><!--Device-UIObserver-onTextChange(callback: Callback<observer.TextChangeEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TextChangeEventInfo&gt; | Yes | The callback function to be called when text field's content is changed. |

## onTextChange

```TypeScript
onTextChange(identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void
```

Registers a callback function to be called when text field's content is changed.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onTextChange(identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void--><!--Device-UIObserver-onTextChange(identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identity | observer.ObserverOptions | Yes | Identity options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.TextChangeEventInfo&gt; | Yes | The callback function to be called when the text field's content is changed. |

## onWillClick

```TypeScript
onWillClick(callback: ClickEventListenerCallback): void
```

Registers a callback function to be called before clickEvent is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onWillClick(callback: ClickEventListenerCallback): void--><!--Device-UIObserver-onWillClick(callback: ClickEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ClickEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-clickeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## onWillDraw

```TypeScript
onWillDraw(callback: Callback<void>): void
```

Registers a callback function to be called when the draw command will be drawn.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onWillDraw(callback: Callback<void>): void--><!--Device-UIObserver-onWillDraw(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | The callback function to be called when the draw command will be drawn. |

## onWillTap

```TypeScript
onWillTap(callback: GestureEventListenerCallback): void
```

Registers a callback function to be called before tapGesture is called.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onWillTap(callback: GestureEventListenerCallback): void--><!--Device-UIObserver-onWillTap(callback: GestureEventListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureEventListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gestureeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## onWindowSizeLayoutBreakpointChange

```TypeScript
onWindowSizeLayoutBreakpointChange(callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void
```

Registers a callback function to be called when the window size layout breakpoint changes. This method allows observing changes in window size breakpoints which can be used to adapt UI layouts responsively based on window dimensions.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-onWindowSizeLayoutBreakpointChange(callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void--><!--Device-UIObserver-onWindowSizeLayoutBreakpointChange(callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;observer.WindowSizeLayoutBreakpointInfo&gt; | Yes | The callback function to be called when the window size layout breakpoint changes. The callback receives a [WindowSizeLayoutBreakpointInfo](arkts-na-uiobserver-windowsizelayoutbreakpointinfo-i.md) object containing the current width and height breakpoint classifications. |

## removeGlobalGestureListener

```TypeScript
removeGlobalGestureListener(type: GestureListenerType, callback?: GestureListenerCallback): void
```

Removes a callback function for one gesture listener type.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIObserver-removeGlobalGestureListener(type: GestureListenerType, callback?: GestureListenerCallback): void--><!--Device-UIObserver-removeGlobalGestureListener(type: GestureListenerType, callback?: GestureListenerCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [GestureListenerType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-gesturelistenertype-e.md) | Yes | The type of event to remove the listener for. |
| callback | [GestureListenerCallback](../../apis-arkui/arkts-apis/arkts-arkui-gesturelistenercallback-t.md) | No | The callback function to be removed. If not provided, all callbacks for the given gesture type will be removed. |

