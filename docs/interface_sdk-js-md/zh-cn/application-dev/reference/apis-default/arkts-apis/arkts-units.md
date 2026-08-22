# units

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ColorFilter](arkts-units-colorfilter-c.md) | 创建具有4*5矩阵的颜色过滤器。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AccessibilityActionOptions](arkts-units-accessibilityactionoptions-i.md) | 设置组件的无障碍操作的可选参数，用于限制或修改屏幕朗读等辅助应用发起的操作行为。仅Slider组件支持使用。在其他组件使用该接口时，编译环节可 正常通过，但接口功能不生效。 |
| [AccessibilityCustomAction](arkts-units-accessibilitycustomaction-i.md) | 自定义无障碍操作接口。 |
| [AccessibilityNextFocusParams](arkts-units-accessibilitynextfocusparams-i.md) | 定义无障碍自定义下一个焦点处理过程中可使用的详细参数对象。 |
| [AccessibilityOptions](arkts-units-accessibilityoptions-i.md) | Defines the struct of AccessibilityOptions. |
| [Area](arkts-units-area-i.md) | 区域类型，用于存储元素所占的区域信息。 |
| [Bias](arkts-units-bias-i.md) | 设置组件在锚点约束下的偏移参数。 |
| [BorderOptions](arkts-units-borderoptions-i.md) | 边框属性集合，用于描述边框相关信息。 |
| [BorderRadiuses](arkts-units-borderradiuses-i.md) | type BorderRadiuses = { topLeft: Length; topRight: Length; bottomLeft: Length; bottomRight: Length; } |
| [CacheCountInfo](arkts-units-cachecountinfo-i.md) | 缓存数量信息。 |
| [ChainWeightOptions](arkts-units-chainweightoptions-i.md) | 链中组件的布局权重。 |
| [ConstraintSizeOptions](arkts-units-constraintsizeoptions-i.md) | 约束尺寸类型，用于描述组件布局时对尺寸大小的范围限制。 |
| [Coordinate2D](arkts-units-coordinate2d-i.md) | 描述一个二维坐标系。 |
| [DirectionalEdgesT](arkts-units-directionaledgest-i.md) | 边缘宽度类型，用于描述组件边缘不同方向的宽度。支持全球化。 |
| [DividerStyleOptions](arkts-units-dividerstyleoptions-i.md) | 分割线样式属性集合, 用于描述分割线相关信息。 |
| [EdgeColors](arkts-units-edgecolors-i.md) | type EdgeColors = { top: ResourceColor; right: ResourceColor; bottom: ResourceColor; left: ResourceColor; } |
| [EdgeOutlineStyles](arkts-units-edgeoutlinestyles-i.md) | 引入该对象时，至少传入一个参数。 |
| [EdgeOutlineWidths](arkts-units-edgeoutlinewidths-i.md) | 引入该对象时，至少传入一个参数。 |
| [Edges](arkts-units-edges-i.md) | 位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置left和right，仅left生效。 |
| [EdgeStyles](arkts-units-edgestyles-i.md) | type EdgeStyles = { top: BorderStyle; right: BorderStyle; bottom: BorderStyle; left: BorderStyle; } |
| [EdgeWidths](arkts-units-edgewidths-i.md) | type EdgeWidths = { top: Length; right: Length; bottom: Length; left: Length; } |
| [Font](arkts-units-font-i.md) | 设置文本样式。 |
| [ItemFillPolicy](arkts-units-itemfillpolicy-i.md) | 定义一个适用于WaterFlow、Grid、 List、Swiper和 [LazyVWaterFlowLayout](../../../reference/apis-arkui/arkui-ts/ts-container-lazyvwaterflowlayout.md)组件的响应式布局策略。 LazyVWaterFlowLayout组件从API版本26.0.0开始支持。 |
| [LengthConstrain](arkts-units-lengthconstrain-i.md) | type LengthConstrain = { minLength: Length; maxLength: Length; } |
| [LocalizedBorderRadiuses](arkts-units-localizedborderradiuses-i.md) | 圆角类型，用于描述组件边框圆角半径。 |
| [LocalizedEdgeColors](arkts-units-localizededgecolors-i.md) | 边框颜色，用于描述组件边框四条边的颜色。 |
| [LocalizedEdges](arkts-units-localizededges-i.md) | 位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置start和end，仅start生效。 |
| [LocalizedEdgeWidths](arkts-units-localizededgewidths-i.md) | 边框宽度类型，用于描述组件边框不同方向的宽度。 |
| [LocalizedPadding](arkts-units-localizedpadding-i.md) | 内边距类型，用于描述组件不同方向的内边距。 |
| [LocalizedPosition](arkts-units-localizedposition-i.md) | 位置类型，用于表示一个坐标点。 |
| [MarkStyle](arkts-units-markstyle-i.md) | Define the style of checkbox mark. |
| [Offset](arkts-units-offset-i.md) | type Offset = { dx: Length; dy: Length; } |
| [OutlineOptions](arkts-units-outlineoptions-i.md) | 外描边选项设置。 |
| [OutlineRadiuses](arkts-units-outlineradiuses-i.md) | 引用该对象时，至少传入一个参数。 |
| [Padding](arkts-units-padding-i.md) | type Padding = { top: Length; right: Length; bottom: Length; left: Length; } |
| [Position](arkts-units-position-i.md) | 位置类型，用于表示一个坐标点。 |
| [ScrollBarMargin](arkts-units-scrollbarmargin-i.md) | 滚动条边距。 |
| [SizeOptions](arkts-units-sizeoptions-i.md) | 宽高尺寸类型，用于描述组件布局时的宽高尺寸大小。 |
| [TouchPoint](arkts-units-touchpoint-i.md) | 配置跟手点坐标，不配置时，默认居中。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ColorMetrics](arkts-colormetrics-t.md) | 定义混合颜色。 |
| [Degree](arkts-degree-t.md) | 角度类型，用于描述以deg像素单位为单位的长度。 |
| [Dimension](arkts-dimension-t.md) | 长度类型，用于描述尺寸单位。 |
| [DrawingCanvas](arkts-drawingcanvas-t.md) | 可用于向DrawingRenderingContext上绘制内容的画布对象。 |
| [EdgeWidth](arkts-edgewidth-t.md) | 边框宽度类型，用于描述组件边框不同方向的宽度。 |
| [FP](arkts-fp-t.md) | 长度类型，用于描述以fp像素单位为单位的长度。 |
| [Length](arkts-length-t.md) | 长度类型，用于描述尺寸单位。 |
| [LengthMetrics](arkts-lengthmetrics-t.md) | 定义长度属性。 |
| [LengthMetricsUnit](arkts-lengthmetricsunit-t.md) | 定义长度属性单位。 |
| [LocalizedMargin](arkts-localizedmargin-t.md) | 外边距类型，用于描述组件不同方向的外边距。 |
| [LPX](arkts-lpx-t.md) | 长度类型，用于描述以lpx像素单位为单位的长度。 |
| [Margin](arkts-margin-t.md) | 外边距类型，用于描述组件不同方向的外边距。 |
| [Percentage](arkts-percentage-t.md) | 长度类型，用于描述以百分比单位为单位的长度。 |
| [PX](arkts-px-t.md) | 长度类型，用于描述以px像素单位为单位的长度。 |
| [Resource](arkts-resource-t.md) | 资源引用类型，用于设置组件属性的值。各类资源文件，需要放入特定子目录中存储管理，资源目录的示例请参考 [资源分类](../../../quick-start/resource-categories-and-access.md#资源分类)。 |
| [ResourceColor](arkts-resourcecolor-t.md) | 颜色类型，用于描述资源颜色类型。 |
| [ResourceStr](arkts-resourcestr-t.md) | 字符串类型，用于描述字符串入参可以使用的类型。 |
| [ResponsiveFillType](arkts-responsivefilltype-t.md) | 响应式布局填充模式，用于WaterFlow、Grid、List、Swiper和LazyVWaterFlowLayout组件。LazyVWaterFlowLayout组件从API版本26.0.0开始支持。 |
| [VoidCallback](arkts-voidcallback-t.md) | Defines VoidCallback. |
| [VP](arkts-vp-t.md) | 长度类型，用于描述以vp像素单位为单位的长度。 |

