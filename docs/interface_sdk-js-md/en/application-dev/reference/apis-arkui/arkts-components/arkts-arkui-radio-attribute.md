# Radio properties/events

In addition to the universal attributes, the following attributes are supported.In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** RadioAttribute extends CommonMethod<RadioAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## checked

```TypeScript
checked(value: boolean)
```

Sets whether the radio button is selected.Since API version 10, this attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md).Since API version 18, this attribute supports two-way binding through [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## checked

```TypeScript
checked(isChecked: Optional<boolean>)
```

Sets whether the radio button is selected. Compared with [checked](#checked), this API supports the **undefined** type for the **isChecked** parameter.This attribute supports two-way binding through [\$\$](../../../ui/state-management/arkts-two-way-sync.md) and [!!](../../../ui/state-management/arkts-new-binding.md#two-way-binding-between-built-in-component-parameters).

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isChecked | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RadioConfiguration>)
```

Creates a content modifier.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-arkui-radioconfiguration-i.md)&gt; | Yes |

## contentModifier

```TypeScript
contentModifier(modifier: Optional<ContentModifier<RadioConfiguration>>)
```

Creates a content modifier. Compared with [contentModifier](#contentmodifier)&lt;sup&gt;12+&lt;/sup&gt;, this API supports the **undefined** type for the **modifier** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [Optional](arkts-arkui-optional-t.md)&lt;[ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-arkui-radioconfiguration-i.md)&gt;&gt; | Yes |

## onChange

```TypeScript
onChange(callback: (isChecked: boolean) => void)
```

Triggered when the selected state of the radio button changes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (isChecked: boolean) = & gt; void | Yes |

## onChange

```TypeScript
onChange(callback: Optional<OnRadioChangeCallback>)
```

Triggered when the selected state of the radio button changes. Compared with onChange, this API supports the **undefined** type for the **callback** parameter.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Optional](arkts-arkui-optional-t.md)&lt;[OnRadioChangeCallback](arkts-arkui-onradiochangecallback-t.md)&gt; | Yes |

## radioStyle

```TypeScript
radioStyle(value?: RadioStyle)
```

Sets the style of the radio button in selected or deselected state.Since API version 10, this API is supported in ArkTS widgets.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RadioStyle](arkts-arkui-radiostyle-i.md) | No |
