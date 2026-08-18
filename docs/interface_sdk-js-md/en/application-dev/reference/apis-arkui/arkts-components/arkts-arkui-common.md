# Common

Common for ide.

## Common

```TypeScript
Common()
```

Constructor

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonInterface-(): CommonAttribute--><!--Device-CommonInterface-(): CommonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AccessibilityHoverEvent](arkts-arkui-accessibilityhoverevent-i.md) | The accessibility hover action triggers this method invocation. |
| [AlignRuleOption](arkts-arkui-alignruleoption-i.md) | Defines the align rule options of relative container. |
| [AnimatableArithmetic](arkts-arkui-animatablearithmetic-i.md) | The **AnimatableArithmetic** API defines animation calculation rules for non-number data types. To animate non-number data (such as arrays, structs, and colors), you need to implement the addition, subtraction, multiplication, and equality checking functions in the **AnimatableArithmetic\&lt;T\&gt;** API. This enables the data to participate in animation interpolation calculations and to detect whether the data has changed. In other words, the non-number data is defined as types that implement the **AnimatableArithmetic\&lt;T\&gt;** API. |
| [AnimateParam](arkts-arkui-animateparam-i.md) | Defines parameters related to animation effects. |
| [AreaChangeOptions](arkts-arkui-areachangeoptions-i.md) | Defines the options for the AreaChangeEvent. |
| [AttributeModifier](arkts-arkui-attributemodifier-i.md) | Defines the attribute modifier. |
| [AxisEvent](arkts-arkui-axisevent-i.md) | Describes the axis event object. Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). |
| [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | Defines the options of backgroundBlurStyle |
| [BackgroundBrightnessOptions](arkts-arkui-backgroundbrightnessoptions-i.md) | Provides background brightness options. > **NOTE：**> > The brightness (gray scale value) of each pixel in the component background content is calculated using the > following formula: > > Y = (0.299R + 0.587G + 0.114B) / 255.0, where **R**, **G**, and **B** represent red, green, and blue channel > values of the pixel, respectively, and **Y** is the gray scale value. This formula normalizes the gray scale value > to a range of 0 to 1. > > The formula for calculating the increase in brightness for each pixel is as follows: ΔY = -rate * Y + > lightUpDegree. For example, when rate = 0.5 and lightUpDegree = 0.5, for a pixel with a gray scale value of 0.2, > the increase in brightness is -0.5 * 0.2 + 0.5 = 0.4. For a pixel with a gray scale value of 1, the increase in > brightness is -0.5 * 1 + 0.5 = 0. |
| [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md) | Defines the options of BackgroundEffect |
| [BackgroundImageOptions](arkts-arkui-backgroundimageoptions-i.md) | Define the options for background image. |
| [BackgroundOptions](arkts-arkui-backgroundoptions-i.md) | Defines background options. |
| [BaseEvent](arkts-arkui-baseevent-i.md) | Basic event type. |
| [BindOptions](arkts-arkui-bindoptions-i.md) | Overlay module options |
| [BlurOptions](arkts-arkui-bluroptions-i.md) | Grayscale blur parameters. |
| [BlurSnapshotOptions](arkts-arkui-blursnapshotoptions-i-sys.md) | Defines the options for blur snapshot optimization. Setting this object enables blur optimization. |
| [BlurStyleOptions](arkts-arkui-blurstyleoptions-i.md) | Defines the options of blurStyle |
| [BorderImageOption](arkts-arkui-borderimageoption-i.md) | Border image option |
| [Callback](arkts-arkui-callback-i.md) | Defines the basic callback. |
| [CaretOffset](arkts-arkui-caretoffset-i.md) | Describes the position of the caret relative to the text box. |
| [ClickEffect](arkts-arkui-clickeffect-i.md) | Defines the click effect. |
| [ClickEvent](arkts-arkui-clickevent-i.md) | Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). |
| [CommonConfiguration](arkts-arkui-commonconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. |
| [ComponentOptions](arkts-arkui-componentoptions-i.md) | Defines the options of Component ClassDecorator. |
| [Configuration](arkts-arkui-configuration-i.md) | Defines the data type of the interface restriction. |
| [ContentCoverOptions](arkts-arkui-contentcoveroptions-i.md) | Inherited from [BindOptions](arkts-arkui-bindoptions-i.md). Provides content options of the modal. |
| [ContentModifier](arkts-arkui-contentmodifier-i.md) | Defines the content modifier. |
| [ContextMenuAnimationOptions](arkts-arkui-contextmenuanimationoptions-i.md) | Defines the style for displaying a long-press preview. |
| [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | Configures menu item information. **Table 1: Menu offset when both offset and placement are set** | Value of placement | Menu Offset | | ------------------------------------------------------------ | ------------------------------------------------------------ | | Placement.TopLeft, Placement.Top, or Placement.TopRight | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts upward relative to the component.| | Placement.BottomLeft, Placement.Bottom, or Placement.BottomRight| If the value of **x** is a positive number for **offset**, the menu shifts to the left relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component.| | Placement.RightTop, Placement.Right, or Placement.RightBottom | If the value of **x** is a positive number for **offset**, the menu shifts to the right relative to the component. If the value of **y** is a positive number, the menu shifts downward relative to the component.| **Table 2: Default position of the menu arrow when both arrowOffset and placement are set** | Value of placement | Menu Arrow Position | | ------------------------------------------- | ------------------------------------------------------------ | | Placement.Top or Placement.Bottom | The arrow is displayed horizontally and centered by default, with a distance from the left edge of the menu equal to the arrow's safe distance.| | Placement.Left or Placement.Right | The arrow is displayed vertically and centered by default, with a distance from the top edge of the menu equal to the arrow's safe distance.| | Placement.TopLeft or Placement.BottomLeft | The arrow is displayed horizontally by default, with a distance from the left edge of the menu equal to the arrow's safe distance.| | Placement.TopRight or Placement.BottomRight | The arrow is displayed horizontally by default, with a distance from the right edge of the menu equal to the arrow's safe distance. | | Placement.LeftTop or Placement.RightTop | The arrow is displayed vertically by default, with a distance from the top edge of the menu equal to the arrow's safe distance. | | Placement.LeftBottom or Placement.RightBottom| The arrow is displayed vertically by default, with a distance from the bottom edge of the menu equal to the arrow's safe distance. | **Table 3 Default menu position when enableArrow is set to true and placement is not set or set to an invalid value** | API| Default Menu Position| |------|-------------| | [bindMenu](arkts-arkui-commonmethod-c.md#bindmenu) | Placement.BottomLeft | | [bindMenu&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#bindmenu) | Placement.BottomLeft | | [bindContextMenu&lt;sup&gt;8+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#bindcontextmenu) | Placement.Top | | [bindContextMenu&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#bindcontextmenu) | Placement.BottomLeft | | [bindContextMenuWithResponse&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#bindcontextmenuwithresponse) | Placement.Top | |
| [CrownEvent](arkts-arkui-crownevent-i.md) | Defines a data structure for the crown event received by a component. It includes the timestamp, angular velocity, rotation angle, crown action, and event propagation disabling. |
| [CustomPopupOptions](arkts-arkui-custompopupoptions-i.md) | Provides information for displaying a custom popup. |
| [DateRange](arkts-arkui-daterange-i.md) | Defines a range of dates. |
| [DepthColorRGB](arkts-arkui-depthcolorrgb-i-sys.md) | RGB color in depth space. |
| [DepthVector3](arkts-arkui-depthvector3-i-sys.md) | 3D vector in depth space. |
| [DepthVector4](arkts-arkui-depthvector4-i-sys.md) | 4D vector in depth space. |
| [DismissContentCoverAction](arkts-arkui-dismisscontentcoveraction-i.md) | Component content cover dismiss |
| [DismissPopupAction](arkts-arkui-dismisspopupaction-i.md) | Provides information about the dismissal of the popup. |
| [DismissSheetAction](arkts-arkui-dismisssheetaction-i.md) | Component sheet dismiss |
| [DragEvent](arkts-arkui-dragevent-i.md) | Provides information about the drag event. |
| [DragInteractionOptions](arkts-arkui-draginteractionoptions-i.md) | Interaction behavior for the floating preview image |
| [DragItemInfo](arkts-arkui-dragiteminfo-i.md) | Defines the information about the dragged item during drag. |
| [DragPreviewOptions](arkts-arkui-dragpreviewoptions-i.md) | Preview image processing mode and badge count during dragging. |
| [DropOptions](arkts-arkui-dropoptions-i.md) | Sets parameters for the drop process. |
| [EdgeEffectOptions](arkts-arkui-edgeeffectoptions-i.md) | Define EdgeEffect Options. |
| [EdgeLightParams](arkts-arkui-edgelightparams-i-sys.md) | Defines the parameters of the edge light effect. |
| [EditModeOptions](arkts-arkui-editmodeoptions-i.md) | Define edit mode options. |
| [EntryOptions](arkts-arkui-entryoptions-i.md) | Defines the options of Entry ClassDecorator. |
| [EventTarget](arkts-arkui-eventtarget-i.md) | Defines the type of the **target** parameter in [BaseEvent](arkts-arkui-baseevent-i.md). Represents the display area of the element object that triggers the event. |
| [ExpectedFrameRateRange](arkts-arkui-expectedframeraterange-i.md) | Sets the expected frame rate range for an animation. |
| [FadingEdgeOptions](arkts-arkui-fadingedgeoptions-i.md) | Defines the fadingEdge options. |
| [FocusAxisEvent](arkts-arkui-focusaxisevent-i.md) | Describes the focus axis event object. Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). |
| [FocusMovement](arkts-arkui-focusmovement-i.md) | Sets the target component for focus movement based on key presses. If it is not specified, the default focus movement logic applies. > **NOTE：**> > Directly using **focusControl** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > [UIContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) object using the **getUIContext()** API and then obtain the > **focusControl** bound to the instance using the > [getFocusController](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#getfocuscontroller) API. |
| [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | Inherits from [BlurStyleOptions](arkts-arkui-blurstyleoptions-i.md) to define the foreground blur options. |
| [ForegroundEffectOptions](arkts-arkui-foregroundeffectoptions-i.md) | Describes the foreground effect. |
| [GeometryInfo](arkts-arkui-geometryinfo-i.md) | Provides layout geometry information of the parent component (a custom component). Inherits from [SizeResult](arkts-arkui-sizeresult-i.md). |
| [GeometryTransitionOptions](arkts-arkui-geometrytransitionoptions-i.md) | Defines the options of geometry transition. |
| [GestureModifier](arkts-arkui-gesturemodifier-i.md) | You need a custom class to implement the **GestureModifier** API. |
| [GravityCenterOptions](arkts-arkui-gravitycenteroptions-i-sys.md) | Defines the parameters of the center of gravity. |
| [HistoricalPoint](arkts-arkui-historicalpoint-i.md) | Provides historical touch point information. |
| [HorizontalAlignParam](arkts-arkui-horizontalalignparam-i.md) | Defines the horizontal align rule of relative container. |
| [HoverEvent](arkts-arkui-hoverevent-i.md) | Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). |
| [ICurve](arkts-arkui-icurve-i.md) | Interface for curve object. |
| [IMonitor](arkts-arkui-imonitor-i.md) | Define IMonitor interface |
| [IMonitorValue](arkts-arkui-imonitorvalue-i.md) | Define IMonitorValue interface |
| [InputCounterOptions](arkts-arkui-inputcounteroptions-i.md) | Provides configuration options for the character counter. |
| [InputEventInterceptResult](arkts-arkui-inputeventinterceptresult-i.md) | Input event interception result interface, used by the listener callback [InputEventListener](arkts-arkui-inputeventlistener-t.md) to return the interception decision. |
| [InputEventMonitor](arkts-arkui-inputeventmonitor-i.md) | Input event monitor identity object. This object is created and returned by the system, serving as the unique identifier of the monitor. > **NOTE：**> > - The object is empty and does not contain any accessible members. > > - Developers cannot create this object on their own. It can only be obtained by registering through the > addLocalInputEventMonitor API. > > - It is used for identity verification when unregistering later. |
| [InvertOptions](arkts-arkui-invertoptions-i.md) | Describes the options for inverting the foreground color. |
| [ItemDragEventHandler](arkts-arkui-itemdrageventhandler-i.md) | Define item drag event handler. |
| [ItemDragInfo](arkts-arkui-itemdraginfo-i.md) | ItemDragInfo object description |
| [KeyEvent](arkts-arkui-keyevent-i.md) | KeyEvent object description. |
| [KeyframeAnimateParam](arkts-arkui-keyframeanimateparam-i.md) | Provides animation configuration options. |
| [KeyframeState](arkts-arkui-keyframestate-i.md) | Provides keyframe configuration options. |
| [Layoutable](arkts-arkui-layoutable-i.md) | Provides the child component layout information. |
| [LayoutBorderInfo](arkts-arkui-layoutborderinfo-i.md) | Provides the border information of the child component. |
| [LayoutChild](arkts-arkui-layoutchild-i.md) | Sub component info passed from framework when layout and measure happens. |
| [LayoutInfo](arkts-arkui-layoutinfo-i.md) | Provides the child component layout information. |
| [LightSource](arkts-arkui-lightsource-i-sys.md) | Each component allows for one light source. |
| [LinearGradient](arkts-arkui-lineargradient-i.md) | Linear Gradient Interface |
| [LinearGradientBlurOptions](arkts-arkui-lineargradientbluroptions-i.md) | Linear Gradient Blur Interface |
| [LinearGradientOptions](arkts-arkui-lineargradientoptions-i.md) | Defines the linear gradient parameters. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [LocalizedAlignRuleOptions](arkts-arkui-localizedalignruleoptions-i.md) | Defines the Localized align rule options of relative container. |
| [LocalizedHorizontalAlignParam](arkts-arkui-localizedhorizontalalignparam-i.md) | Defines the localized horizontal align param of relative container. |
| [LocalizedVerticalAlignParam](arkts-arkui-localizedverticalalignparam-i.md) | Defines the localized vertical align param of relative container. |
| [Measurable](arkts-arkui-measurable-i.md) | Provides the child component position information. |
| [MeasureResult](arkts-arkui-measureresult-i.md) | Provides the measurement result of the component. This API inherits from [SizeResult](arkts-arkui-sizeresult-i.md). |
| [MenuElement](arkts-arkui-menuelement-i.md) | Configures icon, text, and interaction information of a menu item. |
| [MenuGridStyleOptions](arkts-arkui-menugridstyleoptions-i.md) | Defines the grid style of menu. |
| [MenuMaskType](arkts-arkui-menumasktype-i.md) | Sets the mask type. |
| [MenuOptions](arkts-arkui-menuoptions-i.md) | Configues menu item information, which is inherited from [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md). |
| [MonitorDecoratorOptions](arkts-arkui-monitordecoratoroptions-i.md) | Defines MonitorDecoratorOptions interface |
| [MotionBlurAnchor](arkts-arkui-motionbluranchor-i.md) | Describes the coordinates of the motion blur anchor. |
| [MotionBlurOptions](arkts-arkui-motionbluroptions-i.md) | Defines motion blur options. |
| [MotionPathOptions](arkts-arkui-motionpathoptions-i.md) | Defines motion path configuration options of the component. |
| [MouseEvent](arkts-arkui-mouseevent-i.md) | Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). |
| [MouseHistoricalPoint](arkts-arkui-mousehistoricalpoint-i.md) | Mouse event historical point information. Historical points are arranged in chronological order. The first historical point obtained is the earliest event, and the last is the most recent event. The number of historical points depends on the system event queue configuration and hardware performance. Historical points are mainly used for the following scenarios: 1. Smooth drawing: Historical points enable smoother drawing effects, especially when the mouse moves quickly. 2. Gesture recognition: By analyzing the trajectory of historical points, various mouse gestures can be recognized. 3. Performance optimization: Processing multiple historical points in one event callback reduces event processing frequency and improves performance. 4. Trajectory analysis: Analyzing mouse movement trajectories for drawing applications or gesture control. 5. Data analysis: The **timestamp** in historical points can be used to calculate mouse movement speed. |
| [MultiShadowOptions](arkts-arkui-multishadowoptions-i.md) | Defines shadow style properties. |
| [NestedScrollOptions](arkts-arkui-nestedscrolloptions-i.md) | Define nested scroll options |
| [OverlayOffset](arkts-arkui-overlayoffset-i.md) | Offset of the overlay from the upper left corner. By default, the overlay is in the upper left corner of the component. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 12. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [OverlayOptions](arkts-arkui-overlayoptions-i.md) | > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 12. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. > **NOTE：**> > When both **align** and **offset** are set, the effects are combined. The overlay is first aligned relative to the > component and then offset from its current upper left corner. |
| [PickerDialogButtonStyle](arkts-arkui-pickerdialogbuttonstyle-i.md) | Provide an interface for the button style of picker |
| [PickerTextStyle](arkts-arkui-pickertextstyle-i.md) | Provide an interface for the text style of picker |
| [PixelMapMock](arkts-arkui-pixelmapmock-i-sys.md) | pixelmap object with release function. |
| [PixelRoundPolicy](arkts-arkui-pixelroundpolicy-i.md) | Enumerates the directions of pixel rounding at the component level. |
| [PixelStretchEffectOptions](arkts-arkui-pixelstretcheffectoptions-i.md) | Describes the pixel stretch effect options. |
| [PointLightStyle](arkts-arkui-pointlightstyle-i-sys.md) | You apply a point light style by setting the light source that emits illumination and the components to be illuminated. |
| [PopupBorderLinearGradient](arkts-arkui-popupborderlineargradient-i.md) | Sets the color and direction of the linear gradient for the outlines. |
| [PopupCommonOptions](arkts-arkui-popupcommonoptions-i.md) | Configures the parameters of a popup. You can use the [getPromptAction()](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [PromptAction](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) object, and then call the attributes of **options** when [openPopup](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#openpopup) or [updatePopup](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#updatepopup) is called. |
| [PopupMaskType](arkts-arkui-popupmasktype-i.md) | Sets the color of the mask. |
| [PopupMessageOptions](arkts-arkui-popupmessageoptions-i.md) | Describes the popup message text style. |
| [PopupOptions](arkts-arkui-popupoptions-i.md) | Provides the configuration options for the popup. |
| [PopupStateChangeParam](arkts-arkui-popupstatechangeparam-i.md) | Display state of the popup. |
| [PreviewConfiguration](arkts-arkui-previewconfiguration-i.md) | Configures the style of the preview image during custom drag operations. |
| [PreviewParams](arkts-arkui-previewparams-i.md) | Define Preview property |
| [ProvideOptions](arkts-arkui-provideoptions-i.md) | Defines the options of Provide PropertyDecorator. |
| [RadialGradientOptions](arkts-arkui-radialgradientoptions-i.md) | Defines the radial gradient parameters. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. > **NOTE：**> > When using the **colors** parameter, take note of the following: > > ResourceColor indicates the color, and **number** indicates the color's position, which > ranges from 0 to 1.0: **0** indicates the start of the container, and **1.0** indicates the end of the container. > To create a gradient with multiple color stops, you are advised to set the **number** values in ascending order. If > a value of **number** in an array is smaller than that in the previous one, it is considered as equal to the > previous value. |
| [Rectangle](arkts-arkui-rectangle-i.md) | The data type used to describe a rectangular area. > **NOTE：**> > - **x** and **y** can be set to a positive or negative percentage value. For example, when **x** is set to > **'100%'**, the touch target is the offset from the right edge of the component by the component's width. When > **x** is set to **'-100%'**, the touch target is the offset from the left edge of the component by the component's > width. When **y** is set to **'100%'**, the touch target is the offset from the bottom edge of the component by the > component's height. When **y** is set to **'-100%'**, the touch target is the offset from the top edge of the > component by the component's height. > > - **width** and **height** can only be set to positive percentage values. When **width** is set to **'100%'**, the > width of the touch target is equal to that of the component. For example, if the width of a component is 100 vp, > **'100%'** indicates that the width of the touch target is also 100 vp. When **height** is set to **'100%'**, the > height of the touch target is equal to that of the component. > > - The percentage is measured relative to the component itself. > > - When the parent component has [clip](arkts-arkui-commonmethod-c.md#clip) set to **true**, child component > interaction is affected by the parent component's response region. Children outside the parent component's response > region won't respond to gestures or events. > > - **width** and **height** do not support **calc()** dynamic calculations. |
| [RectResult](arkts-arkui-rectresult-i.md) | Describes the position, width, and height of a component. |
| [ResponseRegion](arkts-arkui-responseregion-i.md) | Defines a touch target consisting of an input tool type, touch position, and size. > **NOTE：**> > - When the parent component has [clip](arkts-arkui-commonmethod-c.md#clip) set to **true**, child component > interaction is affected by the parent component's response region. Children outside the parent component's response > region won't respond to gestures or events. > > - If the input tool type, touch position, and size are not configured for a touch target, default values are used. > > - Positive calculation results for x and y represent shifts to the right and down, respectively. Negative > calculation results represent shifts to the left and up, respectively. > > - If the width and height are of the string type, the string must be in lowercase. Dynamic calculation with > **calc()** is supported. The format of the input string for **calc()** is Width/Height scaling ratio ± Width/Height > increment, where the scaling ratio is a percentage and the increment unit is px or vp. For example, in > **calc(80% + 10vp)**, **80%** is the width/height scaling ratio, and **10vp** is the width/height increment. If the > width and height are of the **LengthMetrics** type and the unit is percent, the width and height are calculated > relative to the component's own width and height. **percent(1)** indicates 100%. If the calculation result is a > negative value, the default value is used. |
| [ReusableOptions](arkts-arkui-reusableoptions-i.md) | Defines the options for Reusable ClassDecorator. |
| [ReuseOptions](arkts-arkui-reuseoptions-i.md) | Defining the reusable configuration parameters. |
| [RotateAngleOptions](arkts-arkui-rotateangleoptions-i.md) | Rotation parameter option of the rotation angle on each axis. |
| [RotateOptions](arkts-arkui-rotateoptions-i.md) | Defines component rotation parameters. |
| [ScaleOptions](arkts-arkui-scaleoptions-i.md) | Defines the options of scale. |
| [SelectionOptions](arkts-arkui-selectionoptions-i.md) | Defines the selection options. |
| [ShadowOptions](arkts-arkui-shadowoptions-i.md) | Provides the shadow attributes, including the blur radius, color, and offset along the x-axis and y-axis. |
| [sharedTransitionOptions](arkts-arkui-sharedtransitionoptions-i.md) | Parameters of the shared element transition animation. > **NOTE：**> > **motionPath** is effective only when **type** is set to **SharedTransitionEffectType.Exchange**. > > When **type** is set to **SharedTransitionEffectType.Exchange**, the effect focuses on smooth transition of the > position and size of matching shared elements, which can be visually observed through the component's border. The > transition, however, does not involve content properties, which will abruptly change to the target page's values at > the end of the animation. For example, if a **Text** component has different **fontSize** values on two pages, the > font size will snap to the target page's value once the shared transition animation completes. |
| [SheetDismiss](arkts-arkui-sheetdismiss-i.md) | Component sheet dismiss |
| [SheetOptions](arkts-arkui-sheetoptions-i.md) | Optional attributes of the sheet. Inherits from [BindOptions](arkts-arkui-bindoptions-i.md). |
| [SheetTitleOptions](arkts-arkui-sheettitleoptions-i.md) | Component sheet title options |
| [SizeResult](arkts-arkui-sizeresult-i.md) | > **NOTE：**> > - The custom layout does not support the LazyForEach syntax. > - When a custom layout is created in builder mode, only **this.builder()** is allowed in the **build()** method > of a custom component, as shown in the recommended usage in the example below. > - The size parameters of the parent component (custom component), except **aspectRatio**, are at a lower > priority than those specified by onMeasureSize. > - The position parameters of the child component, except **offset**, **position**, and **markAnchor**, are at > a lower priority than those specified by onPlaceChildren, > and do not take effect. > - When using the custom layout method, you must call **onMeasureSize** and **onPlaceChildren** at the same > time for the layout to display properly. |
| [SmartGestureShortcutOptions](arkts-arkui-smartgestureshortcutoptions-i.md) | Smart gesture response behavior configuration object. |
| [SpatialEffectParams](arkts-arkui-spatialeffectparams-i-sys.md) | Spatial effect params. |
| [SpatialPosition](arkts-arkui-spatialposition-i-sys.md) | Spatial corner positions in 3D space. |
| [SpringBackAction](arkts-arkui-springbackaction-i.md) | Defines sheet spring back action |
| [StateStyles](arkts-arkui-statestyles-i.md) | State-specific styles for the component. |
| [SweepGradientOptions](arkts-arkui-sweepgradientoptions-i.md) | Defines the sweep gradient parameters. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. > **NOTE：**> > When using the **metricsColors** parameter, take note of the following: > > [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) represents the fill color, which can be constructed with a specified > color gamut attribute using the [colorWithSpace](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md#colorwithspace) API. **number** > represents the position of the specified color, with a value range of [0, 1.0]. **0** indicates the start of the > container where the gradient color is set, and **1.0** indicates the end of the container. To achieve multi-color > gradients, the **number** parameters in the array should be set in ascending order. If a later number is less than > a previous one, it is treated as equal to the previous value. |
| [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | Provides parameters for system adaptive adjustments. By default, the system performs adaptive adjustments based on chip performance. |
| [TextContentControllerOptions](arkts-arkui-textcontentcontrolleroptions-i.md) | Provides configuration options for text insertion operations in text input components. |
| [TextDecorationOptions](arkts-arkui-textdecorationoptions-i.md) | Provides text decoration options. |
| [TipsOptions](arkts-arkui-tipsoptions-i.md) | Defines the parameters of the tooltip. |
| [TouchEvent](arkts-arkui-touchevent-i.md) | Inherits from [BaseEvent](arkts-arkui-baseevent-i.md). In non-event injection scenarios, **changedTouches** contains points resampled at the screen refresh rate, while **touches** contains points reported at the device's refresh rate. As such, **changedTouches** data may differ from **touches**. |
| [TouchObject](arkts-arkui-touchobject-i.md) | Type of the touch event. |
| [TransitionOptions](arkts-arkui-transitionoptions-i.md) | Defines the transition effect by setting parameters in the struct. > **NOTE：**> > 1. When set to a value of the **TransitionOptions** type, the **transition** attribute must work with > [animateTo](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#animateto). The animation duration, > curve, and delay follow the settings in **animateTo**. > > 2. If the value of the **TransitionOptions** type has only **type** specified, the transition effect will take on > the default opacity. For example, **{type: TransitionType.Insert}** produces the same effect as > **{type: TransitionType.Insert, opacity: 0}**. If a specific style is specified, the transition effect will not > take on the default opacity. |
| [TranslateOptions](arkts-arkui-translateoptions-i.md) | Defines the options of translate. |
| [UICommonEvent](arkts-arkui-uicommonevent-i.md) | Implements a common event callback. Passing **undefined** as the input parameter resets the corresponding event callback. |
| [UIGestureEvent](arkts-arkui-uigestureevent-i.md) | Provides APIs for configuring gestures bound to a component. |
| [UIScrollableCommonEvent](arkts-arkui-uiscrollablecommonevent-i.md) | Defines a UIScrollableCommonEvent which is used to set event to target component. |
| [VerticalAlignParam](arkts-arkui-verticalalignparam-i.md) | Defines the vertical align rule of relative container. |
| [VisibleAreaEventOptions](arkts-arkui-visibleareaeventoptions-i.md) | Describes visible area change configuration options. |

### Types

| Name | Description |
| --- | --- |
| [AccessibilityActionInterceptCallback](arkts-arkui-accessibilityactioninterceptcallback-t.md) | Defines the callback type used in accessibility action intercept. The value of action indicates the accessibility action type. |
| [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) | Defines the callback type used in accessibility hover events. The value of isHover indicates whether the touch is hovering over the component. The value of event contains information about AccessibilityHoverEvent. |
| [AccessibilityFocusCallback](arkts-arkui-accessibilityfocuscallback-t.md) | Defines the callback type used in accessibility focus. The value of isFocus indicates whether the current component is focused |
| [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) | Defines the callback type used in accessibility hover transparent event. |
| [AnimationRange](arkts-arkui-animationrange-t.md) | Sets the relative scale ratio at the start and end of the animation compared to the original preview image. |
| [AreaChangeCallback](arkts-arkui-areachangecallback-t.md) | Callback type for the component area change event. |
| [Blender](arkts-arkui-blender-t-sys.md) | Blender |
| [BorderRadiusType](arkts-arkui-borderradiustype-t.md) | Enumerates the border corner radius types. |
| [BuilderCallback](arkts-arkui-buildercallback-t.md) | Defines the callback type used in mutableBuilder. |
| [CircleShape](arkts-arkui-circleshape-t.md) | Defines the CircleShape type. |
| [ComponentContent](arkts-arkui-componentcontent-t.md) | Represents a constructor used to create a **ComponentContent** object. |
| [Context](arkts-arkui-context-t.md) | Get context. |
| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Defines the CustomBuilder Type. |
| [CustomBuilderT](arkts-arkui-custombuildert-t.md) | Defines the CustomBuilder type with parameter. |
| [DataLoadParams](arkts-arkui-dataloadparams-t.md) | Defines the data loading parameters used during a drop operation. |
| [DataSyncOptions](arkts-arkui-datasyncoptions-t.md) | Defines the input parameter object for **startDataLoading**. |
| [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | Defines the configuration parameters for drag hover detection. |
| [DrawContext](arkts-arkui-drawcontext-t.md) | DrawContext |
| [EllipseShape](arkts-arkui-ellipseshape-t.md) | Defines the EllipseShape type. |
| [EnvDecorator](arkts-arkui-envdecorator-t.md) | Define Env Decorator type |
| [Filter](arkts-arkui-filter-t.md) | Represents a filter object. |
| [FractionStop](arkts-arkui-fractionstop-t.md) | Defines a gradient blur stop. |
| [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | Defines the callback type used in [onGestureCollectIntercept](arkts-arkui-commonmethod-c.md#ongesturecollectintercept). |
| [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | Represents a custom gesture recognizer judgment callback type. |
| [HoverCallback](arkts-arkui-hovercallback-t.md) | Defines the callback type for hover events. |
| [ImageModifier](arkts-arkui-imagemodifier-t.md) | ImageModifier |
| [InputEventListener](arkts-arkui-inputeventlistener-t.md) | Input event listener callback type. > **NOTE：**> > - **RawInputEventWrapper** is an abstract class. Developers cannot create instances using the `new` operator. > > - The system automatically creates instances when an event is triggered and passes them to the callback through > this parameter. > > - The current callback parameter **event** only encapsulates the following raw input event types: > [MouseEvent](arkts-arkui-mouseevent-i.md), [TouchEvent](arkts-arkui-touchevent-i.md), [KeyEvent](arkts-arkui-keyevent-i.md). Developers can obtain > the corresponding event objects using [asMouseEvent](arkts-arkui-rawinputeventwrapper-c.md#asmouseevent), > [asTouchEvent](arkts-arkui-rawinputeventwrapper-c.md#astouchevent), and [asKeyEvent](arkts-arkui-rawinputeventwrapper-c.md#askeyevent). > > - Do not perform time-consuming operations (such as complex calculations or network requests) in the callback, as > this may cause application lag. > > - The listener executes synchronously on the UI thread, which directly blocks the event processing flow. It is > recommended to only perform simple judgment and calculation. |
| [IntentionCode](arkts-arkui-intentioncode-t.md) | Intention corresponding to the key. |
| [Matrix4Transit](arkts-arkui-matrix4transit-t.md) | Import the Matrix4Transit type object for common method. |
| [NavDestinationInfo](arkts-arkui-navdestinationinfo-t.md) | The navigation destination information. |
| [NavigationInfo](arkts-arkui-navigationinfo-t.md) | The navigation information. |
| [OnDidStopDraggingCallback](arkts-arkui-ondidstopdraggingcallback-t.md) | On scroll callback using in scrollable onDidStopDragging. |
| [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) | Defines a callback for drag events. |
| [OnGetPreviewBadgeCallback](arkts-arkui-ongetpreviewbadgecallback-t.md) | Defines the callback type used in onGetPreviewBadge of EditModeOptions. |
| [OnItemDragStartCallback](arkts-arkui-onitemdragstartcallback-t.md) | Defines the callback type used in onItemDragStart. |
| [OnMoveHandler](arkts-arkui-onmovehandler-t.md) | Defines the onMove callback. |
| [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) | Defines the callback type used in onNeedSoftkeyboard. Called when component is focused, the return value indicates whether keyboard is needed. |
| [OnScrollCallback](arkts-arkui-onscrollcallback-t.md) | On scroll callback using in scrollable onDidScroll. |
| [OnVisibleIndexesChangeCallback](arkts-arkui-onvisibleindexeschangecallback-t.md) | Defines the callback type used in OnVisibleIndexesChange. |
| [OnWillScrollCallback](arkts-arkui-onwillscrollcallback-t.md) | Called before scroll to allow developer to control real offset the Scrollable can scroll. |
| [OnWillStopDraggingCallback](arkts-arkui-onwillstopdraggingcallback-t.md) | On scroll callback using in scrollable onWillStopDragging. |
| [Optional](arkts-arkui-optional-t.md) | Defines the Optional type. The value can be **undefined**. |
| [PathShape](arkts-arkui-pathshape-t.md) | Defines the PathShape type. |
| [PixelMap](arkts-arkui-pixelmap-t.md) | Defines the PixelMap type object for ui component. |
| [PointerStyle](arkts-arkui-pointerstyle-t.md) | Defines the pointer style. > **NOTE：**> > Directly using **cursorControl** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > [UIContext](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) object using the **getUIContext()** API and then obtain the > **cursorControl** bound to the instance using the > getCursorController API. |
| [PopupStateChangeCallback](arkts-arkui-popupstatechangecallback-t.md) | Represents the callback invoked when the popup state changes. |
| [PromptActionDialogController](arkts-arkui-promptactiondialogcontroller-t.md) | Import the DialogController type from promptAction. |
| [RectShape](arkts-arkui-rectshape-t.md) | Defines the RectShape type. |
| [ReuseIdCallback](arkts-arkui-reuseidcallback-t.md) | ReuseId callback type. It is used to compute reuseId. |
| [ReusePoolOwnership](arkts-arkui-reusepoolownership-t.md) | Defining the reuse type of a custom component. |
| [RouterPageInfo](arkts-arkui-routerpageinfo-t.md) | The router page information. |
| [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) | Represents the callback used to set the parallel relationship between built-in gestures and gestures of other components in the response chain. |
| [ShouldRecognizerParallelWithCallback](arkts-arkui-shouldrecognizerparallelwithcallback-t.md) | Represents the callback used to set the parallel relationship between gestures of the current component and gestures of other components in the response chain. |
| [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) | Defines the callback type used in onSizeChange. The value of oldValue is last size of the component. The value of newValue is new size of the component. |
| [SpringLoadingContext](arkts-arkui-springloadingcontext-t.md) | Defines callback context information, which is passed to the application in the hover detection callback to allow the application to access the drag status. |
| [Summary](arkts-arkui-summary-t.md) | Provides a summary of drag-related data. |
| [SymbolGlyphModifier](arkts-arkui-symbolglyphmodifier-t.md) | Defines custom icon symbol configurations. |
| [SystemUiMaterial](arkts-arkui-systemuimaterial-t-sys.md) | Base class for system material objects. |
| [Theme](arkts-arkui-theme-t.md) | Theme. |
| [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) | Provides information about the tooltip. |
| [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) | Represents the callback type for dynamically specifying gesture recognizer participation in gesture processing. |
| [TransitionEffects](arkts-arkui-transitioneffects-t.md) | Defines all transition effects. |
| [TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md) | Represents the type of callback for the end of a component's transition animation. |
| [UIContext](arkts-arkui-uicontext-t.md) | UIContext |
| [UnifiedData](arkts-arkui-unifieddata-t.md) | Defines drag-related data. |
| [UniformDataType](arkts-arkui-uniformdatatype-t.md) | Import the UniformDataType type object for ui component. |
| [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | Represents a callback for visible area changes of the component. |
| [VisualEffect](arkts-arkui-visualeffect-t.md) | Represents a visual effect configuration object. |
| [window](arkts-arkui-window-t.md) | The type for window. |

### Enums

| Name | Description |
| --- | --- |
| [AccessibilityAction](arkts-arkui-accessibilityaction-e.md) | Enum for accessibility action type |
| [AccessibilityActionInterceptResult](arkts-arkui-accessibilityactioninterceptresult-e.md) | Enum for the result of accessibility action intercept function |
| [AccessibilityRoleType](arkts-arkui-accessibilityroletype-e.md) | Enumerates the component role types used by screen readers. |
| [AccessibilitySamePageMode](arkts-arkui-accessibilitysamepagemode-e.md) | Enumerates the same-page modes for cross-process embedded components and their host applications. |
| [AdaptiveColor](arkts-arkui-adaptivecolor-e.md) | Enumerates the adaptive color modes used for the background blur effect. |
| [AnchoredColorMode](arkts-arkui-anchoredcolormode-e.md) |  |
| [AvailableLayoutArea](arkts-arkui-availablelayoutarea-e.md) | Enumerates the reference sizes of the available layout area when the preview image width and height are set to percentages. |
| [BlendApplyType](arkts-arkui-blendapplytype-e.md) | Defines how to apply the specified blend mode to the content of a view. |
| [BlendMode](arkts-arkui-blendmode-e.md) | Blend mode. > **NOTE：**> > In the **blendMode** enums, **s** indicates the source pixel, **d** indicates the target pixel, **sa** indicates > the opacity of the source pixel, **da** indicates the opacity of the target pixel, **r** indicates the pixel after > blending, and **ra** indicates the opacity of the pixel after blending. |
| [BlurStyle](arkts-arkui-blurstyle-e.md) | Enumerates blur styles. |
| [BlurStyleActivePolicy](arkts-arkui-blurstyleactivepolicy-e.md) | Enumerates the policies for activating the blur style. |
| [ChainStyle](arkts-arkui-chainstyle-e.md) | Enumerates the chain styles in relative container. |
| [ContentClipMode](arkts-arkui-contentclipmode-e.md) | Enum of scrollable containers' content clip mode. |
| [DismissReason](arkts-arkui-dismissreason-e.md) | Enumerates the reasons for popup dismissal. |
| [DistortionMode](arkts-arkui-distortionmode-e-sys.md) | Enum for distortion animation mode. |
| [DragAnimationType](arkts-arkui-draganimationtype-e-sys.md) | Enumerates drag animation types. |
| [DragBehavior](arkts-arkui-dragbehavior-e.md) | Describes the drag behavior. When [DragResult](arkts-arkui-dragresult-e.md) is set to **DROP_ENABLED**, you can define **DragBehavior** as either **COPY** or **MOVE**. When **DragBehavior** is set to **COPY**, a plus sign will be displayed in the badge of the dragged object. When **DragBehavior** is set to **MOVE**, the plus sign will not be displayed. **DragBehavior** is used to indicate the intended way of handling data (either copy or move) without governing the actual data processing. This behavior is reported back to the drag source through **onDragEnd**, enabling the drag initiator to distinguish whether the operation results in a copy or a move of the data. |
| [DraggingSizeChangeEffect](arkts-arkui-draggingsizechangeeffect-e.md) | Enumerates the transition effects for switching between the floating image (set through [bindContextMenu](arkts-arkui-commonmethod-c.md#bindcontextmenu) ) and the drag preview when both are configured on a component. |
| [DragPreviewMode](arkts-arkui-dragpreviewmode-e.md) | Sets the display mode of the drag preview. |
| [DragResult](arkts-arkui-dragresult-e.md) | Defines the result of a drag operation and the drop-selection state of a component. |
| [EdgeLightMode](arkts-arkui-edgelightmode-e-sys.md) | Edge light animation mode enumeration. |
| [EffectEdge](arkts-arkui-effectedge-e.md) | Enumerates the effective edge of the edge effect. |
| [EffectType](arkts-arkui-effecttype-e.md) | Enum of using the effects template mode. **Effect Template: ** | Device Type | Fuzzy Radius (Unit: px) | Saturation | Brightness | Color | | -------- | ---- | ---------------------- | -------- | -------- | | Mobile device | 0 | 0 | 0 | '#ffffffff', displayed as white.| | 2-in-1 device: dark mode | 80 | 1.5 | 1.0 | '#e52e3033', displayed as a semi-transparent light red.| | 2-in-1 device: light mode | 80 | 1.9 | 1.0 | '#e5ffffff', displayed as a semi-transparent dark red.| | Tablet | 0 | 0 | 0 | '#ffffffff', displayed as white.| |
| [FinishCallbackType](arkts-arkui-finishcallbacktype-e.md) | Defines the type of the **onFinish** callback. |
| [HapticFeedbackMode](arkts-arkui-hapticfeedbackmode-e.md) | Enumerates the haptic feedback modes used when the menu is displayed. |
| [HoverModeAreaType](arkts-arkui-hovermodeareatype-e.md) | Enumerates the type of area in hover mode. |
| [KeyboardAvoidMode](arkts-arkui-keyboardavoidmode-e.md) | Enumerates modes in which a popup responds when the keyboard is displayed. |
| [LayoutSafeAreaEdge](arkts-arkui-layoutsafeareaedge-e.md) | Define the edges for expanding the safe area in layout. |
| [LayoutSafeAreaType](arkts-arkui-layoutsafeareatype-e.md) | Enumerates the types for expanding layout safe areas. |
| [MenuGridPosition](arkts-arkui-menugridposition-e.md) | The position of grid in menu. |
| [MenuKeyboardAvoidMode](arkts-arkui-menukeyboardavoidmode-e.md) | Enumerates the modes in which the menu avoids the soft keyboard. |
| [MenuPolicy](arkts-arkui-menupolicy-e.md) | Enumerates menu display policies. |
| [MenuPreviewMode](arkts-arkui-menupreviewmode-e.md) | Defines the preview style of a menu. |
| [ModalMode](arkts-arkui-modalmode-e.md) | Enumerates modal modes of the sub-window menu. |
| [ModalTransition](arkts-arkui-modaltransition-e.md) | Defines modal transition type. |
| [OutlineStyle](arkts-arkui-outlinestyle-e.md) | Enumerates outline styles. |
| [PreDragStatus](arkts-arkui-predragstatus-e.md) | Defines the states before the drag gesture is triggered. |
| [PreviewScaleMode](arkts-arkui-previewscalemode-e.md) | Enumerates the scale modes of the preview image. |
| [RepeatMode](arkts-arkui-repeatmode-e.md) | Defines the Border Image Repeat Mode. |
| [ReusableMemOptStrategy](arkts-arkui-reusablememoptstrategy-e.md) | Defines a type for memory optimization strategy. |
| [SafeAreaEdge](arkts-arkui-safeareaedge-e.md) | Enumerates the edges for expanding the safe area. |
| [SafeAreaType](arkts-arkui-safeareatype-e.md) | Enumerates the types for expanding layout safe areas. |
| [ScrollSizeMode](arkts-arkui-scrollsizemode-e.md) | Define the scroll size mode of the sheet. |
| [ShadowStyle](arkts-arkui-shadowstyle-e.md) | enum Shadow style |
| [ShadowType](arkts-arkui-shadowtype-e.md) | Define the type of shadow |
| [SheetKeyboardAvoidMode](arkts-arkui-sheetkeyboardavoidmode-e.md) | Define the mode of sheet how to avoid keyboard. |
| [SheetMode](arkts-arkui-sheetmode-e.md) | Define the display mode of the sheet. |
| [SheetSize](arkts-arkui-sheetsize-e.md) | Defines sheet size type. |
| [SheetType](arkts-arkui-sheettype-e.md) | Defines the sheet type. |
| [SourceTool](arkts-arkui-sourcetool-e.md) | Enumerates the input source tool types. |
| [SourceType](arkts-arkui-sourcetype-e.md) | Enumerates the input source device types. |
| [SpatialPositionMode](arkts-arkui-spatialpositionmode-e-sys.md) | Spatial position mode. Indicates the coordinate system used by the corner positions. |
| [SystemProperties](arkts-arkui-systemproperties-e.md) | Defining Environment variable enumeration value. |
| [ThemeColorMode](arkts-arkui-themecolormode-e.md) | Enumerates the color modes. |
| [TouchTestStrategy](arkts-arkui-touchteststrategy-e.md) | Event dispatch strategy. |
| [TransitionEdge](arkts-arkui-transitionedge-e.md) | Enumerates the transition edge types. |
| [TransitionHierarchyStrategy](arkts-arkui-transitionhierarchystrategy-e-sys.md) | Enumerates the strategies for the hierarchical position movement of **in** / **out** components in the component tree during the shared element transition process. |

