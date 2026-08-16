# UIPickerComponentAttribute

Defines the Picker component attributes.

**Inheritance/Implementation:** UIPickerComponentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface UIPickerComponentAttribute--><!--Device-unnamed-export declare interface UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-UIPickerComponentAttribute-attributeModifier(modifier: AttributeModifier<UIPickerComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## canLoop

```TypeScript
canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-canLoop(isLoop: boolean | undefined): UIPickerComponentAttribute-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md) |  |

## displayedItemCount

```TypeScript
displayedItemCount(count: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-displayedItemCount(count: int | undefined): this--><!--Device-UIPickerComponentAttribute-displayedItemCount(count: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: boolean | undefined): UIPickerComponentAttribute-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md) |  |

## itemHeight

```TypeScript
itemHeight(height: LengthMetrics | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-itemHeight(height: LengthMetrics | undefined): this--><!--Device-UIPickerComponentAttribute-itemHeight(height: LengthMetrics | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onChange(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-na-onuipickercomponentcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md) |  |

## onScrollStop

```TypeScript
onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onScrollStop(callback: OnUIPickerComponentCallback | undefined): UIPickerComponentAttribute-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnUIPickerComponentCallback](arkts-na-onuipickercomponentcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md) |  |

## selectionIndicator

```TypeScript
selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-selectionIndicator(style: PickerIndicatorStyle | undefined): UIPickerComponentAttribute-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [PickerIndicatorStyle](arkts-na-uipickercomponent-pickerindicatorstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-na-uipickercomponent-uipickercomponentattribute-i.md) |  |

## setUIPickerComponentOptions

```TypeScript
setUIPickerComponentOptions(options?: UIPickerComponentOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-UIPickerComponentAttribute-setUIPickerComponentOptions(options?: UIPickerComponentOptions): this--><!--Device-UIPickerComponentAttribute-setUIPickerComponentOptions(options?: UIPickerComponentOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UIPickerComponentOptions](arkts-na-uipickercomponent-uipickercomponentoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Sets the total number of visible items.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIPickerComponentAttribute-default--><!--Device-UIPickerComponentAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

