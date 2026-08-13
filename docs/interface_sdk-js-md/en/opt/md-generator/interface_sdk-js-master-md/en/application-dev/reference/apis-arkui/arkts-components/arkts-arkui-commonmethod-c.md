# CommonMethod

CommonMethod.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-declare class CommonMethod--><!--Device-unnamed-declare class CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityActionOptions

```TypeScript
accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T
```

Provides optional parameters for setting accessibility operations of a component, which is used to restrict or &lt;br&gt;modify the operations initiated by accessibility applications such as the screen reader.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-CommonMethod-accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T--><!--Device-CommonMethod-accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [AccessibilityActionOptions](../arkts-apis/arkts-arkui-accessibilityactionoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityChecked

```TypeScript
accessibilityChecked(isCheck: boolean): T
```

Sets the checked state for the accessibility node. This API is used in multi-select scenarios and only affects &lt;br&gt;component state announcements in screen reading scenarios.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**Widget capability:** This API can be used in ArkTS widgets since API version 13.

<!--Device-CommonMethod-accessibilityChecked(isCheck: boolean): T--><!--Device-CommonMethod-accessibilityChecked(isCheck: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isCheck | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityCustomActions

```TypeScript
accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T
```

Sets the custom accessibility operations of the component, allowing developers to set an array of custom actions &lt;br&gt;for binding custom operation callbacks to components by operation name.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-CommonMethod-accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T--><!--Device-CommonMethod-accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [actions](../../apis-ability-kit/arkts-apis/arkts-ability-skill-i.md) | Array&lt;[AccessibilityCustomAction](../arkts-apis/arkts-arkui-accessibilitycustomaction-i.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityDefaultFocus

```TypeScript
accessibilityDefaultFocus(focus: boolean): T
```

Sets the initial screen reader focus on the page.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-accessibilityDefaultFocus(focus: boolean): T--><!--Device-CommonMethod-accessibilityDefaultFocus(focus: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| focus | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityDescription

```TypeScript
accessibilityDescription(value: string): T
```

Sets the accessibility description. &lt;br&gt;This attribute provides additional context and explanation for the component, helping users understand its &lt;br&gt;functionality and purpose.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityDescription(value: string): T--><!--Device-CommonMethod-accessibilityDescription(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityDescription

```TypeScript
accessibilityDescription(description: Resource): T
```

Sets the accessibility description, with support for resource references using Resource. &lt;br&gt;This attribute provides additional context and explanation for the component, helping users understand its &lt;br&gt;functionality and purpose. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;Reference resource of the accessibility description. You can specify further explanation &lt;br&gt;of the current component, for example, possible operation consequences, especially those that &lt;br&gt;cannot be learned from component attributes and accessibility text. If a component contains &lt;br&gt;both text information and the accessibility description, the text is read first and then the &lt;br&gt;accessibility description, when the component is selected.&lt;/p&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityDescription(description: Resource): T--><!--Device-CommonMethod-accessibilityDescription(description: Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityFocusDrawLevel

```TypeScript
accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T
```

Sets the drawing level for the accessibility focus highlight (green frame).

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-CommonMethod-accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T--><!--Device-CommonMethod-accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| drawLevel | [FocusDrawLevel](../arkts-apis/arkts-arkui-focusdrawlevel-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityGroup

```TypeScript
accessibilityGroup(value: boolean): T
```

Sets whether to enable accessibility grouping. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;Whether to enable accessibility grouping. When accessibility grouping is enabled, &lt;br&gt;the component and all its children are treated as a single selectable unit, and the accessibility &lt;br&gt;service will no longer focus on the individual child components.&lt;/p&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityGroup(value: boolean): T--><!--Device-CommonMethod-accessibilityGroup(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityGroup

```TypeScript
accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T
```

Sets whether to enable accessibility grouping. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;If accessibility grouping is enabled and the component does not contain a universal text attribute &lt;br&gt;or an accessibility text attribute, the system will concatenate the universal text attributes of &lt;br&gt;its child components to form a merged text for the component. If a child component lacks a universal &lt;br&gt;text attribute, it will be ignored in the concatenation process. &lt;br&gt;When accessibilityPreferred is set to true, the system will prioritize concatenating the accessibility &lt;br&gt;text attributes of the child components to form the merged text. If a child component lacks an &lt;br&gt;accessibility text attribute, the system will continue to concatenate its universal text attribute. &lt;br&gt;If a child component lacks both, it will be ignored.&lt;/p&gt;

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 14.

<!--Device-CommonMethod-accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T--><!--Device-CommonMethod-accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isGroup | boolean | Yes |
| accessibilityOptions | [AccessibilityOptions](../arkts-apis/arkts-arkui-accessibilityoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityLevel

```TypeScript
accessibilityLevel(value: string): T
```

Sets the accessibility level. This property determines whether the component can be recognized by accessibility services. &lt;p&gt; Accessibility level, which is used to decide whether a component can be identified by the accessibility service. &lt;br&gt;The options are as follows: &lt;br&gt;"auto": The component's recognizability is determined by the accessibility grouping service and ArkUI. &lt;br&gt;"yes": The component can be recognized by accessibility services. &lt;br&gt;"no": The component cannot be recognized by accessibility services. &lt;br&gt;"no-hide-descendants": Neither the component nor its child components can be recognized by accessibility services. &lt;strong&gt;NOTE&lt;/strong&gt; &lt;br&gt;When accessibilityLevel is set to "auto", the component's recognizability depends on the following factors: &lt;br&gt;1. The accessibility service internally determines whether the component can be recognized. &lt;br&gt;2. If the parent component's accessibilityGroup property has isGroup set to true, the accessibility service will &lt;br&gt;not focus on its child components, making them unrecognizable. &lt;br&gt;3. If the parent component's accessibilityLevel is set to "no-hide-descendants", the component will not be &lt;br&gt;recognized by accessibility services.&lt;/p&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityLevel(value: string): T--><!--Device-CommonMethod-accessibilityLevel(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string): T
```

Sets the next component to receive focus during screen reader navigation.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-accessibilityNextFocusId(nextId: string): T--><!--Device-CommonMethod-accessibilityNextFocusId(nextId: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nextId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T
```

Sets the next component to receive focus during screen reader navigation, with optional detailed parameters. The detailed parameters can provide additional behavior for the accessibility focus transition.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T--><!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nextId | string | Yes |
| nextFocusParams | [AccessibilityNextFocusParams](../arkts-apis/arkts-arkui-accessibilitynextfocusparams-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T
```

Enable or disable specific smart gesture shortcuts, and set response priorities for them.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T--><!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nextId | string | Yes |
| nextFocusParams | [AccessibilityNextFocusParams](../arkts-apis/arkts-arkui-accessibilitynextfocusparams-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityRole

```TypeScript
accessibilityRole(role: AccessibilityRoleType): T
```

Sets the role type of the accessibility component, which affects how the component is announced by screen readers.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-accessibilityRole(role: AccessibilityRoleType): T--><!--Device-CommonMethod-accessibilityRole(role: AccessibilityRoleType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| role | [AccessibilityRoleType](arkts-arkui-accessibilityroletype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityScrollTriggerable

```TypeScript
accessibilityScrollTriggerable(isTriggerable: boolean): T
```

Sets whether the accessibility node triggers automatic screen scrolling. When no focusable components are visible &lt;br&gt;on the current page within a container, this setting determines whether automatic scrolling is initiated.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-accessibilityScrollTriggerable(isTriggerable: boolean): T--><!--Device-CommonMethod-accessibilityScrollTriggerable(isTriggerable: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTriggerable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilitySelected

```TypeScript
accessibilitySelected(isSelect: boolean): T
```

Sets the checked state for the accessibility node. This API is used in single-select scenarios and only affects &lt;br&gt;component state announcements in screen reading scenarios.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**Widget capability:** This API can be used in ArkTS widgets since API version 13.

<!--Device-CommonMethod-accessibilitySelected(isSelect: boolean): T--><!--Device-CommonMethod-accessibilitySelected(isSelect: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isSelect | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription(description: string | Resource | undefined): T
```

Sets the state description of a component for broadcasting, which clearly describes the real-time state of the &lt;br&gt;component in screen reading scenarios. Screen reader will broadcast the state description first.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-CommonMethod-accessibilityStateDescription(description: string | Resource | undefined): T--><!--Device-CommonMethod-accessibilityStateDescription(description: string | Resource | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| description | string \| Resource \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityText

```TypeScript
accessibilityText(value: string): T
```

Sets the accessibility text. When a component does not contain a text attribute, you can use this API to set an accessibility text attribute, so that accessibility services can announce the specified content for the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityText(value: string): T--><!--Device-CommonMethod-accessibilityText(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityText

```TypeScript
accessibilityText(text: Resource): T
```

Sets the accessibility text. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt; If a component has both text content and accessibility text, only the accessibility text is announced. &lt;br&gt;If a component is grouped for accessibility purposes but lacks both text content and accessibility &lt;br&gt;text, the screen reader will concatenate text from its child components (depth-first traversal). &lt;br&gt;To prioritize accessibility text concatenation, set accessibilityPreferred in accessibilityGroup. &lt;/p&gt;

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityText(text: Resource): T--><!--Device-CommonMethod-accessibilityText(text: Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityTextHint

```TypeScript
accessibilityTextHint(value: string): T
```

Sets the text hint for the component, which can be queried by accessibility services.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityTextHint(value: string): T--><!--Device-CommonMethod-accessibilityTextHint(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityUseSamePage

```TypeScript
accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T
```

Sets the same-page mode for the current component and its host application.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T--><!--Device-CommonMethod-accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pageMode | [AccessibilitySamePageMode](arkts-arkui-accessibilitysamepagemode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## accessibilityVirtualNode

```TypeScript
accessibilityVirtualNode(builder: CustomBuilder): T
```

Sets an accessibility virtual child node. For custom drawing components, a **CustomBuilder** is passed, which is &lt;br&gt;used to provide accessibility information. The components within the **CustomBuilder** are only used for layout &lt;br&gt;and not for display.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-accessibilityVirtualNode(builder: CustomBuilder): T--><!--Device-CommonMethod-accessibilityVirtualNode(builder: CustomBuilder): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## align

```TypeScript
align(value: Alignment): T
```

Sets the alignment mode for child elements within the container's drawing area. This attribute can be dynamically set using [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-align(value: Alignment): T--><!--Device-CommonMethod-align(value: Alignment): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## align

```TypeScript
align(alignment: Alignment | LocalizedAlignment): T
```

Sets the alignment mode for child elements within the container's drawing area. The mirroring capability is supported. This attribute can be dynamically set using [attributeModifier](#attributeModifier).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CommonMethod-align(alignment: Alignment | LocalizedAlignment): T--><!--Device-CommonMethod-align(alignment: Alignment | LocalizedAlignment): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignment | [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) \| [LocalizedAlignment](../arkts-apis/arkts-arkui-localizedalignment-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## alignRules

```TypeScript
alignRules(value: AlignRuleOption): T
```

Sets the alignment rule for child components within the relative container. This attribute only takes effect when the parent container is RelativeContainer, and supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-alignRules(value: AlignRuleOption): T--><!--Device-CommonMethod-alignRules(value: AlignRuleOption): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [AlignRuleOption](arkts-arkui-alignruleoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## alignRules

```TypeScript
alignRules(alignRule: LocalizedAlignRuleOptions): T
```

Sets the alignment rules in the relative container. This API is valid only when the container is RelativeContainer,. This attribute replaces the original **left** and **right** directional parameters with **start** and **end** to support proper mirroring in right-to-left (RTL) layout modes. It is recommended that you use this attribute for configuring child component alignment rules in relative containers. This attribute supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T--><!--Device-CommonMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignRule | [LocalizedAlignRuleOptions](arkts-arkui-localizedalignruleoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## alignSelf

```TypeScript
alignSelf(value: ItemAlign): T
```

Sets the alignment mode of the child components along the cross axis of the parent container.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-alignSelf(value: ItemAlign): T--><!--Device-CommonMethod-alignSelf(value: ItemAlign): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ItemAlign](../arkts-apis/arkts-arkui-itemalign-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## allowDrop

```TypeScript
allowDrop(value: Array<UniformDataType> | null | Array<string>): T
```

Sets the types of data that can be dropped to the component. If **allowDrop** is not set, the component accepts all data types by default.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-allowDrop(value: Array<UniformDataType> | null | Array<string>): T--><!--Device-CommonMethod-allowDrop(value: Array<UniformDataType> | null | Array<string>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[UniformDataType](arkts-arkui-uniformdatatype-t.md)&gt; \| null \| Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## allowForceDark

```TypeScript
allowForceDark(value: boolean): T
```

Set whether the component enables the ability to invert colors. This interface needs to be set as the first attribute of the component.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-CommonMethod-allowForceDark(value: boolean): T--><!--Device-CommonMethod-allowForceDark(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## animation

```TypeScript
animation(value: AnimateParam): T
```

Sets a property animation for the component. > **NOTE：**> > - When a single page contains a large number of components with animations, use > [renderGroup](#renderGroup) to minimize frame freezing and improve animation > performance. For best practices, see > [Animation Usage Guide – Using RenderGroup](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fair-use-animation#section1223162922415). > > > - This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-animation(value: AnimateParam): T--><!--Device-CommonMethod-animation(value: AnimateParam): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-animateparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## aspectRatio

```TypeScript
aspectRatio(value: number): T
```

Sets the aspect ratio of the component, which can be obtained using the following formula: width/height. &lt;br&gt;- If only **width** and **aspectRatio** are set, the height is calculated using the following formula: width/aspectRatio. &lt;br&gt;- If only **height** and **aspectRatio** are set, the width is calculated using the following formula: height x aspectRatio. &lt;br&gt;- If **width**, **height**, and **aspectRatio** are all set, the explicitly set height is ignored, and the effective height is calculated using the following formula: width/aspectRatio. &lt;br&gt;After the **aspectRatio** attribute is set, the component's width and height will be limited by the size of the parent component's content area. The priority of [constraintSize](#constraintSize) is higher than that of **aspectRatio**.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-aspectRatio(value: number): T--><!--Device-CommonMethod-aspectRatio(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<T>): T
```

Sets the attribute modifier.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-attributeModifier(modifier: AttributeModifier<T>): T--><!--Device-CommonMethod-attributeModifier(modifier: AttributeModifier<T>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](arkts-arkui-attributemodifier-i.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(value: number, options?: BlurOptions): T
```

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-backdropBlur(value: number, options?: BlurOptions): T--><!--Device-CommonMethod-backdropBlur(value: number, options?: BlurOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(radius: Optional<number>, options?: BlurOptions): T
```

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters. Compared to [backdropBlur](#backdropBlur), the **radius** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions): T--><!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T
```

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters. Compared with [backdropBlur&lt;sup&gt;18+&lt;/sup&gt;](#backdropBlur), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## background

```TypeScript
background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T
```

Add a background for the component. Anonymous Object Rectification.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T--><!--Device-CommonMethod-background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |
| options | [BackgroundOptions](arkts-arkui-backgroundoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T
```

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T
```

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values. Compared to [backgroundBlurStyle&lt;sup&gt;9+&lt;/sup&gt;](#backgroundBlurStyle), the **style** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[BlurStyle](arkts-arkui-blurstyle-e.md)&gt; | Yes |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T
```

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values. Compared with [backgroundBlurStyle&lt;sup&gt;18+&lt;/sup&gt;](#backgroundBlurStyle), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[BlurStyle](arkts-arkui-blurstyle-e.md)&gt; | Yes |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | No |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundBrightness

```TypeScript
backgroundBrightness(params: BackgroundBrightnessOptions): T
```

Sets the background brightness of the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-backgroundBrightness(params: BackgroundBrightnessOptions): T--><!--Device-CommonMethod-backgroundBrightness(params: BackgroundBrightnessOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [BackgroundBrightnessOptions](arkts-arkui-backgroundbrightnessoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundBrightness

```TypeScript
backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T
```

Sets the background brightness of the component. Compared to [backgroundBrightness&lt;sup&gt;12+&lt;/sup&gt;](#backgroundBrightness), the **options** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T--><!--Device-CommonMethod-backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[BackgroundBrightnessOptions](arkts-arkui-backgroundbrightnessoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor): T
```

Background color

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-backgroundColor(value: ResourceColor): T--><!--Device-CommonMethod-backgroundColor(value: ResourceColor): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(color: Optional<ResourceColor>): T
```

Background color

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor>): T--><!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T
```

Background color

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T--><!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| ColorMetrics & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: BackgroundEffectOptions): T
```

Sets the background effect of the component, including the blur radius, brightness, saturation, and color.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-backgroundEffect(options: BackgroundEffectOptions): T--><!--Device-CommonMethod-backgroundEffect(options: BackgroundEffectOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: Optional<BackgroundEffectOptions>): T
```

Sets the background effect of the component, including the blur radius, brightness, saturation, and color. Compared to [backgroundEffect&lt;sup&gt;11+&lt;/sup&gt;](#backgroundEffect), the **options** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>): T--><!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T
```

Sets the background effect of the component, including the blur radius, brightness, saturation, and color. Compared with [backgroundEffect&lt;sup&gt;18+&lt;/sup&gt;](#backgroundEffect), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments. > **NOTE：**> > **backgroundEffect** performs real-time rendering per frame, resulting in high performance overhead. When the > background blur effect remains unchanged, it is recommended that you use the static blur API > [blur](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-effectkit-filter-i.md#blur). For best practices, see > [Image Blurring Optimization – When to Use](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519).

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md)&gt; | Yes |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundFilter

```TypeScript
backgroundFilter(filter: Filter): T
```

Sets the visual effect of the background filter. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-backgroundFilter(filter: Filter): T--><!--Device-CommonMethod-backgroundFilter(filter: Filter): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundImage

```TypeScript
backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T
```

Background image src: Image address url

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T--><!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) | Yes |
| repeat | [ImageRepeat](../arkts-apis/arkts-arkui-imagerepeat-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundImage

```TypeScript
backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T
```

Background image

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T--><!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) | Yes |
| options | [BackgroundImageOptions](arkts-arkui-backgroundimageoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundImagePosition

```TypeScript
backgroundImagePosition(value: Position | Alignment): T
```

Background image position x:Horizontal coordinate;y:Vertical axis coordinate.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-backgroundImagePosition(value: Position | Alignment): T--><!--Device-CommonMethod-backgroundImagePosition(value: Position | Alignment): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Position \| [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundImageResizable

```TypeScript
backgroundImageResizable(value: ResizableOptions): T
```

Background image resizable. value:resizable options

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-backgroundImageResizable(value: ResizableOptions): T--><!--Device-CommonMethod-backgroundImageResizable(value: ResizableOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-resizableoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backgroundImageSize

```TypeScript
backgroundImageSize(value: SizeOptions | ImageSize): T
```

Background image size

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-backgroundImageSize(value: SizeOptions | ImageSize): T--><!--Device-CommonMethod-backgroundImageSize(value: SizeOptions | ImageSize): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) \| [ImageSize](../arkts-apis/arkts-arkui-imagesize-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContentCover

```TypeScript
bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T
```

Binds a full-screen modal to the component, which can be displayed when the component is touched. The content of the modal is customizable. The transition type can be set to none, slide-up and slide-down animation, and opacity gradient animation. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T--><!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShow | boolean | Yes |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| type | [ModalTransition](arkts-arkui-modaltransition-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContentCover

```TypeScript
bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T
```

Binds a full-screen modal to the component, which can be displayed when the component is touched. The modal page content and transition mode are configurable.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T--><!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShow | boolean | Yes |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [ContentCoverOptions](arkts-arkui-contentcoveroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenu

```TypeScript
bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| responseType | [ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md) | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenu

```TypeScript
bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T
```

Binds a context menu to the component, whose visibility is subject to the isShown settings.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShown | boolean | Yes |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenuByIsShow

```TypeScript
bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T
```

Binds a context menu to the component, whose visibility is subject to the isShow settings.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShow | boolean | Yes |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenuByResponseType

```TypeScript
bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,
      options?: ContextMenuOptions): T
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Custom or fixed-style menu items are supported.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,      options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,      options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; | Yes |
| responseType | [ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md) | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenuWithResponse

```TypeScript
bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported. Long pressing with a mouse device is not supported.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md)&gt; \| undefined | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindContextMenuWithResponse

```TypeScript
bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,
    options?: ContextMenuOptions): T
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Custom or fixed-style menu items are supported. Long pressing with a mouse device is not supported.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,    options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,    options?: ContextMenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md)&gt; \| Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; \| undefined | Yes |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindMenu

```TypeScript
bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T
```

Menu control

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T--><!--Device-CommonMethod-bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [MenuOptions](arkts-arkui-menuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindMenu

```TypeScript
bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T
```

Menu control

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T--><!--Device-CommonMethod-bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShow | boolean | Yes |
| content | Array&lt;[MenuElement](arkts-arkui-menuelement-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [MenuOptions](arkts-arkui-menuoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindPopup

```TypeScript
bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T
```

Popup control &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;The popup can be displayed only after the entire page is fully constructed. Therefore, to avoid incorrect display positions and shapes, do not set this parameter to true while the page is still being constructed. &lt;/p&gt;

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T--><!--Device-CommonMethod-bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| show | boolean | Yes |
| popup | [PopupOptions](arkts-arkui-popupoptions-i.md) \| [CustomPopupOptions](arkts-arkui-custompopupoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindSheet

```TypeScript
bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T
```

Binds a sheet to the component, which is displayed when the component is touched. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T--><!--Device-CommonMethod-bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isShow | boolean | Yes |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [SheetOptions](arkts-arkui-sheetoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## bindTips

```TypeScript
bindTips(message: TipsMessageType, options?: TipsOptions): T
```

Tips control

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CommonMethod-bindTips(message: TipsMessageType, options?: TipsOptions): T--><!--Device-CommonMethod-bindTips(message: TipsMessageType, options?: TipsOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) | Yes |
| options | [TipsOptions](arkts-arkui-tipsoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## blendMode

```TypeScript
blendMode(value: BlendMode, type?: BlendApplyType): T
```

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-blendMode(value: BlendMode, type?: BlendApplyType): T--><!--Device-CommonMethod-blendMode(value: BlendMode, type?: BlendApplyType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlendMode](arkts-arkui-blendmode-e.md) | Yes |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## blendMode

```TypeScript
blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T
```

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below. Compared to [blendMode&lt;sup&gt;11+&lt;/sup&gt;](#blendMode), the **mode** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T--><!--Device-CommonMethod-blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [Optional](arkts-arkui-optional-t.md)&lt;[BlendMode](arkts-arkui-blendmode-e.md)&gt; | Yes |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## blur

```TypeScript
blur(value: number, options?: BlurOptions): T
```

Applies a foreground blur effect to the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-blur(value: number, options?: BlurOptions): T--><!--Device-CommonMethod-blur(value: number, options?: BlurOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## blur

```TypeScript
blur(blurRadius: Optional<number>, options?: BlurOptions): T
```

Applies a foreground blur effect to the component. Compared to [blur](#blur), the **blurRadius** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions): T--><!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textshadow-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## blur

```TypeScript
blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T
```

Applies a foreground blur effect to the component. Compared to [blur&lt;sup&gt;18+&lt;/sup&gt;](#blur), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textshadow-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | No |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## border

```TypeScript
border(value: BorderOptions): T
```

Sets the border. When neither color nor radius is specified, set borderColor and borderRadius after border to ensure they take effect.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-border(value: BorderOptions): T--><!--Device-CommonMethod-border(value: BorderOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BorderOptions](../arkts-apis/arkts-arkui-borderoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderColor

```TypeScript
borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T
```

Sets the border color.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T--><!--Device-CommonMethod-borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [EdgeColors](../arkts-apis/arkts-arkui-edgecolors-t.md) \| [LocalizedEdgeColors](../arkts-apis/arkts-arkui-localizededgecolors-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderImage

```TypeScript
borderImage(value: BorderImageOption): T
```

Sets the border image of the component.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-borderImage(value: BorderImageOption): T--><!--Device-CommonMethod-borderImage(value: BorderImageOption): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BorderImageOption](arkts-arkui-borderimageoption-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T
```

Sets the border radius.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T--><!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](../arkts-apis/arkts-arkui-localizedborderradiuses-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T
```

Sets the border corner radius and the rendering strategy for rounded corners. NOTE 1. **RenderStrategy.FAST**: The current component and its child components will be drawn directly onto the canvas with rounded corners applied. 2. **RenderStrategy.OFFSCREEN**: The current component and its child components will first be rendered onto an off-screen canvas, then undergo a rounded corner clipping, and finally be drawn onto the main canvas.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T--><!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](../arkts-apis/arkts-arkui-localizedborderradiuses-i.md) | Yes |
| type | [RenderStrategy](../arkts-apis/arkts-arkui-renderstrategy-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderStyle

```TypeScript
borderStyle(value: BorderStyle | EdgeStyles): T
```

Border style

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-borderStyle(value: BorderStyle | EdgeStyles): T--><!--Device-CommonMethod-borderStyle(value: BorderStyle | EdgeStyles): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BorderStyle](../arkts-apis/arkts-arkui-borderstyle-e.md) \| [EdgeStyles](../arkts-apis/arkts-arkui-edgestyles-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## borderWidth

```TypeScript
borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T
```

Sets the border width.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T--><!--Device-CommonMethod-borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| [EdgeWidths](../arkts-apis/arkts-arkui-edgewidths-t.md) \| [LocalizedEdgeWidths](../arkts-apis/arkts-arkui-localizededgewidths-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## brightness

```TypeScript
brightness(value: number): T
```

Applies a brightness effect to the component. If this API is not used, there will be no change by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-brightness(value: number): T--><!--Device-CommonMethod-brightness(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## brightness

```TypeScript
brightness(brightness: Optional<number>): T
```

Applies a brightness effect to the component. If this API is not used, there will be no change by default. Compared with [brightness](#brightness), this API supports the **undefined** type for the **brightness** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-brightness(brightness: Optional<number>): T--><!--Device-CommonMethod-brightness(brightness: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [brightness](#brightness) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## chainMode

```TypeScript
chainMode(direction: Axis, style: ChainStyle): T
```

Sets the parameters of the chain in which the component is the head. This attribute takes effect only when the parent container is RelativeContainer. The chain head is the first component in the chain that satisfies the chain formation rules. In a horizontal layout, it starts from the left (or from the right in a mirrored language layout). In a vertical layout, it starts from the top.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-chainMode(direction: Axis, style: ChainStyle): T--><!--Device-CommonMethod-chainMode(direction: Axis, style: ChainStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [direction](#direction) | [Axis](../../apis-na/arkts-apis/arkts-na-enums-axis-e.md) | Yes |
| style | [ChainStyle](arkts-arkui-chainstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## chainWeight

```TypeScript
chainWeight(chainWeight: ChainWeightOptions): T
```

Sets the weight of the component in a chain, which is used to re-lay out components that form the chain. This attribute takes effect only when the parent container is RelativeContainer. **NOTE：**Since API version 23, dynamic configuration via [attributeModifier](#attributeModifier) is supported

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CommonMethod-chainWeight(chainWeight: ChainWeightOptions): T--><!--Device-CommonMethod-chainWeight(chainWeight: ChainWeightOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [chainWeight](#chainWeight) | [ChainWeightOptions](../arkts-apis/arkts-arkui-chainweightoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clickEffect

```TypeScript
clickEffect(value: ClickEffect | null): T
```

Sets the click feedback effect of the component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-clickEffect(value: ClickEffect | null): T--><!--Device-CommonMethod-clickEffect(value: ClickEffect | null): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ClickEffect](arkts-arkui-clickeffect-i.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clickEffect

```TypeScript
clickEffect(effect: Optional<ClickEffect | null>): T
```

Sets the click feedback effect of the component. Compared with [clickEffect](#clickEffect), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-clickEffect(effect: Optional<ClickEffect | null>): T--><!--Device-CommonMethod-clickEffect(effect: Optional<ClickEffect | null>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [Optional](arkts-arkui-optional-t.md)&lt;[ClickEffect](arkts-arkui-clickeffect-i.md) \| null & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clip

```TypeScript
clip(value: boolean): T
```

Sets whether to clip the areas of child components that extend beyond this component's bounds, that is, whether to perform clipping based on the edge contour of the parent container If this API is not used, the area of child components extending beyond the current component's bounds is not clipped by default.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-clip(value: boolean): T--><!--Device-CommonMethod-clip(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clip

```TypeScript
clip(clip: Optional<boolean>): T
```

Sets whether to clip the areas of child components that extend beyond this component's bounds, that is, whether to perform clipping based on the edge contour of the parent container If this API is not used, the area of child components extending beyond the current component's bounds is not clipped by default. Compared with [clip&lt;sup&gt;12+&lt;/sup&gt;](#clip), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-clip(clip: Optional<boolean>): T--><!--Device-CommonMethod-clip(clip: Optional<boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [clip](#clip) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clip

```TypeScript
clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T
```

Sets whether to clip this component based on the given shape.

**Since:** 7

**Deprecated since:** 12

**Substitutes:** [clipShape](#clipShape)

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T--><!--Device-CommonMethod-clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| CircleAttribute \| EllipseAttribute \| PathAttribute \| RectAttribute | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clipShape

```TypeScript
clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T
```

Clips this component according to the specified shape (which may include position information). > **NOTE：**> > Different shapes support different ranges of attributes. A path is one type of shape, along with others like > ellipses and rectangles. > > Path shapes do not support setting width and height attributes. For details about the supported attributes, see > the specific shape documentation. > > The [fill](../arkts-apis/arkts-arkui-arkui-shape-commonshapemethod-c.md#fill) attribute of shapes has no effect on the **clipShape** > API.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T--><!--Device-CommonMethod-clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-circleshape-t.md) \| [EllipseShape](arkts-arkui-ellipseshape-t.md) \| [PathShape](arkts-arkui-pathshape-t.md) \| [RectShape](arkts-arkui-rectshape-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clipShape

```TypeScript
clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T
```

Clips this component according to the specified shape (which may include position information). Compared with [clipShape&lt;sup&gt;12+&lt;/sup&gt;](#clipShape), this API supports the **undefined** type. > **NOTE：**> > Different shapes support different ranges of attributes. A path is one type of shape, along with others like > ellipses and rectangles. > > Path shapes do not support setting width and height attributes. For details about the supported attributes, see > the specific shape documentation. > > The [fill](../arkts-apis/arkts-arkui-arkui-shape-commonshapemethod-c.md#fill) attribute of shapes has no effect on the **clipShape** > API.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T--><!--Device-CommonMethod-clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shape | [Optional](arkts-arkui-optional-t.md)&lt;[CircleShape](arkts-arkui-circleshape-t.md) \| [EllipseShape](arkts-arkui-ellipseshape-t.md) \| [PathShape](arkts-arkui-pathshape-t.md) \| [RectShape](arkts-arkui-rectshape-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## colorBlend

```TypeScript
colorBlend(value: Color | string | Resource): T
```

Applies a color blend effect to the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-colorBlend(value: Color | string | Resource): T--><!--Device-CommonMethod-colorBlend(value: Color | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Color \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## colorBlend

```TypeScript
colorBlend(color: Optional<Color | string | Resource>): T
```

Applies a color blend effect to the component. Compared with [colorBlend](#colorBlend), this API supports the **undefined** type for the **color** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-colorBlend(color: Optional<Color | string | Resource>): T--><!--Device-CommonMethod-colorBlend(color: Optional<Color | string | Resource>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;Color \| string \| Resource & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## compositingFilter

```TypeScript
compositingFilter(filter: Filter): T
```

Sets the visual effect of the compositing filter. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-compositingFilter(filter: Filter): T--><!--Device-CommonMethod-compositingFilter(filter: Filter): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## constraintSize

```TypeScript
constraintSize(value: ConstraintSizeOptions): T
```

Sets the constraint size of the component, which is used to limit the size range during component layout. &lt;br&gt;Since API version 10, this API supports the calc calculation feature. **Impact of constraintSize(minWidth/maxWidth/minHeight/maxHeight) on width/height** | Default Value | Result | | ---------------------------------------- | ---------------------------------------- | | \ | width=MAX(minWidth,MIN(maxWidth,width))&lt;br&gt;height=MAX(minHeight,MIN(maxHeight,height)) | | maxWidth, maxHeight| width=MAX(minWidth,width)&lt;br&gt;height=MAX(minHeight,height) | minWidth, minHeight| width=MIN(maxWidth,width)&lt;br&gt;height=MIN(maxHeight,height) | | width, height| If minWidth < maxWidth, the layout logic of the component takes effect, and the value range of **width** is [minWidth, maxWidth]. Otherwise, width = MAX(minWidth, maxWidth).&lt;br&gt;If minHeight < maxHeight, the layout logic of the component takes effect, and the value range of **height** is [minHeight, maxHeight]. Otherwise, height = MAX (minHeight, maxHeight).| | width and maxWidth; height and maxHeight| width = minWidth&lt;br&gt;height = minHeight | | width and minWidth; and height and minHeight| The layout logic of the component takes effect, and the value of **width** cannot be greater than that of **maxWidth**.&lt;br&gt;The layout logic of the component takes effect, and the value of **height** cannot be greater than that of **maxHeight**.| | minWidth and maxWidth; minHeight and maxHeight| The width of the component is initially determined by the value of **width**, and it may be adjusted based on other layout attributes.&lt;br&gt;The height of the component is initially determined by the value of **height**, and it may be adjusted based on other layout attributes.| | width, minWidth, and maxWidth| The layout restrictions passed by the parent container are used for layout.| | height, minHeight, and maxHeight| The layout restrictions passed by the parent container are used for layout.|

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-constraintSize(value: ConstraintSizeOptions): T--><!--Device-CommonMethod-constraintSize(value: ConstraintSizeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## contrast

```TypeScript
contrast(value: number): T
```

Applies a contrast effect to the component. If this API is not used, there will be no change by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-contrast(value: number): T--><!--Device-CommonMethod-contrast(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## contrast

```TypeScript
contrast(contrast: Optional<number>): T
```

Applies a contrast effect to the component. If this API is not used, there will be no change by default. Compared to [contrast](#contrast), the **contrast** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-contrast(contrast: Optional<number>): T--><!--Device-CommonMethod-contrast(contrast: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [contrast](#contrast) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## customProperty

```TypeScript
customProperty(name: string, value: Optional<Object>): T
```

Sets a custom property for this component. In versions earlier than API 26.0.0, [custom components](../../../ui/state-management/arkts-create-custom-components.md) do not support custom properties. Since API 26.0.0, custom components support setting and reading custom properties.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-customProperty(name: string, value: Optional<Object>): T--><!--Device-CommonMethod-customProperty(name: string, value: Optional<Object>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | [Optional](arkts-arkui-optional-t.md)&lt;Object&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## defaultFocus

```TypeScript
defaultFocus(value: boolean): T
```

Specifies whether to set this component as the default focus of the current [hierarchical page](../../../ui/arkts-common-events-focus-event.md#basic-concepts). If **defaultFocus** is not set, the component will not receive initial focus on the current page. > **NOTE：**> > This setting applies to pages that support routing or modal-type container components, such as **Page**, > **NaviDestination**, **NavBar**, **PopUp**, and **Dialog**.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-defaultFocus(value: boolean): T--><!--Device-CommonMethod-defaultFocus(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## direction

```TypeScript
direction(value: Direction): T
```

Sets how elements are laid out along the main axis of the container. This attribute supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-direction(value: Direction): T--><!--Device-CommonMethod-direction(value: Direction): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Direction](#direction) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## displayPriority

```TypeScript
displayPriority(value: number): T
```

Sets the display priority for the component in the layout container. &lt;br&gt;This parameter is only effective in Row, Column, and Flex (single-line) container components.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-displayPriority(value: number): T--><!--Device-CommonMethod-displayPriority(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## doubleSided

```TypeScript
doubleSided(value: Optional<boolean>): T
```

Sets whether to component is double-sided.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-CommonMethod-doubleSided(value: Optional<boolean>): T--><!--Device-CommonMethod-doubleSided(value: Optional<boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## dragPreview

```TypeScript
dragPreview(value: CustomBuilder | DragItemInfo | string): T
```

Sets the preview image displayed during component drag operations.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-dragPreview(value: CustomBuilder | DragItemInfo | string): T--><!--Device-CommonMethod-dragPreview(value: CustomBuilder | DragItemInfo | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [DragItemInfo](arkts-arkui-dragiteminfo-i.md) \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## dragPreview

```TypeScript
dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T
```

Sets the drag preview for the component. This API specifically configures or disables the lift animation effect. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T--><!--Device-CommonMethod-dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| preview | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [DragItemInfo](arkts-arkui-dragiteminfo-i.md) \| string | Yes |
| config | [PreviewConfiguration](arkts-arkui-previewconfiguration-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## dragPreviewOptions

```TypeScript
dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T
```

Sets the preview image processing mode, badge count, and interaction behavior during drag operations. The **onItemDragStart** drag mode is not supported. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T--><!--Device-CommonMethod-dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DragPreviewOptions](arkts-arkui-dragpreviewoptions-i.md) | Yes |
| options | [DragInteractionOptions](arkts-arkui-draginteractionoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## draggable

```TypeScript
draggable(value: boolean): T
```

Sets whether the component is draggable. By default, the component is not draggable.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-draggable(value: boolean): T--><!--Device-CommonMethod-draggable(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## drawModifier

```TypeScript
drawModifier(modifier: DrawModifier | undefined): T
```

Sets the drawModifier of the current component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-drawModifier(modifier: DrawModifier | undefined): T--><!--Device-CommonMethod-drawModifier(modifier: DrawModifier | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [DrawModifier](arkts-arkui-drawmodifier-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## enableClickSoundEffect

```TypeScript
enableClickSoundEffect(enabled: boolean | undefined): T
```

Sets whether to enable the default click sound effect for a component. Whether the sound can be played depends on the sound settings of the device. For example, the sound effect is not played in mute mode.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CommonMethod-enableClickSoundEffect(enabled: boolean | undefined): T--><!--Device-CommonMethod-enableClickSoundEffect(enabled: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [enabled](#enabled) | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## enabled

```TypeScript
enabled(value: boolean): T
```

Sets whether the component responds to user interactions. If **enabled** is not set, the component responds to user interactions by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-enabled(value: boolean): T--><!--Device-CommonMethod-enabled(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## expandSafeArea

```TypeScript
expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T
```

Expands the safe area. > **NOTE：**> > - When using **expandSafeArea** to expand the drawing of a component, avoid setting fixed width and height values > (except percentages). If fixed width and height values are set (including **'auto'**), the edges for expanding the > safe area can only be **[SafeAreaEdge.TOP, SafeAreaEdge.START]**, and the size of the component remains unchanged > after safe area expansion. > > - The safe area does not restrict the layout or size of components inside, nor does it clip the components. > > - If the parent container is a scrollable container, the component does not extend after the **expandSafeArea** > attribute is set, but it can still trigger updates to the extension range of its child nodes that have > **expandSafeArea** set. > > - When **expandSafeArea()** is set without parameters, default values are applied. When **expandSafeArea([],[])** > is used with empty arrays, the setting has no effect. > > - Prerequisites for the **expandSafeArea** attribute to take effect: > 1. When **type** is set to **SafeAreaType.KEYBOARD**, the settings take effect by default. This behaves as the > component not avoiding the virtual keyboard. > 2. When **type** is set to any other value, the settings take effect only if its boundaries overlap with the > safe area. For example, if the height of the status bar is 100, the absolute position of the component on the > screen must be 0 &lt;= y <= 100 for the settings to take effect. > &gt;&lt;= 100 for the settings to take effect. &gt; > - When a component extends into a non-safe area, events in the non-safe area (such as click events) may be > intercepted by the system. Built-in components like the status bar will be given priority to respond to these > events. > > - Avoid setting the **expandSafeArea** attribute for components within scrollable containers. If you do set it, > you must apply the **expandSafeArea** attribute to all direct nodes from the current node to the scrollable > ancestor container, following the component nesting relationship. Otherwise, the **expandSafeArea** attribute may > become ineffective after scrolling. > > - The **expandSafeArea** attribute only affects the current component and does not propagate to parent or child > components. Therefore, all relevant components must be configured individually. > > - When both **expandSafeArea** and **position** attributes are set, the **position** attribute takes effect first, > followed by the **expandSafeArea** attribute. For components that do not have **position**, **offset**, or other > rendering attributes set, such as dialog boxes and sheets, the **expandSafeArea** attribute will not take effect if > their boundaries do not overlap with the non-safe area. > > - In scenarios where the **expandSafeArea** attribute is ineffective, and you need to place a component in the > safe area, you will need to manually adjust the component's coordinates.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T--><!--Device-CommonMethod-expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-na/arkts-apis/arkts-na-util-types-c.md) | Array&lt;[SafeAreaType](arkts-arkui-safeareatype-e.md)&gt; | No |
| edges | Array&lt;[SafeAreaEdge](arkts-arkui-safeareaedge-e.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## flexBasis

```TypeScript
flexBasis(value: number | string): T
```

Sets the base size of the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-flexBasis(value: number | string): T--><!--Device-CommonMethod-flexBasis(value: number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## flexGrow

```TypeScript
flexGrow(value: number): T
```

Sets the percentage of the parent container's remaining space that is allocated to the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-flexGrow(value: number): T--><!--Device-CommonMethod-flexGrow(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## flexShrink

```TypeScript
flexShrink(value: number): T
```

Sets the percentage of the parent container's shrink size that is allocated to the component. When the parent container is Column or Row, you must set the size along the main axis. When [getInspectorByKey](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-component-id.md#getinspectorbykey9) is used to obtain the **flexShrink** attribute, if the node does not have **flexShrink** set, the default value of **1** is returned by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-flexShrink(value: number): T--><!--Device-CommonMethod-flexShrink(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusBox

```TypeScript
focusBox(style: FocusBoxStyle): T
```

Sets the system focus box style for the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-focusBox(style: FocusBoxStyle): T--><!--Device-CommonMethod-focusBox(style: FocusBoxStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [FocusBoxStyle](../arkts-apis/arkts-arkui-focusboxstyle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusOnTouch

```TypeScript
focusOnTouch(value: boolean): T
```

Sets whether the component is focusable on touch. If **focusOnTouch** is not set, the component is not focusable on touch by default.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-focusOnTouch(value: boolean): T--><!--Device-CommonMethod-focusOnTouch(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusScopeId

```TypeScript
focusScopeId(id: string, isGroup?: boolean): T
```

Set container as a focus group with a specific identifier.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean): T--><!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |
| isGroup | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusScopeId

```TypeScript
focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T
```

Set container as a focus group with a specific identifier.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T--><!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |
| isGroup | boolean | No |
| arrowStepOut | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusScopePriority

```TypeScript
focusScopePriority(scopeId: string, priority?: FocusPriority): T
```

Set the focus priority of component in a specific focus scope.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-focusScopePriority(scopeId: string, priority?: FocusPriority): T--><!--Device-CommonMethod-focusScopePriority(scopeId: string, priority?: FocusPriority): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scopeId | string | Yes |
| priority | [FocusPriority](../arkts-apis/arkts-arkui-focuspriority-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## focusable

```TypeScript
focusable(value: boolean): T
```

Sets whether the component is focusable.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-focusable(value: boolean): T--><!--Device-CommonMethod-focusable(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T
```

Applies a foreground blur style to the component. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 18.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T
```

Applies a foreground blur style to the component. Compared to [foregroundBlurStyle](#foregroundBlurStyle), the **style** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[BlurStyle](arkts-arkui-blurstyle-e.md)&gt; | Yes |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T
```

Foreground blur style. blurStyle:Blur style type. sysOptions: system adaptive options.

**Since:** 19

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[BlurStyle](arkts-arkui-blurstyle-e.md)&gt; | Yes |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | No |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundColor

```TypeScript
foregroundColor(value: ResourceColor | ColoringStrategy): T
```

Sets the foreground color of the component. Components without explicit foreground color settings inherit from their parent components by default.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-foregroundColor(value: ResourceColor | ColoringStrategy): T--><!--Device-CommonMethod-foregroundColor(value: ResourceColor | ColoringStrategy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColoringStrategy](../arkts-apis/arkts-arkui-coloringstrategy-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundColor

```TypeScript
foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T
```

Sets the foreground color of the component. Components without explicit foreground color settings inherit from their parent components by default. Compared to [foregroundColor](#foregroundColor), the **color** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T--><!--Device-CommonMethod-foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColoringStrategy](../arkts-apis/arkts-arkui-coloringstrategy-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundEffect

```TypeScript
foregroundEffect(options: ForegroundEffectOptions): T
```

Sets the foreground effect of the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-foregroundEffect(options: ForegroundEffectOptions): T--><!--Device-CommonMethod-foregroundEffect(options: ForegroundEffectOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ForegroundEffectOptions](arkts-arkui-foregroundeffectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## foregroundFilter

```TypeScript
foregroundFilter(filter: Filter): T
```

Sets the visual effect of the foreground (content) filter. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-foregroundFilter(filter: Filter): T--><!--Device-CommonMethod-foregroundFilter(filter: Filter): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## freeze

```TypeScript
freeze(value: boolean): T
```

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-freeze(value: boolean): T--><!--Device-CommonMethod-freeze(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## freeze

```TypeScript
freeze(freeze: Optional<boolean>): T
```

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. Compared with [freeze](#freeze), this API supports the **undefined** type for the **freeze** parameter. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-freeze(freeze: Optional<boolean>): T--><!--Device-CommonMethod-freeze(freeze: Optional<boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [freeze](#freeze) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## geometryTransition

```TypeScript
geometryTransition(id: string): T
```

Implements an implicit shared element transition.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-geometryTransition(id: string): T--><!--Device-CommonMethod-geometryTransition(id: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## geometryTransition

```TypeScript
geometryTransition(id: string, options?: GeometryTransitionOptions): T
```

Implements an implicit shared element transition.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-geometryTransition(id: string, options?: GeometryTransitionOptions): T--><!--Device-CommonMethod-geometryTransition(id: string, options?: GeometryTransitionOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |
| options | [GeometryTransitionOptions](arkts-arkui-geometrytransitionoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## gesture

```TypeScript
gesture(gesture: GestureType, mask?: GestureMask): T
```

Gesture to bind. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-gesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-gesture(gesture: GestureType, mask?: GestureMask): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../arkts-apis/arkts-arkui-gesturecontrol-gesturetype-e.md) | Yes |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## gestureModifier

```TypeScript
gestureModifier(modifier: GestureModifier): T
```

Creates a gesture modifier. > **NOTE：**> > **gestureModifier** does not support custom components. > > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-gestureModifier(modifier: GestureModifier): T--><!--Device-CommonMethod-gestureModifier(modifier: GestureModifier): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [GestureModifier](arkts-arkui-gesturemodifier-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## grayscale

```TypeScript
grayscale(value: number): T
```

Applies a grayscale effect to the component. The grayscale rendering of the upper layer will overlay that of lower- layer child components. If this API is not used, there will be no change by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-grayscale(value: number): T--><!--Device-CommonMethod-grayscale(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## grayscale

```TypeScript
grayscale(grayscale: Optional<number>): T
```

Applies a grayscale effect to the component. The grayscale rendering of the upper layer will overlay that of lower- layer child components. If this API is not used, there will be no change by default. Compared to [grayscale](#grayscale), the **grayscale** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-grayscale(grayscale: Optional<number>): T--><!--Device-CommonMethod-grayscale(grayscale: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [grayscale](#grayscale) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## gridOffset

```TypeScript
gridOffset(value: number): T
```

The default offset column number indicates the number of offset columns of the current component in the start direction of the parent component when the useSizeType attribute does not set the offset of the corresponding dimension. That is, the current component is located in the nth column.

**Since:** 11

**Deprecated since:** 14

**Substitutes:** grid_col/GridColInterface and grid_row/GridRowInterface

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-gridOffset(value: number): T--><!--Device-CommonMethod-gridOffset(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## gridSpan

```TypeScript
gridSpan(value: number): T
```

Default number of occupied columns, indicating the number of occupied grid columns when the number of columns (span) of the corresponding size is not set in the useSizeType attribute.

**Since:** 11

**Deprecated since:** 14

**Substitutes:** grid_col/GridColInterface and grid_row/GridRowInterface

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-gridSpan(value: number): T--><!--Device-CommonMethod-gridSpan(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## groupDefaultFocus

```TypeScript
groupDefaultFocus(value: boolean): T
```

Specifies whether to set the component as the default focus of the container. If **groupDefaultFocus** is not set, the component will not receive focus by default when its container is focused.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-groupDefaultFocus(value: boolean): T--><!--Device-CommonMethod-groupDefaultFocus(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## height

```TypeScript
height(value: Length): T
```

Sets the height of the component. By default, the height required to fully hold the component content is used. If a component is higher than its parent, it will overflow. &lt;br&gt;Since API version 10, this API supports the calc calculation feature.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-height(value: Length): T--><!--Device-CommonMethod-height(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## height

```TypeScript
height(heightValue: Length | LayoutPolicy): T
```

Sets the height of the component or its vertical layout policy. By default, the component uses the height required for its content. If a component is higher than its parent, it will overflow.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-CommonMethod-height(heightValue: Length | LayoutPolicy): T--><!--Device-CommonMethod-height(heightValue: Length | LayoutPolicy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| heightValue | [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LayoutPolicy](arkts-arkui-layoutpolicy-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## hitTestBehavior

```TypeScript
hitTestBehavior(value: HitTestMode): T
```

Sets the hit test mode for a component. If **hitTestBehavior** is not set, the component defaults to **HitTestMode.Default**.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-CommonMethod-hitTestBehavior(value: HitTestMode): T--><!--Device-CommonMethod-hitTestBehavior(value: HitTestMode): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [HitTestMode](../arkts-apis/arkts-arkui-hittestmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## hoverEffect

```TypeScript
hoverEffect(value: HoverEffect): T
```

Sets the hover effect for the component. When no hover effect is specified, the component uses the default **HoverEffect.Auto** effect. For components with hover effects applied, the hover effect is hidden when the mouse hovers and presses down on the component, and restored when the mouse button is released.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-hoverEffect(value: HoverEffect): T--><!--Device-CommonMethod-hoverEffect(value: HoverEffect): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [HoverEffect](../arkts-apis/arkts-arkui-hovereffect-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## hueRotate

```TypeScript
hueRotate(value: number | string): T
```

Rotates the hue of the component. If this API is not used, there will be no change by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-hueRotate(value: number | string): T--><!--Device-CommonMethod-hueRotate(value: number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## hueRotate

```TypeScript
hueRotate(rotation: Optional<number | string>): T
```

Rotates the hue of the component. If this API is not used, there will be no change by default. Compared to [hueRotate](#hueRotate), the **rotation** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-hueRotate(rotation: Optional<number | string>): T--><!--Device-CommonMethod-hueRotate(rotation: Optional<number | string>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rotation | [Optional](arkts-arkui-optional-t.md)&lt;number \| string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## id

```TypeScript
id(value: string): T
```

Id. User can set an id to the component to identify it.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-id(value: string): T--><!--Device-CommonMethod-id(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T
```

Ignores the safe area for component layout. > **NOTE：**> > - For a component that ignores layout safe area edges: If its width or height is set to > [LayoutPolicy.matchParent](arkts-arkui-layoutpolicy-c.md#matchParent), both its size and position > will change; otherwise, only its position will change. > > - Based on the **safeAreaPadding** accumulation feature, a component can expand its safe area edges to all > detectable continuous safe areas. > > - When child elements of scrollable components ignore layout safe area edges, the safe areas of the scrollable > component itself and its parent components are not considered in the scrolling direction. Scrollable components > include **List**, **ArcListItem**, **Grid**, **WaterFlow**, **Swiper**, and **Tabs**. > > - When both the layout safe area ignore attribute (**.ignoreLayoutSafeArea**) and the rendering safe area ignore > attribute (**.expandSafeArea**) are set: **.ignoreLayoutSafeArea** takes effect first, and **.expandSafeArea** > takes effect on the basis of the former.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T--><!--Device-CommonMethod-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-na/arkts-apis/arkts-na-util-types-c.md) | Array&lt;[LayoutSafeAreaType](arkts-arkui-layoutsafeareatype-e.md)&gt; | No |
| edges | Array&lt;[LayoutSafeAreaEdge](arkts-arkui-layoutsafeareaedge-e.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## inspectorLabel

```TypeScript
inspectorLabel(label: string | undefined): T
```

Set the component's inspector label which only display on DevEco Studio.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-inspectorLabel(label: string | undefined): T--><!--Device-CommonMethod-inspectorLabel(label: string | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| label | string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## invert

```TypeScript
invert(value: number | InvertOptions): T
```

Inverts an image.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-invert(value: number | InvertOptions): T--><!--Device-CommonMethod-invert(value: number | InvertOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [InvertOptions](arkts-arkui-invertoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## invert

```TypeScript
invert(options: Optional<number | InvertOptions>): T
```

Inverts an image. Compared with [invert](#invert), this API supports the **undefined** type for the **options** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-invert(options: Optional<number | InvertOptions>): T--><!--Device-CommonMethod-invert(options: Optional<number | InvertOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;number \| [InvertOptions](arkts-arkui-invertoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## key

```TypeScript
key(value: string): T
```

Key. User can set an key to the component to identify it.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CommonMethod-key(value: string): T--><!--Device-CommonMethod-key(value: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## keyboardShortcut

```TypeScript
keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T
```

Sets a keyboard shortcut for the component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T--><!--Device-CommonMethod-keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [FunctionKey](../../apis-input-kit/arkts-apis/arkts-input-inputdevice-functionkey-e.md) | Yes |
| keys | Array&lt;[ModifierKey](../arkts-apis/arkts-arkui-modifierkey-e.md)&gt; | Yes |
| action | () = & gt; void | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## layoutGravity

```TypeScript
layoutGravity(alignment: LocalizedAlignment): T
```

Sets the alignment rule for child components in the **Stack** container. This API only takes effect when the parent container is **Stack**. When used with the align attribute, **layoutGravity** takes precedence. This attribute supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CommonMethod-layoutGravity(alignment: LocalizedAlignment): T--><!--Device-CommonMethod-layoutGravity(alignment: LocalizedAlignment): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignment | [LocalizedAlignment](../arkts-apis/arkts-arkui-localizedalignment-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## layoutWeight

```TypeScript
layoutWeight(value: number | string): T
```

Sets the weight of the component during layout. A component with this attribute is allocated space along the main axis of its parent container (Row, Column, or Flex based on its specified weight.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-layoutWeight(value: number | string): T--><!--Device-CommonMethod-layoutWeight(value: number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## lightUpEffect

```TypeScript
lightUpEffect(value: number): T
```

Applies a light up effect to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-lightUpEffect(value: number): T--><!--Device-CommonMethod-lightUpEffect(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## lightUpEffect

```TypeScript
lightUpEffect(degree: Optional<number>): T
```

Applies a light up effect to the component. Compared to [lightUpEffect&lt;sup&gt;12+&lt;/sup&gt;](#lightUpEffect), the **degree** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-lightUpEffect(degree: Optional<number>): T--><!--Device-CommonMethod-lightUpEffect(degree: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degree | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## linearGradient

```TypeScript
linearGradient(value: LinearGradientOptions): T
```

Creates a linear gradient.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-linearGradient(value: LinearGradientOptions): T--><!--Device-CommonMethod-linearGradient(value: LinearGradientOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [LinearGradientOptions](arkts-arkui-lineargradientoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## linearGradient

```TypeScript
linearGradient(options: Optional<LinearGradientOptions>): T
```

Creates a linear gradient. Compared to [linearGradient](#linearGradient), this API supports the **undefined** type for the **options** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-linearGradient(options: Optional<LinearGradientOptions>): T--><!--Device-CommonMethod-linearGradient(options: Optional<LinearGradientOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[LinearGradientOptions](arkts-arkui-lineargradientoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## linearGradientBlur

```TypeScript
linearGradientBlur(value: number, options: LinearGradientBlurOptions): T
```

Applies a linear gradient foreground blur effect to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-linearGradientBlur(value: number, options: LinearGradientBlurOptions): T--><!--Device-CommonMethod-linearGradientBlur(value: number, options: LinearGradientBlurOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| options | [LinearGradientBlurOptions](arkts-arkui-lineargradientbluroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## linearGradientBlur

```TypeScript
linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T
```

Applies a linear gradient foreground blur effect to the component. Compared with [linearGradientBlur&lt;sup&gt;12+&lt;/sup&gt;](#linearGradientBlur), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T--><!--Device-CommonMethod-linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [blurRadius](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textshadow-i.md) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[LinearGradientBlurOptions](arkts-arkui-lineargradientbluroptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## margin

```TypeScript
margin(value: Margin | Length | LocalizedMargin): T
```

Sets the margin of the component. The margin is considered as a part of the component's size during position calculation, thereby affecting the component's placement. &lt;br&gt;Since API version 10, this API supports the calc calculation feature.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-margin(value: Margin | Length | LocalizedMargin): T--><!--Device-CommonMethod-margin(value: Margin | Length | LocalizedMargin): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Margin](../arkts-apis/arkts-arkui-margin-t.md) \| [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LocalizedMargin](../arkts-apis/arkts-arkui-localizedmargin-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## markAnchor

```TypeScript
markAnchor(value: Position | LocalizedPosition): T
```

Sets the anchor for element positioning. This attribute supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-markAnchor(value: Position | LocalizedPosition): T--><!--Device-CommonMethod-markAnchor(value: Position | LocalizedPosition): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Position \| [LocalizedPosition](../arkts-apis/arkts-arkui-localizedposition-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## mask

```TypeScript
mask(value: ProgressMask): T
```

Adds a mask to the component to indicate the progress.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-mask(value: ProgressMask): T--><!--Device-CommonMethod-mask(value: ProgressMask): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ProgressMask](arkts-arkui-progressmask-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## mask

```TypeScript
mask(mask: Optional<ProgressMask>): T
```

Adds a mask to the component to indicate the progress. Compared with [mask&lt;sup&gt;12+&lt;/sup&gt;](#mask), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-mask(mask: Optional<ProgressMask>): T--><!--Device-CommonMethod-mask(mask: Optional<ProgressMask>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [mask](#mask) | [Optional](arkts-arkui-optional-t.md)&lt;[ProgressMask](arkts-arkui-progressmask-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## mask

```TypeScript
mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T
```

Adds a mask of the specified shape to the component.

**Since:** 7

**Deprecated since:** 12

**Substitutes:** [maskShape](#maskShape)

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T--><!--Device-CommonMethod-mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | CircleAttribute \| EllipseAttribute \| PathAttribute \| RectAttribute \| [ProgressMask](arkts-arkui-progressmask-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## maskShape

```TypeScript
maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T
```

Adds a mask of the specified shape to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T--><!--Device-CommonMethod-maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-circleshape-t.md) \| [EllipseShape](arkts-arkui-ellipseshape-t.md) \| [PathShape](arkts-arkui-pathshape-t.md) \| [RectShape](arkts-arkui-rectshape-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## maskShape

```TypeScript
maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T
```

Adds a mask of the specified shape to the component. Compared with [maskShape&lt;sup&gt;12+&lt;/sup&gt;](#maskShape), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T--><!--Device-CommonMethod-maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shape | [Optional](arkts-arkui-optional-t.md)&lt;[CircleShape](arkts-arkui-circleshape-t.md) \| [EllipseShape](arkts-arkui-ellipseshape-t.md) \| [PathShape](arkts-arkui-pathshape-t.md) \| [RectShape](arkts-arkui-rectshape-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## materialFilter

```TypeScript
materialFilter(filter: Filter | undefined): T
```

Sets the visual effect of the material filter. The effects it contains are rendered at a level before the shadow.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CommonMethod-materialFilter(filter: Filter | undefined): T--><!--Device-CommonMethod-materialFilter(filter: Filter | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## monopolizeEvents

```TypeScript
monopolizeEvents(monopolize: boolean): T
```

Sets whether the component exclusively handles events.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-monopolizeEvents(monopolize: boolean): T--><!--Device-CommonMethod-monopolizeEvents(monopolize: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| monopolize | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## motionBlur

```TypeScript
motionBlur(value: MotionBlurOptions):T
```

Applies a motion blur effect to the component being scaled or moved. > **NOTE：**> > - Do not use this API in intra-component transitions, shared element transitions, implicit element transitions, > or particle animations. Doing so may cause unexpected results. > > - The **radius** parameter of **motionBlur** must be set to **0** for the initial state. Otherwise, there may be > unexpected results during a cold start. > > - This API must be used together with the **onFinish** parameter of **AnimateParam**. Its **radius** parameter > must be set to **0** when the animation ends; otherwise, there may be unexpected results. > > - When using this API, do not frequently change the blur radius of the same component; otherwise, there may be > unexpected results. For example, if you frequently click the image in the example, the blur effect may not work > sometimes. > > - To avoid unexpected results, make sure the coordinates of the motion blur anchor point are the same as those of > the animation scaling anchor point. > > - To avoid unexpected results, set the blur radius to a value less than 1.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-motionBlur(value: MotionBlurOptions):T--><!--Device-CommonMethod-motionBlur(value: MotionBlurOptions):T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [MotionBlurOptions](arkts-arkui-motionbluroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## motionBlur

```TypeScript
motionBlur(motionBlur: Optional<MotionBlurOptions>): T
```

Applies a motion blur effect to the component being scaled or moved. Compared with [motionBlur](#motionBlur), this API supports the **undefined** type for the **motionBlur** parameter. 1. Do not use this API in intra-component transitions, shared element transitions, implicit element transitions, or particle animations. Doing so may cause unexpected results. 2. The **radius** parameter of **motionBlur** must be set to **0** for the initial state. Otherwise, there may be unexpected results during a cold start. 3. This API must be used together with the **onFinish** parameter of **AnimateParam**. Its **radius** parameter must be set to **0** when the animation ends; otherwise, there may be unexpected results. 4. When using this API, do not frequently change the blur radius of the same component; otherwise, there may be unexpected results. For example, if you frequently click the image in the example, the blur effect may not work sometimes. 5. To avoid unexpected results, make sure the coordinates of the motion blur anchor point are the same as those of the animation scaling anchor point. 6. To avoid unexpected results, set the blur radius to a value less than 1.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-motionBlur(motionBlur: Optional<MotionBlurOptions>): T--><!--Device-CommonMethod-motionBlur(motionBlur: Optional<MotionBlurOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [motionBlur](#motionBlur) | [Optional](arkts-arkui-optional-t.md)&lt;[MotionBlurOptions](arkts-arkui-motionbluroptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## motionPath

```TypeScript
motionPath(value: MotionPathOptions): T
```

Sets a path animation for the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-motionPath(value: MotionPathOptions): T--><!--Device-CommonMethod-motionPath(value: MotionPathOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [MotionPathOptions](arkts-arkui-motionpathoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## mouseResponseRegion

```TypeScript
mouseResponseRegion(value: Array<Rectangle> | Rectangle): T
```

Sets one or more mouse response regions.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-mouseResponseRegion(value: Array<Rectangle> | Rectangle): T--><!--Device-CommonMethod-mouseResponseRegion(value: Array<Rectangle> | Rectangle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[Rectangle](arkts-arkui-rectangle-i.md)&gt; \| [Rectangle](arkts-arkui-rectangle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## nextFocus

```TypeScript
nextFocus(nextStep: Optional<FocusMovement>): T
```

Set nextFocus.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-nextFocus(nextStep: Optional<FocusMovement>): T--><!--Device-CommonMethod-nextFocus(nextStep: Optional<FocusMovement>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nextStep | [Optional](arkts-arkui-optional-t.md)&lt;[FocusMovement](arkts-arkui-focusmovement-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## obscured

```TypeScript
obscured(reasons: Array<ObscuredReasons>): T
```

Sets how the component content is obscured.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-obscured(reasons: Array<ObscuredReasons>): T--><!--Device-CommonMethod-obscured(reasons: Array<ObscuredReasons>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reasons | Array&lt;[ObscuredReasons](../arkts-apis/arkts-arkui-obscuredreasons-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## offset

```TypeScript
offset(value: Position | Edges | LocalizedEdges): T
```

Sets the offset of the component relative to its original position. When **offset** is used in combination with the position attribute, the **position** attribute takes precedence and the configured offset will not be applied. This attribute supports dynamic configuration via [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-offset(value: Position | Edges | LocalizedEdges): T--><!--Device-CommonMethod-offset(value: Position | Edges | LocalizedEdges): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Position \| Edges \| [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAccessibilityActionIntercept

```TypeScript
onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T
```

Register accessibility action intercept callback, when accessibility action is to be executed,the callback will be executed

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CommonMethod-onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T--><!--Device-CommonMethod-onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AccessibilityActionInterceptCallback](arkts-arkui-accessibilityactioninterceptcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAccessibilityFocus

```TypeScript
onAccessibilityFocus(callback: AccessibilityFocusCallback): T
```

Register accessibility focus callback,when the component is focused or out of focus,the callback will be executed

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-onAccessibilityFocus(callback: AccessibilityFocusCallback): T--><!--Device-CommonMethod-onAccessibilityFocus(callback: AccessibilityFocusCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AccessibilityFocusCallback](arkts-arkui-accessibilityfocuscallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAccessibilityHover

```TypeScript
onAccessibilityHover(callback: AccessibilityCallback): T
```

Trigger a accessibility hover event.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onAccessibilityHover(callback: AccessibilityCallback): T--><!--Device-CommonMethod-onAccessibilityHover(callback: AccessibilityCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAccessibilityHoverTransparent

```TypeScript
onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T
```

prompt for current component and descendants unable to handle accessibility hover event

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T--><!--Device-CommonMethod-onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAppear

```TypeScript
onAppear(event: () => void): T
```

Triggered when this component appears. > **NOTE：**> > This callback may be called after the component layout and rendering process.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-onAppear(event: () => void): T--><!--Device-CommonMethod-onAppear(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAreaChange

```TypeScript
onAreaChange(event: (oldValue: Area, newValue: Area) => void): T
```

Triggered when the component area changes in size or position due to layout updates. This event is not triggered for render attribute changes caused by re-rendering, such as changes to [translate](#translate), [offset](#offset), [markAnchor](#markAnchor), [scale](#scale), or [transform](#transform). In addition, if the component position is altered due to drawing changes, for example, through [bindSheet](#bindSheet), this event is also not triggered. > **NOTE：**> > When a component is bound to both the **onAreaChange** event and the [position](#position) > attribute, the **onAreaChange** event responds to changes in the **position** attribute of type > Position, but does not respond to changes in the **position** attribute of type > Edges or [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md#LocalizedEdges).

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onAreaChange(event: (oldValue: Area, newValue: Area) => void): T--><!--Device-CommonMethod-onAreaChange(event: (oldValue: Area, newValue: Area) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (oldValue: Area, newValue: Area) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAreaChange

```TypeScript
onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T
```

Triggered when the component area changes. The interval at which the callback is triggered can be set using expectedUpdateInterval in [AreaChangeOptions](arkts-arkui-areachangeoptions-i.md#AreaChangeOptions). This event is triggered only in response to changes in component size or position caused by layout updates.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T--><!--Device-CommonMethod-onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [AreaChangeCallback](arkts-arkui-areachangecallback-t.md) | Yes |
| options | [AreaChangeOptions](arkts-arkui-areachangeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAttach

```TypeScript
onAttach(callback: Callback<void>): T
```

Triggered when this component is mounted to the component tree. Due to the following limitations, it is recommended that you use [onAppear](#onAppear) instead of this callback. > **NOTE：**> > - This callback is triggered before the component layout and rendering process. > > - Modifying the component tree within the callback is prohibited, including initiating animations or altering the > component structure through conditional statements like **if-else**.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onAttach(callback: Callback<void>): T--><!--Device-CommonMethod-onAttach(callback: Callback<void>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onAxisEvent

```TypeScript
onAxisEvent(event: Callback<AxisEvent>): T
```

Triggered by mouse wheel scrolling, a two-finger sliding gesture, or a pinch gesture on the touchpad.

**Since:** 17

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-CommonMethod-onAxisEvent(event: Callback<AxisEvent>): T--><!--Device-CommonMethod-onAxisEvent(event: Callback<AxisEvent>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[AxisEvent](arkts-arkui-axisevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onBlur

```TypeScript
onBlur(event: () => void): T
```

Triggered when the current component loses focus.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onBlur(event: () => void): T--><!--Device-CommonMethod-onBlur(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onChildTouchTest

```TypeScript
onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T
```

Allows the current component to customize the hit test and control child component behavior during the test by setting a callback. > **NOTE：**> > - The array of child node information only includes information about named nodes, that is, nodes for which the > **id** attribute is explicitly set. > > - This API can be called in [attributeModifier](#attributeModifier) since API version 20.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T--><!--Device-CommonMethod-onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (value: Array&lt;[TouchTestInfo](arkts-arkui-touchtestinfo-c.md)&gt;) =&gt; TouchResult | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onClick

```TypeScript
onClick(event: (event: ClickEvent) => void): T
```

Called when a click event occurs. When triggered by keyboard or gamepad input, the event's **SourceTool** is **Unknown**, and [SourceType](arkts-arkui-sourcetype-e.md#SourceType) is **KEY** or **JOYSTICK**. > **NOTE：**> > Since API version 9, the following constraints apply when this API is used in service widgets: > > 1. Click events will not be triggered if the finger is pressed for more than 800 ms. > > 2. Click events will not be triggered if the finger moves more than 20 px after pressing down.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-onClick(event: (event: ClickEvent) => void): T--><!--Device-CommonMethod-onClick(event: (event: ClickEvent) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: ClickEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onClick

```TypeScript
onClick(event: Callback<ClickEvent>, distanceThreshold: number): T
```

Called when a click event occurs. When triggered by keyboard or gamepad input, the event's [SourceTool](arkts-arkui-sourcetool-e.md#SourceTool) is **Unknown**, and [SourceType](arkts-arkui-sourcetype-e.md#SourceType) is **KEY** or **JOYSTICK**. Compared with the original **onClick** API, this API has the **distanceThreshold** parameter that specifies the finger movement threshold for click events. If the finger's movement exceeds the set threshold, the gesture recognition will fail. The click gesture recognition will fail if finger movement exceeds this threshold. For scenarios where there is no restriction on the finger movement distance during a click, the original API is preferred. To limit finger movement range during a click, use this new API. > **NOTE：**> > - Since API version 12, the following constraints apply when this API is used in service widgets: > > 1. Click events will not be triggered if the finger is pressed for more than 800 ms. > > 2. Click events will not be triggered if the finger moves more than 20 px after pressing down. > > - This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-onClick(event: Callback<ClickEvent>, distanceThreshold: number): T--><!--Device-CommonMethod-onClick(event: Callback<ClickEvent>, distanceThreshold: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[ClickEvent](arkts-arkui-clickevent-i.md)&gt; | Yes |
| distanceThreshold | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDetach

```TypeScript
onDetach(callback: Callback<void>): T
```

Triggered when this component is unmounted from the component tree. You are advised to use [onDisAppear](#onDisAppear) instead.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onDetach(callback: Callback<void>): T--><!--Device-CommonMethod-onDetach(callback: Callback<void>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDigitalCrown

```TypeScript
onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T
```

Called when the crown is rotated while the component has focus. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T--><!--Device-CommonMethod-onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;[Callback](arkts-arkui-callback-i.md)&lt;[CrownEvent](arkts-arkui-crownevent-i.md)&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDisAppear

```TypeScript
onDisAppear(event: () => void): T
```

Triggered when this component disappears.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-onDisAppear(event: () => void): T--><!--Device-CommonMethod-onDisAppear(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragEnd

```TypeScript
onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T
```

Triggered when the dragging of the component bound to the event ends.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragEnter

```TypeScript
onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T
```

Triggered when a dragged item enters a valid drop target. This event takes effect only when a listener for the onDrop event is enabled.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragLeave

```TypeScript
onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T
```

Triggered when a dragged item leaves a valid drop target. This event takes effect only when a listener for the onDrop event is enabled.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragMove

```TypeScript
onDragMove(event: (event: DragEvent, extraParams?: string) => void): T
```

Triggered when a dragged item moves in a valid drop target. This event takes effect only when a listener for the onDrop event is enabled.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDragMove(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragMove(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragSpringLoading

```TypeScript
onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T
```

The component bound to this event can be used as a drag-response target with hover detection capability. When the dragged object hovers over the target, the callback is triggered. Only one target can become the responder at any time, and child components always have higher response priority. For details about the hover detection triggering mechanism and usage, see [Spring Loading (Hover Detection) Support](../../../ui/arkts-common-events-drag-event.md#spring-loading-hover-detection-support).

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T--><!--Device-CommonMethod-onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;[SpringLoadingContext](arkts-arkui-springloadingcontext-t.md)&gt; \| null | Yes |
| configuration | [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDragStart

```TypeScript
onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T
```

In a gesture-based drag scenario, this callback is triggered when a user long-presses a draggable component for more than 500 ms and then moves the finger more than 10 vp. In a mouse-drag scenario, it is triggered when the left mouse button is pressed on a draggable component and moved more than 1 vp. For components that provide drag and drop capabilities by default, a custom **onDragStart** event, if set, is executed and: - If a custom drag preview is returned, it is used in place of the default drag preview. - If drag data is set, it is used in place of the default drag data. The custom drag preview is not supported for dragging selected text in the following components: Text, Search, TextInput, TextArea, RichEditor When **onDragStart** is used with menu preview or any component that provides default drag and drop capabilities, custom content on menu items and the preview cannot be dragged. > **NOTE：**> > This API can be called in [attributeModifier](#attributeModifier) since API version 13.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T--><!--Device-CommonMethod-onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; CustomBuilder \ | [DragItemInfo](arkts-arkui-dragiteminfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDrop

```TypeScript
onDrop(event: (event: DragEvent, extraParams?: string) => void): T
```

A component bound with this event can serve as a drop target. This callback is triggered when the drag-and-drop action stops within the bounds of this component If **event.setResult()** is not explicitly called in the **onDrop** callback to set the drag-and-drop result, then: For supported components, the result is determined based on the actual data processed; for other components, the system considers the data as successfully received.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onDrop(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDrop(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDrop

```TypeScript
onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T
```

Triggered when a dragged item is dropped on a valid drop target. If you do not explicitly call event. [setResult](arkts-arkui-dragevent-i.md#setResult)() in **onDrop** to set the result of the drag reception, the system handles it as follows: - If the component being dragged is one that supports drop actions by default, the system's actual data processing result is used. - For other components, the system assumes that the data is received successfully.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T--><!--Device-CommonMethod-onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventCallback | [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) | Yes |
| dropOptions | [DropOptions](arkts-arkui-dropoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onFocus

```TypeScript
onFocus(event: () => void): T
```

Triggered when the current component obtains focus.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onFocus(event: () => void): T--><!--Device-CommonMethod-onFocus(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onFocusAxisEvent

```TypeScript
onFocusAxisEvent(event: Callback<FocusAxisEvent>): T
```

Binds a focus axis event callback to the component. Triggered when any operation is performed with the game controller's directional pad or joystick on the bound component.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-onFocusAxisEvent(event: Callback<FocusAxisEvent>): T--><!--Device-CommonMethod-onFocusAxisEvent(event: Callback<FocusAxisEvent>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[FocusAxisEvent](arkts-arkui-focusaxisevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onGestureCollectIntercept

```TypeScript
onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T
```

Triggered after events and gestures on the current node and higher-priority nodes are collected. This callback can be used to intervene in the collection results of events and gestures. This callback uses an asynchronous callback.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T--><!--Device-CommonMethod-onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onGestureJudgeBegin

```TypeScript
onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T
```

Binds a custom gesture determination callback to the component. When the gesture is about to succeed, the user- defined callback is triggered to obtain the result.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T--><!--Device-CommonMethod-onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (gestureInfo: GestureInfo, event: BaseGestureEvent) = & gt; GestureJudgeResult | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onGestureRecognizerJudgeBegin

```TypeScript
onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T
```

Binds a custom gesture recognizer judgment callback to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T--><!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onGestureRecognizerJudgeBegin

```TypeScript
onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T
```

Binds a custom gesture recognizer judgment callback to the component. The **exposeInnerGesture** parameter indicates whether to expose gestures from built-in components within ArkUI system composite components to developers. When this parameter is set to **true**, these internal gestures are exposed. For scenarios where exposure of internal gestures is not required, use the original [onGestureRecognizerJudgeBegin](#onGestureRecognizerJudgeBegin) API. Use this API with **exposeInnerGesture** set to **true** only when internal gesture exposure is necessary.

**Since:** 13

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T--><!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | Yes |
| exposeInnerGesture | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onHover

```TypeScript
onHover(event: (isHover: boolean, event: HoverEvent) => void): T
```

Triggered when the mouse pointer or stylus enters or leaves the component.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onHover(event: (isHover: boolean, event: HoverEvent) => void): T--><!--Device-CommonMethod-onHover(event: (isHover: boolean, event: HoverEvent) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (isHover: boolean, event: HoverEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onHoverMove

```TypeScript
onHoverMove(event: Callback<HoverEvent>): T
```

Triggered when a stylus hovers over the component.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-onHoverMove(event: Callback<HoverEvent>): T--><!--Device-CommonMethod-onHoverMove(event: Callback<HoverEvent>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[HoverEvent](arkts-arkui-hoverevent-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onKeyEvent

```TypeScript
onKeyEvent(event: (event: KeyEvent) => void): T
```

Triggered when a key event occurs.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onKeyEvent(event: (event: KeyEvent) => void): T--><!--Device-CommonMethod-onKeyEvent(event: (event: KeyEvent) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: KeyEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onKeyEvent

```TypeScript
onKeyEvent(event: Callback<KeyEvent, boolean>): T
```

Triggered when a key operation is performed on the bound component after it obtains focus. If the callback returns **true**, the key event is considered handled.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-onKeyEvent(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyEvent(event: Callback<KeyEvent, boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[KeyEvent](arkts-arkui-keyevent-i.md), boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onKeyEventDispatch

```TypeScript
onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T
```

Triggered when the bound component receives a key event. The key event will not be dispatched to its child components. Only existing key events can be intercepted; creating new **KeyEvent** objects for dispatch is not supported. If the callback returns **true**, the key event is marked as consumed and will not [bubble up](../../../ui/arkts-interaction-basic-principles.md#event-bubbling) to parent components.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-CommonMethod-onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[KeyEvent](arkts-arkui-keyevent-i.md), boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onKeyPreIme

```TypeScript
onKeyPreIme(event: Callback<KeyEvent, boolean>): T
```

Triggered before other callbacks when a key operation is performed on the bound component after it obtains focus. If the return value of this callback is **true**, the key event is considered consumed, and subsequent event callbacks (**keyboardShortcut**, input method events, **onKeyEventDispatch**, and **onKeyEvent**) will be intercepted and no longer triggered.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onKeyPreIme(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyPreIme(event: Callback<KeyEvent, boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-i.md)&lt;[KeyEvent](arkts-arkui-keyevent-i.md), boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onMouse

```TypeScript
onMouse(event: (event: MouseEvent) => void): T
```

Triggered when the component is clicked by a mouse button or the mouse pointer moves on the component.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onMouse(event: (event: MouseEvent) => void): T--><!--Device-CommonMethod-onMouse(event: (event: MouseEvent) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: MouseEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onNeedSoftkeyboard

```TypeScript
onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T
```

Called when component is focused, the return value indicates whether keyboard is needed.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-CommonMethod-onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T--><!--Device-CommonMethod-onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onNeedSoftkeyboardCallback | [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onPreDrag

```TypeScript
onPreDrag(callback: Callback<PreDragStatus>): T
```

Triggered when the component enters a state prior to a gesture-based drag operation. For details about the state prior to the drag-and-drop operation, see [PreDragStatus](arkts-arkui-predragstatus-e.md#PreDragStatus). This API cannot be triggered in mouse-based drag scenarios. > **NOTE：**> > This API can be called in [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onPreDrag(callback: Callback<PreDragStatus>): T--><!--Device-CommonMethod-onPreDrag(callback: Callback<PreDragStatus>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;[PreDragStatus](arkts-arkui-predragstatus-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onSizeChange

```TypeScript
onSizeChange(event: SizeChangeCallback): T
```

Triggered when the component size changes due to layout updates. > **NOTE：**> > 1. This API is triggered upon layout changes. Due to calculation precision limitations, the return value may > deviate slightly from the actual physical size. > > 2. **onSizeChange** is a synchronous callback triggered during the layout process. Directly modifying state > variables within **onSizeChange** may cause the changes to be included in the animation closure. Specifically, > animations compare the layout state before the animation starts with the state after the animation closure is > executed. If the **onSizeChange** callback is triggered synchronously during the pre-animation layout phase, the > changes made in this callback will be processed as part of the animation, along with the changes in the animation > closure. To avoid this issue, you can use setTimeout or > [postFrameCallback](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#postFrameCallback) (with a 0 ms delay) inside > **onSizeChange** to defer the UI processing logic to asynchronous execution.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-onSizeChange(event: SizeChangeCallback): T--><!--Device-CommonMethod-onSizeChange(event: SizeChangeCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onTouch

```TypeScript
onTouch(event: (event: TouchEvent) => void): T
```

Invoked when a touch event is triggered. Touch events [bubble](../../../ui/arkts-interaction-basic-principles.md#event-bubbling) by default and can be consumed by multiple components. To prevent event bubbling, use the **stopPropagation** API of [TouchEvent](arkts-arkui-touchevent-i.md#TouchEvent). Mouse left-click events are converted to touch events and will also trigger this callback.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onTouch(event: (event: TouchEvent) => void): T--><!--Device-CommonMethod-onTouch(event: (event: TouchEvent) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (event: TouchEvent) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onTouchIntercept

```TypeScript
onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T
```

Binds a custom event interception callback to a component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T--><!--Device-CommonMethod-onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;[TouchEvent](arkts-arkui-touchevent-i.md), [HitTestMode](../arkts-apis/arkts-arkui-hittestmode-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onTouchTestDone

```TypeScript
onTouchTestDone(callback: TouchTestDoneCallback): T
```

Specifies whether gesture recognizers participate in subsequent processing after [hit testing](../../../ui/arkts-interaction-basic-principles.md#hit-testing) completes.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-onTouchTestDone(callback: TouchTestDoneCallback): T--><!--Device-CommonMethod-onTouchTestDone(callback: TouchTestDoneCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onVisibleAreaApproximateChange

```TypeScript
onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T
```

Configures a callback for the **onVisibleAreaApproximateChange** event, with options to limit the callback execution interval. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 23.

**Since:** 17

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-CommonMethod-onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T--><!--Device-CommonMethod-onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [VisibleAreaEventOptions](arkts-arkui-visibleareaeventoptions-i.md) | Yes |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onVisibleAreaChange

```TypeScript
onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T
```

Called when the visible area of the component changes. For details about the development guidelines and FAQs, see [Detecting Component Visibility](../../../ui/arkts-manage-components-visibility.md). > **NOTE：**> > - This API can be called in [attributeModifier](#attributeModifier) since API version 20. > > - This API only takes into account the relative clipped area ratio of the component with respect to all ancestor > nodes (up to the window boundary) and its own area. > > - The following calculation scenarios are not supported: clipping by sibling nodes, clipping by siblings of any > ancestor node, window-level occlusion, and component rotation. Examples include layouts using > [Stack](../../apis-na/arkts-apis/arkts-na-lib-es5-error-i.md#stack), [z-order control](#zIndex), and > [rotate](#rotate) transformations. > > - It does not support visibility change calculations for nodes that are not in the component tree. For example, > preloaded nodes or custom nodes mounted using the > [overlay](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-overlay.md#overlay) capability. > > - This API does not support the [scale](#scale) attribute. To enable > support for the [scale](#scale) attribute, use > [onVisibleAreaChange&lt;sup&gt;22+&lt;/sup&gt;](#onVisibleAreaChange) > and set **measureFromViewport** to **true**.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T--><!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ratios | Array & lt;number & gt; | Yes |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onVisibleAreaChange

```TypeScript
onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T
```

Called when the visible area of the component changes. You can use **measureFromViewport** to set the visible area calculation mode. For details about the development guidelines and FAQs, see [Detecting Component Visibility](../../../ui/arkts-manage-components-visibility.md).

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T--><!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ratios | Array & lt;number & gt; | Yes |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | Yes |
| measureFromViewport | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## opacity

```TypeScript
opacity(value: number | Resource): T
```

Sets the opacity of the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-opacity(value: number | Resource): T--><!--Device-CommonMethod-opacity(value: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## opacity

```TypeScript
opacity(opacity: Optional<number | Resource>): T
```

Sets the opacity of the component. Compared with [opacity](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-opacity.md#opacity), this API supports the **undefined** type for the **opacity** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-opacity(opacity: Optional<number | Resource>): T--><!--Device-CommonMethod-opacity(opacity: Optional<number | Resource>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [opacity](#opacity) | [Optional](arkts-arkui-optional-t.md)&lt;number \| Resource & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outline

```TypeScript
outline(value: OutlineOptions): T
```

Sets the outline attributes in one declaration.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-outline(value: OutlineOptions): T--><!--Device-CommonMethod-outline(value: OutlineOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [OutlineOptions](../arkts-apis/arkts-arkui-outlineoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outline

```TypeScript
outline(options: Optional<OutlineOptions>): T
```

Sets the outline attributes in one declaration. Compared with [outline](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-outline.md#outline), this API supports the **undefined** type for the **options** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-outline(options: Optional<OutlineOptions>): T--><!--Device-CommonMethod-outline(options: Optional<OutlineOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[OutlineOptions](../arkts-apis/arkts-arkui-outlineoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineColor

```TypeScript
outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T
```

Sets the outline color. If this API is not used, the default color black will be applied.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T--><!--Device-CommonMethod-outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [EdgeColors](../arkts-apis/arkts-arkui-edgecolors-t.md) \| [LocalizedEdgeColors](../arkts-apis/arkts-arkui-localizededgecolors-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineColor

```TypeScript
outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T
```

Sets the outline color. If this API is not used, the default color black will be applied. Compared with [outlineColor](#outlineColor), this API supports the **undefined** type for the **color** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T--><!--Device-CommonMethod-outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [EdgeColors](../arkts-apis/arkts-arkui-edgecolors-t.md) \| [LocalizedEdgeColors](../arkts-apis/arkts-arkui-localizededgecolors-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineRadius

```TypeScript
outlineRadius(value: Dimension | OutlineRadiuses): T
```

Sets the radius of the outline corners. If this API is not used, there will be no change by default.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-outlineRadius(value: Dimension | OutlineRadiuses): T--><!--Device-CommonMethod-outlineRadius(value: Dimension | OutlineRadiuses): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [OutlineRadiuses](../arkts-apis/arkts-arkui-outlineradiuses-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineRadius

```TypeScript
outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T
```

Sets the radius of the outline corners. If this API is not used, there will be no change by default. Compared with [outlineRadius](#outlineRadius), this API supports the **undefined** type for the **radius** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T--><!--Device-CommonMethod-outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;[Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [OutlineRadiuses](../arkts-apis/arkts-arkui-outlineradiuses-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineStyle

```TypeScript
outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T
```

Sets the outline style. If this API is not used, a solid line is displayed by default.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T--><!--Device-CommonMethod-outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [OutlineStyle](arkts-arkui-outlinestyle-e.md) \| [EdgeOutlineStyles](../arkts-apis/arkts-arkui-edgeoutlinestyles-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineStyle

```TypeScript
outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T
```

Sets the outline style. If this API is not used, a solid line is displayed by default. Compared with [outlineStyle](#outlineStyle), this API supports the **undefined** type for the **style** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T--><!--Device-CommonMethod-outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[OutlineStyle](arkts-arkui-outlinestyle-e.md) \| [EdgeOutlineStyles](../arkts-apis/arkts-arkui-edgeoutlinestyles-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineWidth

```TypeScript
outlineWidth(value: Dimension | EdgeOutlineWidths): T
```

Sets the thickness of the outline. If this API is not used, there will be no change by default.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-outlineWidth(value: Dimension | EdgeOutlineWidths): T--><!--Device-CommonMethod-outlineWidth(value: Dimension | EdgeOutlineWidths): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [EdgeOutlineWidths](../arkts-apis/arkts-arkui-edgeoutlinewidths-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## outlineWidth

```TypeScript
outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T
```

Sets the thickness of the outline. If this API is not used, there will be no change by default. Compared with [outlineWidth](#outlineWidth), this API supports the **undefined** type for the **width** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T--><!--Device-CommonMethod-outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [width](#width) | [Optional](arkts-arkui-optional-t.md)&lt;[Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [EdgeOutlineWidths](../arkts-apis/arkts-arkui-edgeoutlinewidths-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## overlay

```TypeScript
overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T
```

Adds an overlay to this component, which can be text, a custom component, or [ComponentContent](arkts-arkui-componentcontent-t.md#ComponentContent). The overlay is positioned based on the current component. The overlay is not rendered through the component tree, meaning some APIs (for example, [getRectangleById](../arkts-apis/arkts-arkui-componentutils-getrectanglebyid-f.md#getRectangleById)) cannot access components within the overlay. > **NOTE：**> > The overlay places the floating layer component above the bound component, blocking all user interactions with > components beneath it. To enable interaction with underlying components, refer to > [Example 2: Setting an Overlay Using a Custom Builder](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-overlay.md#example-2-setting-an-overlay-using-a-custom-builder) > and apply **.hitTestBehavior(HitTestMode.Transparent)** to the outermost component in the overlay builder. This > configuration is particularly crucial for watermark implementations, where the overlay must not interfere with > user interaction with the underlying content.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T--><!--Device-CommonMethod-overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ComponentContent](arkts-arkui-componentcontent-t.md) | Yes |
| options | [OverlayOptions](arkts-arkui-overlayoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## padding

```TypeScript
padding(value: Padding | Length | LocalizedPadding): T
```

Sets the padding of the component. &lt;br&gt;Since API version 10, this API supports the calc calculation feature.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-padding(value: Padding | Length | LocalizedPadding): T--><!--Device-CommonMethod-padding(value: Padding | Length | LocalizedPadding): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Padding](../arkts-apis/arkts-arkui-padding-t.md) \| [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## parallelGesture

```TypeScript
parallelGesture(gesture: GestureType, mask?: GestureMask): T
```

Gesture that can be recognized at once by the component and its child component. The gesture event is not a bubbling event. When **parallelGesture** is set for a component, both it and its child component can respond to the same gesture events, thereby implementing a quasi-bubbling effect. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-parallelGesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-parallelGesture(gesture: GestureType, mask?: GestureMask): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../arkts-apis/arkts-arkui-gesturecontrol-gesturetype-e.md) | Yes |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## pixelRound

```TypeScript
pixelRound(value: PixelRoundPolicy): T
```

Sets the pixel rounding policy for the current component in the specified direction. If a direction is not set, the pixels are rounded to the nearest whole number in that direction. > **NOTE：**> > - In API version 11, this API uses half-pixel alignment (that is, 0-0.25 rounds to 0, 0.25-0.75 rounds to 0.5, > 0.75-1.0 rounds to 1). Since API version 12, this API rounds pixels to the nearest integers and allows you to > disable pixel rounding for individual components. > > - This API can be called within > [attributeModifier](#attributeModifier) > since API version 12. In normal calculations, the vertical direction (top and bottom) correspond to the component height, and the horizontal direction (the starting direction of mirroring is considered "left") correspond to the component width. For ease of description, these two sets of directions are referred to as top-left and bottom-right. - Calculate the top-left coordinates of the current component: offset of the top-left corner relative to the parent container. - Calculate the bottom-right coordinates of the current component: offset of the top-left corner relative to the parent container plus the size of the component itself. - Recalculate the size of the current component: bottom-right corner rounded value minus the top-left corner rounded value.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-pixelRound(value: PixelRoundPolicy): T--><!--Device-CommonMethod-pixelRound(value: PixelRoundPolicy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelRoundPolicy](arkts-arkui-pixelroundpolicy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## pixelStretchEffect

```TypeScript
pixelStretchEffect(options: PixelStretchEffectOptions): T
```

Applies a pixel stretch effect to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-pixelStretchEffect(options: PixelStretchEffectOptions): T--><!--Device-CommonMethod-pixelStretchEffect(options: PixelStretchEffectOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [PixelStretchEffectOptions](arkts-arkui-pixelstretcheffectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## pixelStretchEffect

```TypeScript
pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T
```

Applies a pixel stretch effect to the component. Compared to [pixelStretchEffect&lt;sup&gt;12+&lt;/sup&gt;](#pixelStretchEffect), the **options** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T--><!--Device-CommonMethod-pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[PixelStretchEffectOptions](arkts-arkui-pixelstretcheffectoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## position

```TypeScript
position(value: Position | Edges | LocalizedEdges): T
```

Sets the absolute positioning, which determines the position of a child component relative to the content area of the parent component. Dynamic configuration via [attributeModifier](#attributeModifier) is supported. **NOTE：**- This API takes effect after the component's size measurement is complete. - When the parent container is Row, Column, or Flex, the child component with **position** set does not occupy any space. - The Position type uses the upper left corner of the parent's content area as the reference point. The Edges type uses all four sides of the parent's content area as reference, where **top**, **left**, **right**, and **bottom** define the margins between the component and corresponding sides of the parent's content area. The [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md#LocalizedEdges) type provides the same functionality as Edges while supporting layout mirroring. - This attribute is applicable to scenarios where the component's position in the parent container is fixed, for example, where it is pinned to top or floating on the UI. - This attribute is unavailable for a layout container whose width and height are zero. - In [RelativeContainer](../../../reference/apis-arkui/arkui-ts/ts-container-relativecontainer.md), if the child component has [alignRules](#alignRules) set, the **position** attribute will not take effect

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-position(value: Position | Edges | LocalizedEdges): T--><!--Device-CommonMethod-position(value: Position | Edges | LocalizedEdges): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Position \| Edges \| [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## priorityGesture

```TypeScript
priorityGesture(gesture: GestureType, mask?: GestureMask): T
```

Gesture to preferentially recognize. 1. By default, the child component preferentially recognizes the gesture specified by **gesture**, and the parent component preferentially recognizes the gesture specified by **priorityGesture** (if set). 2. For long press gestures, the component with the shortest minimum hold-down time responds first, ignoring the **priorityGesture** settings. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-priorityGesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-priorityGesture(gesture: GestureType, mask?: GestureMask): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../arkts-apis/arkts-arkui-gesturecontrol-gesturetype-e.md) | Yes |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## radialGradient

```TypeScript
radialGradient(value: RadialGradientOptions): T
```

Radial Gradient center:Center point of radial gradient radius:Radius of Radial Gradient. value range [0, +∞) colors:Color description for gradients repeating: Refill. The default value is false Anonymous Object Rectification.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-radialGradient(value: RadialGradientOptions): T--><!--Device-CommonMethod-radialGradient(value: RadialGradientOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RadialGradientOptions](arkts-arkui-radialgradientoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## radialGradient

```TypeScript
radialGradient(options: Optional<RadialGradientOptions>): T
```

Radial Gradient center:Center point of radial gradient radius:Radius of Radial Gradient. value range [0, +∞) colors:Color description for gradients repeating: Refill. The default value is false

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-radialGradient(options: Optional<RadialGradientOptions>): T--><!--Device-CommonMethod-radialGradient(options: Optional<RadialGradientOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[RadialGradientOptions](arkts-arkui-radialgradientoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## renderFit

```TypeScript
renderFit(fitMode: RenderFit): T
```

Sets how the final state of the component's content is rendered during its width and height animation process. If it is not set via this API, the content size at the end of the animation is maintained, and the content always remains top-left aligned with the component.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-renderFit(fitMode: RenderFit): T--><!--Device-CommonMethod-renderFit(fitMode: RenderFit): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fitMode | [RenderFit](../arkts-apis/arkts-arkui-renderfit-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## renderFit

```TypeScript
renderFit(fitMode: Optional<RenderFit>): T
```

Sets how the final state of the component's content is rendered during its width and height animation process. If it is not set via this API, the content size at the end of the animation is maintained, and the content always remains top-left aligned with the component. Compared to [renderFit](#renderFit), this API supports the **undefined** type for the **fitMode** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-renderFit(fitMode: Optional<RenderFit>): T--><!--Device-CommonMethod-renderFit(fitMode: Optional<RenderFit>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fitMode | [Optional](arkts-arkui-optional-t.md)&lt;[RenderFit](../arkts-apis/arkts-arkui-renderfit-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## renderGroup

```TypeScript
renderGroup(value: boolean): T
```

Sets whether to form a render group. A render group means that the subtree composed of the current component and its child components is first rendered on an offscreen canvas and then composited with the parent component. Setting a render group allows the system to cache the rendering result, improving performance. However, if components within the render group are frequently updated, cache invalidation may lead to performance degradation. Additionally, when a render group is set and the current component's opacity is not **1**, the rendering effect may differ. If this attribute is not set, no render group is formed by default.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-renderGroup(value: boolean): T--><!--Device-CommonMethod-renderGroup(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## renderGroup

```TypeScript
renderGroup(isGroup: Optional<boolean>): T
```

Composite the contents of this view and its children into an offscreen cache before display in the screen.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-renderGroup(isGroup: Optional<boolean>): T--><!--Device-CommonMethod-renderGroup(isGroup: Optional<boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isGroup | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## responseRegion

```TypeScript
responseRegion(value: Array<Rectangle> | Rectangle): T
```

Sets one or more touch targets.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-responseRegion(value: Array<Rectangle> | Rectangle): T--><!--Device-CommonMethod-responseRegion(value: Array<Rectangle> | Rectangle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[Rectangle](arkts-arkui-rectangle-i.md)&gt; \| [Rectangle](arkts-arkui-rectangle-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## responseRegionList

```TypeScript
responseRegionList(regions: Array<ResponseRegion>): T
```

Sets the touch target list for the component. When this API is called, the [responseRegion](#responseRegion) and [mouseResponseRegion](#mouseResponseRegion) APIs do not take effect.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CommonMethod-responseRegionList(regions: Array<ResponseRegion>): T--><!--Device-CommonMethod-responseRegionList(regions: Array<ResponseRegion>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| regions | Array&lt;[ResponseRegion](arkts-arkui-responseregion-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## restoreId

```TypeScript
restoreId(value: number): T
```

id for distribute identification.

**Since:** 11

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-restoreId(value: number): T--><!--Device-CommonMethod-restoreId(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## reuse

```TypeScript
reuse(options: ReuseOptions): T
```

Reuse id is used for identify the reuse type of each @ComponentV2 custom component, which can give user control of sub-component recycle and reuse.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-reuse(options: ReuseOptions): T--><!--Device-CommonMethod-reuse(options: ReuseOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ReuseOptions](arkts-arkui-reuseoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## reuseId

```TypeScript
reuseId(id: string): T
```

Reuse id is used for identify the reuse type for each custom node.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-reuseId(id: string): T--><!--Device-CommonMethod-reuseId(id: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## rotate

```TypeScript
rotate(value: RotateOptions): T
```

Rotates the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-rotate(value: RotateOptions): T--><!--Device-CommonMethod-rotate(value: RotateOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [RotateOptions](arkts-arkui-rotateoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## rotate

```TypeScript
rotate(options: Optional<RotateOptions>): T
```

Rotates the component. Compared with [rotate](#rotate), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-rotate(options: Optional<RotateOptions>): T--><!--Device-CommonMethod-rotate(options: Optional<RotateOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[RotateOptions](arkts-arkui-rotateoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## rotate

```TypeScript
rotate(options: Optional<RotateOptions | RotateAngleOptions>): T
```

Sets the component rotation effect. Compared with [rotate](#rotate), this API supports the **RotateAngleOptions** type for the **options** parameter.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CommonMethod-rotate(options: Optional<RotateOptions | RotateAngleOptions>): T--><!--Device-CommonMethod-rotate(options: Optional<RotateOptions | RotateAngleOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[RotateOptions](arkts-arkui-rotateoptions-i.md) \| [RotateAngleOptions](arkts-arkui-rotateangleoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## safeAreaPadding

```TypeScript
safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T
```

Sets the safe area padding. This allows the container to add a component-level safe area for its child components to extend into. This attribute can be dynamically set using [attributeModifier](#attributeModifier). > **NOTE：**> In API version 18, this API can be invoked in attributeModifier. > When parent and ancestor containers define component-level safe areas, child components can detect and utilize > these areas, referred to as Accumulated Safe Area Expansion (SAE), which represents the maximum extendable length > in each direction. > When ancestor containers have contiguous safeAreaPadding (undivided by margin, border, or padding), > SAE accumulates recursively outward until no adjacent outer safeAreaPadding exists or the recursion extends > beyond the page container. > System-level avoid areas (status bar, navigation bar, notch areas, and more) are treated as the page container's > inherent safeAreaPadding and participate in SAE calculations. > For details about the avoid areas, see Safe Area. These component-level safe areas can be leveraged by combining > with other attributes. > For example, setting the ignoreLayoutSafeArea attribute on a child component allows it to extend its layout into > the SAE region.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 14.

<!--Device-CommonMethod-safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T--><!--Device-CommonMethod-safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| paddingValue | [Padding](../arkts-apis/arkts-arkui-padding-t.md) \| LengthMetrics \| [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## saturate

```TypeScript
saturate(value: number): T
```

Applies a saturation effect to the component. If this API is not used, there will be no change by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-saturate(value: number): T--><!--Device-CommonMethod-saturate(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## saturate

```TypeScript
saturate(saturate: Optional<number>): T
```

Applies a saturation effect to the component. If this API is not used, there will be no change by default. Compared to [saturate](#saturate), the **saturate** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-saturate(saturate: Optional<number>): T--><!--Device-CommonMethod-saturate(saturate: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [saturate](#saturate) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scale

```TypeScript
scale(value: ScaleOptions): T
```

Scales the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-scale(value: ScaleOptions): T--><!--Device-CommonMethod-scale(value: ScaleOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scale

```TypeScript
scale(options: Optional<ScaleOptions>): T
```

Scales the component. Compared with [scale](#scale), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-scale(options: Optional<ScaleOptions>): T--><!--Device-CommonMethod-scale(options: Optional<ScaleOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[ScaleOptions](arkts-arkui-scaleoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sepia

```TypeScript
sepia(value: number): T
```

Converts the image to a sepia tone, reducing color intensity to create a warm, vintage image style.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-sepia(value: number): T--><!--Device-CommonMethod-sepia(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sepia

```TypeScript
sepia(sepia: Optional<number>): T
```

Converts the image to a sepia tone, reducing color intensity to create a warm, vintage image style. Compared to [sepia](#sepia), this API supports the **undefined** type for the **sepia** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-sepia(sepia: Optional<number>): T--><!--Device-CommonMethod-sepia(sepia: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sepia](#sepia) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## shadow

```TypeScript
shadow(value: ShadowOptions | ShadowStyle): T
```

Applies a shadow effect to the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-shadow(value: ShadowOptions | ShadowStyle): T--><!--Device-CommonMethod-shadow(value: ShadowOptions | ShadowStyle): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](arkts-arkui-shadowstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## shadow

```TypeScript
shadow(options: Optional<ShadowOptions | ShadowStyle>): T
```

Applies a shadow effect to the component. Compared to [shadow](#shadow), the **options** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-shadow(options: Optional<ShadowOptions | ShadowStyle>): T--><!--Device-CommonMethod-shadow(options: Optional<ShadowOptions | ShadowStyle>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[ShadowOptions](arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](arkts-arkui-shadowstyle-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sharedTransition

```TypeScript
sharedTransition(id: string, options?: sharedTransitionOptions): T
```

Sets the shared transition animation.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-sharedTransition(id: string, options?: sharedTransitionOptions): T--><!--Device-CommonMethod-sharedTransition(id: string, options?: sharedTransitionOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [id](#id) | string | Yes |
| options | [sharedTransitionOptions](arkts-arkui-sharedtransitionoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## shouldBuiltInRecognizerParallelWith

```TypeScript
shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T
```

Provides a callback to set the parallel relationship between built-in gestures and gestures of other components in the response chain. The corresponding C API is [setInnerGestureParallelTo](../../../reference/apis-arkui/capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto).

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T--><!--Device-CommonMethod-shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## shouldRecognizerParallelWith

```TypeScript
shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T
```

Provides a callback to set the parallel relationship between gestures of the current component and gestures of other components in the response chain. This callback uses an asynchronous callback. The corresponding C API is [setGestureParallelTo](../../../reference/apis-arkui/capi-arkui-nativemodule-arkui-nativegestureapi-3.md#setgestureparallelto).

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T--><!--Device-CommonMethod-shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ShouldRecognizerParallelWithCallback](arkts-arkui-shouldrecognizerparallelwithcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## size

```TypeScript
size(value: SizeOptions): T
```

Sets the width and height of the component. &lt;br&gt;Since API version 10, this API supports the calc calculation feature.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-size(value: SizeOptions): T--><!--Device-CommonMethod-size(value: SizeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## smartGestureShortcut

```TypeScript
smartGestureShortcut(options?: SmartGestureShortcutOptions): T
```

Enable or disable specific smart gesture shortcuts, and set response priorities for them.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CommonMethod-smartGestureShortcut(options?: SmartGestureShortcutOptions): T--><!--Device-CommonMethod-smartGestureShortcut(options?: SmartGestureShortcutOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SmartGestureShortcutOptions](arkts-arkui-smartgestureshortcutoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sphericalEffect

```TypeScript
sphericalEffect(value: number): T
```

Applies a spherical effect to the component.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-sphericalEffect(value: number): T--><!--Device-CommonMethod-sphericalEffect(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sphericalEffect

```TypeScript
sphericalEffect(effect: Optional<number>): T
```

Applies a spherical effect to the component. Compared to [sphericalEffect&lt;sup&gt;12+&lt;/sup&gt;](#sphericalEffect), the **effect** parameter supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-sphericalEffect(effect: Optional<number>): T--><!--Device-CommonMethod-sphericalEffect(effect: Optional<number>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## stateStyles

```TypeScript
stateStyles(value: StateStyles): T
```

Sets the state-specific styles for the component. > **NOTE：**> > This API cannot be called within [attributeModifier](#attributeModifier).

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-stateStyles(value: StateStyles): T--><!--Device-CommonMethod-stateStyles(value: StateStyles): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [StateStyles](arkts-arkui-statestyles-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sweepGradient

```TypeScript
sweepGradient(value: SweepGradientOptions): T
```

Angle Gradient center:is the center point of the angle gradient start:Start point of angle gradient. The default value is 0 end:End point of angle gradient. The default value is 0 rotating:rotating. The default value is 0 colors:Color description for gradients repeating:repeating. The default value is false Anonymous Object Rectification.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-sweepGradient(value: SweepGradientOptions): T--><!--Device-CommonMethod-sweepGradient(value: SweepGradientOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SweepGradientOptions](arkts-arkui-sweepgradientoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## sweepGradient

```TypeScript
sweepGradient(options: Optional<SweepGradientOptions>): T
```

Angle Gradient center:is the center point of the angle gradient start:Start point of angle gradient. The default value is 0 end:End point of angle gradient. The default value is 0 rotating:rotating. The default value is 0 colors:Color description for gradients repeating:repeating. The default value is false

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-sweepGradient(options: Optional<SweepGradientOptions>): T--><!--Device-CommonMethod-sweepGradient(options: Optional<SweepGradientOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;[SweepGradientOptions](arkts-arkui-sweepgradientoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## systemBarEffect

```TypeScript
systemBarEffect(): T
```

Applies a system bar effect to the component, which means to invert colors based on the background and add a blur.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-systemBarEffect(): T--><!--Device-CommonMethod-systemBarEffect(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## tabIndex

```TypeScript
tabIndex(index: number): T
```

Sets the tab navigation order of the component in sequential focus navigation with the **Tab** key. Components without explicit **tabIndex** settings follow default focus navigation rules. > **NOTE：**> > - **tabIndex** only customizes **Tab** key navigation. For arrow key navigation customization, use > [nextFocus](#nextFocus).

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-tabIndex(index: number): T--><!--Device-CommonMethod-tabIndex(index: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## tabStop

```TypeScript
tabStop(isTabStop: boolean): T
```

Set TabStop on component focus

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CommonMethod-tabStop(isTabStop: boolean): T--><!--Device-CommonMethod-tabStop(isTabStop: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isTabStop | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## toolbar

```TypeScript
toolbar(value: CustomBuilder): T
```

Config toolbar for current component.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-toolbar(value: CustomBuilder): T--><!--Device-CommonMethod-toolbar(value: CustomBuilder): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## touchable

```TypeScript
touchable(value: boolean): T
```

Whether the component can respond to finger interactions such as click and touch events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [hitTestBehavior](#hitTestBehavior)

<!--Device-CommonMethod-touchable(value: boolean): T--><!--Device-CommonMethod-touchable(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## transform

```TypeScript
transform(value: object): T
```

Displays the matrix transformation when 2D transformation is performed. If 3D transformation is included, the [transform3D](#transform3D) API is required.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CommonMethod-transform(value: object): T--><!--Device-CommonMethod-transform(value: object): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | object | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## transform

```TypeScript
transform(transform: Optional<object>): T
```

Displays the matrix transformation when 2D transformation is performed. If 3D transformation is included, the [transform3D](#transform3D) API is required. Compared with [transform](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-transformation.md#transform), the transform&lt;sup&gt;18+&lt;/sup&gt; parameter supports the undefined type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-transform(transform: Optional<object>): T--><!--Device-CommonMethod-transform(transform: Optional<object>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transform](#transform) | [Optional](arkts-arkui-optional-t.md)&lt;object&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## transform3D

```TypeScript
transform3D(transform: Optional<Matrix4Transit>): T
```

Sets the 3D transformation matrix of the component. When 3D transformation with the perspective effect is involved, the display effect of the transform interface may be incorrect. In this case, the transform3D interface is recommended.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-CommonMethod-transform3D(transform: Optional<Matrix4Transit>): T--><!--Device-CommonMethod-transform3D(transform: Optional<Matrix4Transit>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [transform](#transform) | [Optional](arkts-arkui-optional-t.md)&lt;[Matrix4Transit](arkts-arkui-matrix4transit-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## transition

```TypeScript
transition(value: TransitionOptions | TransitionEffect): T
```

Sets the transition effects used when a component is inserted or removed.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-transition(value: TransitionOptions | TransitionEffect): T--><!--Device-CommonMethod-transition(value: TransitionOptions | TransitionEffect): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TransitionOptions](arkts-arkui-transitionoptions-i.md) \| [TransitionEffect](arkts-arkui-transitioneffect-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## transition

```TypeScript
transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T
```

Sets the transition effects used when a component is inserted or removed. Compared with [transition](#transition), this API provides the callback when the transition animation ends. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-CommonMethod-transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T--><!--Device-CommonMethod-transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | Yes |
| onFinish | [Optional](arkts-arkui-optional-t.md)&lt;[TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## translate

```TypeScript
translate(value: TranslateOptions): T
```

Translates the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-translate(value: TranslateOptions): T--><!--Device-CommonMethod-translate(value: TranslateOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TranslateOptions](arkts-arkui-translateoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## translate

```TypeScript
translate(translate: Optional<TranslateOptions>): T
```

Translates the component. Compared with [translate](#translate), this API supports the **undefined** type.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-translate(translate: Optional<TranslateOptions>): T--><!--Device-CommonMethod-translate(translate: Optional<TranslateOptions>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [translate](#translate) | [Optional](arkts-arkui-optional-t.md)&lt;[TranslateOptions](arkts-arkui-translateoptions-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useEffect

```TypeScript
useEffect(useEffect: boolean, effectType: EffectType): T
```

Sets whether the component should apply the effects template defined by the parent effectComponent or window. If multiple parent effectComponents are found, the nearest one will be used. If no parent effectComponent is found, this method has no effect.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-CommonMethod-useEffect(useEffect: boolean, effectType: EffectType): T--><!--Device-CommonMethod-useEffect(useEffect: boolean, effectType: EffectType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [useEffect](#useEffect) | boolean | Yes |
| [effectType](../../apis-camera-kit/arkts-apis/arkts-camera-camera-controlcenterstatusinfo-i.md) | [EffectType](arkts-arkui-effecttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useEffect

```TypeScript
useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T
```

Sets whether the component should apply the effects template defined by the parent effectComponent or window. If multiple parent effectComponents are found, the nearest one will be used. If no parent effectComponent is found, this method has no effect.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CommonMethod-useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T--><!--Device-CommonMethod-useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [useEffect](#useEffect) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |
| [effectType](../../apis-camera-kit/arkts-apis/arkts-camera-camera-controlcenterstatusinfo-i.md) | [EffectType](arkts-arkui-effecttype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useEffect

```TypeScript
useEffect(value: boolean): T
```

Sets whether the component should apply the effects template defined by the parent effectComponent. If multiple parent effectComponents are found, the nearest one will be used. If no parent effectComponent is found, this method has no effect.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-useEffect(value: boolean): T--><!--Device-CommonMethod-useEffect(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useShadowBatching

```TypeScript
useShadowBatching(value: boolean): T
```

Sets whether to render child node shadows at the same layer, enabling shadow overlap within the same layer.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-CommonMethod-useShadowBatching(value: boolean): T--><!--Device-CommonMethod-useShadowBatching(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useShadowBatching

```TypeScript
useShadowBatching(use: Optional<boolean>): T
```

Sets whether to render child node shadows at the same layer, enabling shadow overlap within the same layer. Compared with [useShadowBatching&lt;sup&gt;11+&lt;/sup&gt;](#useShadowBatching), this API supports the **undefined** type for the **use** parameter.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-CommonMethod-useShadowBatching(use: Optional<boolean>): T--><!--Device-CommonMethod-useShadowBatching(use: Optional<boolean>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| use | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## useSizeType

```TypeScript
useSizeType(value: {
    xs?: number | { span: number; offset: number };
    sm?: number | { span: number; offset: number };
    md?: number | { span: number; offset: number };
    lg?: number | { span: number; offset: number };
  }): T
```

Sets the number of occupied columns and offset columns for a specific device width type.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** grid_col/GridColColumnOption and grid_row/GridRowColumnOption

<!--Device-CommonMethod-useSizeType(value: {    xs?: number | { span: number; offset: number };    sm?: number | { span: number; offset: number };    md?: number | { span: number; offset: number };    lg?: number | { span: number; offset: number };  }): T--><!--Device-CommonMethod-useSizeType(value: {    xs?: number | { span: number; offset: number };    sm?: number | { span: number; offset: number };    md?: number | { span: number; offset: number };    lg?: number | { span: number; offset: number };  }): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | {     xs?: number \| { span: number; offset: number };     sm?: number \| { span: number; offset: number };     md?: number \| { span: number; offset: number };     lg?: number \| { span: number; offset: number };   } | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## visibility

```TypeScript
visibility(value: Visibility): T
```

Sets the visibility of the component. If **visibility** is not set, the component is displayed by default.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-visibility(value: Visibility): T--><!--Device-CommonMethod-visibility(value: Visibility): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Visibility](#visibility) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## visualEffect

```TypeScript
visualEffect(effect: VisualEffect): T
```

Sets a visual effect that is not a filter effect. > **NOTE：**> > This API can be called within [attributeModifier](#attributeModifier) since API version 20.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CommonMethod-visualEffect(effect: VisualEffect): T--><!--Device-CommonMethod-visualEffect(effect: VisualEffect): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| effect | [VisualEffect](arkts-arkui-visualeffect-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## width

```TypeScript
width(value: Length): T
```

Sets the width of the component. By default, the width required to fully hold the component content is used. If a component is wider than its parent, it will overflow. &lt;br&gt;Since API version 10, this API supports the calc calculation feature.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-width(value: Length): T--><!--Device-CommonMethod-width(value: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## width

```TypeScript
width(widthValue: Length | LayoutPolicy): T
```

Sets the width of the component or its horizontal layout policy. By default, the component uses the width required for its content. If a component is wider than its parent, it will overflow.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-CommonMethod-width(widthValue: Length | LayoutPolicy): T--><!--Device-CommonMethod-width(widthValue: Length | LayoutPolicy): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| widthValue | [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LayoutPolicy](arkts-arkui-layoutpolicy-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## zIndex

```TypeScript
zIndex(value: number): T
```

Sets the stacking order of the component.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonMethod-zIndex(value: number): T--><!--Device-CommonMethod-zIndex(value: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
