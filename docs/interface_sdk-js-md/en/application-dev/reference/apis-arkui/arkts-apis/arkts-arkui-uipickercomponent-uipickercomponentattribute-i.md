# UIPickerComponentAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

除支持[通用事件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下事件：

**Inheritance/Implementation:** UIPickerComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIPickerComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface UIPickerComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-UIPickerComponentAttribute-default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## canLoop

```TypeScript
default canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute
```

设置选项列是否可循环滚动。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## displayedItemCount

```TypeScript
default displayedItemCount(count: int | undefined): this
```

设置UIPickerComponent容器可见选项的数量。未通过该接口设置时，可见选项的数量为7行。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default displayedItemCount(count: int | undefined): this--><!--Device-UIPickerComponentAttribute-default displayedItemCount(count: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int \| undefined | Yes | 可见选项数量。&lt;br/&gt;取值范围：[2, 9]内的整数。&lt;br/&gt;设置小数时，使用向下取整后的整数。 &lt;br/&gt;设置偶数时，自动转为不小于该值的奇数（例如2变为3、8变为9）。 &lt;br/&gt;设置不在取值范围内时，使用默认值7行。&lt;br/&gt;当count的值为undefined时，使用默认值7行。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute
```

设置是否开启触控反馈。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | 设置是否开启触控反馈。&lt;br/&gt;- true：开启触控反馈。&lt;br/&gt;- false：不开启触控反馈。 &lt;br/&gt;默认值：true&lt;br/&gt;当enable的值为undefined时，使用默认值。&lt;br/&gt;开启后，是否存在触控反馈取决于系统硬件支持情况。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## itemHeight

```TypeScript
default itemHeight(height: LengthMetrics | undefined): this
```

设置UIPickerComponent容器每个选项的高度。未通过该接口设置时，每个选项的高度为40vp。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default itemHeight(height: LengthMetrics | undefined): this--><!--Device-UIPickerComponentAttribute-default itemHeight(height: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) \| undefined | Yes | 选项高度。&lt;br/&gt;单位：与 [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)一致。&lt;br/&gt;取值范围：[40vp, 64vp]&lt;br/&gt;设置小于40vp或 大于64vp时，使用默认值40vp。&lt;br/&gt;当height的值为undefined时，使用默认值40vp。&lt;br/&gt;不支持"百分比"类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

滑动选择器选项时，若选中项发生变化，触发该事件。

> **说明：**
> 
> 如果某个选项有一半以上的区域进入选中项区域内，则该选项成为选中项。
> 
> 选中项区域可通过设置[selectionIndicator](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md#selectionindicator)进行标识。如果设置选中项指示器为背景，则背景区域即为
> 选中项区域。如果设置选中项指示器为分割线，则上下分割线的中心线内的区域为选中项区域。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | Yes | 当选中项发生变化时触发的回调函数。&lt;br/&gt;当callback的值为 undefined时，不使用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## onScrollStop

```TypeScript
default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

选择器滑动停止时，触发该事件。选择器滑动停止指某次行为触发的滑动动画完全结束。如果某次滑动动画还未结束时又触发了新的滑动动画，则不属于滑动停止。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | Yes | 当选择器滑动停止时触发的回调函数。&lt;br/&gt;当callback的值为 undefined时，不使用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## selectionIndicator

```TypeScript
default selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute
```

设置选中项指示器的样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [PickerIndicatorStyle](arkts-arkui-uipickercomponent-pickerindicatorstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

