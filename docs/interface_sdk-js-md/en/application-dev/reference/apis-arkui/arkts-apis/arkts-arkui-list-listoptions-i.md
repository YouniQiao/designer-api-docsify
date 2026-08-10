# ListOptions

定义List组件参数。

&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;:&lt;br&gt;- List组件通用属性clip的默认值为true。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ListOptions--><!--Device-unnamed-export interface ListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: int
```

设置当前List初次加载时显示区域起始位置的item索引值。匿名对象整改。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。取值限定为整数。&lt;br&gt;设置为负数或超过了当前List最后一个item的索引值时视为无效取值，无效取值按默认值显示。&lt;/p&gt;

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-initialIndex?: int--><!--Device-ListOptions-initialIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

可滚动组件的控制器，与List绑定后，可以通过它控制List的滚动。匿名对象整改。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;不允许和其他滚动类组件绑定同一个滚动控制对象。&lt;/p&gt;

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-scroller?: Scroller--><!--Device-ListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: double | string
```

子组件主轴方向的间隔。匿名对象整改。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;设置为负数或者大于等于List内容区长度时，按默认值显示。&lt;br&gt;space参数值小于List分割线宽度时，子组件主轴方向的间隔取分割线宽度。&lt;br&gt; List子组件的visibility属性设置为None时不显示，但该子组件上下的space还是会生效。&lt;/p&gt;

**Type:** double \| string

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-space?: double | string--><!--Device-ListOptions-space?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

子组件主轴方向的间隔。&lt;p&gt;&lt;strong&gt;说明&lt;/strong&gt;。&lt;br&gt;设置为负数或者大于等于List内容区长度时，按默认值显示。&lt;br&gt;space参数值小于List分割线宽度时，子组件主轴方向的间隔取分割线宽度。&lt;br&gt; List子组件的visibility属性设置为None时不显示，但该子组件上下的space还是会生效。&lt;br&gt; 如果同时设置了spaceWidth和space，则spaceWidth优先生效。&lt;/p&gt;

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-spaceWidth?: Dimension--><!--Device-ListOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

