# common

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
| [$$](arkts-arkui-common-$$-f.md#$$) | Convert to a bindable property. |
| [$r](arkts-arkui-common-$r-f.md#$r) | global \\$r function |
| [$rawfile](arkts-arkui-common-$rawfile-f.md#$rawfile) | global \\$rawfile function |
| [animateToImmediately](arkts-arkui-common-animatetoimmediately-f.md#animatetoimmediately) | Define animation functions for immediate distribution.This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use{@link ohos.arkui.UIContext.UIContext#animateToImmediately} to explicitly specify the UI context. |
| [applyStyles](arkts-arkui-common-applystyles-f.md#applystyles) | Apply style function on this CommonMethod. |
| [makeBindable](arkts-arkui-common-makebindable-f.md#makebindable) | Create a bindable property instance. |

### Classes

| Name | Description |
| --- | --- |
| [ChildrenMainSize](arkts-arkui-common-childrenmainsize-c.md) | Indicates children main size. |
| [ContentTransitionEffect](arkts-arkui-common-contenttransitioneffect-c.md) | Defines the content transition effect. |
| [DrawModifier](arkts-arkui-common-drawmodifier-c.md) | Defined the draw modifier of node. Provides draw callbacks for the associated Node.Each DrawModifier instance can be set for only one component. Repeated setting is not allowed. |
| [LayoutPolicy](arkts-arkui-common-layoutpolicy-c.md) | Defines the policy of Layout |
| [ProgressMask](arkts-arkui-common-progressmask-c.md) | Implements a ProgressMask object to set the progress, maximum value, and color of the mask. |
| [RawInputEventWrapper](arkts-arkui-common-rawinputeventwrapper-c.md) | Defines the raw input event wrapper. |
| [ScrollResult](arkts-arkui-common-scrollresult-c.md) | The actual offset by which the scrollable scrolls. |
| [TextContentControllerBase](arkts-arkui-common-textcontentcontrollerbase-c.md) | TextContentControllerBase |
| [TouchResult](arkts-arkui-common-touchresult-c.md) | Defines TouchResult class. |
| [TouchTestInfo](arkts-arkui-common-touchtestinfo-c.md) | Defines TouchTestInfo class. |
| [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) | 定义TransitionEffect类指定转场效果。 |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [TextContentControllerBase](arkts-arkui-common-textcontentcontrollerbase-c-sys.md) | TextContentControllerBase |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AccessibilityHoverEvent](arkts-arkui-common-accessibilityhoverevent-i.md) | The accessibility hover action triggers this method invocation. |
| [AlignRuleOption](arkts-arkui-common-alignruleoption-i.md) | Defines the align rule options of relative container. |
| [AnimatableArithmetic](arkts-arkui-common-animatablearithmetic-i.md) | 该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic\&lt;T\&gt;接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic\&lt;T\&gt;接口的类型。 |
| [AnimateParam](arkts-arkui-common-animateparam-i.md) | 动画效果相关参数。 |
| [AreaChangeOptions](arkts-arkui-common-areachangeoptions-i.md) | Defines the options about AreaChangeEvent. |
| [AsymmetricTransitionOption](arkts-arkui-common-asymmetrictransitionoption-i.md) | Defines the option of asymmetric transition. |
| [AttributeModifier](arkts-arkui-common-attributemodifier-i.md) | Defines the attribute modifier. |
| [AxisEvent](arkts-arkui-common-axisevent-i.md) | The axis event triggers this method invocation. |
| [BackgroundBlurStyleOptions](arkts-arkui-common-backgroundblurstyleoptions-i.md) | 继承自[BlurStyleOptions](../arkts-components/arkts-arkui-blurstyleoptions-i.md/arkts-arkui-blurstyleoptions-i.md)。 |
| [BackgroundBrightnessOptions](arkts-arkui-common-backgroundbrightnessoptions-i.md) | 背景亮度选项。 |
| [BackgroundEffectOptions](arkts-arkui-common-backgroundeffectoptions-i.md) | 背景效果参数。 |
| [BackgroundImageOptions](arkts-arkui-common-backgroundimageoptions-i.md) | Define the options for background image. |
| [BackgroundOptions](arkts-arkui-common-backgroundoptions-i.md) | Defines background options. |
| [BaseEvent](arkts-arkui-common-baseevent-i.md) | Defines the base event. |
| [BindOptions](arkts-arkui-common-bindoptions-i.md) | 半模态、全模态的公共配置接口。 |
| [Bindable](arkts-arkui-common-bindable-i.md) | Defines a bindable property |
| [BlurOptions](arkts-arkui-common-bluroptions-i.md) | Defines the options of blur |
| [BlurStyleOptions](arkts-arkui-common-blurstyleoptions-i.md) | Defines the options of blurStyle |
| [BorderImageOption](arkts-arkui-common-borderimageoption-i.md) | Border image option |
| [CaretOffset](arkts-arkui-common-caretoffset-i.md) | CaretOffset info. |
| [ClickEffect](arkts-arkui-common-clickeffect-i.md) | 定义点击效果。 |
| [ClickEvent](arkts-arkui-common-clickevent-i.md) | The tap action triggers this method invocation. |
| [CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md) | Defines the common configuration. |
| [CommonMethod](arkts-arkui-common-commonmethod-i.md) | CommonMethod |
| [Configuration](arkts-arkui-common-configuration-i.md) | Defines the data type of the interface restriction. |
| [ContentCoverOptions](arkts-arkui-common-contentcoveroptions-i.md) | 继承自[BindOptions](../arkts-components/arkts-arkui-bindoptions-i.md/arkts-arkui-bindoptions-i.md)。  全屏模态页面内容选项。 |
| [ContentModifier](arkts-arkui-common-contentmodifier-i.md) | Defines the content modifier. |
| [ContextMenuAnimationOptions](arkts-arkui-common-contextmenuanimationoptions-i.md) | Defines the ContextMenu's preview animator options. |
| [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | Defines the context menu options. |
| [CrownEvent](arkts-arkui-common-crownevent-i.md) | CrownEvent object description |
| [CustomPopupOptions](arkts-arkui-common-custompopupoptions-i.md) | Defines the custom popup options. |
| [DateRange](arkts-arkui-common-daterange-i.md) | Defines a range of dates. |
| [DismissContentCoverAction](arkts-arkui-common-dismisscontentcoveraction-i.md) | Component content cover dismiss |
| [DismissPopupAction](arkts-arkui-common-dismisspopupaction-i.md) | Component popup dismiss |
| [DismissSheetAction](arkts-arkui-common-dismisssheetaction-i.md) | 控制半模态的关闭。 |
| [DividerStyle](arkts-arkui-common-dividerstyle-i.md) | Provides an interface for the style of an divider including stroke width, color, start margin and end margin |
| [DragEvent](arkts-arkui-common-dragevent-i.md) | DragEvent object description |
| [DragInteractionOptions](arkts-arkui-common-draginteractionoptions-i.md) | Defines the drag options. |
| [DragItemInfo](arkts-arkui-common-dragiteminfo-i.md) | DragItemInfo object description |
| [DragPreviewOptions](arkts-arkui-common-dragpreviewoptions-i.md) | Defines the preview options. |
| [DropOptions](arkts-arkui-common-dropoptions-i.md) | Defines the options for the drop handling. |
| [DynamicNode](arkts-arkui-common-dynamicnode-i.md) | Define DynamicNode. |
| [EdgeEffectOptions](arkts-arkui-common-edgeeffectoptions-i.md) | Define EdgeEffect Options. |
| [EditModeOptions](arkts-arkui-common-editmodeoptions-i.md) | Define edit mode options. |
| [EventTarget](arkts-arkui-common-eventtarget-i.md) | Defines the event target. |
| [ExpectedFrameRateRange](arkts-arkui-common-expectedframeraterange-i.md) | 设置动画期望的帧率。 |
| [FadingEdgeOptions](arkts-arkui-common-fadingedgeoptions-i.md) | Defines the fadingEdge options. |
| [FocusAxisEvent](arkts-arkui-common-focusaxisevent-i.md) | Focus axis event object description. |
| [FocusMovement](arkts-arkui-common-focusmovement-i.md) | Defines the next focus item. |
| [ForegroundBlurStyleOptions](arkts-arkui-common-foregroundblurstyleoptions-i.md) | Defines the options of ForegroundBlurStyle |
| [ForegroundEffectOptions](arkts-arkui-common-foregroundeffectoptions-i.md) | Defines the options of ForegroundEffect |
| [GeometryInfo](arkts-arkui-common-geometryinfo-i.md) | Sub component layout info. |
| [GeometryTransitionOptions](arkts-arkui-common-geometrytransitionoptions-i.md) | Defines the options of geometry transition. |
| [GestureModifier](arkts-arkui-common-gesturemodifier-i.md) | Defines the gesture modifier. |
| [HistoricalPoint](arkts-arkui-common-historicalpoint-i.md) | TouchObject getHistoricalPoints Function Parameters |
| [HorizontalAlignParam](arkts-arkui-common-horizontalalignparam-i.md) | Defines the horizontal align rule options of relative container. |
| [HoverEvent](arkts-arkui-common-hoverevent-i.md) | The hover action triggers this method invocation. |
| [InputCounterOptions](arkts-arkui-common-inputcounteroptions-i.md) | Define the ratio of characters entered by the the percentage of InputCounterOptions. |
| [InputEventInterceptResult](arkts-arkui-common-inputeventinterceptresult-i.md) | Defines the input event intercept result. |
| [InputEventMonitor](arkts-arkui-common-inputeventmonitor-i.md) | Defines the input event monitor identifier.  Important Notes:  - This object is created and returned by the system as a unique identifier for the listener.  - The object is an empty object with no accessible members.  - Developers cannot actively construct this object, it can only be obtained through the registration interface.  - Used for subsequent unregistration to verify identity. |
| [InvertOptions](arkts-arkui-common-invertoptions-i.md) | Define the options of invert |
| [ItemDragEventHandler](arkts-arkui-common-itemdrageventhandler-i.md) | Define item drag event handler. |
| [ItemDragInfo](arkts-arkui-common-itemdraginfo-i.md) | ItemDragInfo object description |
| [KeyEvent](arkts-arkui-common-keyevent-i.md) | KeyEvent object description: |
| [KeyframeAnimateParam](arkts-arkui-common-keyframeanimateparam-i.md) | 动画选项设置。 |
| [KeyframeState](arkts-arkui-common-keyframestate-i.md) | 设置关键帧选项。 |
| [Layoutable](arkts-arkui-common-layoutable-i.md) | Provides the child component layout information. |
| [LinearGradientBlurOptions](arkts-arkui-common-lineargradientbluroptions-i.md) | Linear Gradient Blur Interface |
| [LinearGradientOptions](arkts-arkui-common-lineargradientoptions-i.md) | Defines the options of linear gradient. |
| [LocalizedAlignRuleOptions](arkts-arkui-common-localizedalignruleoptions-i.md) | Defines the Localized align rule options of relative container. |
| [LocalizedHorizontalAlignParam](arkts-arkui-common-localizedhorizontalalignparam-i.md) | Defines the localized horizontal align param of relative container. |
| [LocalizedVerticalAlignParam](arkts-arkui-common-localizedverticalalignparam-i.md) | Defines the localized vertical align param of relative container. |
| [Measurable](arkts-arkui-common-measurable-i.md) | Sub component info passed from framework when measure happens. |
| [MeasureResult](arkts-arkui-common-measureresult-i.md) | Provides the measurement result of the component. |
| [MenuElement](arkts-arkui-common-menuelement-i.md) | Defines the menu element. |
| [MenuGridStyleOptions](arkts-arkui-common-menugridstyleoptions-i.md) | Defines grid style of menu. |
| [MenuMaskType](arkts-arkui-common-menumasktype-i.md) | Menu mask type |
| [MenuOptions](arkts-arkui-common-menuoptions-i.md) | Defines the menu options. |
| [MotionBlurAnchor](arkts-arkui-common-motionbluranchor-i.md) | Define motion blur anchor coordinates. |
| [MotionBlurOptions](arkts-arkui-common-motionbluroptions-i.md) | Define motion blur options. |
| [MotionPathOptions](arkts-arkui-common-motionpathoptions-i.md) | 设置组件的运动路径。 |
| [MouseEvent](arkts-arkui-common-mouseevent-i.md) | The mouse click action triggers this method invocation. |
| [MouseHistoricalPoint](arkts-arkui-common-mousehistoricalpoint-i.md) | Defines the historical point information for mouse event. |
| [MultiShadowOptions](arkts-arkui-common-multishadowoptions-i.md) | Defines the options of Shadow. |
| [NestedScrollOptions](arkts-arkui-common-nestedscrolloptions-i.md) | Define nested scroll options |
| [OverlayOffset](arkts-arkui-common-overlayoffset-i.md) | Defines the OverlayOffset. |
| [OverlayOptions](arkts-arkui-common-overlayoptions-i.md) | Defines the OverlayOptions interface.  &lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;When both align and offset are set, the effects are combined.The overlay is first aligned relative to the component and then offset from its current upper left corner. |
| [PickerDialogButtonStyle](arkts-arkui-common-pickerdialogbuttonstyle-i.md) | Provide an interface for the button style of picker |
| [PickerTextStyle](arkts-arkui-common-pickertextstyle-i.md) | Provide an interface for the text style of picker |
| [PixelRoundPolicy](arkts-arkui-common-pixelroundpolicy-i.md) | Defines the direction of pixel rounding at the component level. |
| [PixelStretchEffectOptions](arkts-arkui-common-pixelstretcheffectoptions-i.md) | Set the edge blur effect distance of the corresponding defense line of the component When the component expand out, no re-layout is triggered |
| [PopupBorderLinearGradient](arkts-arkui-common-popupborderlineargradient-i.md) | Popup border LinearGradient |
| [PopupButton](arkts-arkui-common-popupbutton-i.md) | Defines the popup button. |
| [PopupCommonOptions](arkts-arkui-common-popupcommonoptions-i.md) | Popup common options |
| [PopupMaskType](arkts-arkui-common-popupmasktype-i.md) | Popup mask type |
| [PopupMessageOptions](arkts-arkui-common-popupmessageoptions-i.md) | Defines the options of popup message. |
| [PopupOptions](arkts-arkui-common-popupoptions-i.md) | Defines the popup options. |
| [PopupStateChangeParam](arkts-arkui-common-popupstatechangeparam-i.md) | Popup state change param |
| [PreviewConfiguration](arkts-arkui-common-previewconfiguration-i.md) | Defines the drag preview configuration. |
| [RadialGradientOptions](arkts-arkui-common-radialgradientoptions-i.md) | Defines the options of radial gradient. |
| [RectResult](arkts-arkui-common-rectresult-i.md) | Describe the position, width, and height of a component. |
| [Rectangle](arkts-arkui-common-rectangle-i.md) | The data type used to describe a rectangular area. |
| [ResponseRegion](arkts-arkui-common-responseregion-i.md) | Defines the response region interface. |
| [ReuseOptions](arkts-arkui-common-reuseoptions-i.md) | Defining the reusable configuration parameters. |
| [RotateAngleOptions](arkts-arkui-common-rotateangleoptions-i.md) | 指定各轴旋转角的旋转参数选项。 |
| [RotateOptions](arkts-arkui-common-rotateoptions-i.md) | 组件旋转参数。 |
| [ScaleOptions](arkts-arkui-common-scaleoptions-i.md) |  |
| [SelectionOptions](arkts-arkui-common-selectionoptions-i.md) | Defines the selection options. |
| [ShadowOptions](arkts-arkui-common-shadowoptions-i.md) | Define the options of shadow |
| [SheetDismiss](arkts-arkui-common-sheetdismiss-i.md) | 控制半模态的关闭。 |
| [SheetOptions](arkts-arkui-common-sheetoptions-i.md) | 继承自[BindOptions](../arkts-components/arkts-arkui-bindoptions-i.md/arkts-arkui-bindoptions-i.md)。  半模态页面内容选项。 |
| [SheetTitleOptions](arkts-arkui-common-sheettitleoptions-i.md) | 半模态面板的标题。 |
| [SizeResult](arkts-arkui-common-sizeresult-i.md) | Provides the component size information. |
| [SmartGestureShortcutOptions](arkts-arkui-common-smartgestureshortcutoptions-i.md) | Options for configuring smart gesture shortcuts. |
| [SpringBackAction](arkts-arkui-common-springbackaction-i.md) | 控制半模态关闭前的回弹。 |
| [StateStyles](arkts-arkui-common-statestyles-i.md) | Component State Styles. |
| [SweepGradientOptions](arkts-arkui-common-sweepgradientoptions-i.md) | Defines the options of sweep gradient. |
| [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 系统自适应调节参数，系统会默认开启根据芯片算力进行自适应效果调节的能力。 |
| [TerminationInfo](arkts-arkui-common-terminationinfo-i.md) | Indicates the information when the provider of the embedded UI is terminated. |
| [TextContentControllerOptions](arkts-arkui-common-textcontentcontrolleroptions-i.md) | Defines the span options of TextContentController. |
| [TextDecorationOptions](arkts-arkui-common-textdecorationoptions-i.md) | Defines the options of decoration. |
| [TipsOptions](arkts-arkui-common-tipsoptions-i.md) | Defines the Tips options. |
| [TouchEvent](arkts-arkui-common-touchevent-i.md) | Touch Action Function Parameters |
| [TouchObject](arkts-arkui-common-touchobject-i.md) | Type of the touch event. |
| [TranslateOptions](arkts-arkui-common-translateoptions-i.md) | Defines the options of translate. |
| [UICommonEvent](arkts-arkui-common-uicommonevent-i.md) | Defines a UICommonEvent which is used to set different common event to target component. |
| [UIGestureEvent](arkts-arkui-common-uigestureevent-i.md) | Defines a UIGestureEvent which is used to set different gestures to target component. |
| [UIScrollableCommonEvent](arkts-arkui-common-uiscrollablecommonevent-i.md) | Defines a UIScrollableCommonEvent which is used to set event to target component. |
| [VerticalAlignParam](arkts-arkui-common-verticalalignparam-i.md) | Defines the align rule options of relative container. |
| [VisibleAreaEventOptions](arkts-arkui-common-visibleareaeventoptions-i.md) | Defines the options about VisibleAreaEvent. |
| [sharedTransitionOptions](arkts-arkui-common-sharedtransitionoptions-i.md) | 共享元素转场动画参数。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [CommonMethod](arkts-arkui-common-commonmethod-i-sys.md) | CommonMethod |
| [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i-sys.md) | Defines the context menu options. |
| [DepthColorRGB](arkts-arkui-common-depthcolorrgb-i-sys.md) | RGB color in depth space. |
| [DepthVector3](arkts-arkui-common-depthvector3-i-sys.md) | 3D vector in depth space. |
| [DepthVector4](arkts-arkui-common-depthvector4-i-sys.md) | 4D vector in depth space. |
| [DragEvent](arkts-arkui-common-dragevent-i-sys.md) | DragEvent object description |
| [EdgeLightParams](arkts-arkui-common-edgelightparams-i-sys.md) | Defines the parameters of the edge light effect. |
| [GeometryTransitionOptions](arkts-arkui-common-geometrytransitionoptions-i-sys.md) | Defines the options of geometry transition. |
| [GravityCenterOptions](arkts-arkui-common-gravitycenteroptions-i-sys.md) | Defines the parameters of the center of gravity. |
| [LightSource](arkts-arkui-common-lightsource-i-sys.md) | 一个组件支持添加1个光源。 |
| [PixelMapMock](arkts-arkui-common-pixelmapmock-i-sys.md) | pixelmap object with release function. |
| [PointLightStyle](arkts-arkui-common-pointlightstyle-i-sys.md) | 通过设置光源和被照亮的类型实现点光源照亮周围组件的UI效果。 |
| [SheetOptions](arkts-arkui-common-sheetoptions-i-sys.md) | 继承自[BindOptions](../arkts-components/arkts-arkui-bindoptions-i.md/arkts-arkui-bindoptions-i.md)。  半模态页面内容选项。 |
| [SpatialEffectParams](arkts-arkui-common-spatialeffectparams-i-sys.md) | Spatial effect params. |
| [SpatialPosition](arkts-arkui-common-spatialposition-i-sys.md) | Spatial corner positions in 3D space. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AccessibilityAction](arkts-arkui-common-accessibilityaction-e.md) | Enum for accessibility action type |
| [AccessibilityActionInterceptResult](arkts-arkui-common-accessibilityactioninterceptresult-e.md) | Enum for the result of accessibility action intercept function |
| [AccessibilityRoleType](arkts-arkui-common-accessibilityroletype-e.md) | Enum for accessibility component type |
| [AccessibilitySamePageMode](arkts-arkui-common-accessibilitysamepagemode-e.md) | Defines the same page mode |
| [AdaptiveColor](arkts-arkui-common-adaptivecolor-e.md) | Defines adaptive color |
| [AnchoredColorMode](arkts-arkui-common-anchoredcolormode-e.md) | enum color mode of pointing popup |
| [AvailableLayoutArea](arkts-arkui-common-availablelayoutarea-e.md) | Defines the available layout area. |
| [BlendApplyType](arkts-arkui-common-blendapplytype-e.md) | Enum for BlendApplyType.Indicate how to apply specified blend mode to the view's content. |
| [BlendMode](arkts-arkui-common-blendmode-e.md) | Enum for BlendMode.Blend modes for compositing current component with overlapping content. Use overlapping content as dst, current component as src. |
| [BlurStyle](arkts-arkui-common-blurstyle-e.md) | 模糊样式类型。 |
| [BlurStyleActivePolicy](arkts-arkui-common-blurstyleactivepolicy-e.md) | 定义背景模糊激活策略。 |
| [ChainStyle](arkts-arkui-common-chainstyle-e.md) | Enumerates the chain styles in relative container. |
| [ContentClipMode](arkts-arkui-common-contentclipmode-e.md) | Enum of scrollable containers' content clip mode. |
| [DismissReason](arkts-arkui-common-dismissreason-e.md) | 关闭原因类型。 |
| [DragBehavior](arkts-arkui-common-dragbehavior-e.md) | Enum for Drag Behavior.  &lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;DragBehavior serves to inform you about the intended method of data handling,whether it's a copy or a move, but it does not actually dictate the real processing of the data. |
| [DragPreviewMode](arkts-arkui-common-dragpreviewmode-e.md) | Defines the drag preview mode. |
| [DragResult](arkts-arkui-common-dragresult-e.md) | Enum for Drag Result. |
| [DraggingSizeChangeEffect](arkts-arkui-common-draggingsizechangeeffect-e.md) | Define drag start animation effect from drag preview to the handle drag image |
| [EffectEdge](arkts-arkui-common-effectedge-e.md) | Enumerates the effective edge of the edge effect. |
| [EffectType](arkts-arkui-common-effecttype-e.md) | Enum of using the effects template mode. |
| [FinishCallbackType](arkts-arkui-common-finishcallbacktype-e.md) | 动画中定义onFinish回调的类型。 |
| [HapticFeedbackMode](arkts-arkui-common-hapticfeedbackmode-e.md) | Defines the menu haptic feedback mode. |
| [HoverModeAreaType](arkts-arkui-common-hovermodeareatype-e.md) | 悬停态显示区域类型。 |
| [KeyboardAvoidMode](arkts-arkui-common-keyboardavoidmode-e.md) | enum keyboard avoid mode |
| [LayoutSafeAreaEdge](arkts-arkui-common-layoutsafeareaedge-e.md) | Define the edges for expanding the safe area in layout. |
| [LayoutSafeAreaType](arkts-arkui-common-layoutsafeareatype-e.md) | Describe the types for expanding the safe area in layout. |
| [MenuGridPosition](arkts-arkui-common-menugridposition-e.md) | Defines menu grid position. |
| [MenuKeyboardAvoidMode](arkts-arkui-common-menukeyboardavoidmode-e.md) | Define the mode of menu how to avoid keyboard. |
| [MenuPolicy](arkts-arkui-common-menupolicy-e.md) | Define the menu pop-up policy |
| [MenuPreviewMode](arkts-arkui-common-menupreviewmode-e.md) | Defines the menu preview mode. |
| [ModalMode](arkts-arkui-common-modalmode-e.md) | Define the modal mode of menu. |
| [ModalTransition](arkts-arkui-common-modaltransition-e.md) | 全屏模态转场方式枚举类型，用于设置全屏模态转场类型。 |
| [OutlineStyle](arkts-arkui-common-outlinestyle-e.md) | Outline Style |
| [PreDragStatus](arkts-arkui-common-predragstatus-e.md) | Defines the drag status before drag action. |
| [PreviewScaleMode](arkts-arkui-common-previewscalemode-e.md) | Defines the scaling mode for custom preview of contextMenu. |
| [RepeatMode](arkts-arkui-common-repeatmode-e.md) | Defines the Border Image Repeat Mode. |
| [SafeAreaEdge](arkts-arkui-common-safeareaedge-e.md) | Enumerates the safe area edges. |
| [SafeAreaType](arkts-arkui-common-safeareatype-e.md) | The types of expanded safe areas. |
| [ScrollSizeMode](arkts-arkui-common-scrollsizemode-e.md) | 半模态面板上下滑动时的内容更新方式。 |
| [ShadowStyle](arkts-arkui-common-shadowstyle-e.md) | enum Shadow style |
| [ShadowType](arkts-arkui-common-shadowtype-e.md) | Define the type of shadow |
| [SheetKeyboardAvoidMode](arkts-arkui-common-sheetkeyboardavoidmode-e.md) | 半模态激活输入法时对软键盘的避让方式。 |
| [SheetMode](arkts-arkui-common-sheetmode-e.md) | 半模态的显示层级模式。 |
| [SheetSize](arkts-arkui-common-sheetsize-e.md) | 指定半模态的高度。 |
| [SheetType](arkts-arkui-common-sheettype-e.md) | 半模态弹窗的样式。 |
| [SourceTool](arkts-arkui-common-sourcetool-e.md) | Defines the event tool type. |
| [SourceType](arkts-arkui-common-sourcetype-e.md) | Defines the event source type. |
| [ThemeColorMode](arkts-arkui-common-themecolormode-e.md) | enum color mode |
| [TouchTestStrategy](arkts-arkui-common-touchteststrategy-e.md) | Defines the touch test strategy object. |
| [TransitionEdge](arkts-arkui-common-transitionedge-e.md) | 转场边缘类型。 |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [BlendApplyType](arkts-arkui-common-blendapplytype-e-sys.md) | Enum for BlendApplyType.Indicate how to apply specified blend mode to the view's content. |
| [DistortionMode](arkts-arkui-common-distortionmode-e-sys.md) | Enum for distortion animation mode. |
| [DragAnimationType](arkts-arkui-common-draganimationtype-e-sys.md) | Enum for Drag Animation Type. |
| [EdgeLightMode](arkts-arkui-common-edgelightmode-e-sys.md) | 边缘光效动画模式枚举。 |
| [TransitionHierarchyStrategy](arkts-arkui-common-transitionhierarchystrategy-e-sys.md) | 共享元素动画过程中in/out组件层级位置移动策略枚举。  \| 名称 \| 值 \| 说明 \|  \| ------ \| - \| ---- \|  \| NONE \| 0 \| 无层级提拉，in/out组件保持原来的层级位置，受父组件scale、position影响。 \|  \| ADAPTIVE \| 1 \| 有层级提拉，in/out组件中相对低层级的组件被提拉至组件树上in/out组件相对高层级的位置上。  此模式还会导致被提拉的组件与父组件解绑，不受父组件scale、position影响。  例如in组件层级高于out组件，开启层级提拉后会在动画过程中将out组件从自己的父组件处解耦，并提拉至in组件的层级位置处，in组件层级位置不变。\| |
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
| [DoubleLengthDetents](arkts-arkui-doublelengthdetents-t.md) | 定义了两个高度的挡位。 |
| [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | The type for DragSpringLoadingConfiguration, see the detailed description in dragController. |
| [DrawContext](arkts-arkui-drawcontext-t.md) | DrawContext. |
| [Filter](arkts-arkui-filter-t.md) | 导入Filter类型对象。 |
| [FractionStop](arkts-arkui-fractionstop-t.md) | Defines the segment of blur.The first element in the tuple means fraction.The range of this value is [0,1]. A value of 1 means opaque and 0 means completely transparent.The second element means the stop position.The range of this value is [0,1]. A value of 1 means region ending position and 0 means region starting position. |
| [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | Defines the callback type used in onGestureCollectIntercept. |
| [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | Defines the callback type used in onGestureRecognizerJudgeBegin. |
| [HoverCallback](arkts-arkui-hovercallback-t.md) | Defines the callback type used in hover events.The value of isHover indicates whether the mouse is hovering over the component.The value of event contains information about HoverEvent. |
| [ICurve](arkts-arkui-icurve-t.md) | 曲线对象。 |
| [InputEventListener](arkts-arkui-inputeventlistener-t.md) | Defines the input event listener callback function type.  Performance Warning: Do not perform time-consuming operations in the callback, otherwise it may cause the application to freeze.  The listener executes synchronously in the UI thread and will directly block the event processing flow.It is recommended to only perform simple judgments and calculations, avoiding:  - Synchronous I/O operations  - Complex data processing  - Network requests  - Massive log output |
| [Matrix4Transit](arkts-arkui-matrix4transit-t.md) | 矩阵对象接口。 |
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
| [SingleLengthDetent](arkts-arkui-singlelengthdetent-t.md) | 定义了单个高度的挡位。 |
| [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) | Defines the callback type used in onSizeChange. |
| [SpringLoadingContext](arkts-arkui-springloadingcontext-t.md) | The type for SpringLoadingContext, see the detailed description in dragController. |
| [Summary](arkts-arkui-summary-t.md) | Import the Summary type object for ui component. |
| [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md) | SystemUiMaterial |
| [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) | Defines the TipsMessageType property with ResourceStr and StyledString. |
| [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) | Defines the callback type used in onTouchTestDone.When the user touch down, the system performs hit test process to collect all gesture recognizers based on the press location, when the collection is completed, and before gesture begin to be recognizing,the callback is triggered, you can get all recognizer's information from this callback. |
| [TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md) | 组件转场动画的结束回调类型。 |
| [TripleLengthDetents](arkts-arkui-triplelengthdetents-t.md) | 定义了三个高度的挡位。 |
| [UIContext](arkts-arkui-uicontext-t.md) | UIContext. |
| [UnifiedData](arkts-arkui-unifieddata-t.md) | Import the UnifiedData type object for ui component. |
| [UniformDataType](arkts-arkui-uniformdatatype-t.md) | Import the UniformDataType type object for ui component. |
| [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | Defines the callback type used in VisibleAreaChange events. |
| [VisualEffect](arkts-arkui-visualeffect-t.md) | 导入VisualEffect类型对象。 |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [Blender](arkts-arkui-blender-t-sys.md) | Blender |
<!--DelEnd-->

