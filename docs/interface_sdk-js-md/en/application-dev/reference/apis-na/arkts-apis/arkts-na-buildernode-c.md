# BuilderNode

Defines BuilderNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class BuilderNode--><!--Device-unnamed-export declare class BuilderNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## build

```TypeScript
build(builder: WrappedBuilder<CustomBuilder>): void
```

Build the BuilderNode with the builder.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilder>): void--><!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilder>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | WrappedBuilder&lt;CustomBuilder&gt; | Yes | Defines the builder that will be called to build the node. |

## build

```TypeScript
build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T): void
```

Build the BuilderNode with the builder.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T): void--><!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | WrappedBuilder&lt;CustomBuilderT&lt;T&gt;&gt; | Yes | Defines the builder that will be called to build the node. |
| arg | T | Yes | Defines the args that will be used in the builder. |

## build

```TypeScript
build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T, options: BuildOptions): void
```

Build the BuilderNode with the builder. Support the type that WrappedBuilder contains builder used different params.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T, options: BuildOptions): void--><!--Device-BuilderNode-build(builder: WrappedBuilder<CustomBuilderT<T>>, arg: T, options: BuildOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | WrappedBuilder&lt;CustomBuilderT&lt;T&gt;&gt; | Yes | Defines the builder that will be called to build the node. |
| arg | T | Yes | Defines the args that will be used in the builder. |
| options | [BuildOptions](../../apis-arkui/arkts-apis/arkts-arkui-buildernode-buildoptions-i.md) | Yes | Defines the options that will be used when building. |

## constructor

```TypeScript
constructor(uiContext: UIContext, options?: RenderOptions)
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)--><!--Device-BuilderNode-constructor(uiContext: UIContext, options?: RenderOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the BuilderNode |
| options | [RenderOptions](../../apis-arkui/arkts-apis/arkts-arkui-buildernode-renderoptions-i.md) | No | Render options of the Builder Node |

## dispose

```TypeScript
dispose(): void
```

Dispose the BuilderNode immediately.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-dispose(): void--><!--Device-BuilderNode-dispose(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | null
```

Get the FrameNode in BuilderNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-getFrameNode(): FrameNode | null--><!--Device-BuilderNode-getFrameNode(): FrameNode | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../../apis-arkui/arkts-apis/arkts-arkui-framenode-c.md) | Returns a FrameNode inside the BuilderNode, or null if not contained. |

## inheritFreezeOptions

```TypeScript
inheritFreezeOptions(enabled: boolean): void
```

