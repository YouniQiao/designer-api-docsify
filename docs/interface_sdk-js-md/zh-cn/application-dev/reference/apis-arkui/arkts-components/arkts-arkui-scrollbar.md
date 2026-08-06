# ScrollBar

滚动条组件ScrollBar，用于配合可滚动组件使用，如[ArcList]{@link @ohos.arkui.ArcList}、[List]{@link list}、[Grid]{@link grid}、
[Scroll]{@link scroll}、[WaterFlow]{@link water_flow}。

> **说明：**
>
> - 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
>
> - ScrollBar主轴方向不设置大小时，采用父组件[布局约束]{@link FrameNode:LayoutConstraint}中的maxSize作为主轴方向大小。如果ScrollBar的父组件存在可滚动组件，如
> [ArcList]{@link @ohos.arkui.ArcList}、[List]{@link list}、[Grid]{@link grid}、[Scroll]{@link scroll}、
> [WaterFlow]{@link water_flow}，建议设置ScrollBar主轴方向大小，否则ScrollBar主轴方向大小可能为无穷大。

## 子组件

可以包含单个子组件。

## ScrollBarOptions对象说明

滚动条组件参数。
    **说明：**  
    
    - ScrollBar组件负责定义可滚动区域的行为样式，ScrollBar的子节点负责定义滚动条的行为样式。  
    
    - 滚动条组件与可滚动组件通过Scroller进行绑定，且只有当两者方向相同时，才能联动，ScrollBar与可滚动组件仅支持一对一绑定。  
    
    - 从API version 12开始，ScrollBar组件没有子节点时，支持显示默认样式的滚动条。  
    
    - ScrollBar组件的显隐是通过BarState设置，组件内部会自动根据BarState设置调整opacity来控制显隐，因此ScrollBar组件设置  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_属性不生效。

**原子化服务API：** 从API version 11开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |  
| -------- | -------- | -------- | -- | -------- |  
| scroller | [Scroller]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ | 否 | 否 | 可滚动组件的控制器。用于与可滚动组件进行绑定。 |  
| direction | \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ | 否 | 是 | 滚动条的方向，控制可滚动组件对应方向的滚动。\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_默认值：ScrollBarDirection.Vertical |  
| state | [BarState]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ | 否 | 是 | 滚动条状态。\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_默认值：BarState.Auto |

## ScrollBarDirection枚举说明

滚动条方向枚举。

**原子化服务API：** 从API version 11开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |  
| -------- | ---- | -------- |  
| Vertical | 0 | 纵向滚动条。 |  
| Horizontal | 1 | 横向滚动条。 |

## 示例1（设置子节点）

该示例为ScrollBar组件有子节点时的滚动条样式。

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## Example 2: Implementing a ScrollBar Component Without Child Components

This example illustrates the style of a **ScrollBar** component without child components. The  
[scrollBarColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute is added since API version 20.

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## Example 3: Enabling Nested Scrolling

This example demonstrates how to enable nested scrolling for a **ScrollBar** component using the  
[enableNestedScroll]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ attribute. This feature is available from API version 20.

\_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

!\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_

## ScrollBar

```TypeScript
ScrollBar(value: ScrollBarOptions)
```

创建滚动条组件。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute--><!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | 是 | 滚动条组件参数。  |

## 汇总

