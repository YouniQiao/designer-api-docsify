# component/common

Defines the namespace of focus controller.

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [cursorControl](arkts-arkui-cursorcontrol-n.md) | CursorControl |
| [focusControl](arkts-arkui-focuscontrol-n.md) | Defines the namespace of focus controller. |

### Functions

| Name | Description |
| --- | --- |
| [$$](common-$$-f.md#$$) | Convert to a bindable property. |
| [$r](common-$r-f.md#$r) | global \_\_\_ESCAPED\_DOLLAR\_\_\_r function |
| [$rawfile](common-$rawfile-f.md#$rawfile) | global \_\_\_ESCAPED\_DOLLAR\_\_\_rawfile function |
| [animateToImmediately](common-animatetoimmediately-f.md#animatetoimmediately) | Define animation functions for immediate distribution.This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to explicitly specify the UI context. |
| [applyStyles](common-applystyles-f.md#applystyles) | Apply style function on this CommonMethod. |
| [makeBindable](common-makebindable-f.md#makebindable) | Create a bindable property instance. |

### Classes

| Name | Description |
| --- | --- |
| [ChildrenMainSize](common-childrenmainsize-c.md) | Indicates children main size. |
| [ContentTransitionEffect](common-contenttransitioneffect-c.md) | Defines the content transition effect. |
| [DrawModifier](common-drawmodifier-c.md) | Defined the draw modifier of node. Provides draw callbacks for the associated Node.Each DrawModifier instance can be set for only one component. Repeated setting is not allowed. |
| [LayoutPolicy](common-layoutpolicy-c.md) | Defines the policy of Layout |
| [ProgressMask](common-progressmask-c.md) | Implements a ProgressMask object to set the progress, maximum value, and color of the mask. |
| [RawInputEventWrapper](common-rawinputeventwrapper-c.md) | Defines the raw input event wrapper. |
| [ScrollResult](common-scrollresult-c.md) | The actual offset by which the scrollable scrolls. |
| [TextContentControllerBase](common-textcontentcontrollerbase-c.md) | TextContentControllerBase |
| [TouchResult](common-touchresult-c.md) | Defines TouchResult class. |
| [TouchTestInfo](common-touchtestinfo-c.md) | Defines TouchTestInfo class. |
| [TransitionEffect](common-transitioneffect-c.md) | Defines the transition effect |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [TextContentControllerBase](common-textcontentcontrollerbase-c-sys.md) | TextContentControllerBase |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AccessibilityHoverEvent](common-accessibilityhoverevent-i.md) | The accessibility hover action triggers this method invocation. |
| [AlignRuleOption](common-alignruleoption-i.md) | Defines the align rule options of relative container. |
| [AnimatableArithmetic](common-animatablearithmetic-i.md) | The **AnimatableArithmetic** API defines the animation operation rules for non-number data types. To animate non-number data (such as arrays, structs,and colors), implement the addition, subtraction, multiplication, and equality judgment functions in the **AnimatableArithmetic\&lt;T\&gt;** API.In this way, the data can be involved in an interpolation operation of the animation and identify whether the data changes, that is, the non-number data is defined as the types that implement the **AnimatableArithmetic\&lt;T\&gt;** API. |
| [AnimateParam](common-animateparam-i.md) | Defines the animate function params. |
| [AreaChangeOptions](common-areachangeoptions-i.md) | Defines the options about AreaChangeEvent. |
| [AsymmetricTransitionOption](common-asymmetrictransitionoption-i.md) | Defines the option of asymmetric transition. |
| [AttributeModifier](common-attributemodifier-i.md) | Defines the attribute modifier. |
| [AxisEvent](common-axisevent-i.md) | The axis event triggers this method invocation. |
| [BackgroundBlurStyleOptions](common-backgroundblurstyleoptions-i.md) | Defines the options of backgroundBlurStyle |
| [BackgroundBrightnessOptions](common-backgroundbrightnessoptions-i.md) | Define BackgroundBrightness Options. |
| [BackgroundEffectOptions](common-backgroundeffectoptions-i.md) | Defines the options of BackgroundEffect |
| [BackgroundImageOptions](common-backgroundimageoptions-i.md) | Define the options for background image. |
| [BackgroundOptions](common-backgroundoptions-i.md) | Defines background options. |
| [BaseEvent](common-baseevent-i.md) | Defines the base event. |
| [BindOptions](common-bindoptions-i.md) | Overlay module options |
| [Bindable](common-bindable-i.md) | Defines a bindable property |
| [BlurOptions](common-bluroptions-i.md) | Defines the options of blur |
| [BlurStyleOptions](common-blurstyleoptions-i.md) | Defines the options of blurStyle |
| [BorderImageOption](common-borderimageoption-i.md) | Border image option |
| [CaretOffset](common-caretoffset-i.md) | CaretOffset info. |
| [ClickEffect](common-clickeffect-i.md) | Defines the click effect. |
| [ClickEvent](common-clickevent-i.md) | The tap action triggers this method invocation. |
| [CommonConfiguration](common-commonconfiguration-i.md) | Defines the common configuration. |
| [CommonMethod](common-commonmethod-i.md) | CommonMethod |
| [Configuration](common-configuration-i.md) | Defines the data type of the interface restriction. |
| [ContentCoverOptions](common-contentcoveroptions-i.md) | Component content cover options |
| [ContentModifier](common-contentmodifier-i.md) | Defines the content modifier. |
| [ContextMenuAnimationOptions](common-contextmenuanimationoptions-i.md) | Defines the ContextMenu's preview animator options. |
| [ContextMenuOptions](common-contextmenuoptions-i.md) | Defines the context menu options. |
| [CrownEvent](common-crownevent-i.md) | CrownEvent object description |
| [CustomPopupOptions](common-custompopupoptions-i.md) | Defines the custom popup options. |
| [DateRange](common-daterange-i.md) | Defines a range of dates. |
| [DismissContentCoverAction](common-dismisscontentcoveraction-i.md) | Component content cover dismiss |
| [DismissPopupAction](common-dismisspopupaction-i.md) | Component popup dismiss |
| [DismissSheetAction](common-dismisssheetaction-i.md) | Component sheet dismiss |
| [DividerStyle](common-dividerstyle-i.md) | Provides an interface for the style of an divider including stroke width, color, start margin and end margin |
| [DragEvent](common-dragevent-i.md) | DragEvent object description |
| [DragInteractionOptions](common-draginteractionoptions-i.md) | Defines the drag options. |
| [DragItemInfo](common-dragiteminfo-i.md) | DragItemInfo object description |
| [DragPreviewOptions](common-dragpreviewoptions-i.md) | Defines the preview options. |
| [DropOptions](common-dropoptions-i.md) | Defines the options for the drop handling. |
| [DynamicNode](common-dynamicnode-i.md) | Define DynamicNode. |
| [EdgeEffectOptions](common-edgeeffectoptions-i.md) | Define EdgeEffect Options. |
| [EditModeOptions](common-editmodeoptions-i.md) | Define edit mode options. |
| [EventTarget](common-eventtarget-i.md) | Defines the event target. |
| [ExpectedFrameRateRange](common-expectedframeraterange-i.md) | Interface for ExpectedFrameRateRange. |
| [FadingEdgeOptions](common-fadingedgeoptions-i.md) | Defines the fadingEdge options. |
| [FocusAxisEvent](common-focusaxisevent-i.md) | Focus axis event object description. |
| [FocusMovement](common-focusmovement-i.md) | Defines the next focus item. |
| [ForegroundBlurStyleOptions](common-foregroundblurstyleoptions-i.md) | Defines the options of ForegroundBlurStyle |
| [ForegroundEffectOptions](common-foregroundeffectoptions-i.md) | Defines the options of ForegroundEffect |
| [GeometryInfo](common-geometryinfo-i.md) | Sub component layout info. |
| [GeometryTransitionOptions](common-geometrytransitionoptions-i.md) | Defines the options of geometry transition. |
| [GestureModifier](common-gesturemodifier-i.md) | Defines the gesture modifier. |
| [HistoricalPoint](common-historicalpoint-i.md) | TouchObject getHistoricalPoints Function Parameters |
| [HorizontalAlignParam](common-horizontalalignparam-i.md) | Defines the horizontal align rule options of relative container. |
| [HoverEvent](common-hoverevent-i.md) | The hover action triggers this method invocation. |
| [InputCounterOptions](common-inputcounteroptions-i.md) | Define the ratio of characters entered by the the percentage of InputCounterOptions. |
| [InputEventInterceptResult](common-inputeventinterceptresult-i.md) | Defines the input event intercept result. |
| [InputEventMonitor](common-inputeventmonitor-i.md) | Defines the input event monitor identifier.  Important Notes:  - This object is created and returned by the system as a unique identifier for the listener.  - The object is an empty object with no accessible members.  - Developers cannot actively construct this object, it can only be obtained through the registration interface.  - Used for subsequent unregistration to verify identity. |
| [InvertOptions](common-invertoptions-i.md) | Define the options of invert |
| [ItemDragEventHandler](common-itemdrageventhandler-i.md) | Define item drag event handler. |
| [ItemDragInfo](common-itemdraginfo-i.md) | ItemDragInfo object description |
| [KeyEvent](common-keyevent-i.md) | KeyEvent object description: |
| [KeyframeAnimateParam](common-keyframeanimateparam-i.md) | Defines the overall animation parameters of the keyframe animation. |
| [KeyframeState](common-keyframestate-i.md) | Defines a keyframe state. |
| [Layoutable](common-layoutable-i.md) | Provides the child component layout information. |
| [LinearGradientBlurOptions](common-lineargradientbluroptions-i.md) | Linear Gradient Blur Interface |
| [LinearGradientOptions](common-lineargradientoptions-i.md) | Defines the options of linear gradient. |
| [LocalizedAlignRuleOptions](common-localizedalignruleoptions-i.md) | Defines the Localized align rule options of relative container. |
| [LocalizedHorizontalAlignParam](common-localizedhorizontalalignparam-i.md) | Defines the localized horizontal align param of relative container. |
| [LocalizedVerticalAlignParam](common-localizedverticalalignparam-i.md) | Defines the localized vertical align param of relative container. |
| [Measurable](common-measurable-i.md) | Sub component info passed from framework when measure happens. |
| [MeasureResult](common-measureresult-i.md) | Provides the measurement result of the component. |
| [MenuElement](common-menuelement-i.md) | Defines the menu element. |
| [MenuGridStyleOptions](common-menugridstyleoptions-i.md) | Defines grid style of menu. |
| [MenuMaskType](common-menumasktype-i.md) | Menu mask type |
| [MenuOptions](common-menuoptions-i.md) | Defines the menu options. |
| [MotionBlurAnchor](common-motionbluranchor-i.md) | Define motion blur anchor coordinates. |
| [MotionBlurOptions](common-motionbluroptions-i.md) | Define motion blur options. |
| [MotionPathOptions](common-motionpathoptions-i.md) | Defines the motion path options. |
| [MouseEvent](common-mouseevent-i.md) | The mouse click action triggers this method invocation. |
| [MouseHistoricalPoint](common-mousehistoricalpoint-i.md) | Defines the historical point information for mouse event. |
| [MultiShadowOptions](common-multishadowoptions-i.md) | Defines the options of Shadow. |
| [NestedScrollOptions](common-nestedscrolloptions-i.md) | Define nested scroll options |
| [OverlayOffset](common-overlayoffset-i.md) | Defines the OverlayOffset. |
| [OverlayOptions](common-overlayoptions-i.md) | Defines the OverlayOptions interface.  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_NOTE\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_:\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_When both align and offset are set, the effects are combined.The overlay is first aligned relative to the component and then offset from its current upper left corner. |
| [PickerDialogButtonStyle](common-pickerdialogbuttonstyle-i.md) | Provide an interface for the button style of picker |
| [PickerTextStyle](common-pickertextstyle-i.md) | Provide an interface for the text style of picker |
| [PixelRoundPolicy](common-pixelroundpolicy-i.md) | Defines the direction of pixel rounding at the component level. |
| [PixelStretchEffectOptions](common-pixelstretcheffectoptions-i.md) | Set the edge blur effect distance of the corresponding defense line of the component When the component expand out, no re-layout is triggered |
| [PopupBorderLinearGradient](common-popupborderlineargradient-i.md) | Popup border LinearGradient |
| [PopupButton](common-popupbutton-i.md) | Defines the popup button. |
| [PopupCommonOptions](common-popupcommonoptions-i.md) | Popup common options |
| [PopupMaskType](common-popupmasktype-i.md) | Popup mask type |
| [PopupMessageOptions](common-popupmessageoptions-i.md) | Defines the options of popup message. |
| [PopupOptions](common-popupoptions-i.md) | Defines the popup options. |
| [PopupStateChangeParam](common-popupstatechangeparam-i.md) | Popup state change param |
| [PreviewConfiguration](common-previewconfiguration-i.md) | Defines the drag preview configuration. |
| [RadialGradientOptions](common-radialgradientoptions-i.md) | Defines the options of radial gradient. |
| [RectResult](common-rectresult-i.md) | Describe the position, width, and height of a component. |
| [Rectangle](common-rectangle-i.md) | The data type used to describe a rectangular area. |
| [ResponseRegion](common-responseregion-i.md) | Defines the response region interface. |
| [ReuseOptions](common-reuseoptions-i.md) | Defining the reusable configuration parameters. |
| [RotateAngleOptions](common-rotateangleoptions-i.md) | The rotation parameters containing multi-axis angle information. |
| [RotateOptions](common-rotateoptions-i.md) | The param of rotate. |
| [ScaleOptions](common-scaleoptions-i.md) | Defines the options of scale. |
| [SelectionOptions](common-selectionoptions-i.md) | Defines the selection options. |
| [ShadowOptions](common-shadowoptions-i.md) | Define the options of shadow |
| [SheetDismiss](common-sheetdismiss-i.md) | Component sheet dismiss |
| [SheetOptions](common-sheetoptions-i.md) | Component sheet options |
| [SheetTitleOptions](common-sheettitleoptions-i.md) | Component sheet title options |
| [SizeResult](common-sizeresult-i.md) | Provides the component size information. |
| [SmartGestureShortcutOptions](common-smartgestureshortcutoptions-i.md) | Options for configuring smart gesture shortcuts. |
| [SpringBackAction](common-springbackaction-i.md) | Defines sheet spring back action |
| [StateStyles](common-statestyles-i.md) | Component State Styles. |
| [SweepGradientOptions](common-sweepgradientoptions-i.md) | Defines the options of sweep gradient. |
| [SystemAdaptiveOptions](common-systemadaptiveoptions-i.md) | Defines the SystemAdaptiveOptions interface |
| [TerminationInfo](common-terminationinfo-i.md) | Indicates the information when the provider of the embedded UI is terminated. |
| [TextContentControllerOptions](common-textcontentcontrolleroptions-i.md) | Defines the span options of TextContentController. |
| [TextDecorationOptions](common-textdecorationoptions-i.md) | Defines the options of decoration. |
| [TipsOptions](common-tipsoptions-i.md) | Defines the Tips options. |
| [TouchEvent](common-touchevent-i.md) | Touch Action Function Parameters |
| [TouchObject](common-touchobject-i.md) | Type of the touch event. |
| [TranslateOptions](common-translateoptions-i.md) | Defines the options of translate. |
| [UICommonEvent](common-uicommonevent-i.md) | Defines a UICommonEvent which is used to set different common event to target component. |
| [UIGestureEvent](common-uigestureevent-i.md) | Defines a UIGestureEvent which is used to set different gestures to target component. |
| [UIScrollableCommonEvent](common-uiscrollablecommonevent-i.md) | Defines a UIScrollableCommonEvent which is used to set event to target component. |
| [VerticalAlignParam](common-verticalalignparam-i.md) | Defines the align rule options of relative container. |
| [VisibleAreaEventOptions](common-visibleareaeventoptions-i.md) | Defines the options about VisibleAreaEvent. |
| [sharedTransitionOptions](common-sharedtransitionoptions-i.md) | Defines the shard transition function params. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [BlurSnapshotOptions](common-blursnapshotoptions-i-sys.md) | Defines the options for blur snapshot optimization.Setting this object enables blur optimization. |
| [CommonMethod](common-commonmethod-i-sys.md) | CommonMethod |
| [ContextMenuOptions](common-contextmenuoptions-i-sys.md) | Defines the context menu options. |
| [DepthColorRGB](common-depthcolorrgb-i-sys.md) | RGB color in depth space. |
| [DepthVector3](common-depthvector3-i-sys.md) | 3D vector in depth space. |
| [DepthVector4](common-depthvector4-i-sys.md) | 4D vector in depth space. |
| [DragEvent](common-dragevent-i-sys.md) | DragEvent object description |
| [EdgeLightParams](common-edgelightparams-i-sys.md) | Defines the parameters of the edge light effect. |
| [GeometryTransitionOptions](common-geometrytransitionoptions-i-sys.md) | Defines the options of geometry transition. |
| [GravityCenterOptions](common-gravitycenteroptions-i-sys.md) | Defines the parameters of the center of gravity. |
| [LightSource](common-lightsource-i-sys.md) | LightSource info |
| [PixelMapMock](common-pixelmapmock-i-sys.md) | pixelmap object with release function. |
| [PointLightStyle](common-pointlightstyle-i-sys.md) | PointLightStyle info |
| [SheetOptions](common-sheetoptions-i-sys.md) | Component sheet options |
| [SpatialEffectParams](common-spatialeffectparams-i-sys.md) | Spatial effect params. |
| [SpatialPosition](common-spatialposition-i-sys.md) | Spatial corner positions in 3D space. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AccessibilityAction](common-accessibilityaction-e.md) | Enum for accessibility action type |
| [AccessibilityActionInterceptResult](common-accessibilityactioninterceptresult-e.md) | Enum for the result of accessibility action intercept function |
| [AccessibilityRoleType](common-accessibilityroletype-e.md) | Enumerates the component role types used by screen readers. |
| [AccessibilitySamePageMode](common-accessibilitysamepagemode-e.md) | Enumerates the same-page modes for cross-process embedded components and their host applications. |
| [AdaptiveColor](common-adaptivecolor-e.md) | Defines adaptive color |
| [AnchoredColorMode](common-anchoredcolormode-e.md) | enum color mode of pointing popup |
| [AvailableLayoutArea](common-availablelayoutarea-e.md) | Defines the available layout area. |
| [BlendApplyType](common-blendapplytype-e.md) | Enum for BlendApplyType.Indicate how to apply specified blend mode to the view's content. |
| [BlendMode](common-blendmode-e.md) | Enum for BlendMode.Blend modes for compositing current component with overlapping content. Use overlapping content as dst, current component as src. |
| [BlurStyle](common-blurstyle-e.md) | enum Blur style |
| [BlurStyleActivePolicy](common-blurstyleactivepolicy-e.md) | Enumerates the policies for activating the blur style. |
| [ChainStyle](common-chainstyle-e.md) | Enumerates the chain styles in relative container. |
| [ContentClipMode](common-contentclipmode-e.md) | Enum of scrollable containers' content clip mode. |
| [DismissReason](common-dismissreason-e.md) | Dismiss reason type. |
| [DragBehavior](common-dragbehavior-e.md) | Enum for Drag Behavior.  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_NOTE\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_:\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_DragBehavior serves to inform you about the intended method of data handling,whether it's a copy or a move, but it does not actually dictate the real processing of the data. |
| [DragPreviewMode](common-dragpreviewmode-e.md) | Defines the drag preview mode. |
| [DragResult](common-dragresult-e.md) | Enum for Drag Result. |
| [DraggingSizeChangeEffect](common-draggingsizechangeeffect-e.md) | Define drag start animation effect from drag preview to the handle drag image |
| [EffectEdge](common-effectedge-e.md) | Enumerates the effective edge of the edge effect. |
| [EffectType](common-effecttype-e.md) | Enum of using the effects template mode. |
| [FinishCallbackType](common-finishcallbacktype-e.md) | Enum for FinishCallbackType. |
| [HapticFeedbackMode](common-hapticfeedbackmode-e.md) | Defines the menu haptic feedback mode. |
| [HoverModeAreaType](common-hovermodeareatype-e.md) | Enumerates the type of area in hover mode. |
| [KeyboardAvoidMode](common-keyboardavoidmode-e.md) | enum keyboard avoid mode |
| [LayoutSafeAreaEdge](common-layoutsafeareaedge-e.md) | Define the edges for expanding the safe area in layout. |
| [LayoutSafeAreaType](common-layoutsafeareatype-e.md) | Describe the types for expanding the safe area in layout. |
| [MenuGridPosition](common-menugridposition-e.md) | Defines menu grid position. |
| [MenuKeyboardAvoidMode](common-menukeyboardavoidmode-e.md) | Define the mode of menu how to avoid keyboard. |
| [MenuPolicy](common-menupolicy-e.md) | Define the menu pop-up policy |
| [MenuPreviewMode](common-menupreviewmode-e.md) | Defines the menu preview mode. |
| [ModalMode](common-modalmode-e.md) | Define the modal mode of menu. |
| [ModalTransition](common-modaltransition-e.md) | Defines modal transition type. |
| [OutlineStyle](common-outlinestyle-e.md) | Outline Style |
| [PreDragStatus](common-predragstatus-e.md) | Defines the drag status before drag action. |
| [PreviewScaleMode](common-previewscalemode-e.md) | Defines the scaling mode for custom preview of contextMenu. |
| [RepeatMode](common-repeatmode-e.md) | Defines the Border Image Repeat Mode. |
| [SafeAreaEdge](common-safeareaedge-e.md) | Enumerates the safe area edges. |
| [SafeAreaType](common-safeareatype-e.md) | The types of expanded safe areas. |
| [ScrollSizeMode](common-scrollsizemode-e.md) | Define the scroll size mode of the sheet. |
| [ShadowStyle](common-shadowstyle-e.md) | enum Shadow style |
| [ShadowType](common-shadowtype-e.md) | Define the type of shadow |
| [SheetKeyboardAvoidMode](common-sheetkeyboardavoidmode-e.md) | Define the mode of sheet how to avoid keyboard. |
| [SheetMode](common-sheetmode-e.md) | Define the display mode of the sheet. |
| [SheetSize](common-sheetsize-e.md) | Defines sheet size type. |
| [SheetType](common-sheettype-e.md) | Defines the sheet type. |
| [SourceTool](common-sourcetool-e.md) | Defines the event tool type. |
| [SourceType](common-sourcetype-e.md) | Defines the event source type. |
| [ThemeColorMode](common-themecolormode-e.md) | enum color mode |
| [TouchTestStrategy](common-touchteststrategy-e.md) | Defines the touch test strategy object. |
| [TransitionEdge](common-transitionedge-e.md) | Defines the Edge object. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [BlendApplyType](common-blendapplytype-e-sys.md) | Enum for BlendApplyType.Indicate how to apply specified blend mode to the view's content. |
| [DistortionMode](common-distortionmode-e-sys.md) | Enum for distortion animation mode. |
| [DragAnimationType](common-draganimationtype-e-sys.md) | Enum for Drag Animation Type. |
| [EdgeLightMode](common-edgelightmode-e-sys.md) | Enum for edgeLight animation mode. |
| [SpatialPositionMode](common-spatialpositionmode-e-sys.md) | Spatial position mode. Indicates the coordinate system used by the corner positions. |
| [TransitionHierarchyStrategy](common-transitionhierarchystrategy-e-sys.md) | Source and target are two matched elements during the geometry transition.The animation starts at the source and ends at the target.TransitionHierarchyStrategy enumeration defines how levels of source and target elements would be changed in the hierarchy during the geometry transition. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [AccessibilityActionInterceptCallback](arkts-arkui-accessibilityactioninterceptcallback-t.md) | Defines the callback type used in accessibility action intercept.The value of action indicates the accessibility action type. |
| [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) | Defines the callback type used in accessibility hover events.The value of isHover indicates whether the touch is hovering over the component.The value of event contains information about AccessibilityHoverEvent. |
| [AccessibilityFocusCallback](arkts-arkui-accessibilityfocuscallback-t.md) | Defines the callback type used in accessibility focus. The value of isFocus indicates whether the current component is focused |
| [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) | Defines the callback type used in accessibility hover transparent event. |
| [AnimationNumberRange](arkts-arkui-animationnumberrange-t.md) | Defines the animator range of start and end property. |
| [AreaChangeCallback](arkts-arkui-areachangecallback-t.md) | Defines the options for the AreaChangeEvent. |
| [BindableResourceStr](arkts-arkui-bindableresourcestr-t.md) | Defines the Two-way binding type of ResourceStr. |
| [BindableResourceStrArray](arkts-arkui-bindableresourcestrarray-t.md) | Defines the Two-way binding type of ResourceStr[]. |
| [BorderRadiusType](arkts-arkui-borderradiustype-t.md) | Defines the type of border radius. |
| [Callback](arkts-arkui-callback-t.md) | Defines the callback |
| [CommonAttribute](arkts-arkui-commonattribute-t.md) | CommonAttribute for ide. |
| [Context](arkts-arkui-context-t.md) | Export Context. |
| [CustomProperty](arkts-arkui-customproperty-t.md) | Defines the value of the custom property.. |
| [CustomStyles](arkts-arkui-customstyles-t.md) | The custom styles function block. |
| [DataLoadParams](arkts-arkui-dataloadparams-t.md) | Import the DataLoadParams type object for ui component. |
| [DataSyncOptions](arkts-arkui-datasyncoptions-t.md) | Import the GetDataParams type object for ui component. |
| [DateTimeOptions](arkts-arkui-datetimeoptions-t.md) | Defines the format for displaying dates and times. |
| [DoubleLengthDetents](arkts-arkui-doublelengthdetents-t.md) | Defines the detent array of a two-length. |
| [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | The type for DragSpringLoadingConfiguration, see the detailed description in dragController. |
| [DrawContext](arkts-arkui-drawcontext-t.md) | DrawContext. |
| [Filter](arkts-arkui-filter-t.md) | Filter |
| [FractionStop](arkts-arkui-fractionstop-t.md) | Defines the segment of blur.The first element in the tuple means fraction.The range of this value is [0,1]. A value of 1 means opaque and 0 means completely transparent.The second element means the stop position.The range of this value is [0,1]. A value of 1 means region ending position and 0 means region starting position. |
| [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | Defines the callback type used in onGestureCollectIntercept. |
| [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | Defines the callback type used in onGestureRecognizerJudgeBegin. |
| [HoverCallback](arkts-arkui-hovercallback-t.md) | Defines the callback type used in hover events.The value of isHover indicates whether the mouse is hovering over the component.The value of event contains information about HoverEvent. |
| [ICurve](arkts-arkui-icurve-t.md) | Interface for curve object. |
| [InputEventListener](arkts-arkui-inputeventlistener-t.md) | Defines the input event listener callback function type.  Performance Warning: Do not perform time-consuming operations in the callback, otherwise it may cause the application to freeze.  The listener executes synchronously in the UI thread and will directly block the event processing flow.It is recommended to only perform simple judgments and calculations, avoiding:  - Synchronous I/O operations  - Complex data processing  - Network requests  - Massive log output |
| [Matrix4Transit](arkts-arkui-matrix4transit-t.md) | Interface for matrix object. |
| [ModifierKeyStateGetter](arkts-arkui-modifierkeystategetter-t.md) | The modifier key state query function block. |
| [NavDestinationInfo](arkts-arkui-navdestinationinfo-t.md) | The navigation destination information. |
| [NavigationInfo](arkts-arkui-navigationinfo-t.md) | The navigation information. |
| [OnDidStopDraggingCallback](arkts-arkui-ondidstopdraggingcallback-t.md) | On scroll callback using in scrollable onDidStopDragging. |
| [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) | The event callback function for drag and drop common interfaces. |
| [OnGetPreviewBadgeCallback](arkts-arkui-ongetpreviewbadgecallback-t.md) | Defines the callback type used in onGetPreviewBadge of EditModeOptions. |
| [OnItemDragStartCallback](arkts-arkui-onitemdragstartcallback-t.md) | Defines the callback type used in onItemDragStart. |
| [OnMoveHandler](arkts-arkui-onmovehandler-t.md) | Defines the onMove callback. |
| [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) | Defines the callback type used in onNeedSoftkeyboard.Called when component is focused, the return value indicates whether keyboard is needed. |
| [OnScrollCallback](arkts-arkui-onscrollcallback-t.md) | On scroll callback using in scrollable onDidScroll. |
| [OnVisibleIndexesChangeCallback](arkts-arkui-onvisibleindexeschangecallback-t.md) | Defines the callback type used in OnVisibleIndexesChange. |
| [OnWillScrollCallback](arkts-arkui-onwillscrollcallback-t.md) | Called before scroll to allow developer to control real offset the Scrollable can scroll. |
| [OnWillStopDraggingCallback](arkts-arkui-onwillstopdraggingcallback-t.md) | On scroll callback using in scrollable onWillStopDragging. |
| [Optional](arkts-arkui-optional-t.md) | Defines the type that can be undefined. |
| [PixelMap](arkts-arkui-pixelmap-t.md) | Defines the PixelMap type object for ui component. |
| [PointerStyle](arkts-arkui-pointerstyle-t.md) | Import the PointerStyle type object for setCursor. |
| [PopupStateChangeCallback](arkts-arkui-popupstatechangecallback-t.md) | Popup state change callback |
| [PromptActionDialogController](arkts-arkui-promptactiondialogcontroller-t.md) | Import the DialogController type from promptAction. |
| [ReuseIdCallback](arkts-arkui-reuseidcallback-t.md) | ReuseId callback type. It is used to compute reuseId. |
| [RouterPageInfo](arkts-arkui-routerpageinfo-t.md) | The router page information. |
| [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) | Defines the callback type used in shouldBuiltInRecognizerParallelWith. |
| [ShouldRecognizerParallelWithCallback](arkts-arkui-shouldrecognizerparallelwithcallback-t.md) | Defines the callback type used in shouldRecognizerParallelWith. |
| [SingleLengthDetent](arkts-arkui-singlelengthdetent-t.md) | Defines the detent array of a single length. |
| [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) | Defines the callback type used in onSizeChange. |
| [SpringLoadingContext](arkts-arkui-springloadingcontext-t.md) | The type for SpringLoadingContext, see the detailed description in dragController. |
| [Summary](arkts-arkui-summary-t.md) | Import the Summary type object for ui component. |
| [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md) | SystemUiMaterial |
| [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) | Defines the TipsMessageType property with ResourceStr and StyledString. |
| [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) | Defines the callback type used in onTouchTestDone.When the user touch down, the system performs hit test process to collect all gesture recognizers based on the press location, when the collection is completed, and before gesture begin to be recognizing,the callback is triggered, you can get all recognizer's information from this callback. |
| [TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md) | Defines the finish callback type used in transition. |
| [TripleLengthDetents](arkts-arkui-triplelengthdetents-t.md) | Defines the detent array of a three-length. |
| [UIContext](arkts-arkui-uicontext-t.md) | UIContext. |
| [UnifiedData](arkts-arkui-unifieddata-t.md) | Import the UnifiedData type object for ui component. |
| [UniformDataType](arkts-arkui-uniformdatatype-t.md) | Import the UniformDataType type object for ui component. |
| [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | Defines the callback type used in VisibleAreaChange events. |
| [VisualEffect](arkts-arkui-visualeffect-t.md) | VisualEffect |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [Blender](arkts-arkui-blender-t-sys.md) | Blender |
<!--DelEnd-->

