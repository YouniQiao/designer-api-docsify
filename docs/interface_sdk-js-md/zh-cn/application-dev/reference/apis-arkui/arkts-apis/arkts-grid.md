# grid

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ExtendableGrid](arkts-arkui-grid-extendablegrid-c.md) | 可扩展Grid组件。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ComputedBarAttribute](arkts-arkui-grid-computedbarattribute-i.md) | 滚动条位置和长度对象。 |
| [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i.md) | Grid布局选项。 |
| [UIGridEvent](arkts-arkui-grid-uigridevent-i.md) | frameNode中[getEvent('Grid')](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#geteventgrid19)方法的返回值，可用于给Grid节点设置滚动事件。  UIGridEvent继承于[UIScrollableCommonEvent](arkts-arkui-common-uiscrollablecommonevent-i.md)。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [GridLayoutOptions](arkts-arkui-grid-gridlayoutoptions-i-sys.md) | Grid布局选项。 |
| [StartLineInfo](arkts-arkui-grid-startlineinfo-i-sys.md) | 用于记录Grid页面内起始行的位置信息。  **系统接口：** 此接口为系统接口。  **模型约束：** 此接口仅可在Stage模型下使用。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [GridDirection](arkts-arkui-grid-griddirection-e.md) | 主轴布局方向枚举。 |
| [GridItemAlignment](arkts-arkui-grid-griditemalignment-e.md) | GridItem的对齐方式枚举。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnGridScrollIndexCallback](arkts-arkui-ongridscrollindexcallback-t.md) | Grid组件可见区域item变化事件的回调类型。 |

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [OnGetStartIndexByIndexCallback](arkts-arkui-ongetstartindexbyindexcallback-t-sys.md) | 根据指定的目标索引，计算Grid滚动到该位置时页面内对应的起始行，用于支持[scrollToIndex](arkts-arkui-scroll-scroller-c.md#scrolltoindex)等操作。  **系统接口：** 此接口为系统接口。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| [OnGetStartIndexByOffsetCallback](arkts-arkui-ongetstartindexbyoffsetcallback-t-sys.md) | 根据Grid的总偏移量，计算当前页面起始行的位置，用于快速滑动或反向滑动场景。  **系统接口：** 此接口为系统接口。  **模型约束：** 此接口仅可在Stage模型下使用。 |
<!--DelEnd-->

