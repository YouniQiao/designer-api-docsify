# ReactiveBuilderNode

Defines ReactiveBuilderNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class ReactiveBuilderNode--><!--Device-unnamed-export declare class ReactiveBuilderNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(builder: CustomBuilder, options?: BuildOptions): void
```

Build the ReactiveBuilderNode with the builder.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-build(builder: CustomBuilder, options?: BuildOptions): void--><!--Device-ReactiveBuilderNode-build(builder: CustomBuilder, options?: BuildOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | Yes | Defines the builder that will be called to build the node. |
| options | [BuildOptions](arkts-arkui-buildernode-buildoptions-i.md) | No | Defines the options that will be used when building. |

## constructor

```TypeScript
constructor(uiContext: UIContext, options?: RenderOptions)
```

Constructor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)--><!--Device-ReactiveBuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the ReactiveBuilderNode |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | No | Render options of the ReactiveBuilderNode |

## dispose

```TypeScript
dispose(): void
```

Dispose the ReactiveBuilderNode immediately.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-dispose(): void--><!--Device-ReactiveBuilderNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## flushState

```TypeScript
flushState(): void
```

Flushes the current state changes to update the ReactiveBuilderNode immediately.This forces a synchronous update of the ReactiveBuilderNode with the latest state values.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-flushState(): void--><!--Device-ReactiveBuilderNode-flushState(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | null
```

Get the FrameNode in ReactiveBuilderNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-getFrameNode(): FrameNode | null--><!--Device-ReactiveBuilderNode-getFrameNode(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](arkts-arkui-framenode-c.md) | Returns a FrameNode inside the ReactiveBuilderNode, or null if not contained. |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the ReactiveBuilderNode is disposed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-isDisposed(): boolean--><!--Device-ReactiveBuilderNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the ReactiveBuilderNode is disposed, false otherwise. |

## postInputEvent

```TypeScript
postInputEvent(event: InputEventType): boolean
```

Dispatch the input event to the FrameNode in the current ReactiveBuilderNode.postInputEvent dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, the event coordinates need to be transformed into the coordinate system of the parent component.

Note:The input coordinate values need to be converted to pixels (px). Left mouse click events will be converted to touch events. When forwarding, note that if touch events and mouse events are bound to outer layers, it may cause coordinate offset. When injecting axis events, since axis events lack rotation axis information,injected events cannot trigger rotate gestures Forwarded events will undergo touch testing in the subtree of the target component where they are dispatched and trigger corresponding gestures. Original events will also trigger gestures in the current component's component tree. The competition outcome between these two types of gestures is not guaranteed. For developer-constructed events, required fields must be assigned values,such as the touches field for touch events and the scrollStep field for axis events. Also, ensure event completeness - for example, both DOWN and UP fields in TouchType for touch events must be present to prevent undefined behavior. Webview has already handled coordinate system transformations, so events be dispatched directly. The postInputEvent interface requires providing gesture coordinates relative to the window coordinates within the input event peer. It is not recommended to forward the same event multiple times.The postInputEvent parameter does not support UIExtensionComponent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-postInputEvent(event: InputEventType): boolean--><!--Device-ReactiveBuilderNode-postInputEvent(event: InputEventType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | Yes | The event which will be sent. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the TouchEvent has been successfully posted, false otherwise. |

## postInputEventWithStrategy

```TypeScript
postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean
```

Dispatch event to targetNode with competition strategy.postInputEventWithStrategy dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, the event coordinates need to be transformed into the coordinate system of the parent component.

Notes:The input coordinate values need to be converted to pixels (px). Left mouse click events will be converted to touch events. When forwarding, note that if touch events and mouse events are bound to outer layers, it may cause coordinate offset. When injecting axis events, since axis events lack rotation axis information,injected events cannot trigger rotate gestures Forwarded events will undergo touch testing in the subtree of the target component where they are dispatched and trigger corresponding gestures. Original events will also trigger gestures in the current component's component tree. The competition outcome between these two types of gestures is not guaranteed. For developer-constructed events, required fields must be assigned values,such as the touches field for touch events and the scrollStep field for axis events. Also, ensure event completeness - for example, both DOWN and UP fields in TouchType for touch events must be present to prevent undefined behavior. Webview has already handled coordinate system transformations, so events can be dispatched directly. The postInputEvent interface requires providing gesture coordinates relative to the window coordinates within the input event peer. It is not recommended to forward the same event multiple times.The postInputEvent parameter does not support UIExtensionComponent.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean--><!--Device-ReactiveBuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InputEventType](arkts-arkui-inputeventtype-t.md) | Yes | The event which will be sent to the targetNode. |
| competitionStrategy | [CompetitionStrategy](arkts-arkui-competitionstrategy-e.md) | No | The competition strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event has been successfully posted to the targetNode, false otherwise. |

## postTouchEvent

```TypeScript
postTouchEvent(event: TouchEvent): boolean
```

Dispatch the touchEvent to the FrameNode in the current ReactiveBuilderNode.postTouchEvent dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, it needs to be transformed into the coordinate system of the parent component.

&lt;p&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;br&gt;The coordinates you pass in need to be converted to pixel values (px). If the ReactiveBuilderNode has any&lt;br&gt;affine transformations applied to it, they must be taken into account and combined with the touch event&lt;br&gt;coordinates. In Webview, coordinate system transformations are already handled internally, so you can&lt;br&gt;directly dispatch the touch event without additional adjustments.&lt;br&gt;The postTouchEvent API can be called only once for the same timestamp.&lt;br&gt;UIExtensionComponent is not supported.&lt;/p&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-postTouchEvent(event: TouchEvent): boolean--><!--Device-ReactiveBuilderNode-postTouchEvent(event: TouchEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md) | Yes | The touchEvent which will be sent. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the TouchEvent has been successfully posted, false otherwise. If the event does not hit the expected component, ensure the following: 1. The coordinate system has been correctly transformed 2. The component is in an interactive state. 3. The event has been bound to the component. |

## recycle

```TypeScript
recycle(): void
```

Recycle the ReactiveBuilderNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-recycle(): void--><!--Device-ReactiveBuilderNode-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: RecordData): void
```

Reuse the ReactiveBuilderNode based on the provided parameters.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-reuse(param?: RecordData): void--><!--Device-ReactiveBuilderNode-reuse(param?: RecordData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | No | Parameters for reusing ReactiveBuilderNode. These parameters will be directly applied to the reuse of all top-level custom components in the ReactiveBuilderNode. They should include the content required for the constructor parameters of each custom component; otherwise, undefined behavior may occur. Calling this method will synchronously trigger the aboutToReuse lifecycle callback of the internal custom components, with these parameters passed as the callback's input. The default value is undefined, in which case the custom components in the ReactiveBuilderNode will directly use the data source from the construction phase. |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

Notify ReactiveBuilderNode to update the configuration to trigger a reload of the ReactiveBuilderNode.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReactiveBuilderNode-updateConfiguration(): void--><!--Device-ReactiveBuilderNode-updateConfiguration(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

