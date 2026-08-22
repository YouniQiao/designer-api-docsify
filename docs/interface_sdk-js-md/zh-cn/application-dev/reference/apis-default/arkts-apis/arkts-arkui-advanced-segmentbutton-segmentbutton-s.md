# SegmentButton

分段按钮组件，包含页签类分段按钮、胶囊类单选分段按钮和胶囊类多选分段按钮。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare struct SegmentButton--><!--Device-unnamed-declare struct SegmentButton-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

build函数用于构造SegmentButton高级组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-@Builder  build(): void--><!--Device-SegmentButton-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## enableStateAnimation

```TypeScript
@PropRef
  enableStateAnimation: boolean
```

设置当通过变量修改selectedIndex值时，是否开启分段按钮的属性动画。

true表示开启分段按钮的属性动画；false表示不开启分段按钮的属性动画，使用原有动画。

默认值：false

**类型：** boolean

**默认值：** false

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-@PropRef  enableStateAnimation: boolean--><!--Device-SegmentButton-@PropRef  enableStateAnimation: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## maxFontScale

```TypeScript
@PropRef
  maxFontScale: double | Resource
```

分段按钮选项文字的最大字体放大倍数。

取值范围：[1, 2]

当设置的值小于1时，按值为1处理，设置的值大于2时，按值为2处理。

**类型：** double \| Resource

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-@PropRef  maxFontScale: double | Resource--><!--Device-SegmentButton-@PropRef  maxFontScale: double | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
onItemClicked?: Callback<int>
```

当分段按钮选项被点击时，触发的回调函数接收被点击的选项下标作为参数。若不传入此参数，则点击时不触发回调。

**类型：** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-onItemClicked?: Callback<int>--><!--Device-SegmentButton-onItemClicked?: Callback<int>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@ObjectLink
  options: SegmentButtonOptions
```

分段按钮选项。

**类型：** [SegmentButtonOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-segmentbutton-segmentbuttonoptions-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-@ObjectLink  options: SegmentButtonOptions--><!--Device-SegmentButton-@ObjectLink  options: SegmentButtonOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Link
  selectedIndexes: int[]
```

分段按钮的选中项编号，第一项的编号为0，之后顺序增加。

**说明：**

`selectedIndexes`使用[@Link装饰器：父子双向同步](../../../ui/state-management/arkts-link.md)，仅支持有效的按钮编号（第一个按钮编号为0，之后按顺序累加），如没有 选中项可传入空数组`[]`。

**类型：** int[]

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SegmentButton-@Link  selectedIndexes: int[]--><!--Device-SegmentButton-@Link  selectedIndexes: int[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