Set if the BuilderNode inherits the freezing policy of the parent CustomComponent, BuilderNode, ComponentContent, ReactiveBuilderNode or ReactiveComponentContent.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-inheritFreezeOptions(enabled: boolean): void--><!--Device-BuilderNode-inheritFreezeOptions(enabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | If the BuilderNode inherits the freezing policy of the parent CustomComponent, BuilderNode, ComponentContent, ReactiveBuilderNode or ReactiveComponentContent. True to inherit, false not to inherit. |

## isDisposed

```TypeScript
isDisposed(): boolean
```

Get if the BuilderNode is disposed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-isDisposed(): boolean--><!--Device-BuilderNode-isDisposed(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the BuilderNode is disposed, false otherwise. |

## postInputEvent

```TypeScript
postInputEvent(event: InputEventType): boolean
```

Dispatches the input event to the FrameNode in the BuilderNode. postInputEvent dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, the event coordinates need to be transformed into the coordinate system of the parent component. Notes: The input coordinate values need to be converted to pixels (px). Left mouse click events will be converted to touch events. When forwarding, note that if touch events and mouse events are bound to outer layers, it may cause coordinate offset. When injecting axis events, since axis events lack rotation axis information, injected events cannot trigger rotate gestures Forwarded events will undergo touch testing in the subtree of the target component where they are dispatched and trigger corresponding gestures. Original events will also trigger gestures in the current component's component tree. The competition outcome between these two types of gestures is not guaranteed. For developer-constructed events, required fields must be assigned values, such as the touches field for touch events and the scrollStep field for axis events. Also, ensure event completeness - for example, both DOWN and UP fields in TouchType for touch events must be present to prevent undefined behavior. Webview has already handled coordinate system transformations, so events can be dispatched directly. The postInputEvent interface requires providing gesture coordinates relative to the window coordinates within the input event peer. It is not recommended to forward the same event multiple times. The postInputEvent parameter does not support UIExtensionComponent.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-postInputEvent(event: InputEventType): boolean--><!--Device-BuilderNode-postInputEvent(event: InputEventType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InputEventType](../../apis-arkui/arkts-apis/arkts-arkui-inputeventtype-t.md) | Yes | The event which will be sent. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event has been successfully posted, false otherwise. |

## postInputEventWithStrategy

```TypeScript
postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean
```

Dispatch event to targetNode with competition strategy. postInputEventWithStrategy dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, the event coordinates need to be transformed into the coordinate system of the parent component. Notes: The input coordinate values need to be converted to pixels (px). Left mouse click events will be converted to touch events. When forwarding, note that if touch events and mouse events are bound to outer layers, it may cause coordinate offset. When injecting axis events, since axis events lack rotation axis information, injected events cannot trigger rotate gestures Forwarded events will undergo touch testing in the subtree of the target component where they are dispatched and trigger corresponding gestures. Original events will also trigger gestures in the current component's component tree. The competition outcome between these two types of gestures is not guaranteed. For developer-constructed events, required fields must be assigned values, such as the touches field for touch events and the scrollStep field for axis events. Also, ensure event completeness - for example, both DOWN and UP fields in TouchType for touch events must be present to prevent undefined behavior. Webview has already handled coordinate system transformations, so events can be dispatched directly. The postInputEvent interface requires providing gesture coordinates relative to the window coordinates within the input event peer. It is not recommended to forward the same event multiple times. The postInputEvent parameter does not support UIExtensionComponent.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean--><!--Device-BuilderNode-postInputEventWithStrategy(event: InputEventType, competitionStrategy?: CompetitionStrategy): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [InputEventType](../../apis-arkui/arkts-apis/arkts-arkui-inputeventtype-t.md) | Yes | The event which will be sent to the targetNode. |
| competitionStrategy | CompetitionStrategy | No | The competition strategy. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the event has been successfully posted to the targetNode, false otherwise. |

## postTouchEvent

```TypeScript
postTouchEvent(event: TouchEvent): boolean
```

Dispatch the touchEvent to the FrameNode in the current BuilderNode. postTouchEvent dispatches the event from a middle node in the component tree downwards. To ensure the event is dispatched correctly, it needs to be transformed into the coordinate system of the parent component. &lt;p&gt;&lt;strong&gt;Note:&lt;/strong&gt; <br>The coordinates you pass in need to be converted to pixel values (px). If the BuilderNode has any <br>affine transformations applied to it, they must be taken into account and combined with the touch event <br>coordinates. In Webview, coordinate system transformations are already handled internally, so you can <br>directly dispatch the touch event without additional adjustments. <br>The postTouchEvent API can be called only once for the same timestamp. <br>UIExtensionComponent is not supported. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-postTouchEvent(event: TouchEvent): boolean--><!--Device-BuilderNode-postTouchEvent(event: TouchEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | TouchEvent | Yes | The touchEvent which will be sent. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the TouchEvent has been successfully posted, false otherwise. If the event does not hit the expected component, ensure the following: 1. The coordinate system has been correctly transformed 2. The component is in an interactive state. 3. The event has been bound to the component. |

## recycle

```TypeScript
recycle(): void
```

Recycle the BuilderNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-recycle(): void--><!--Device-BuilderNode-recycle(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuse

```TypeScript
reuse(param?: RecordData): void
```

Reuse the BuilderNode based on the provided parameters.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-reuse(param?: RecordData): void--><!--Device-BuilderNode-reuse(param?: RecordData): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | No | Parameters for reusing BuilderNode. These parameters will be directly applied to the reuse of all top-level custom components in the BuilderNode. They should include the content required for the constructor parameters of each custom component; otherwise, undefined behavior may occur. Calling this method will synchronously trigger the aboutToReuse lifecycle callback of the internal custom components, with these parameters passed as the callback's input. The default value is undefined, in which case the custom components in the BuilderNode will directly use the data source from the construction phase. |

## update

```TypeScript
update(arg: T): void
```

Update the BuilderNode based on the provided parameters.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-update(arg: T): void--><!--Device-BuilderNode-update(arg: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arg | T | Yes | Parameters used to update the BuilderNode, which must match the types required by the builder bound to the BuilderNode. |

## updateConfiguration

```TypeScript
updateConfiguration(): void
```

Notify BuilderNode to update the configuration to trigger a reload of the BuilderNode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuilderNode-updateConfiguration(): void--><!--Device-BuilderNode-updateConfiguration(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

