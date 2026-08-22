# TabsOptions

Tabs组件参数，设置Tabs的页签位置，当前显示页签的索引，Tabs控制器和TabBar的通用属性。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface TabsOptions--><!--Device-unnamed-export declare interface TabsOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## barModifier

```TypeScript
barModifier?: CommonModifier
```

设置TabBar的通用属性。 **说明：** 动态置为undefined时会保持当前状态不变，不会重置各通用属性。 由一个CommonModifier切换为另一个CommonModifier时，重复属性会进行覆盖，非重复属性会同时生效，不会重置前一个CommonModifier的通用属性。 Tabs的[barWidth](arkts-tabs-attribute.md#barwidth)、 barHeight、 [barBackgroundColor](arkts-tabs-attribute.md#barbackgroundcolor)、 barBackgroundBlurStyle 、[barBackgroundEffect](arkts-tabs-attribute.md#barbackgroundeffect)属性会覆盖CommonModifier的 [width](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#width)、 [height](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#height)、 [backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor18) 、 [backgroundBlurStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundblurstyle18) 、 [backgroundEffect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundeffect18) 属性。 [align](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-location.md#align)属性仅在 [BarMode.Scrollable](../../../reference/apis-arkui/arkui-ts/ts-container-tabs copy.md#barmode10-1)模式下生效，且Tabs为横向 时还需[nonScrollableLayoutStyle](arkts-tabs-scrollablebarmodeoptions-i.md)未设置或设置为异常值时才能生效。 TabContent组件的 [tabBar](../../../reference/apis-arkui/arkui-ts/ts-container-tabcontent.md#tabbar18)属性为底部页签样式时不支持拖拽功能。

**类型：** [CommonModifier](../../apis-arkui/arkts-components/arkts-arkui-commonmodifier-t.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabsOptions-barModifier?: CommonModifier--><!--Device-TabsOptions-barModifier?: CommonModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## barPosition

```TypeScript
barPosition?: BarPosition
```

设置Tabs的页签位置。 默认值： BarPosition.Start。

**类型：** [BarPosition](arkts-tabs-barposition-e.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabsOptions-barPosition?: BarPosition--><!--Device-TabsOptions-barPosition?: BarPosition-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TabsController
```

设置Tabs控制器。

**类型：** [TabsController](arkts-tabs-tabscontroller-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabsOptions-controller?: TabsController--><!--Device-TabsOptions-controller?: TabsController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index?: int | Bindable<int>
```

设置当前显示页签的索引。 **说明：** 设置为小于0的值时按默认值显示. 可选值为[0, TabContent子节点数量-1]. 直接修改index跳页时，切换动效不生效. 使用TabController的changeIndex时，默认生效切换动效，可以设置 animationDuration为0关闭动画. 从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync. md)双向绑定变量. Tabs重建、系统资源切换（如系统字体切换、系统深浅色切换）或者组件属性变化时，会跳转到index对应的页面. 若需要在上述情况下不跳转，建议使用双向绑定。 默认值： 0。

**类型：** int \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;int&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabsOptions-index?: int | Bindable<int>--><!--Device-TabsOptions-index?: int | Bindable<int>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

