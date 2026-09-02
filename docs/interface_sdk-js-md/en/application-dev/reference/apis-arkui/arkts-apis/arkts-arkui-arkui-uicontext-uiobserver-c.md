# UIObserver

Provides APIs for listening for UI component behavior changes.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 11.
> 
> - In the following API examples, you must first use [getUIObserver()](arkts-arkui-arkui-uicontext-uicontext-c.md#getuiobserver) in
> **UIContext** to obtain a **UIObserver** instance, and then call the APIs using the obtained instance.
> 
> - UIObserver can only listen for relevant information within the current process and does not support obtaining
> information in cross-process scenarios<!--Del--
> such as UIExtensionComponent<!--
> DelEnd-->.

**Since:** 11

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## addGlobalGestureListener

```TypeScript
addGlobalGestureListener(type: GestureListenerType,
      option: GestureObserverConfigs, callback: GestureListenerCallback): void
```

Registers a callback to listen for gesture triggering information.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [GestureListenerType](arkts-arkui-arkui-uicontext-gesturelistenertype-e.md) | Yes | Type of gesture to listen for. |
| option | [GestureObserverConfigs](arkts-arkui-arkui-uicontext-gestureobserverconfigs-i.md) | Yes | Configuration options for binding the global listener. |
| callback | [GestureListenerCallback](arkts-arkui-gesturelistenercallback-t.md) | Yes | Callback triggered when the gesture state updates. |

**Examples**

This example uses global gesture listeners to monitor the trigger status of three independent areas (Tap, Pan, and LongPress) in real time, records the trigger count and last operation information for each gesture, and automatically manages the registration and unregistration of listeners during the component's lifecycle.

```TypeScript
// Index.ets
// Example usage of uiObserver.addGlobalGestureListener(type, option, callback)
// uiObserver.removeGlobalGestureListener(type, callback)

import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureListenerCallback } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tapCount: number = 0;
  @State panCount: number = 0;
  @State longPressCount: number = 0;
  @State lastAction: string = 'None';
  @State lastArea: string = 'None';

  // Store listener callback references.
  private tapCallback?: GestureListenerCallback;
  private panCallback?: GestureListenerCallback;
  private longPressCallback?: GestureListenerCallback;

  // Enable global listeners.
  aboutToAppear() {
    this.addGlobalListeners();
  }
  // Disable global listeners.
  aboutToDisappear() {
    this.removeGlobalListeners();
  }

  private addGlobalListeners() {
    const observer = this.getUIContext().getUIObserver();

    // Tap listener.
    this.tapCallback = (info: GestureTriggerInfo) => {
      if (info.event?.target?.id === 'tap-area') {
        this.tapCount++;
        this.lastAction = 'Tap';
        this.lastArea = 'Tap area';
      }
    };
    observer.addGlobalGestureListener(
      GestureListenerType.TAP,
      { actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END] },
      this.tapCallback
    );

    // Pan listener.
    this.panCallback = (info: GestureTriggerInfo) => {
      if (info.event?.target?.id === 'pan-area') {
        this.panCount++;
        this.lastAction = 'Pan';
        this.lastArea = 'Pan area';
      }
    };
    observer.addGlobalGestureListener(
      GestureListenerType.PAN,
      {
        actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END]
      },
      this.panCallback
    );

    // LongPress listener.
    this.longPressCallback = (info: GestureTriggerInfo) => {
      if (info.event?.target?.id === 'longpress-area') {
        this.longPressCount++;
        this.lastAction = 'Long press';
        this.lastArea = 'Long press area';
      }
    };
    observer.addGlobalGestureListener(
      GestureListenerType.LONG_PRESS,
      {
        actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END]
      },
      this.longPressCallback
    );
  }

  private removeGlobalListeners() {
    const observer = this.getUIContext().getUIObserver();
// 0, 2, and 1 indicate the tap, pan, and long-press gesture types, respectively, which are used to remove the corresponding global listeners.
    if (this.tapCallback) {
      observer.removeGlobalGestureListener(GestureListenerType.TAP, this.tapCallback);
    }
    if (this.panCallback) {
      observer.removeGlobalGestureListener(GestureListenerType.PAN, this.panCallback);
    }
    if (this.longPressCallback) {
      observer.removeGlobalGestureListener(GestureListenerType.LONG_PRESS, this.longPressCallback);
    }
  }

  build() {
    Column() {
      // Gesture data statistics panel.
      Row({ space: 30 }) {
        Column() {
          Text('Tap count:').fontSize(16)
          Text(`${this.tapCount}`).fontSize(24).fontColor('#FF6B81')
        }
        Column() {
          Text('Pan count:').fontSize(16)
          Text(`${this.panCount}`).fontSize(24).fontColor('#7BED9F')
        }
        Column() {
          Text('Long-press count:').fontSize(16)
          Text(`${this.longPressCount}`).fontSize(24).fontColor('#70A1FF')
        }
      }
      .margin(10)

      Text(`Last action: ${this.lastAction} (${this.lastArea})`)
        .fontSize(18)
        .margin(10)

      // Gesture areas.
      Row() {
        Text('Tap area').fontSize(18)
      }
      .id('tap-area')
      .width('90%')
      .height(120)
      .margin(10)
      .border({ width: 2, color: '#FF6B81' })
      .justifyContent(FlexAlign.Center)
      .gesture(TapGesture().onAction((event: GestureEvent) => {
        // Implementation details.
      }))

      Row() {
        Text('Pan area').fontSize(18)
      }
      .id('pan-area')
      .width('90%')
      .height(120)
      .margin(10)
      .border({ width: 2, color: '#7BED9F' })
      .justifyContent(FlexAlign.Center)
      .gesture(
        PanGesture()
          .onActionStart((event: GestureEvent) => {
            // Implementation details.
          })
          .onActionEnd((event: GestureEvent) => {
            // Implementation details.
          })
      )

      Row() {
        Text('LongPress area').fontSize(18)
      }
      .id('longpress-area')
      .width('90%')
      .height(120)
      .margin(10)
      .border({ width: 2, color: '#70A1FF' })
      .justifyContent(FlexAlign.Center)
      .gesture(
        LongPressGesture()
          .onAction((event: GestureEvent) => {
            // Implementation details.
          })
          .onActionEnd((event: GestureEvent) => {
            // Implementation details.
          })
      )
    }
    .width('100%')
    .height('100%')
  }
}
```

## off('navDestinationUpdate')

```TypeScript
off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | The type of event to remove the listener for. Must be 'navDestinationUpdate'. |
| options | { navigationId: ResourceStr } | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and navigation ID will be removed. |

## off('navDestinationUpdate')

```TypeScript
off(type: 'navDestinationUpdate', callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | The type of event to remove the listener for. Must be 'navDestinationUpdate'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('navDestinationUpdateByUniqueId')

```TypeScript
off(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdateByUniqueId' | Yes | The type of event to remove the listener for. Must be 'navDestinationUpdateByUniqueId'. |
| navigationUniqueId | number | Yes | The uniqueId of the navigation. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('scrollEvent')

```TypeScript
off(type: 'scrollEvent', options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to remove the listener for. Must be 'scrollEvent'. |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.ScrollEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and scroll ID will be removed. |

## off('scrollEvent')

```TypeScript
off(type: 'scrollEvent', callback?: Callback<observer.ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to remove the listener for. Must be 'scrollEvent'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.ScrollEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('routerPageUpdate')

```TypeScript
off(type: 'routerPageUpdate', callback?: Callback<observer.RouterPageInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'routerPageUpdate' | Yes | The type of event to remove the listener for. Must be 'routerPageUpdate'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.RouterPageInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('densityUpdate')

```TypeScript
off(type: 'densityUpdate', callback?: Callback<observer.DensityInfo>): void
```

Unregisters the listener for screen pixel density changes.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'densityUpdate' | Yes | Event type. The value **'densityUpdate'** indicates the pixel density changes of the screen. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.DensityInfo&gt; | No | Target listener to unregister. If no parameter is provided, all screen pixel density change listeners for the current [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) are removed. |

## off('willDraw')

```TypeScript
off(type: 'willDraw', callback?: Callback<void>): void
```

Unregisters the listener for drawing instruction dispatch in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willDraw' | Yes | Event event. The value **'willDraw'** indicates whether drawing is about to occur. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Target listener to unregister. If no parameter is provided, all drawing instruction dispatch listeners are unregistered. |

## off('didLayout')

```TypeScript
off(type: 'didLayout', callback?: Callback<void>): void
```

Unregisters the listener for layout completion status in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didLayout' | Yes | Event type. The value **'didLayout'** indicates whether the layout has been completed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Target listener to unregister. If no parameter is provided, all layout completion listeners are unregistered. |

## off('navDestinationSwitch')

```TypeScript
off(
    type: 'navDestinationSwitch',
    callback?: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationSwitch' | Yes | The type of event to remove the listener for. Must be 'navDestinationSwitch'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationSwitchInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('navDestinationSwitch')

```TypeScript
off(
    type: 'navDestinationSwitch',
    observerOptions: observer.NavDestinationSwitchObserverOptions,
    callback?: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationSwitch' | Yes | The type of event to remove the listener for. Must be 'navDestinationSwitch'. |
| observerOptions | observer.NavDestinationSwitchObserverOptions | Yes | Options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationSwitchInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('willClick')

```TypeScript
off(type: 'willClick', callback?: ClickEventListenerCallback): void
```

Removes a callback function to be called before clickEvent is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willClick' | Yes | The type of event to remove the listener for. |
| callback | [ClickEventListenerCallback](arkts-arkui-clickeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('didClick')

```TypeScript
off(type: 'didClick', callback?: ClickEventListenerCallback): void
```

Removes a callback function to be called after clickEvent is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didClick' | Yes | The type of event to remove the listener for. |
| callback | [ClickEventListenerCallback](arkts-arkui-clickeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('willClick')

```TypeScript
off(type: 'willClick', callback?: GestureEventListenerCallback): void
```

Removes a callback function to be called before tapGesture is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willClick' | Yes | The type of event to remove the listener for. |
| callback | [GestureEventListenerCallback](arkts-arkui-gestureeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('didClick')

```TypeScript
off(type: 'didClick', callback?: GestureEventListenerCallback): void
```

Removes a callback function to be called after tapGesture is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didClick' | Yes | The type of event to remove the listener for. |
| callback | [GestureEventListenerCallback](arkts-arkui-gestureeventlistenercallback-t.md) | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('beforePanStart')

```TypeScript
off(type: 'beforePanStart', callback?: PanListenerCallback): void
```

Unregisters the listener for pan gesture onActionStart pre-execution events, canceling callbacks registered via [on('beforePanStart')](#onbeforepanstart).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'beforePanStart' | Yes | Event type. The value is fixed at **'beforePanStart'**, indicating command dispatch before the execution of the pan gesture onActionStart event. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | No | Target listener to unregister. If no parameter is provided, all callback listeners for command dispatch before the execution of the pan gesture onActionStart event will be removed. |

## off('beforePanEnd')

```TypeScript
off(type: 'beforePanEnd', callback?: PanListenerCallback): void
```

Unregisters the listener for pan gesture onActionEnd pre-execution events, canceling callbacks registered via [on('beforePanEnd')](#onbeforepanend).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'beforePanEnd' | Yes | Event type. The value is fixed at **'beforePanEnd'**, indicating command dispatch before the execution of the pan gesture onActionEnd event. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | No | Target listener to unregister. If no parameter is provided, all callback listeners for command dispatch before the execution of the pan gesture onActionEnd event will be removed. |

## off('afterPanStart')

```TypeScript
off(type: 'afterPanStart', callback?: PanListenerCallback): void
```

Unregisters the listener for pan gesture onActionStart post-execution events, canceling callbacks registered via [on('afterPanStart')](#onafterpanstart).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'afterPanStart' | Yes | Event type. The value is fixed at **'afterPanStart'**, indicating command dispatch after the execution of the pan gesture onActionStart event. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | No | Target listener to unregister. If no parameter is provided, all callback listeners for command dispatch after the execution of the pan gesture onActionStart event will be removed. |

## off('afterPanEnd')

```TypeScript
off(type: 'afterPanEnd', callback?: PanListenerCallback): void
```

Unregisters the listener for pan gesture onActionEnd post-execution events, canceling callbacks registered via [on('afterPanEnd')](#onafterpanend).

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'afterPanEnd' | Yes | Event type. The value is fixed at **'afterPanEnd'**, indicating command dispatch after the execution of the pan gesture onActionEnd event. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | No | Target listener to unregister. If no parameter is provided, all callback listeners for command dispatch after the execution of the pan gesture onActionEnd event will be removed. |

## off('tabContentUpdate')

```TypeScript
off(type: 'tabContentUpdate', options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | The type of event to remove the listener for. Must be 'tabContentUpdate'. |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## off('tabContentUpdate')

```TypeScript
off(type: 'tabContentUpdate', callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | The type of event to remove the listener for. Must be 'tabContentUpdate'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## off('tabChange')

```TypeScript
off(type: 'tabChange', config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabChange' | Yes | The type of event to remove the listener for. Must be 'tabChange'. |
| config | observer.ObserverOptions | Yes | The config object. Includes the observed component id. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |

## off('tabChange')

```TypeScript
off(type: 'tabChange', callback?: Callback<observer.TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabChange' | Yes | The type of event to remove the listener for. Must be 'tabChange'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('windowSizeLayoutBreakpointChange')

```TypeScript
off(type: 'windowSizeLayoutBreakpointChange', callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void
```

Unregisters previously registered window size layout breakpoint change listeners. If no callback is specified, all listeners for the current UI context are removed. This API uses an asynchronous callback to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'windowSizeLayoutBreakpointChange' | Yes | Event type. The value is fixed at **'windowSizeLayoutBreakpointChange'**, indicating window size layout breakpoint changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.WindowSizeLayoutBreakpointInfo&gt; | No | Target listener to unregister. If no parameter is provided, all window size layout breakpoint change listeners for the current [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) are removed. |

## off('nodeRenderState')

```TypeScript
off(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void
```

Unregisters the callback for listening for node rendering state changes.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'nodeRenderState' | Yes | Event type. The value is fixed at **'nodeRenderState'**. |
| nodeIdentity | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | Yes | Node ID. |
| callback | [NodeRenderStateChangeCallback](arkts-arkui-noderenderstatechangecallback-t.md) | No | Target listener to unregister. If no parameter is provided, all node rendering state change listeners are unregistered. |

## off('textChange')

```TypeScript
off(type: 'textChange', callback?: Callback<observer.TextChangeEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | The type of event to remove the listener for. Must be 'textChange'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TextChangeEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## off('textChange')

```TypeScript
off(type: 'textChange', identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | The type of event to remove the listener for. Must be 'textChange'. |
| identity | observer.ObserverOptions | Yes | Identity options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TextChangeEventInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

## offNavDestinationSizeChange

```TypeScript
offNavDestinationSizeChange(callback?: Callback<observer.NavDestinationInfo>): void
```

Removes the listener callback registered using the **onNavDestinationSizeChange** API. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | No | Callback to be removed. If no parameter is passed, all callbacks are removed. |

**Examples**

See the example for the [onNavDestinationSizeChange](#onnavdestinationsizechange) API.

## offNavDestinationSizeChangeByUniqueId

```TypeScript
offNavDestinationSizeChangeByUniqueId(navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void
```

Removes a callback function that was previously registered with 'onNavDestinationSizeChangeByUniqueId()'.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | number | Yes | The uniqueId of the Navigation to which NavDestination belongs. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

**Examples**

See the example for the [onNavDestinationSizeChangeByUniqueId](#onnavdestinationsizechangebyuniqueid) API.

## offRouterPageSizeChange

```TypeScript
offRouterPageSizeChange(callback?: Callback<observer.RouterPageInfo>): void
```

Removes the listener callback registered using the **onRouterPageSizeChange** API. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.RouterPageInfo&gt; | No | Callback to be removed. If no parameter is passed, all callbacks are removed. |

**Examples**

See the example for the [onRouterPageSizeChange](#onrouterpagesizechange) API.

## offSwiperContentUpdate

```TypeScript
offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void
```

Unregister the listener for content switching events of the **Swiper** component.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwiperContentInfo](arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | No | Target listener to unregister. If no parameter is provided, all listeners for the **Swiper** component are unregistered. |

**Examples**

See the example for the [onSwiperContentUpdate](#onswipercontentupdate) API.

## offSwiperContentUpdate

```TypeScript
offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void
```

Unregister the listener for content switching events of a specific **Swiper** component identified by its ID.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | Information about the target **Swiper** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwiperContentInfo](arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | No | Target listener to unregister. If no parameter is provided, all listeners for the **Swiper** component are unregistered. |

**Examples**

See the example for the [onSwiperContentUpdate](#onswipercontentupdate) API.

## on('navDestinationUpdate')

```TypeScript
on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<observer.NavDestinationInfo>): void
```

Subscribes to status changes of this **NavDestination** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | Event type. The value is fixed at **'navDestinationUpdate'**, which indicates the state change event of the **NavDestination** component. |
| options | { navigationId: ResourceStr } | Yes | ID of the target **NavDestination** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | Yes | Callback used to return the current state of the **NavDestination** component. |

## on('navDestinationUpdate')

```TypeScript
on(type: 'navDestinationUpdate', callback: Callback<observer.NavDestinationInfo>): void
```

Subscribes to status changes of this **NavDestination** component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdate' | Yes | Event type. The value is fixed at **'navDestinationUpdate'**, which indicates the state change event of the **NavDestination** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | Yes | Callback used to return the current state of the **NavDestination** component. |

## on('navDestinationUpdateByUniqueId')

```TypeScript
on(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback function to be called when the navigation destination is updated.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationUpdateByUniqueId' | Yes | The type of event to listen for. Must be 'navDestinationUpdateByUniqueId'. |
| navigationUniqueId | number | Yes | The uniqueId of the navigation. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | Yes | The callback function to be called when the navigation destination is updated. |

## on('scrollEvent')

```TypeScript
on(type: 'scrollEvent', options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to listen for. Must be 'scrollEvent'. |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |

## on('scrollEvent')

```TypeScript
on(type: 'scrollEvent', callback: Callback<observer.ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to listen for. Must be 'scrollEvent'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |

## on('routerPageUpdate')

```TypeScript
on(type: 'routerPageUpdate', callback: Callback<observer.RouterPageInfo>): void
```

Unsubscribes to state changes of the page in the router.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'routerPageUpdate' | Yes | Event type. The value is fixed at 'routerPageUpdate', which indicates the state change event of the page in the router. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.RouterPageInfo&gt; | Yes | Callback to be unregistered. |

## on('densityUpdate')

```TypeScript
on(type: 'densityUpdate', callback: Callback<observer.DensityInfo>): void
```

Listens for screen pixel density changes.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'densityUpdate' | Yes | Event type. The value **'densityUpdate'** indicates the pixel density changes of the screen. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.DensityInfo&gt; | Yes | Callback used to return the updated screen pixel density using a [DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md) object. |

## on('willDraw')

```TypeScript
on(type: 'willDraw', callback: Callback<void>): void
```

Listens for drawing instruction dispatch in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willDraw' | Yes | Event event. The value **'willDraw'** indicates whether drawing is about to occur. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

## on('didLayout')

```TypeScript
on(type: 'didLayout', callback: Callback<void>): void
```

Listens for layout completion status in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didLayout' | Yes | Event type. The value **'didLayout'** indicates whether the layout has been completed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

## on('navDestinationSwitch')

```TypeScript
on(
    type: 'navDestinationSwitch',
    callback: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationSwitch' | Yes | The type of event to listen for. Must be 'navDestinationSwitch'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationSwitchInfo&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |

## on('navDestinationSwitch')

```TypeScript
on(
    type: 'navDestinationSwitch',
    observerOptions: observer.NavDestinationSwitchObserverOptions,
    callback: Callback<observer.NavDestinationSwitchInfo>
  ): void
```

Registers a callback function to be called when the navigation switched to a new navDestination.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'navDestinationSwitch' | Yes | The type of event to listen for. Must be 'navDestinationSwitch'. |
| observerOptions | observer.NavDestinationSwitchObserverOptions | Yes | Options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationSwitchInfo&gt; | Yes | The callback function to be called when the navigation switched to a new navDestination. |

## on('willClick')

```TypeScript
on(type: 'willClick', callback: ClickEventListenerCallback): void
```

Registers a callback function to be called before clickEvent is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willClick' | Yes | The type of event to listen for. |
| callback | [ClickEventListenerCallback](arkts-arkui-clickeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## on('didClick')

```TypeScript
on(type: 'didClick', callback: ClickEventListenerCallback): void
```

Registers a callback function to be called after clickEvent is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didClick' | Yes | The type of event to listen for. |
| callback | [ClickEventListenerCallback](arkts-arkui-clickeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## on('willClick')

```TypeScript
on(type: 'willClick', callback: GestureEventListenerCallback): void
```

Registers a callback function to be called before tapGesture is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'willClick' | Yes | The type of event to listen for. |
| callback | [GestureEventListenerCallback](arkts-arkui-gestureeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## on('didClick')

```TypeScript
on(type: 'didClick', callback: GestureEventListenerCallback): void
```

Registers a callback function to be called after tapGesture is called.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didClick' | Yes | The type of event to listen for. |
| callback | [GestureEventListenerCallback](arkts-arkui-gestureeventlistenercallback-t.md) | Yes | The callback function to be called when the clickEvent will be trigger or after. |

## on('beforePanStart')

```TypeScript
on(type: 'beforePanStart', callback: PanListenerCallback): void
```

Listens for pan gesture onActionStart pre-execution events, executing the callback before the actual onActionStart event. It works for finger swiping, mouse dragging, mouse wheel scrolling, and touchpad movements, but not for screen reader touch mode.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'beforePanStart' | Yes | Event type. The value is fixed at **'beforePanStart'**, indicating command dispatch before the execution of the pan gesture onActionStart event. The registered callback is triggered before **onActionStart** is executed. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | Yes | Callback used to return the result. It provides [GestureEvent](arkts-arkui-gestureevent-i.md), [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md), and the target component's [FrameNode](arkts-arkui-framenode-c.md) information. |

## on('beforePanEnd')

```TypeScript
on(type: 'beforePanEnd', callback: PanListenerCallback): void
```

Listens for pan gesture onActionEnd pre-execution events, executing the callback before the actual onActionEnd event. It works for finger swiping, mouse dragging, mouse wheel scrolling, and touchpad movements, but not for screen reader touch mode.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'beforePanEnd' | Yes | Event type. The value is fixed at **'beforePanEnd'**, indicating command dispatch before the execution of the pan gesture onActionEnd event. The registered callback is triggered before **onActionEnd** is executed. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | Yes | Callback used to return the result. It provides [GestureEvent](arkts-arkui-gestureevent-i.md), [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md), and the target component's [FrameNode](arkts-arkui-framenode-c.md) information. |

## on('afterPanStart')

```TypeScript
on(type: 'afterPanStart', callback: PanListenerCallback): void
```

Listens for pan gesture onActionStart post-execution events, executing the callback after the actual onActionStart event. It works for finger swiping, mouse dragging, mouse wheel scrolling, and touchpad movements, but not for screen reader touch mode.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'afterPanStart' | Yes | Event type. The value is fixed at **'afterPanStart'**, indicating command dispatch after the execution of the pan gesture onActionStart event. The registered callback is triggered after **onActionStart** is executed. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | Yes | Callback used to return the result. It provides [GestureEvent](arkts-arkui-gestureevent-i.md), [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md), and the target component's [FrameNode](arkts-arkui-framenode-c.md) information. |

## on('afterPanEnd')

```TypeScript
on(type: 'afterPanEnd', callback: PanListenerCallback): void
```

Listens for pan gesture onActionEnd post-execution events, executing the callback after the actual onActionEnd event. It works for finger swiping, mouse dragging, mouse wheel scrolling, and touchpad movements, but not for screen reader touch mode.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'afterPanEnd' | Yes | Event type. The value is fixed at **'beforePanEnd'**, indicating command dispatch after the execution of the pan gesture onActionEnd event. The registered callback is triggered after **onActionEnd** is executed. |
| callback | [PanListenerCallback](arkts-arkui-panlistenercallback-t.md) | Yes | Callback used to return the result. It provides [GestureEvent](arkts-arkui-gestureevent-i.md), [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md), and the target component's [FrameNode](arkts-arkui-framenode-c.md) information. |

## on('tabContentUpdate')

```TypeScript
on(type: 'tabContentUpdate', options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | The type of event to listen for. Must be 'tabContentUpdate'. |
| options | observer.ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent show or hide. |

## on('tabContentUpdate')

```TypeScript
on(type: 'tabContentUpdate', callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabContentUpdate' | Yes | The type of event to listen for. Must be 'tabContentUpdate'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

## on('tabChange')

```TypeScript
on(type: 'tabChange', config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden. Include the cases when the first tab content shows and when the tab changes current index.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabChange' | Yes | The type of event to listen for. Must be 'tabChange'. |
| config | observer.ObserverOptions | Yes | The options object. Includes the observed component id. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when when the tabContent is showed or hidden. |

## on('tabChange')

```TypeScript
on(type: 'tabChange', callback: Callback<observer.TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden. Include the cases when the first tab content shows and when the tab changes current index.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'tabChange' | Yes | The type of event to listen for. Must be 'tabChange'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

## on('windowSizeLayoutBreakpointChange')

```TypeScript
on(type: 'windowSizeLayoutBreakpointChange', callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void
```

Registers a callback for window size layout breakpoint changes. This enables adaptive UI layout adjustments based on window size variations. This API uses an asynchronous callback to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'windowSizeLayoutBreakpointChange' | Yes | Event type. The value is fixed at **'windowSizeLayoutBreakpointChange'**, indicating window size layout breakpoint changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.WindowSizeLayoutBreakpointInfo&gt; | Yes | Callback used to return the result. It provides window width and height layout breakpoint enumerations using a **WindowSizeLayoutBreakpointinfo** object. |

## on('nodeRenderState')

```TypeScript
on(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void
```

Registers a callback to be invoked when the rendering state of a specific node changes. This callback is executed immediately once upon successful registration.

Be mindful of node quantity limitations. For performance reasons, registering too many nodes within a single UI instance will throw an exception.

Typically, a **RENDER_OUT** notification is received when a component moves off-screen. However, in certain scenarios, a **RENDER_OUT** notification might not be triggered even if a component has moved off-screen. For example, components with caching capabilities like Swiper will not trigger **RENDER_OUT** notifications even when the **isShown** parameter in the cachedCount attribute is set to **true**.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'nodeRenderState' | Yes | Event type. The value is fixed at **'nodeRenderState'**, indicating rendering state changes. |
| nodeIdentity | [NodeIdentity](arkts-arkui-nodeidentity-t.md) | Yes | Node ID. |
| callback | [NodeRenderStateChangeCallback](arkts-arkui-noderenderstatechangecallback-t.md) | Yes | Callback used to return the result. It provides the [NodeRenderState](arkts-arkui-arkui-uicontext-noderenderstate-e.md) of the node rendering state change event and the component's [FrameNode](arkts-arkui-framenode-c.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [161001](../errorcode-node-render-monitor.md#161001-number-of-nodes-listening-for-render-state-exceeds-the-limit) | The count of nodes monitoring render state is over the limitation. |

## on('textChange')

```TypeScript
on(type: 'textChange', callback: Callback<observer.TextChangeEventInfo>): void
```

Registers a callback function to be called when text field's content is changed.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | The type of event to listen for. Must be 'textChange'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TextChangeEventInfo&gt; | Yes | The callback function to be called when text field's content is changed. |

## on('textChange')

```TypeScript
on(type: 'textChange', identity: observer.ObserverOptions, callback: Callback<observer.TextChangeEventInfo>): void
```

Registers a callback function to be called when text field's content is changed.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | The type of event to listen for. Must be 'textChange'. |
| identity | observer.ObserverOptions | Yes | Identity options. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.TextChangeEventInfo&gt; | Yes | The callback function to be called when the text field's content is changed. |

## onNavDestinationSizeChange

```TypeScript
onNavDestinationSizeChange(callback: Callback<observer.NavDestinationInfo>): void
```

Registers a callback that is triggered when the size of the visible navigation destination changes. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | Yes | Callback used to return navigation destination information. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOneContent {
  destSizeCallback(info: uiObserver.NavDestinationInfo): void {
    console.info(`testTag destSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
  }

  aboutToAppear(): void {
    // You can obtain the size of the navigation destination page by registering a listener.
    this.getUIContext().getUIObserver().onNavDestinationSizeChange(this.destSizeCallback);
  }

  aboutToDisappear(): void {
    this.getUIContext().getUIObserver().offNavDestinationSizeChange(this.destSizeCallback);
  }

  build() {
    Column() {
      Button('queryDestSize').onClick(() => {
        // You can also proactively obtain the size of the navigation destination page.
        let info = this.queryNavDestinationInfo();
        console.info(`testTag destSize: ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
      })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct PageOne {
  build() {
    NavDestination() {
      PageOneContent()
    }
    .title('pageOne')
  }
}

@Entry
@Component
struct QueryNavDestinationSize {
  private stack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.stack.pushPath({name: 'one'});
  }

  @Builder
  myPageMap(name: string) {
    PageOne()
  }

  build() {
    Navigation(this.stack) {
    }
    .width('100%')
    .height('100%')
    .navDestination(this.myPageMap)
    .hideNavBar(true)
  }
}
```

## onNavDestinationSizeChangeByUniqueId

```TypeScript
onNavDestinationSizeChangeByUniqueId(navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void
```

Removes the listener callback registered using the **onNavDestinationSizeChangeByUniqueId** API. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| navigationUniqueId | number | Yes | Unique ID of the **Navigation** component to which the **NavDestination** component to be listened belongs, which can be obtained through [queryNavigationInfo](../arkts-components/arkts-arkui-basecustomcomponent-c.md#querynavigationinfo). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.NavDestinationInfo&gt; | Yes | Callback to be removed. If no parameter is passed, all callbacks with the same **navigationUniqueId** setting are removed. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOneContent {
  private navUniqueId: number = 0;

  destSizeCallback(info: uiObserver.NavDestinationInfo): void {
    console.info(`testTag destSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
  }

  aboutToAppear(): void {
    let navInfo = this.queryNavigationInfo();
    if (navInfo && navInfo.uniqueId) {
      this.navUniqueId = navInfo.uniqueId;
      // You can obtain the size of the navigation destination page by registering a listener.
      this.getUIContext().getUIObserver().onNavDestinationSizeChangeByUniqueId(this.navUniqueId, this.destSizeCallback);
    }
  }

  aboutToDisappear(): void {
    this.getUIContext().getUIObserver().offNavDestinationSizeChangeByUniqueId(this.navUniqueId, this.destSizeCallback);
  }

  build() {
    Column() {
      Button('queryDestSize').onClick(() => {
        // You can also proactively obtain the size of the navigation destination page.
        let info = this.queryNavDestinationInfo();
        console.info(`testTag destSize: ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
      })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct PageOne {
  build() {
    NavDestination() {
      PageOneContent()
    }
    .title('pageOne')
  }
}

@Entry
@Component
struct QueryNavDestinationSize {
  private stack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.stack.pushPath({name: 'one'});
  }

  @Builder
  myPageMap(name: string) {
    PageOne()
  }

  build() {
    Navigation(this.stack) {
    }
    .width('100%')
    .height('100%')
    .navDestination(this.myPageMap)
    .hideNavBar(true)
  }
}
```

## onRouterPageSizeChange

```TypeScript
onRouterPageSizeChange(callback: Callback<observer.RouterPageInfo>): void
```

Registers a callback that is triggered when the size of the visible router page changes. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;observer.RouterPageInfo&gt; | Yes | Callback used to return the information about the router page. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

const myPageRouterPageSizeCallback = (info: uiObserver.RouterPageInfo): void => {
  console.info(`testTag pageSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
}

@Entry
@Component
struct QueryRouterPageSize {
  aboutToAppear(): void {
    // You can obtain the page size information by registering a listener.
    this.getUIContext().getUIObserver().onRouterPageSizeChange(myPageRouterPageSizeCallback);
  }

  aboutToDisappear(): void {
    this.getUIContext().getUIObserver().offRouterPageSizeChange(myPageRouterPageSizeCallback);
  }

  build() {
    Column() {
      Button('querySize').onClick(() => {
        // You can also proactively obtain the page size.
        let info = this.queryRouterPageInfo();
        console.info(`testTag pageSize: ${info && info.size ? JSON.stringify(info.size) : 'NA'}`);
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## onSwiperContentUpdate

```TypeScript
onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void
```

Listens for content switching events of the **Swiper** component. This API uses an asynchronous callback to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwiperContentInfo](arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | Yes | Callback used to return the result. It provides the **Swiper** content switching information using a **SwiperContentInfo** object. |

**Examples**

```TypeScript
// Index.ets
import { SwiperContentInfo } from '@kit.ArkUI';

// Define callbacks for event listeners.
const callbackFunc = (info: SwiperContentInfo) => {
  console.info('swiperContentUpdate', JSON.stringify(info));
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();

  aboutToAppear(): void {
    // Listen for 'swiperContentUpdate' events.
    this.getUIContext().getUIObserver().onSwiperContentUpdate(callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listener for 'swiperContentUpdate' events.
    this.getUIContext().getUIObserver().offSwiperContentUpdate(callbackFunc);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        Column() {
          Text('SwiperItem1')
        }.width('100%').height('100%').backgroundColor('#00CB87')

        Column() {
          Text('SwiperItem2')
        }.width('100%').height('100%').backgroundColor('#007DFF')

        Column() {
          Text('SwiperItem3')
        }.width('100%').height('100%').backgroundColor('#FFBF00')

        Column() {
          Text('SwiperItem4')
        }.width('100%').height('100%').backgroundColor('#E67C92')
      }
      .width(360)
      .height(300)
    }.width('100%')
  }
}
```

## onSwiperContentUpdate

```TypeScript
onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void
```

Listens for content switching events of a specific **Swiper** component identified by its ID. This API uses an asynchronous callback to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | observer.ObserverOptions | Yes | Information about the target **Swiper** component. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwiperContentInfo](arkts-arkui-arkui-uicontext-swipercontentinfo-i.md)&gt; | Yes | Callback used to return the result. It provides the **Swiper** content switching information using a **SwiperContentInfo** object. |

**Examples**

```TypeScript
// Index.ets
import { SwiperContentInfo } from '@kit.ArkUI';

// Define callbacks for event listeners.
function callbackFunc(info: SwiperContentInfo) {
  console.info('swiperContentUpdate', JSON.stringify(info));
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();

  aboutToAppear(): void {
    // Listen for 'swiperContentUpdate' events for the component with the specified ID.
    this.getUIContext().getUIObserver().onSwiperContentUpdate({ id: 'swiperId' }, callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listener for 'swiperContentUpdate' events for the component with the specified ID.
    this.getUIContext().getUIObserver().offSwiperContentUpdate({ id: 'swiperId' }, callbackFunc);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        Column() {
          Text('SwiperItem1')
        }.width('100%').height('100%').backgroundColor('#00CB87')

        Column() {
          Text('SwiperItem2')
        }.width('100%').height('100%').backgroundColor('#007DFF')

        Column() {
          Text('SwiperItem3')
        }.width('100%').height('100%').backgroundColor('#FFBF00')

        Column() {
          Text('SwiperItem4')
        }.width('100%').height('100%').backgroundColor('#E67C92')
      }
      .id('swiperId')
      .width(360)
      .height(300)
    }.width('100%')
  }
}
```

## removeGlobalGestureListener

```TypeScript
removeGlobalGestureListener(type: GestureListenerType, callback?: GestureListenerCallback): void
```

Unregisters the specified global gesture listener.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [GestureListenerType](arkts-arkui-arkui-uicontext-gesturelistenertype-e.md) | Yes | Event type. |
| callback | [GestureListenerCallback](arkts-arkui-gesturelistenercallback-t.md) | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for this gesture type. |

**Examples**

See the example for the [addGlobalGestureListener](#addglobalgesturelistener) API .
