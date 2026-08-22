# common

Defines the namespace of focus controller.

## 汇总

### 命名空间

| 名称 | 说明 |
| --- | --- |
| [cursorControl](arkts-cursorcontrol-n.md) | CursorControl |
| [focusControl](arkts-focuscontrol-n.md) | Defines the namespace of focus controller. |

### 函数

| 名称 | 说明 |
| --- | --- |
| [$$](arkts-common--f.md#) | Convert to a bindable property. |
| [$r](arkts-common-r-f.md#r) | global \\$r function |
| [$rawfile](arkts-common-rawfile-f.md#rawfile) | global \\$rawfile function |
| [animateToImmediately](arkts-common-animatetoimmediately-f.md) | Define animation functions for immediate distribution. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use animateToImmediately to explicitly specify the UI context. |
| [applyStyles](arkts-common-applystyles-f.md) | Apply style function on this CommonMethod. |
| [makeBindable](arkts-common-makebindable-f.md) | Create a bindable property instance. |

### 类

| 名称 | 说明 |
| --- | --- |
| [ChildrenMainSize](arkts-common-childrenmainsize-c.md) | Indicates children main size. |
| [ContentTransitionEffect](arkts-common-contenttransitioneffect-c.md) | Defines the content transition effect. |
| [DrawModifier](arkts-common-drawmodifier-c.md) | Defined the draw modifier of node. Provides draw callbacks for the associated Node. Each DrawModifier instance can be set for only one component. Repeated setting is not allowed. |
| [LayoutPolicy](arkts-common-layoutpolicy-c.md) | Defines the policy of Layout |
| [ProgressMask](arkts-common-progressmask-c.md) | Implements a ProgressMask object to set the progress, maximum value, and color of the mask. |
| [RawInputEventWrapper](arkts-common-rawinputeventwrapper-c.md) | Defines the raw input event wrapper. |
| [ScrollResult](arkts-common-scrollresult-c.md) | The actual offset by which the scrollable scrolls. |
| [TextContentControllerBase](arkts-common-textcontentcontrollerbase-c.md) | TextContentControllerBase |
| [TouchResult](arkts-common-touchresult-c.md) | Defines TouchResult class. |
| [TouchTestInfo](arkts-common-touchtestinfo-c.md) | Defines TouchTestInfo class. |
| [TransitionEffect](arkts-common-transitioneffect-c.md) | 定义TransitionEffect类指定转场效果。 |

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [TextContentControllerBase](arkts-common-textcontentcontrollerbase-c-sys.md) | TextContentControllerBase |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [AccessibilityHoverEvent](arkts-common-accessibilityhoverevent-i.md) | The accessibility hover action triggers this method invocation. |
| [AlignRuleOption](arkts-common-alignruleoption-i.md) | Defines the align rule options of relative container. |
| [AnimatableArithmetic](arkts-common-animatablearithmetic-i.md) | 该接口定义非number数据类型的动画运算规则。对非number类型的数据（如数组、结构体、颜色等）做动画，需要实现AnimatableArithmetic\&lt;T\&gt;接口中加法、减法、乘法和判断相等函数，使得该数据能参与动画的插值运算 和识别该数据是否发生改变。即定义它们为实现了AnimatableArithmetic\&lt;T\&gt;接口的类型。 |
| [AnimateParam](arkts-common-animateparam-i.md) | 动画效果相关参数。 |
| [AreaChangeOptions](arkts-common-areachangeoptions-i.md) | Defines the options about AreaChangeEvent. |
| [AsymmetricTransitionOption](arkts-common-asymmetrictransitionoption-i.md) | Defines the option of asymmetric transition. |
| [AttributeModifier](arkts-common-attributemodifier-i.md) | Defines the attribute modifier. |
| [AxisEvent](arkts-common-axisevent-i.md) | The axis event triggers this method invocation. |
| [BackgroundBlurStyleOptions](arkts-common-backgroundblurstyleoptions-i.md) | 继承自[BlurStyleOptions](arkts-common-blurstyleoptions-i.md)。 |
| [BackgroundBrightnessOptions](arkts-common-backgroundbrightnessoptions-i.md) | 背景亮度选项。 |
| [BackgroundEffectOptions](arkts-common-backgroundeffectoptions-i.md) | 背景效果参数。 |
| [BackgroundImageOptions](arkts-common-backgroundimageoptions-i.md) | Define the options for background image. |
| [BackgroundOptions](arkts-common-backgroundoptions-i.md) | Defines background options. |
| [BaseEvent](arkts-common-baseevent-i.md) | Defines the base event. |
| [Bindable](arkts-common-bindable-i.md) | Defines a bindable property |
| [BindOptions](arkts-common-bindoptions-i.md) | 半模态、全模态的公共配置接口。 |
| [BlurOptions](arkts-common-bluroptions-i.md) | Defines the options of blur |
| [BlurStyleOptions](arkts-common-blurstyleoptions-i.md) | Defines the options of blurStyle |
| [BorderImageOption](arkts-common-borderimageoption-i.md) | Border image option |
| [CaretOffset](arkts-common-caretoffset-i.md) | CaretOffset info. |
| [ClickEffect](arkts-common-clickeffect-i.md) | 定义点击效果。 |
| [ClickEvent](arkts-common-clickevent-i.md) | The tap action triggers this method invocation. |
| [CommonConfiguration](arkts-common-commonconfiguration-i.md) | Defines the common configuration. |
| [CommonMethod](arkts-common-commonmethod-i.md) | CommonMethod |
| [CommonShapeMethod](arkts-common-commonshapemethod-i.md) | CommonShapeMethod |
| [Configuration](arkts-common-configuration-i.md) | Defines the data type of the interface restriction. |
| [ContentCoverOptions](arkts-common-contentcoveroptions-i.md) | 继承自[BindOptions](arkts-common-bindoptions-i.md)。 |
| [ContentModifier](arkts-common-contentmodifier-i.md) | Defines the content modifier. |
| [ContextMenuAnimationOptions](arkts-common-contextmenuanimationoptions-i.md) | Defines the ContextMenu's preview animator options. |
| [ContextMenuOptions](arkts-common-contextmenuoptions-i.md) | Defines the context menu options. |
| [CrownEvent](arkts-common-crownevent-i.md) | CrownEvent object description |
| [CustomPopupOptions](arkts-common-custompopupoptions-i.md) | Defines the custom popup options. |
| [DateRange](arkts-common-daterange-i.md) | Defines a range of dates. |
| [DismissContentCoverAction](arkts-common-dismisscontentcoveraction-i.md) | Component content cover dismiss |
| [DismissPopupAction](arkts-common-dismisspopupaction-i.md) | Component popup dismiss |
| [DismissSheetAction](arkts-common-dismisssheetaction-i.md) | 控制半模态的关闭。 |
| [DividerStyle](arkts-common-dividerstyle-i.md) | Provides an interface for the style of an divider including stroke width, color, start margin and end margin |
| [DragEvent](arkts-common-dragevent-i.md) | DragEvent object description |
| [DragInteractionOptions](arkts-common-draginteractionoptions-i.md) | Defines the drag options. |
| [DragItemInfo](arkts-common-dragiteminfo-i.md) | DragItemInfo object description |
| [DragPreviewOptions](arkts-common-dragpreviewoptions-i.md) | Defines the preview options. |
| [DropOptions](arkts-common-dropoptions-i.md) | Defines the options for the drop handling. |
| [DynamicNode](arkts-common-dynamicnode-i.md) | Define DynamicNode. |
| [EdgeEffectOptions](arkts-common-edgeeffectoptions-i.md) | Define EdgeEffect Options. |
| [EditModeOptions](arkts-common-editmodeoptions-i.md) | Define edit mode options. |
| [EventTarget](arkts-common-eventtarget-i.md) | Defines the event target. |
| [ExpectedFrameRateRange](arkts-common-expectedframeraterange-i.md) | 设置动画期望的帧率。 |
| [FadingEdgeOptions](arkts-common-fadingedgeoptions-i.md) | Defines the fadingEdge options. |
| [FocusAxisEvent](arkts-common-focusaxisevent-i.md) | Focus axis event object description. |
| [FocusMovement](arkts-common-focusmovement-i.md) | Defines the next focus item. |
| [ForegroundBlurStyleOptions](arkts-common-foregroundblurstyleoptions-i.md) | Defines the options of ForegroundBlurStyle |
| [ForegroundEffectOptions](arkts-common-foregroundeffectoptions-i.md) | Defines the options of ForegroundEffect |
| [GeometryInfo](arkts-common-geometryinfo-i.md) | Sub component layout info. |
| [GeometryTransitionOptions](arkts-common-geometrytransitionoptions-i.md) | Defines the options of geometry transition. |
| [GestureModifier](arkts-common-gesturemodifier-i.md) | Defines the gesture modifier. |
| [HistoricalPoint](arkts-common-historicalpoint-i.md) | TouchObject getHistoricalPoints Function Parameters |
| [HorizontalAlignParam](arkts-common-horizontalalignparam-i.md) | Defines the horizontal align rule options of relative container. |
| [HoverEvent](arkts-common-hoverevent-i.md) | The hover action triggers this method invocation. |
| [InputCounterOptions](arkts-common-inputcounteroptions-i.md) | Define the ratio of characters entered by the the percentage of InputCounterOptions. |
| [InputEventInterceptResult](arkts-common-inputeventinterceptresult-i.md) | Defines the input event intercept result. |
| [InputEventMonitor](arkts-common-inputeventmonitor-i.md) | Defines the input event monitor identifier. |
| [InvertOptions](arkts-common-invertoptions-i.md) | Define the options of invert |
| [ItemDragEventHandler](arkts-common-itemdrageventhandler-i.md) | Define item drag event handler. |
| [ItemDragInfo](arkts-common-itemdraginfo-i.md) | ItemDragInfo object description |
| [KeyEvent](arkts-common-keyevent-i.md) | KeyEvent object description: |
| [KeyframeAnimateParam](arkts-common-keyframeanimateparam-i.md) | 动画选项设置。 |
| [KeyframeState](arkts-common-keyframestate-i.md) | 设置关键帧选项。 |
| [Layoutable](arkts-common-layoutable-i.md) | Provides the child component layout information. |
| [LinearGradientBlurOptions](arkts-common-lineargradientbluroptions-i.md) | Linear Gradient Blur Interface |
| [LinearGradientOptions](arkts-common-lineargradientoptions-i.md) | Defines the options of linear gradient. |
| [LocalizedAlignRuleOptions](arkts-common-localizedalignruleoptions-i.md) | Defines the Localized align rule options of relative container. |
| [LocalizedHorizontalAlignParam](arkts-common-localizedhorizontalalignparam-i.md) | Defines the localized horizontal align param of relative container. |
| [LocalizedVerticalAlignParam](arkts-common-localizedverticalalignparam-i.md) | Defines the localized vertical align param of relative container. |
| [Measurable](arkts-common-measurable-i.md) | Sub component info passed from framework when measure happens. |
| [MeasureResult](arkts-common-measureresult-i.md) | Provides the measurement result of the component. |
| [MenuElement](arkts-common-menuelement-i.md) | Defines the menu element. |
| [MenuGridStyleOptions](arkts-common-menugridstyleoptions-i.md) | Defines grid style of menu. |
| [MenuMaskType](arkts-common-menumasktype-i.md) | Menu mask type |
| [MenuOptions](arkts-common-menuoptions-i.md) | Defines the menu options. |
| [MotionBlurAnchor](arkts-common-motionbluranchor-i.md) | Define motion blur anchor coordinates. |
| [MotionBlurOptions](arkts-common-motionbluroptions-i.md) | Define motion blur options. |
| [MotionPathOptions](arkts-common-motionpathoptions-i.md) | 设置组件的运动路径。 |
| [MouseEvent](arkts-common-mouseevent-i.md) | The mouse click action triggers this method invocation. |
| [MouseHistoricalPoint](arkts-common-mousehistoricalpoint-i.md) | Defines the historical point information for mouse event. |
| [MultiShadowOptions](arkts-common-multishadowoptions-i.md) | Defines the options of Shadow. |
| [NestedScrollOptions](arkts-common-nestedscrolloptions-i.md) | Define nested scroll options |
| [OverlayOffset](arkts-common-overlayoffset-i.md) | Defines the OverlayOffset. |
| [OverlayOptions](arkts-common-overlayoptions-i.md) | Defines the OverlayOptions interface. |
| [PickerDialogButtonStyle](arkts-common-pickerdialogbuttonstyle-i.md) | Provide an interface for the button style of picker |
| [PickerTextStyle](arkts-common-pickertextstyle-i.md) | Provide an interface for the text style of picker |
| [PixelRoundPolicy](arkts-common-pixelroundpolicy-i.md) | Defines the direction of pixel rounding at the component level. |
| [PixelStretchEffectOptions](arkts-common-pixelstretcheffectoptions-i.md) | Set the edge blur effect distance of the corresponding defense line of the component When the component expand out, no re-layout is triggered |
| [PopupBorderLinearGradient](arkts-common-popupborderlineargradient-i.md) | Popup border LinearGradient |
| [PopupButton](arkts-common-popupbutton-i.md) | Defines the popup button. |
| [PopupCommonOptions](arkts-common-popupcommonoptions-i.md) | Popup common options |
| [PopupMaskType](arkts-common-popupmasktype-i.md) | Popup mask type |
| [PopupMessageOptions](arkts-common-popupmessageoptions-i.md) | Defines the options of popup message. |
| [PopupOptions](arkts-common-popupoptions-i.md) | Defines the popup options. |
| [PopupStateChangeParam](arkts-common-popupstatechangeparam-i.md) | Popup state change param |
| [PreviewConfiguration](arkts-common-previewconfiguration-i.md) | Defines the drag preview configuration. |
| [RadialGradientOptions](arkts-common-radialgradientoptions-i.md) | Defines the options of radial gradient. |
| [Rectangle](arkts-common-rectangle-i.md) | The data type used to describe a rectangular area. |
| [RectResult](arkts-common-rectresult-i.md) | Describe the position, width, and height of a component. |
| [ResponseRegion](arkts-common-responseregion-i.md) | Defines the response region interface. |
| [ReuseOptions](arkts-common-reuseoptions-i.md) | Defining the reusable configuration parameters. |
| [RotateAngleOptions](arkts-common-rotateangleoptions-i.md) | 指定各轴旋转角的旋转参数选项。 |
| [RotateOptions](arkts-common-rotateoptions-i.md) | 组件旋转参数。 |
| [ScaleOptions](arkts-common-scaleoptions-i.md) |  |
| [ScrollableCommonMethod](arkts-common-scrollablecommonmethod-i.md) | CommonScrollableMethod |
| [SelectionOptions](arkts-common-selectionoptions-i.md) | Defines the selection options. |
| [ShadowOptions](arkts-common-shadowoptions-i.md) | Define the options of shadow |
| [sharedTransitionOptions](arkts-common-sharedtransitionoptions-i.md) | 共享元素转场动画参数。 |
| [SheetDismiss](arkts-common-sheetdismiss-i.md) | 控制半模态的关闭。 |
| [SheetOptions](arkts-common-sheetoptions-i.md) | 继承自[BindOptions](arkts-common-bindoptions-i.md)。 |
| [SheetTitleOptions](arkts-common-sheettitleoptions-i.md) | 半模态面板的标题。 |
| [SizeResult](arkts-common-sizeresult-i.md) | Provides the component size information. |
| [SmartGestureShortcutOptions](arkts-common-smartgestureshortcutoptions-i.md) | Options for configuring smart gesture shortcuts. |
| [SpringBackAction](arkts-common-springbackaction-i.md) | 控制半模态关闭前的回弹。 |
| [StateStyles](arkts-common-statestyles-i.md) | Component State Styles. |
| [SweepGradientOptions](arkts-common-sweepgradientoptions-i.md) | Defines the options of sweep gradient. |
| [SystemAdaptiveOptions](arkts-common-systemadaptiveoptions-i.md) | 系统自适应调节参数，系统会默认开启根据芯片算力进行自适应效果调节的能力。 |
| [TerminationInfo](arkts-common-terminationinfo-i.md) | Indicates the information when the provider of the embedded UI is terminated. |
| [TextContentControllerOptions](arkts-common-textcontentcontrolleroptions-i.md) | Defines the span options of TextContentController. |
| [TextDecorationOptions](arkts-common-textdecorationoptions-i.md) | Defines the options of decoration. |
| [TipsOptions](arkts-common-tipsoptions-i.md) | Defines the Tips options. |
| [TouchEvent](arkts-common-touchevent-i.md) | Touch Action Function Parameters |
| [TouchObject](arkts-common-touchobject-i.md) | Type of the touch event. |
| [TranslateOptions](arkts-common-translateoptions-i.md) | Defines the options of translate. |
| [UICommonEvent](arkts-common-uicommonevent-i.md) | Defines a UICommonEvent which is used to set different common event to target component. |
| [UIGestureEvent](arkts-common-uigestureevent-i.md) | Defines a UIGestureEvent which is used to set different gestures to target component. |
| [UIScrollableCommonEvent](arkts-common-uiscrollablecommonevent-i.md) | Defines a UIScrollableCommonEvent which is used to set event to target component. |
| [VerticalAlignParam](arkts-common-verticalalignparam-i.md) | Defines the align rule options of relative container. |
| [VisibleAreaEventOptions](arkts-common-visibleareaeventoptions-i.md) | Defines the options about VisibleAreaEvent. |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [ContextMenuOptions](arkts-common-contextmenuoptions-i-sys.md) | Defines the context menu options. |
| [DepthColorRGB](arkts-common-depthcolorrgb-i-sys.md) | RGB color in depth space. |
| [DepthVector3](arkts-common-depthvector3-i-sys.md) | 3D vector in depth space. |
| [DepthVector4](arkts-common-depthvector4-i-sys.md) | 4D vector in depth space. |
| [DragEvent](arkts-common-dragevent-i-sys.md) | DragEvent object description |
| [EdgeLightParams](arkts-common-edgelightparams-i-sys.md) | Defines the parameters of the edge light effect. |
| [GeometryTransitionOptions](arkts-common-geometrytransitionoptions-i-sys.md) | Defines the options of geometry transition. |
| [GravityCenterOptions](arkts-common-gravitycenteroptions-i-sys.md) | Defines the parameters of the center of gravity. |
| [LightSource](arkts-common-lightsource-i-sys.md) | 一个组件支持添加1个光源。 |
| [PixelMapMock](arkts-common-pixelmapmock-i-sys.md) | pixelmap object with release function. |
| [PointLightStyle](arkts-common-pointlightstyle-i-sys.md) | 通过设置光源和被照亮的类型实现点光源照亮周围组件的UI效果。 |
| [SheetOptions](arkts-common-sheetoptions-i-sys.md) | 继承自[BindOptions](arkts-common-bindoptions-i.md)。 |
| [SpatialEffectParams](arkts-common-spatialeffectparams-i-sys.md) | Spatial effect params. |
| [SpatialPosition](arkts-common-spatialposition-i-sys.md) | Spatial corner positions in 3D space. |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AccessibilityAction](arkts-common-accessibilityaction-e.md) | Enum for accessibility action type @enum { int } |
| [AccessibilityActionInterceptResult](arkts-common-accessibilityactioninterceptresult-e.md) | Enum for the result of accessibility action intercept function @enum { int } |
| [AccessibilityRoleType](arkts-common-accessibilityroletype-e.md) | Enum for accessibility component type @enum { int } |
| [AccessibilitySamePageMode](arkts-common-accessibilitysamepagemode-e.md) | Defines the same page mode @enum { int } |
| [AdaptiveColor](arkts-common-adaptivecolor-e.md) | Defines adaptive color |
| [AnchoredColorMode](arkts-common-anchoredcolormode-e.md) | enum color mode of pointing popup @enum { number } |
| [AvailableLayoutArea](arkts-common-availablelayoutarea-e.md) | Defines the available layout area. |
| [BlendApplyType](arkts-common-blendapplytype-e.md) | Enum for BlendApplyType. Indicate how to apply specified blend mode to the view's content. |
| [BlendMode](arkts-common-blendmode-e.md) | Enum for BlendMode. Blend modes for compositing current component with overlapping content. Use overlapping content as dst, current component as src. |
| [BlurStyle](arkts-common-blurstyle-e.md) | 模糊样式类型。 |
| [BlurStyleActivePolicy](arkts-common-blurstyleactivepolicy-e.md) | 定义背景模糊激活策略。 |
| [ChainStyle](arkts-common-chainstyle-e.md) | Enumerates the chain styles in relative container. |
| [ContentClipMode](arkts-common-contentclipmode-e.md) | Enum of scrollable containers' content clip mode. |
| [DismissReason](arkts-common-dismissreason-e.md) | 关闭原因类型。 |
| [DragBehavior](arkts-common-dragbehavior-e.md) | Enum for Drag Behavior. |
| [DraggingSizeChangeEffect](arkts-common-draggingsizechangeeffect-e.md) | Define drag start animation effect from drag preview to the handle drag image |
| [DragPreviewMode](arkts-common-dragpreviewmode-e.md) | Defines the drag preview mode. |
| [DragResult](arkts-common-dragresult-e.md) | Enum for Drag Result. |
| [EffectEdge](arkts-common-effectedge-e.md) | Enumerates the effective edge of the edge effect. |
| [EffectType](arkts-common-effecttype-e.md) | Enum of using the effects template mode. |
| [FinishCallbackType](arkts-common-finishcallbacktype-e.md) | 动画中定义onFinish回调的类型。 |
| [HapticFeedbackMode](arkts-common-hapticfeedbackmode-e.md) | Defines the menu haptic feedback mode. |
| [HoverModeAreaType](arkts-common-hovermodeareatype-e.md) | 悬停态显示区域类型。 |
| [KeyboardAvoidMode](arkts-common-keyboardavoidmode-e.md) | enum keyboard avoid mode |
| [LayoutSafeAreaEdge](arkts-common-layoutsafeareaedge-e.md) | Define the edges for expanding the safe area in layout. |
| [LayoutSafeAreaType](arkts-common-layoutsafeareatype-e.md) | Describe the types for expanding the safe area in layout. |
| [MenuGridPosition](arkts-common-menugridposition-e.md) | Defines menu grid position. |
| [MenuKeyboardAvoidMode](arkts-common-menukeyboardavoidmode-e.md) | Define the mode of menu how to avoid keyboard. |
| [MenuPolicy](arkts-common-menupolicy-e.md) | Define the menu pop-up policy |
| [MenuPreviewMode](arkts-common-menupreviewmode-e.md) | Defines the menu preview mode. |
| [ModalMode](arkts-common-modalmode-e.md) | Define the modal mode of menu. |
| [ModalTransition](arkts-common-modaltransition-e.md) | 全屏模态转场方式枚举类型，用于设置全屏模态转场类型。 |
| [OutlineStyle](arkts-common-outlinestyle-e.md) | Outline Style |
| [PreDragStatus](arkts-common-predragstatus-e.md) | Defines the drag status before drag action. |
| [PreviewScaleMode](arkts-common-previewscalemode-e.md) | Defines the scaling mode for custom preview of contextMenu. |
| [RepeatMode](arkts-common-repeatmode-e.md) | Defines the Border Image Repeat Mode. |
| [SafeAreaEdge](arkts-common-safeareaedge-e.md) | Enumerates the safe area edges. |
| [SafeAreaType](arkts-common-safeareatype-e.md) | The types of expanded safe areas. |
| [ScrollSizeMode](arkts-common-scrollsizemode-e.md) | 半模态面板上下滑动时的内容更新方式。 |
| [ShadowStyle](arkts-common-shadowstyle-e.md) | enum Shadow style |
| [ShadowType](arkts-common-shadowtype-e.md) | Define the type of shadow |
| [SheetKeyboardAvoidMode](arkts-common-sheetkeyboardavoidmode-e.md) | 半模态激活输入法时对软键盘的避让方式。 |
| [SheetMode](arkts-common-sheetmode-e.md) | 半模态的显示层级模式。 |
| [SheetSize](arkts-common-sheetsize-e.md) | 指定半模态的高度。 |
| [SheetType](arkts-common-sheettype-e.md) | 半模态弹窗的样式。 |
| [SourceTool](arkts-common-sourcetool-e.md) | Defines the event tool type. |
| [SourceType](arkts-common-sourcetype-e.md) | Defines the event source type. |
| [ThemeColorMode](arkts-common-themecolormode-e.md) | enum color mode |
| [TouchTestStrategy](arkts-common-touchteststrategy-e.md) | Defines the touch test strategy object. |
| [TransitionEdge](arkts-common-transitionedge-e.md) | 转场边缘类型。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BlendApplyType](arkts-common-blendapplytype-e-sys.md) | Enum for BlendApplyType. Indicate how to apply specified blend mode to the view's content. |
| [DistortionMode](arkts-common-distortionmode-e-sys.md) | Enum for distortion animation mode. |
| [DragAnimationType](arkts-common-draganimationtype-e-sys.md) | Enum for Drag Animation Type. |
| [EdgeLightMode](arkts-common-edgelightmode-e-sys.md) | 边缘光效动画模式枚举。 |
| [TransitionHierarchyStrategy](arkts-common-transitionhierarchystrategy-e-sys.md) | 共享元素动画过程中in/out组件层级位置移动策略枚举。 |
<!--DelEnd-->

### 类型

| 名称 | 说明 |
| --- | --- |
| [AccessibilityActionInterceptCallback](arkts-accessibilityactioninterceptcallback-t.md) | Defines the callback type used in accessibility action intercept. The value of action indicates the accessibility action type. |
| [AccessibilityCallback](arkts-accessibilitycallback-t.md) | Defines the callback type used in accessibility hover events. The value of isHover indicates whether the touch is hovering over the component. The value of event contains information about AccessibilityHoverEvent. |
| [AccessibilityFocusCallback](arkts-accessibilityfocuscallback-t.md) | Defines the callback type used in accessibility focus. The value of isFocus indicates whether the current component is focused |
| [AccessibilityTransparentCallback](arkts-accessibilitytransparentcallback-t.md) | Defines the callback type used in accessibility hover transparent event. |
| [AnimationNumberRange](arkts-animationnumberrange-t.md) | Defines the animator range of start and end property. |
| [AreaChangeCallback](arkts-areachangecallback-t.md) | Defines the options for the AreaChangeEvent. |
| [BindableResourceStr](arkts-bindableresourcestr-t.md) | Defines the Two-way binding type of ResourceStr. |
| [BindableResourceStrArray](arkts-bindableresourcestrarray-t.md) | Defines the Two-way binding type of ResourceStr[]. |
| [BorderRadiusType](arkts-borderradiustype-t.md) | Defines the type of border radius. |
| [Callback](arkts-callback-t.md) | Defines the callback |
| [CommonAttribute](arkts-commonattribute-t.md) | CommonAttribute for ide. |
| [Context](arkts-context-t.md) | Export Context. |
| [CustomProperty](arkts-customproperty-t.md) | Defines the value of the custom property.. |
| [CustomStyles](arkts-customstyles-t.md) | The custom styles function block. |
| [DataLoadParams](arkts-dataloadparams-t.md) | Import the DataLoadParams type object for ui component. |
| [DataSyncOptions](arkts-datasyncoptions-t.md) | Import the GetDataParams type object for ui component. |
| [DateTimeOptions](arkts-datetimeoptions-t.md) | Defines the format for displaying dates and times. |
| [DoubleLengthDetents](arkts-doublelengthdetents-t.md) | 定义了两个高度的挡位。 |
| [DragSpringLoadingConfiguration](arkts-dragspringloadingconfiguration-t.md) | The type for DragSpringLoadingConfiguration, see the detailed description in dragController. |
| [DrawContext](arkts-drawcontext-t.md) | DrawContext. |
| [Filter](arkts-filter-t.md) | 导入Filter类型对象。 |
| [FractionStop](arkts-fractionstop-t.md) | Defines the segment of blur. The first element in the tuple means fraction. The range of this value is [0,1]. A value of 1 means opaque and 0 means completely transparent. The second element means the stop position. The range of this value is [0,1]. A value of 1 means region ending position and 0 means region starting position. |
| [GestureCollectInterceptCallback](arkts-gesturecollectinterceptcallback-t.md) | Defines the callback type used in onGestureCollectIntercept. |
| [GestureRecognizerJudgeBeginCallback](arkts-gesturerecognizerjudgebegincallback-t.md) | Defines the callback type used in onGestureRecognizerJudgeBegin. |
| [HoverCallback](arkts-hovercallback-t.md) | Defines the callback type used in hover events. The value of isHover indicates whether the mouse is hovering over the component. The value of event contains information about HoverEvent. |
| [ICurve](arkts-icurve-t.md) | 曲线对象。 |
| [InputEventListener](arkts-inputeventlistener-t.md) | Defines the input event listener callback function type. |
| [Matrix4Transit](arkts-matrix4transit-t.md) | 矩阵对象接口。 |
| [ModifierKeyStateGetter](arkts-modifierkeystategetter-t.md) | The modifier key state query function block. |
| [NavDestinationInfo](arkts-navdestinationinfo-t.md) | The navigation destination information. |
| [NavigationInfo](arkts-navigationinfo-t.md) | The navigation information. |
| [OnDidStopDraggingCallback](arkts-ondidstopdraggingcallback-t.md) | On scroll callback using in scrollable onDidStopDragging. |
| [OnDragEventCallback](arkts-ondrageventcallback-t.md) | The event callback function for drag and drop common interfaces. |
| [OnGetPreviewBadgeCallback](arkts-ongetpreviewbadgecallback-t.md) | Defines the callback type used in onGetPreviewBadge of EditModeOptions. |
| [OnItemDragStartCallback](arkts-onitemdragstartcallback-t.md) | Defines the callback type used in onItemDragStart. |
| [OnMoveHandler](arkts-onmovehandler-t.md) | Defines the onMove callback. |
| [OnNeedSoftkeyboardCallback](arkts-onneedsoftkeyboardcallback-t.md) | Defines the callback type used in onNeedSoftkeyboard. Called when component is focused, the return value indicates whether keyboard is needed. |
| [OnScrollCallback](arkts-onscrollcallback-t.md) | On scroll callback using in scrollable onDidScroll. |
| [OnVisibleIndexesChangeCallback](arkts-onvisibleindexeschangecallback-t.md) | Defines the callback type used in OnVisibleIndexesChange. |
| [OnWillScrollCallback](arkts-onwillscrollcallback-t.md) | Called before scroll to allow developer to control real offset the Scrollable can scroll. |
| [OnWillStopDraggingCallback](arkts-onwillstopdraggingcallback-t.md) | On scroll callback using in scrollable onWillStopDragging. |
| [Optional](arkts-optional-t.md) | Defines the type that can be undefined. |
| [PixelMap](arkts-pixelmap-t.md) | Defines the PixelMap type object for ui component. |
| [PointerStyle](arkts-pointerstyle-t.md) | Import the PointerStyle type object for setCursor. |
| [PopupStateChangeCallback](arkts-popupstatechangecallback-t.md) | Popup state change callback |
| [PromptActionDialogController](arkts-promptactiondialogcontroller-t.md) | Import the DialogController type from promptAction. |
| [ReuseIdCallback](arkts-reuseidcallback-t.md) | ReuseId callback type. It is used to compute reuseId. |
| [RouterPageInfo](arkts-routerpageinfo-t.md) | The router page information. |
| [ShouldBuiltInRecognizerParallelWithCallback](arkts-shouldbuiltinrecognizerparallelwithcallback-t.md) | Defines the callback type used in shouldBuiltInRecognizerParallelWith. |
| [ShouldRecognizerParallelWithCallback](arkts-shouldrecognizerparallelwithcallback-t.md) | Defines the callback type used in shouldRecognizerParallelWith. |
| [SingleLengthDetent](arkts-singlelengthdetent-t.md) | 定义了单个高度的挡位。 |
| [SizeChangeCallback](arkts-sizechangecallback-t.md) | Defines the callback type used in onSizeChange. |
| [SpringLoadingContext](arkts-springloadingcontext-t.md) | The type for SpringLoadingContext, see the detailed description in dragController. |
| [Summary](arkts-summary-t.md) | Import the Summary type object for ui component. |
| [TipsMessageType](arkts-tipsmessagetype-t.md) | Defines the TipsMessageType property with ResourceStr and StyledString. |
| [TouchTestDoneCallback](arkts-touchtestdonecallback-t.md) | Defines the callback type used in onTouchTestDone. When the user touch down, the system performs hit test process to collect all gesture recognizers based on the press location, when the collection is completed, and before gesture begin to be recognizing, the callback is triggered, you can get all recognizer's information from this callback. |
| [TransitionFinishCallback](arkts-transitionfinishcallback-t.md) | 组件转场动画的结束回调类型。 |
| [TripleLengthDetents](arkts-triplelengthdetents-t.md) | 定义了三个高度的挡位。 |
| [UIContext](arkts-uicontext-t.md) | UIContext. |
| [UnifiedData](arkts-unifieddata-t.md) | Import the UnifiedData type object for ui component. |
| [UniformDataType](arkts-uniformdatatype-t.md) | Import the UniformDataType type object for ui component. |
| [VisibleAreaChangeCallback](arkts-visibleareachangecallback-t.md) | Defines the callback type used in VisibleAreaChange events. |
| [VisualEffect](arkts-visualeffect-t.md) | 导入VisualEffect类型对象。 |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [Blender](arkts-blender-t-sys.md) | Blender |
| [SystemUiMaterial](arkts-systemuimaterial-t-sys.md) | SystemUiMaterial |
<!--DelEnd-->

