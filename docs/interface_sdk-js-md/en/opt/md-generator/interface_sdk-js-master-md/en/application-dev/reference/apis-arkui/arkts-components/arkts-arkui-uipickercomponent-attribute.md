# UIPickerComponent properties/events

In addition to the universal attributes, the following attributes are supported. In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** UIPickerComponentAttribute extends CommonMethod<UIPickerComponentAttribute>

**Since:** 22

**Deprecated since:** -1

<!--Device-unnamed-declare class UIPickerComponentAttribute--><!--Device-unnamed-declare class UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## canLoop

```TypeScript
canLoop(isLoop: Optional<boolean>)
```

Sets whether the option list can loop scrolling. - true: Loop scrolling is enabled. - false: Loop scrolling is disabled. Default value: true If the value of isLoop is undefined, the default value is used. If the number of child components is less than 8, loop scrolling will not occur regardless of whether isLoop is set to true or false.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentAttribute-canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-canLoop(isLoop: Optional<boolean>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isLoop | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## displayedItemCount

```TypeScript
displayedItemCount(count: Optional<number>)
```

Sets the total number of visible items.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UIPickerComponentAttribute-displayedItemCount(count: Optional<int>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-displayedItemCount(count: Optional<int>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: Optional<boolean>)
```

Sets whether to enable haptic feedback. To enable haptic feedback, you must declare the following permission under **requestPermissions** in **module** in **src/main/module.json5** of the project. - true: Enable haptic feedback. - false: Disable haptic feedback. Default value: true If the value of enable is undefined, the default value is used. After this function is enabled, whether haptic feedback is available depends on the hardware support of the system.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-enableHapticFeedback(enable: Optional<boolean>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## itemHeight

```TypeScript
itemHeight(height: Optional<LengthMetrics>)
```

Sets the height of each item.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-UIPickerComponentAttribute-itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-itemHeight(height: Optional<LengthMetrics>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| height | [Optional](arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes |

## onChange

```TypeScript
onChange(callback: Optional<OnUIPickerComponentCallback>)
```

Triggered when the selected item changes. If callback is set to undefined, the callback is not used. NOTE - If more than half of an option's area enters the selected item area, the option becomes the selected item. - The selected item area can be identified by setting [selectionIndicator](#selectionIndicator). If the selected item indicator is set to the background, the background area is the selected item area. If the selected item indicator is set to the divider, the area between the center lines of the upper and lower dividers is the selected item area.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentAttribute-onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onChange(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md)&gt; | Yes |

## onScrollStop

```TypeScript
onScrollStop(callback: Optional<OnUIPickerComponentCallback>)
```

Triggered when the picker scrolling stops. The picker scrolling stops when the scrolling animation triggered by an action is complete. If a new scrolling animation is triggered before the previous one finishes, it does not count as scrolling stop. If callback is set to undefined, the callback is not used.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentAttribute-onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-onScrollStop(callback: Optional<OnUIPickerComponentCallback>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnUIPickerComponentCallback](arkts-arkui-onuipickercomponentcallback-t.md)&gt; | Yes |

## selectionIndicator

```TypeScript
selectionIndicator(style: Optional<PickerIndicatorStyle>)
```

Sets the style of the selected item indicator. Default value: { type: PickerIndicatorType.BACKGROUND, borderRadius: { value:12, unit:LengthUnit.vp }, backgroundColor: 'sys.color.comp_background_tertiary' } If the value of style is undefined, the default value is used.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-UIPickerComponentAttribute-selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute--><!--Device-UIPickerComponentAttribute-selectionIndicator(style: Optional<PickerIndicatorStyle>): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[PickerIndicatorStyle](arkts-arkui-pickerindicatorstyle-i.md)&gt; | Yes |
