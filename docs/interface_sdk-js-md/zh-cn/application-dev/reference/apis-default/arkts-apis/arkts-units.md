# units

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ColorFilter](arkts-units-colorfilter-c.md) | 创建具有4*5矩阵的颜色过滤器。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AccessibilityActionOptions](arkts-units-accessibilityactionoptions-i.md) | 设置组件的无障碍操作的可选参数，用于限制或修改屏幕朗读等辅助应用发起的操作行为。仅Slider组件支持使用。在其他组件使用该接口时，编译环节可 正常通过，但接口功能不生效。@interface AccessibilityActionOptions |
| [AccessibilityCustomAction](arkts-units-accessibilitycustomaction-i.md) | 自定义无障碍操作接口。@interface AccessibilityCustomAction |
| [AccessibilityNextFocusParams](arkts-units-accessibilitynextfocusparams-i.md) | 定义无障碍自定义下一个焦点处理过程中可使用的详细参数对象。 |
| [AccessibilityOptions](arkts-units-accessibilityoptions-i.md) | Defines the struct of AccessibilityOptions.@interface AccessibilityOptions |
| [Area](arkts-units-area-i.md) | 区域类型，用于存储元素所占的区域信息。@interface Area |
| [Bias](arkts-units-bias-i.md) | 设置组件在锚点约束下的偏移参数。以水平方向Bias为例，其值为组件到左锚点的距离 D&lt;sub&gt;start&lt;/sub&gt;与组件到水平方向锚点间总距离 D&lt;sub&gt;start&lt;/sub&gt; + D&lt;sub&gt;end&lt;/sub&gt;的比值。镜像语言下，D&lt;sub&gt;start&lt;/ sub&gt;为组件到右锚点的距离。下图中D&lt;sub&gt;width&lt;/sub&gt;表示组件宽度。竖直方向同理，其值为组件到上锚点的距离D&lt;sub&gt;top&lt;/sub&gt;与组件到竖直方向锚点间总距离D&lt;sub&gt;top&lt;/sub&gt; + D&lt;sub&gt;bottom&lt;/sub&gt;的比值。下图中D&lt;sub&gt;height&lt;/sub&gt;表示组件高度。@interface Bias |
| [BorderOptions](arkts-units-borderoptions-i.md) | 边框属性集合，用于描述边框相关信息。@interface BorderOptions |
| [BorderRadiuses](arkts-units-borderradiuses-i.md) | type BorderRadiuses = { topLeft: Length; topRight: Length; bottomLeft: Length; bottomRight: Length; }圆角类型，用于描述组件边框圆角半径。引用该对象时，至少传入一个参数。@interface BorderRadiuses |
| [CacheCountInfo](arkts-units-cachecountinfo-i.md) | 缓存数量信息。@interface CacheCountInfo |
| [ChainWeightOptions](arkts-units-chainweightoptions-i.md) | 链中组件的布局权重。@interface ChainWeightOptions |
| [ConstraintSizeOptions](arkts-units-constraintsizeoptions-i.md) | 约束尺寸类型，用于描述组件布局时对尺寸大小的范围限制。 |
| [Coordinate2D](arkts-units-coordinate2d-i.md) | 描述一个二维坐标系。 |
| [DirectionalEdgesT](arkts-units-directionaledgest-i.md) | 边缘宽度类型，用于描述组件边缘不同方向的宽度。支持全球化。@interface DirectionalEdgesT |
| [DividerStyleOptions](arkts-units-dividerstyleoptions-i.md) | 分割线样式属性集合, 用于描述分割线相关信息。@interface DividerStyleOptions |
| [EdgeColors](arkts-units-edgecolors-i.md) | type EdgeColors = { top: ResourceColor; right: ResourceColor; bottom: ResourceColor; left: ResourceColor; }边框颜色，用于描述组件边框四条边的颜色。引入该对象时，至少传入一个参数。@interface EdgeColors |
| [EdgeOutlineStyles](arkts-units-edgeoutlinestyles-i.md) | 引入该对象时，至少传入一个参数。@interface EdgeOutlineStyles |
| [EdgeOutlineWidths](arkts-units-edgeoutlinewidths-i.md) | 引入该对象时，至少传入一个参数。@interface EdgeOutlineWidths |
| [Edges](arkts-units-edges-i.md) | 位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置left和right，仅left生效。@interface Edges |
| [EdgeStyles](arkts-units-edgestyles-i.md) | type EdgeStyles = { top: BorderStyle; right: BorderStyle; bottom: BorderStyle; left: BorderStyle; }边框样式，用于描述组件边框四条边的样式。引入该对象时，至少传入一个参数。@interface EdgeStyles |
| [EdgeWidths](arkts-units-edgewidths-i.md) | type EdgeWidths = { top: Length; right: Length; bottom: Length; left: Length; }边框宽度类型，用于描述组件边框不同方向的宽度。引入该对象时，至少传入一个参数。@interface EdgeWidths |
| [Font](arkts-units-font-i.md) | 设置文本样式。 |
| [ItemFillPolicy](arkts-units-itemfillpolicy-i.md) | 定义一个适用于WaterFlow、Grid、 List、Swiper和 [LazyVWaterFlowLayout](arkts-arkui-components-arklazywaterflowlayout-lazyvwaterflowlayout-f.md)组件的响应式布局策略。 LazyVWaterFlowLayout组件从API版本26.0.0开始支持。@interface ItemFillPolicy |
| [LengthConstrain](arkts-units-lengthconstrain-i.md) | type LengthConstrain = { minLength: Length; maxLength: Length; }长度约束，用于对组件最大、最小长度做限制。 |
| [LocalizedBorderRadiuses](arkts-units-localizedborderradiuses-i.md) | 圆角类型，用于描述组件边框圆角半径。引用该对象时，至少传入一个参数。@interface LocalizedBorderRadiuses |
| [LocalizedEdgeColors](arkts-units-localizededgecolors-i.md) | 边框颜色，用于描述组件边框四条边的颜色。引入该对象时，至少传入一个参数。@interface LocalizedEdgeColors |
| [LocalizedEdges](arkts-units-localizededges-i.md) | 位置类型，表示相对四边的偏移量。同时设置top和bottom，仅top生效；同时设置start和end，仅start生效。@interface LocalizedEdges |
| [LocalizedEdgeWidths](arkts-units-localizededgewidths-i.md) | 边框宽度类型，用于描述组件边框不同方向的宽度。引入该对象时，至少传入一个参数。@interface LocalizedEdgeWidths |
| [LocalizedPadding](arkts-units-localizedpadding-i.md) | 内边距类型，用于描述组件不同方向的内边距。@interface LocalizedPadding |
| [LocalizedPosition](arkts-units-localizedposition-i.md) | 位置类型，用于表示一个坐标点。@interface LocalizedPosition |
| [MarkStyle](arkts-units-markstyle-i.md) | Define the style of checkbox mark.@interface MarkStyle |
| [Offset](arkts-units-offset-i.md) | type Offset = { dx: Length; dy: Length; }相对布局完成位置坐标偏移量。@interface Offset |
| [OutlineOptions](arkts-units-outlineoptions-i.md) | 外描边选项设置。@interface OutlineOptions |
| [OutlineRadiuses](arkts-units-outlineradiuses-i.md) | 引用该对象时，至少传入一个参数。@interface OutlineRadiuses |
| [Padding](arkts-units-padding-i.md) | type Padding = { top: Length; right: Length; bottom: Length; left: Length; }内边距类型，用于描述组件不同方向的内边距。引入该对象时，至少传入一个参数。@interface Padding |
| [Position](arkts-units-position-i.md) | 位置类型，用于表示一个坐标点。@interface Position |
| [ScrollBarMargin](arkts-units-scrollbarmargin-i.md) | 滚动条边距。@interface ScrollBarMargin |
| [SizeOptions](arkts-units-sizeoptions-i.md) | 宽高尺寸类型，用于描述组件布局时的宽高尺寸大小。@interface SizeOptions |
| [TouchPoint](arkts-units-touchpoint-i.md) | 配置跟手点坐标，不配置时，默认居中。@interface TouchPoint |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ColorMetrics](arkts-colormetrics-t.md) | 定义混合颜色。 |
| [Degree](arkts-degree-t.md) | 角度类型，用于描述以deg像素单位为单位的长度。 |
| [Dimension](arkts-dimension-t.md) | 长度类型，用于描述尺寸单位。 |
| [DrawingCanvas](arkts-drawingcanvas-t.md) | 可用于向DrawingRenderingContext上绘制内容的画布对象。 |
| [EdgeWidth](arkts-edgewidth-t.md) | 边框宽度类型，用于描述组件边框不同方向的宽度。引入该对象时，至少传入一个参数。 |
| [FP](arkts-fp-t.md) | 长度类型，用于描述以fp像素单位为单位的长度。 |
| [Length](arkts-length-t.md) | 长度类型，用于描述尺寸单位。 |
| [LengthMetrics](arkts-lengthmetrics-t.md) | 定义长度属性。 |
| [LengthMetricsUnit](arkts-lengthmetricsunit-t.md) | 定义长度属性单位。 |
| [LocalizedMargin](arkts-localizedmargin-t.md) | 外边距类型，用于描述组件不同方向的外边距。引入该对象时，至少传入一个参数。 |
| [LPX](arkts-lpx-t.md) | 长度类型，用于描述以lpx像素单位为单位的长度。 |
| [Margin](arkts-margin-t.md) | 外边距类型，用于描述组件不同方向的外边距。引入该对象时，至少传入一个参数。 |
| [Percentage](arkts-percentage-t.md) | 长度类型，用于描述以百分比单位为单位的长度。 |
| [PX](arkts-px-t.md) | 长度类型，用于描述以px像素单位为单位的长度。 |
| [Resource](arkts-resource-t.md) | 资源引用类型，用于设置组件属性的值。各类资源文件，需要放入特定子目录中存储管理，资源目录的示例请参考 [资源分类](../../../quick-start/resource-categories-and-access.md#资源分类)。可以通过`\\$r`或者`\\$rawfile`创建Resource类型对象，不可以修改Resource中的各属性的值。  - `\\$r('belonging.type.name')`  belonging：系统资源或者应用资源，相应的取值为'sys'和'app'；type：资源类型，支持'boolean'、'color'、'float'、'intarray'、'integer'、'pattern'、'plural'、'strarray'、'string'、'media'；name：资源名称，在资源定义时确定。 - `\\$rawfile('filename')`filename：工程中resources/rawfile目录下的文件名称。 |
| [ResourceColor](arkts-resourcecolor-t.md) | 颜色类型，用于描述资源颜色类型。 |
| [ResourceStr](arkts-resourcestr-t.md) | 字符串类型，用于描述字符串入参可以使用的类型。 |
| [ResponsiveFillType](arkts-responsivefilltype-t.md) | 响应式布局填充模式，用于WaterFlow、Grid、List、Swiper和LazyVWaterFlowLayout组件。LazyVWaterFlowLayout组件从API版本26.0.0开始支持。 |
| [VoidCallback](arkts-voidcallback-t.md) | Defines VoidCallback. |
| [VP](arkts-vp-t.md) | 长度类型，用于描述以vp像素单位为单位的长度。 |

