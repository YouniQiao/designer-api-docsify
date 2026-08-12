# UIPickerComponentAttribute

Defines the Picker component attributes.

**Inheritance/Implementation:** UIPickerComponentAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UIPickerComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface UIPickerComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-UIPickerComponentAttribute-default attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## canLoop

```TypeScript
default canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute
```

Can scroll loop if true is set, on the contrary it can not.

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

Sets the total number of visible items.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default displayedItemCount(count: int | undefined): this--><!--Device-UIPickerComponentAttribute-default displayedItemCount(count: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int \| undefined | Yes | Total number of visible items. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute
```

Enable or disable haptic feedback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | Default value is true, set false to disable haptic feedback. Default value is true, set false to disable haptic feedback. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## itemHeight

```TypeScript
default itemHeight(height: LengthMetrics | undefined): this
```

Sets the height of each item.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default itemHeight(height: LengthMetrics | undefined): this--><!--Device-UIPickerComponentAttribute-default itemHeight(height: LengthMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | Yes | Height of each item. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

This event is triggered when a Picker item is selected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | Yes | The callback of onChange. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## onScrollStop

```TypeScript
default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

This event is triggered when a Picker item is selected and scrolling has stopped.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-default onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md) \| undefined | Yes | The callback of onScrollStop. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |  |

## selectionIndicator

```TypeScript
default selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute
```

Sets the indicator's type and style.

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

## setUIPickerComponentOptions

```TypeScript
default setUIPickerComponentOptions(options?: UIPickerComponentOptions): this
```

Sets the UI picker component options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default setUIPickerComponentOptions(options?: UIPickerComponentOptions): this--><!--Device-UIPickerComponentAttribute-default setUIPickerComponentOptions(options?: UIPickerComponentOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UIPickerComponentOptions](arkts-arkui-uipickercomponent-uipickercomponentoptions-i.md) | No | picker options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

