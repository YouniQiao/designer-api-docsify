# CommonMethod

CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CommonMethod--><!--Device-unnamed-export declare interface CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityActionOptions

```TypeScript
default accessibilityActionOptions(option: AccessibilityActionOptions | undefined): this
```

Provides optional parameters for setting accessibility operations of a component, which is used to restrict or&lt;br&gt;modify the operations initiated by accessibility applications such as the screen reader.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityActionOptions(option: AccessibilityActionOptions | undefined): this--><!--Device-CommonMethod-default accessibilityActionOptions(option: AccessibilityActionOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [AccessibilityActionOptions](arkts-arkui-accessibilityactionoptions-i.md) \| undefined | Yes | Parameter of the accessibility operation, which is used &lt;br&gt;to restrict or modify the sliding behavior in the accessibility operation. &lt;br&gt;The **scrollStep** parameter in **AccessibilityActionOptions** is used to set the number of sliding steps in &lt;br&gt;the accessibility operation. When the value is **undefined**, **scrollStep** is processed as **1**. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return component instance who call the method. |

## accessibilityChecked

```TypeScript
default accessibilityChecked(isCheck: boolean | undefined): this
```

Sets the checked state for the accessibility node. This API is used in multi-select scenarios and only affects&lt;br&gt;component state announcements in screen reading scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityChecked(isCheck: boolean | undefined): this--><!--Device-CommonMethod-default accessibilityChecked(isCheck: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isCheck | boolean \| undefined | Yes | Whether the current component is selected. &lt;br&gt;**true**: The component is selected. &lt;br&gt;**false**: The component is not selected. &lt;br&gt;**undefined**: The component determines its own selected state. &lt;br&gt;Default value: **undefined |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityCustomActions

```TypeScript
default accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): this
```

Sets the custom accessibility operations of the component, allowing developers to set an array of custom actions&lt;br&gt;for binding custom operation callbacks to components by operation name.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): this--><!--Device-CommonMethod-default accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| actions | Array&lt;[AccessibilityCustomAction](arkts-arkui-accessibilitycustomaction-i.md)&gt; \| undefined | Yes | Array of custom accessibility operations, where &lt;br&gt;each operation contains an operation name and a callback, used for binding custom operation callbacks to &lt;br&gt;components by operation name. &lt;br&gt;**NOTE：**: The array supports a maximum of 16 entries; any excess will not take effect. &lt;br&gt;When the value is **undefined**, no custom operations are set. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return component instance who call method. |

## accessibilityDefaultFocus

```TypeScript
default accessibilityDefaultFocus(focus: boolean | undefined): this
```

Sets the initial screen reader focus on the page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityDefaultFocus(focus: boolean | undefined): this--><!--Device-CommonMethod-default accessibilityDefaultFocus(focus: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| focus | boolean \| undefined | Yes | Initial screen reader focus on the page. The value **true** means the &lt;br&gt;component is the default initial focus for screen readers on the current page. Other values are ignored. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityDescription

```TypeScript
default accessibilityDescription(description: Resource | string | undefined): this
```

Sets the accessibility description, with support for resource references using Resource.&lt;br&gt;This attribute provides additional context and explanation for the component, helping users understand its&lt;br&gt;functionality and purpose.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;Reference resource of the accessibility description. You can specify further explanation&lt;br&gt;of the current component, for example, possible operation consequences, especially those that&lt;br&gt;cannot be learned from component attributes and accessibility text. If a component contains&lt;br&gt;both text information and the accessibility description, the text is read first and then the&lt;br&gt;accessibility description, when the component is selected.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityDescription(description: Resource | string | undefined): this--><!--Device-CommonMethod-default accessibilityDescription(description: Resource | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| string \| undefined | Yes | set description of accessibility, default value is "". |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityFocusDrawLevel

```TypeScript
default accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel | undefined): this
```

Sets the drawing level for the accessibility focus highlight (green frame).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel | undefined): this--><!--Device-CommonMethod-default accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| drawLevel | [FocusDrawLevel](arkts-arkui-focusdrawlevel-e.md) \| undefined | Yes | Drawing level for the accessibility focus highlight frame. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityGroup

```TypeScript
default accessibilityGroup(isGroup: boolean | undefined, accessibilityOptions?: AccessibilityOptions): this
```

Sets whether to enable accessibility grouping.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;Whether to enable accessibility grouping. When accessibility grouping is enabled,&lt;br&gt;the component and all its children are treated as a single selectable unit, and the accessibility&lt;br&gt;service will no longer focus on the individual child components.

&lt;br&gt;If accessibility grouping is enabled and the component does not contain a universal text attribute&lt;br&gt;or an accessibility text attribute, the system will concatenate the universal text attributes of&lt;br&gt;its child components to form a merged text for the component. If a child component lacks a universal&lt;br&gt;text attribute, it will be ignored in the concatenation process.

&lt;br&gt;When accessibilityPreferred is set to true, the system will prioritize concatenating the accessibility&lt;br&gt;text attributes of the child components to form the merged text. If a child component lacks an&lt;br&gt;accessibility text attribute, the system will continue to concatenate its universal text attribute.&lt;br&gt;If a child component lacks both, it will be ignored.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityGroup(isGroup: boolean | undefined, accessibilityOptions?: AccessibilityOptions): this--><!--Device-CommonMethod-default accessibilityGroup(isGroup: boolean | undefined, accessibilityOptions?: AccessibilityOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isGroup | boolean \| undefined | Yes | set group with accessibility, default value is false. |
| accessibilityOptions | [AccessibilityOptions](arkts-arkui-accessibilityoptions-i.md) | No | options for accessibility, default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityLevel

```TypeScript
default accessibilityLevel(value: string | undefined): this
```

Sets the accessibility level.This property determines whether the component can be recognized by accessibility services.&lt;p&gt;Accessibility level, which is used to decide whether a component can be identified by the accessibility service.&lt;br&gt;The options are as follows:&lt;br&gt;"auto": The component's recognizability is determined by the accessibility grouping service and ArkUI.&lt;br&gt;"yes": The component can be recognized by accessibility services.&lt;br&gt;"no": The component cannot be recognized by accessibility services.&lt;br&gt;"no-hide-descendants": Neither the component nor its child components can be recognized by accessibility services.&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;When accessibilityLevel is set to "auto", the component's recognizability depends on the following factors:&lt;br&gt;1. The accessibility service internally determines whether the component can be recognized.&lt;br&gt;2. If the parent component's accessibilityGroup property has isGroup set to true, the accessibility service will&lt;br&gt;not focus on its child components, making them unrecognizable.&lt;br&gt;3. If the parent component's accessibilityLevel is set to "no-hide-descendants", the component will not be&lt;br&gt;recognized by accessibility services.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityLevel(value: string | undefined): this--><!--Device-CommonMethod-default accessibilityLevel(value: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | set accessibility level, default value is auto. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityNextFocusId

```TypeScript
default accessibilityNextFocusId(nextId: string | undefined): this
```

Sets the next component to receive focus during screen reader navigation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityNextFocusId(nextId: string | undefined): this--><!--Device-CommonMethod-default accessibilityNextFocusId(nextId: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nextId | string \| undefined | Yes | [Unique ID](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#id) of the next component to receive focus. &lt;br&gt;If the ID does not correspond to any component, the setting is ignored. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityNextFocusId

```TypeScript
default accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): this
```

Sets the next component to receive focus during screen reader navigation, with optional detailed parameters.The detailed parameters can provide additional behavior for the accessibility focus transition.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): this--><!--Device-CommonMethod-default accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nextId | string | Yes | [Unique ID](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#id) of the next component to receive focus. &lt;br&gt;If the ID does not correspond to any component, the setting is ignored. |
| nextFocusParams | [AccessibilityNextFocusParams](arkts-arkui-accessibilitynextfocusparams-i.md) \| undefined | Yes | Detailed parameters for accessibility next &lt;br&gt;focus processing, used to configure whether to search for focusable nodes among descendant nodes. &lt;br&gt;When the value is **undefined**, no detailed parameters are configured and no focus search is performed &lt;br&gt;among descendant nodes. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return component instance who call the method. |

## accessibilityRole

```TypeScript
default accessibilityRole(role: AccessibilityRoleType | undefined): this
```

Sets the role type of the accessibility component, which affects how the component is announced by screen readers.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityRole(role: AccessibilityRoleType | undefined): this--><!--Device-CommonMethod-default accessibilityRole(role: AccessibilityRoleType | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| role | [AccessibilityRoleType](arkts-arkui-common-accessibilityroletype-e.md) \| undefined | Yes | Role of the component as announced by screen readers (for &lt;br&gt;example, button or chart). You can define custom roles. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityScrollTriggerable

```TypeScript
default accessibilityScrollTriggerable(isTriggerable: boolean | undefined): this
```

Sets whether the accessibility node triggers automatic screen scrolling. When no focusable components are visible&lt;br&gt;on the current page within a container, this setting determines whether automatic scrolling is initiated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityScrollTriggerable(isTriggerable: boolean | undefined): this--><!--Device-CommonMethod-default accessibilityScrollTriggerable(isTriggerable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isTriggerable | boolean \| undefined | Yes | Whether the component triggers automatic scrolling for screen &lt;br&gt;readers when the current page has no focusable components. &lt;br&gt;**true**: The component triggers automatic scrolling. &lt;br&gt;**false**: The component does not trigger automatic scrolling. &lt;br&gt;**undefined**: The default settings are restored. &lt;br&gt;Default value: **true |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilitySelected

```TypeScript
default accessibilitySelected(isSelect: boolean | undefined): this
```

Sets the checked state for the accessibility node. This API is used in single-select scenarios and only affects&lt;br&gt;component state announcements in screen reading scenarios.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilitySelected(isSelect: boolean | undefined): this--><!--Device-CommonMethod-default accessibilitySelected(isSelect: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSelect | boolean \| undefined | Yes | Whether the current component is selected. &lt;br&gt;**true**: The component is selected. &lt;br&gt;**false**: The component is not selected. &lt;br&gt;**undefined**: The component determines its own selected state. &lt;br&gt;Default value: **undefined |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityStateDescription

```TypeScript
default accessibilityStateDescription(description: string | Resource | undefined): this
```

Sets the state description of a component for broadcasting, which clearly describes the real-time state of the&lt;br&gt;component in screen reading scenarios. Screen reader will broadcast the state description first.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityStateDescription(description: string | Resource | undefined): this--><!--Device-CommonMethod-default accessibilityStateDescription(description: string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | string \| Resource \| undefined | Yes | Text to be broadcasted for the current state of the component. &lt;br&gt;If the text contains more than 1000 characters, the first 1000 characters will be broadcasted. &lt;br&gt;**undefined**: The text is empty by default. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return component instance who call the method. |

## accessibilityText

```TypeScript
default accessibilityText(text: Resource | string | undefined): this
```

Sets the accessibility text.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;When a component does not contain a text attribute, you can use this API to set an accessibility&lt;br&gt;text attribute, so that accessibility services can announce the specified content for the component.&lt;br&gt;If a component has both text content and accessibility text, only the accessibility text is announced.&lt;br&gt;If a component is grouped for accessibility purposes but lacks both text content and accessibility&lt;br&gt;text, the screen reader will concatenate text from its child components (depth-first traversal).&lt;br&gt;To prioritize accessibility text concatenation, set accessibilityPreferred in accessibilityGroup.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityText(text: Resource | string | undefined): this--><!--Device-CommonMethod-default accessibilityText(text: Resource | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| string \| undefined | Yes | set accessibility text, default value is "". |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityTextHint

```TypeScript
default accessibilityTextHint(value: string | undefined): this
```

Sets the text hint for the component, which can be queried by accessibility services.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityTextHint(value: string | undefined): this--><!--Device-CommonMethod-default accessibilityTextHint(value: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | Text hint for the component, which can be queried by accessibility services. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityUseSamePage

```TypeScript
default accessibilityUseSamePage(pageMode: AccessibilitySamePageMode | undefined): this
```

Sets the same-page mode for the current component and its host application.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityUseSamePage(pageMode: AccessibilitySamePageMode | undefined): this--><!--Device-CommonMethod-default accessibilityUseSamePage(pageMode: AccessibilitySamePageMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pageMode | [AccessibilitySamePageMode](../arkts-components/arkts-arkui-accessibilitysamepagemode-e.md) \| undefined | Yes | Same-page mode for the cross-process embedded &lt;br&gt;component and the host application. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## accessibilityVirtualNode

```TypeScript
default accessibilityVirtualNode(builder: CustomBuilder | undefined): this
```

Sets an accessibility virtual child node. For custom drawing components, a **CustomBuilder** is passed, which is&lt;br&gt;used to provide accessibility information. The components within the **CustomBuilder** are only used for layout&lt;br&gt;and not for display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default accessibilityVirtualNode(builder: CustomBuilder | undefined): this--><!--Device-CommonMethod-default accessibilityVirtualNode(builder: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | set virtual node of accessibility |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## align

```TypeScript
default align(alignment: Alignment | LocalizedAlignment | undefined): this
```

Sets the alignment mode of the component content in the drawing area.Default value: **Alignment.Center**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default align(alignment: Alignment | LocalizedAlignment | undefined): this--><!--Device-CommonMethod-default align(alignment: Alignment | LocalizedAlignment | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignment | [Alignment](arkts-arkui-alignment-e.md) \| LocalizedAlignment \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## alignRules

```TypeScript
default alignRules(value: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this
```

Sets the alignment rules in the relative container.&lt;br&gt;This API is valid only when the container is RelativeContainer.&lt;br&gt;LocalizedAlignRuleOptions takes the right-to-left scripts into account, using start and end instead of  left and right for alignment in the horizontal direction. Prioritize this API in aligning  child components in the relative container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default alignRules(value: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this--><!--Device-CommonMethod-default alignRules(value: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AlignRuleOption](arkts-arkui-common-alignruleoption-i.md) \| LocalizedAlignRuleOptions \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## alignSelf

```TypeScript
default alignSelf(value: ItemAlign | undefined): this
```

Sets the alignment mode of the child components along the cross axis of the parent container.Default value: **ItemAlign.Auto**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default alignSelf(value: ItemAlign | undefined): this--><!--Device-CommonMethod-default alignSelf(value: ItemAlign | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ItemAlign](arkts-arkui-itemalign-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## allowDrop

```TypeScript
default allowDrop(value: Array<UniformDataType> | null | Array<string> | undefined): this
```

Allowed drop uniformData type for this node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default allowDrop(value: Array<UniformDataType> | null | Array<string> | undefined): this--><!--Device-CommonMethod-default allowDrop(value: Array<UniformDataType> | null | Array<string> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;UniformDataType&gt; \| null \| Array&lt;string&gt; \| undefined | Yes | the uniformData type for this node. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## animation

```TypeScript
default animation(value: AnimateParam | undefined): this
```

animation

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default animation(value: AnimateParam | undefined): this--><!--Device-CommonMethod-default animation(value: AnimateParam | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [AnimateParam](../arkts-components/arkts-arkui-animateparam-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## applyAttributesFinish

```TypeScript
default applyAttributesFinish(): void
```

Notify the component is fiished setting up its attributes.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default applyAttributesFinish(): void--><!--Device-CommonMethod-default applyAttributesFinish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aspectRatio

```TypeScript
default aspectRatio(value: double | undefined): this
```

Sets the aspect ratio of the component, which can be obtained using the following formula: width/height.&lt;br&gt;If only width and aspectRatio are set, the height is calculated using the following formula: width/aspectRatio.&lt;br&gt;If only height and aspectRatio are set, the width is calculated using the following formula: height x aspectRatio.&lt;br&gt;If width, height, and aspectRatio are all set, the explicitly set height is ignored, and the effective height is calculated using the following formula: width/aspectRatio.&lt;br&gt;This parameter takes effect only when a valid value greater than 0 is specified.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default aspectRatio(value: double | undefined): this--><!--Device-CommonMethod-default aspectRatio(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backdropBlur

```TypeScript
default backdropBlur(radius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this
```

Adds the background blur effect for the current component. The input parameter is the blur radius.The larger the blur radius, the more blurred the background. If the value is 0, the background blur is not blurred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backdropBlur(radius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this--><!--Device-CommonMethod-default backdropBlur(radius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double \| undefined | Yes | radius indicates radius of backdrop blur. |
| options | [BlurOptions](../arkts-components/arkts-arkui-bluroptions-i.md) | No | options indicates the backdrop blur options. |
| sysOptions | [SystemAdaptiveOptions](../arkts-components/arkts-arkui-systemadaptiveoptions-i.md) | No | system adaptive options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## background

```TypeScript
default background(content: CustomBuilder | ResourceColor | undefined, options?: BackgroundOptions): this
```

Set the background to a given CustomBuilder, or set it to a specific ResourceColor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default background(content: CustomBuilder | ResourceColor | undefined, options?: BackgroundOptions): this--><!--Device-CommonMethod-default background(content: CustomBuilder | ResourceColor | undefined, options?: BackgroundOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| ResourceColor \| undefined | Yes |  |
| options | [BackgroundOptions](../arkts-components/arkts-arkui-backgroundoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundBlurStyle

```TypeScript
default backgroundBlurStyle(style: BlurStyle | undefined, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this
```

Defines the blur style to apply between the background and content of a component.It encapsulates various blur radius, mask color, mask opacity, saturation.And brightness values through enum values.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundBlurStyle(style: BlurStyle | undefined, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this--><!--Device-CommonMethod-default backgroundBlurStyle(style: BlurStyle | undefined, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | Yes | Settings of the background blur style &lt;br&gt;including the blur radius, mask color, mask opacity, saturation, and brightness. |
| options | [BackgroundBlurStyleOptions](arkts-arkui-common-backgroundblurstyleoptions-i.md) | No |  |
| sysOptions | [SystemAdaptiveOptions](../arkts-components/arkts-arkui-systemadaptiveoptions-i.md) | No | system adaptive options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundBrightness

```TypeScript
default backgroundBrightness(params: BackgroundBrightnessOptions | undefined): this
```

Sets the background brightness of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundBrightness(params: BackgroundBrightnessOptions | undefined): this--><!--Device-CommonMethod-default backgroundBrightness(params: BackgroundBrightnessOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [BackgroundBrightnessOptions](../arkts-components/arkts-arkui-backgroundbrightnessoptions-i.md) \| undefined | Yes | Parameters for setting the background brightness. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundColor

```TypeScript
default backgroundColor(value: ResourceColor | ColorMetrics | undefined): this
```

Background color

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundColor(value: ResourceColor | ColorMetrics | undefined): this--><!--Device-CommonMethod-default backgroundColor(value: ResourceColor | ColorMetrics | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColorMetrics \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundEffect

```TypeScript
default backgroundEffect(options: BackgroundEffectOptions | undefined, sysOptions?: SystemAdaptiveOptions): this
```

options:background effect options.sysOptions: system adaptive options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundEffect(options: BackgroundEffectOptions | undefined, sysOptions?: SystemAdaptiveOptions): this--><!--Device-CommonMethod-default backgroundEffect(options: BackgroundEffectOptions | undefined, sysOptions?: SystemAdaptiveOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | Yes | options indicates the effect options. |
| sysOptions | [SystemAdaptiveOptions](../arkts-components/arkts-arkui-systemadaptiveoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundFilter

```TypeScript
default backgroundFilter(filter: Filter | undefined): this
```

Sets the visual effect of the background filter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundFilter(filter: Filter | undefined): this--><!--Device-CommonMethod-default backgroundFilter(filter: Filter | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) \| undefined | Yes | Filter effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined): this
```

Background image

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined): this--><!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap \| undefined | Yes | the background image source |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined, options: BackgroundImageOptions): this
```

Background image

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined, options: BackgroundImageOptions): this--><!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined, options: BackgroundImageOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap \| undefined | Yes | the background image source |
| options | [BackgroundImageOptions](../arkts-components/arkts-arkui-backgroundimageoptions-i.md) | Yes | config the options |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined, repeat: ImageRepeat): this
```

Background image src:Image address url

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined, repeat: ImageRepeat): this--><!--Device-CommonMethod-default backgroundImage(src: ResourceStr | PixelMap | undefined, repeat: ImageRepeat): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| PixelMap \| undefined | Yes |  |
| repeat | [ImageRepeat](arkts-arkui-imagerepeat-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImagePosition

```TypeScript
default backgroundImagePosition(value: Position | Alignment | undefined): this
```

Background image position x:Horizontal coordinate;y:Vertical axis coordinate.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImagePosition(value: Position | Alignment | undefined): this--><!--Device-CommonMethod-default backgroundImagePosition(value: Position | Alignment | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| Alignment \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImageResizable

```TypeScript
default backgroundImageResizable(value: ResizableOptions | undefined): this
```

Background image resizable.value:resizable options

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImageResizable(value: ResizableOptions | undefined): this--><!--Device-CommonMethod-default backgroundImageResizable(value: ResizableOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResizableOptions](../arkts-components/arkts-arkui-resizableoptions-i.md) \| undefined | Yes | Indicates the resizable options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## backgroundImageSize

```TypeScript
default backgroundImageSize(value: SizeOptions | ImageSize | undefined): this
```

Background image size

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default backgroundImageSize(value: SizeOptions | ImageSize | undefined): this--><!--Device-CommonMethod-default backgroundImageSize(value: SizeOptions | ImageSize | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| ImageSize \| undefined | Yes | The width and height of the background image. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContentCover

```TypeScript
default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, type?: ModalTransition): this
```

Binds a modal page to the component, whose visibility is subject to the isShow settings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, type?: ModalTransition): this--><!--Device-CommonMethod-default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, type?: ModalTransition): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | true means display content, false means hide content. |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | the content to be displayed. |
| type | [ModalTransition](../arkts-components/arkts-arkui-modaltransition-e.md) | No | transition type. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContentCover

```TypeScript
default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: ContentCoverOptions): this
```

Bind content cover

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: ContentCoverOptions): this--><!--Device-CommonMethod-default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: ContentCoverOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | true means display content, false means hide content. |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | the content to be displayed. |
| options | [ContentCoverOptions](arkts-arkui-common-contentcoveroptions-i.md) | No | options of content cover. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenu

```TypeScript
default bindContextMenu(content: CustomBuilder | undefined, responseType: ResponseType | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenu(content: CustomBuilder | undefined, responseType: ResponseType | undefined, options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenu(content: CustomBuilder | undefined, responseType: ResponseType | undefined, options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | Indicates the content of context menu. |
| responseType | [ResponseType](arkts-arkui-responsetype-e.md) \| undefined | Yes | Indicates response type of context menu, Long pressing with a mouse device is not supported. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenu

```TypeScript
default bindContextMenu(isShow: boolean | Bindable<boolean> | undefined, content: CustomBuilder | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to the component, whose visibility is subject to the isShow settings.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenu(isShow: boolean | Bindable<boolean> | undefined, content: CustomBuilder | undefined, options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenu(isShow: boolean | Bindable<boolean> | undefined, content: CustomBuilder | undefined, options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | Menu display switch, supports incoming twoway binding parameters. true means display content, false means hide content, default is false. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;The menu can be displayed properly only when the related page has been constructed. If this parameter is set to true before the construction is complete, display issues, such as misplacement, distortion, or failure to pop up, may occur. To trigger dragging by long presses is not supported. &lt;/p&gt; |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | Indicates the content of context menu. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenuByIsShow

```TypeScript
default bindContextMenuByIsShow(isShow: boolean | Bindable<boolean> | undefined,
        content: CustomBuilder | Array<MenuElement> | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to the component, whose visibility is subject to the isShow settings.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenuByIsShow(isShow: boolean | Bindable<boolean> | undefined,        content: CustomBuilder | Array<MenuElement> | undefined, options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenuByIsShow(isShow: boolean | Bindable<boolean> | undefined,        content: CustomBuilder | Array<MenuElement> | undefined, options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | Menu display switch, supports incoming two-way binding parameters. true means display content, false means hide content, default is false. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;The menu can be displayed properly only when the related page has been constructed. If this parameter is set to true before the construction is complete, display issues, such as misplacement, distortion, or failure to pop up, may occur. Dragging via long press is not supported. &lt;/p&gt; |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| Array&lt;MenuElement&gt; \| undefined | Yes | Indicates the content of context menu. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenuByResponseType

```TypeScript
default bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement> | undefined,
        responseType: ResponseType | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement> | undefined,        responseType: ResponseType | undefined, options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement> | undefined,        responseType: ResponseType | undefined, options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| Array&lt;MenuElement&gt; \| undefined | Yes | Indicates the content of context menu. |
| responseType | [ResponseType](arkts-arkui-responsetype-e.md) \| undefined | Yes | Indicates response type of context menu. Long pressing with a mouse device is not supported. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenuWithResponse

```TypeScript
default bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported. Long pressing with a mouse device is not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;[ResponseType](arkts-arkui-responsetype-e.md)&gt; \| undefined | Yes | Indicates the content of context menu. Undefined means unbinding. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindContextMenuWithResponseArray

```TypeScript
default bindContextMenuWithResponseArray(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,
        options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported. Long pressing with a mouse device is not supported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindContextMenuWithResponseArray(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,        options?: ContextMenuOptions): this--><!--Device-CommonMethod-default bindContextMenuWithResponseArray(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,        options?: ContextMenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;[ResponseType](arkts-arkui-responsetype-e.md)&gt; \| Array&lt;MenuElement&gt; \| undefined | Yes | Indicates the content of context menu. Undefined means unbinding. |
| options | [ContextMenuOptions](../arkts-components/arkts-arkui-contextmenuoptions-i.md) | No | Indicates the options of context menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindMenu

```TypeScript
default bindMenu(content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this
```

Menu control

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindMenu(content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this--><!--Device-CommonMethod-default bindMenu(content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | Array&lt;MenuElement&gt; \| CustomBuilder \| undefined | Yes | Indicates the content of menu. |
| options | [MenuOptions](arkts-arkui-common-menuoptions-i.md) | No | Indicates the options of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindMenu

```TypeScript
default bindMenu(isShow: boolean | Bindable<boolean> | undefined, content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this
```

Menu control

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindMenu(isShow: boolean | Bindable<boolean> | undefined, content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this--><!--Device-CommonMethod-default bindMenu(isShow: boolean | Bindable<boolean> | undefined, content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | Menu display switch, supports incoming two-way binding parameters. true means display menu, false means hide menu, default is false. |
| content | Array&lt;MenuElement&gt; \| CustomBuilder \| undefined | Yes | Indicates the content of menu. |
| options | [MenuOptions](arkts-arkui-common-menuoptions-i.md) | No | Indicates the options of menu. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindPopup

```TypeScript
default bindPopup(show: boolean | undefined, popup: PopupOptions | CustomPopupOptions | undefined): this
```

Popup control&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The popup can be displayed only after the entire page is fully constructed. Therefore, to avoid incorrect display positions and shapes, do not set this parameter to true while the page is still being constructed.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindPopup(show: boolean | undefined, popup: PopupOptions | CustomPopupOptions | undefined): this--><!--Device-CommonMethod-default bindPopup(show: boolean | undefined, popup: PopupOptions | CustomPopupOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| show | boolean \| undefined | Yes | Whether to show the popup, default is false. |
| popup | [PopupOptions](arkts-arkui-arkui-advanced-popup-popupoptions-i.md) \| CustomPopupOptions \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## bindSheet

```TypeScript
default bindSheet(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: SheetOptions): this
```

Bind sheet

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindSheet(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: SheetOptions): this--><!--Device-CommonMethod-default bindSheet(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: SheetOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isShow | boolean \| Bindable&lt;boolean&gt; \| undefined | Yes | true means display sheet, false means hide sheet. |
| builder | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes | the sheet to be displayed. |
| options | [SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md) | No | options of sheet. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## bindTips

```TypeScript
default bindTips(message: TipsMessageType | undefined, options?: TipsOptions): this
```

Tips control

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default bindTips(message: TipsMessageType | undefined, options?: TipsOptions): this--><!--Device-CommonMethod-default bindTips(message: TipsMessageType | undefined, options?: TipsOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | [TipsMessageType](../arkts-components/arkts-arkui-tipsmessagetype-t.md) \| undefined | Yes |  |
| options | [TipsOptions](../arkts-components/arkts-arkui-tipsoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blendMode

```TypeScript
default blendMode(value: BlendMode | undefined, type?: BlendApplyType): this
```

Defines how the component's content (including the content of it child components)is blended with the existing content on the canvas (possibly offscreen canvas) below.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default blendMode(value: BlendMode | undefined, type?: BlendApplyType): this--><!--Device-CommonMethod-default blendMode(value: BlendMode | undefined, type?: BlendApplyType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BlendMode](arkts-arkui-common-blendmode-e.md) \| undefined | Yes | Blend mode. &lt;br&gt;Default value: **BlendMode.NONE**. &lt;br&gt;**NOTE：**&lt;br&gt;When **BlendMode.NONE** is used, the blend effect is **BlendMode.SRC_OVER** by default, and **BlendApplyType** does not take effect. |
| type | [BlendApplyType](../arkts-components/arkts-arkui-blendapplytype-e.md) | No | Whether the blend mode is implemented offscreen. &lt;br&gt;Default value: **BlendApplyType.FAST**. &lt;br&gt;**NOTE：**&lt;br&gt;1. **BlendApplyType.FAST**: The blend mode is not implemented offscreen. &lt;br&gt;2. **BlendApplyType.OFFSCREEN**: An offscreen canvas of the size of the current component is created. The content of the current component (including child components) is then drawn onto the offscreen canvas, and blended with the existing content on the canvas below using the specified blend mode. This approach may cause issues with screen capture for APIs such as linearGradientBlur&lt;sup&gt;12+&lt;/sup&gt;, backgroundEffect, and brightness. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## blur

```TypeScript
default blur(blurRadius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this
```

Adds the content blurring effect for the current component. The input parameter is the blurring radius.The larger the blurring radius, the more blurring the content.If the value is 0, the content blurring effect is not blurring.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default blur(blurRadius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this--><!--Device-CommonMethod-default blur(blurRadius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blurRadius | double \| undefined | Yes | value indicates radius of backdrop blur. |
| options | [BlurOptions](../arkts-components/arkts-arkui-bluroptions-i.md) | No | options indicates blur options. |
| sysOptions | [SystemAdaptiveOptions](../arkts-components/arkts-arkui-systemadaptiveoptions-i.md) | No | system adaptive options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## border

```TypeScript
default border(value: BorderOptions | undefined): this
```

Sets the border.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default border(value: BorderOptions | undefined): this--><!--Device-CommonMethod-default border(value: BorderOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BorderOptions](arkts-arkui-borderoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## borderColor

```TypeScript
default borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this
```

Sets the border color.Default value: **Color.Black**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this--><!--Device-CommonMethod-default borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| EdgeColors \| LocalizedEdgeColors \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## borderImage

```TypeScript
default borderImage(value: BorderImageOption | undefined): this
```

Sets the border image of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default borderImage(value: BorderImageOption | undefined): this--><!--Device-CommonMethod-default borderImage(value: BorderImageOption | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BorderImageOption](../arkts-components/arkts-arkui-borderimageoption-i.md) \| undefined | Yes | Border image or border gradient. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## borderRadius

```TypeScript
default borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses | undefined, type?: RenderStrategy | undefined): this
```

Sets the radius of the border rounded corners. The radius is restricted by the component size. The maximum value is half of the component width or height.NOTE 1. **RenderStrategy.FAST**: The current component and its child components will be drawn directly  onto the canvas with rounded corners applied. 2. **RenderStrategy.OFFSCREEN**: The current component and its child components will first be rendered onto  an off-screen canvas, then undergo a rounded corner clipping, and finally be drawn onto the main canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses | undefined, type?: RenderStrategy | undefined): this--><!--Device-CommonMethod-default borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses | undefined, type?: RenderStrategy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| BorderRadiuses \| LocalizedBorderRadiuses \| undefined | Yes |  |
| type | [RenderStrategy](arkts-arkui-renderstrategy-e.md) \| undefined | No | Application types for drawing rounded corners. Default value: **RenderStrategy.FAST**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## borderStyle

```TypeScript
default borderStyle(value: BorderStyle | EdgeStyles | undefined): this
```

Sets the border style.Default value: **BorderStyle.Solid**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default borderStyle(value: BorderStyle | EdgeStyles | undefined): this--><!--Device-CommonMethod-default borderStyle(value: BorderStyle | EdgeStyles | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [BorderStyle](arkts-arkui-borderstyle-e.md) \| EdgeStyles \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## borderWidth

```TypeScript
default borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths | undefined): this
```

Sets the border width.Percentage values are not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths | undefined): this--><!--Device-CommonMethod-default borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| EdgeWidths \| LocalizedEdgeWidths \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## brightness

```TypeScript
default brightness(value: double | undefined): this
```

Applies a brightness effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default brightness(value: double | undefined): this--><!--Device-CommonMethod-default brightness(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Brightness of the component. The value **1** indicates no effects. The value **0** indicates the complete darkness. If the value is less than **1**, the brightness decreases. If the value is greater than **1**, the brightness increases. A larger value indicates a higher brightness. A brightness of 2 turns the component completely white. &lt;br&gt;Default value: **1.0**&lt;br&gt;Recommended value range: [0, 2]. &lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the value **0**. &lt;br&gt;**Widget capability**: This API can be used in ArkTS widgets since API version 9. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## chainMode

```TypeScript
default chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this
```

Sets the parameters of the chain in which the component is the head.&lt;br&gt;This parameter has effect only when the parent container is RelativeContainer.&lt;br&gt;The chain head is the first component in the chain that satisfies the chain formation rules.In a horizontal layout, it starts from the left (or from the right in a mirrored language layout). In a vertical layout, it starts from the top.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this--><!--Device-CommonMethod-default chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| direction | [Axis](arkts-arkui-axis-e.md) \| undefined | Yes | indicates direction of the chain |
| style | [ChainStyle](../arkts-components/arkts-arkui-chainstyle-e.md) \| undefined | Yes | indicates style of the chain |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## chainWeight

```TypeScript
default chainWeight(chainWeight: ChainWeightOptions | undefined): this
```

Sets the weight of the component in a chain, which is used to re-lay out components that form the chain.&lt;br&gt;This API has effect only when the parent container is RelativeContainer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default chainWeight(chainWeight: ChainWeightOptions | undefined): this--><!--Device-CommonMethod-default chainWeight(chainWeight: ChainWeightOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| chainWeight | [ChainWeightOptions](arkts-arkui-chainweightoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## clickEffect

```TypeScript
default clickEffect(value: ClickEffect | null | undefined): this
```

The click effect level and scale number.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default clickEffect(value: ClickEffect | null | undefined): this--><!--Device-CommonMethod-default clickEffect(value: ClickEffect | null | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ClickEffect](../arkts-components/arkts-arkui-clickeffect-i.md) \| null \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## clip

```TypeScript
default clip(value: boolean | undefined): this
```

Sets whether to clip the areas of child components that extend beyond this component's boundaries,That is, whether to perform clipping based on the edge contour of the parent container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default clip(value: boolean | undefined): this--><!--Device-CommonMethod-default clip(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to perform clipping based on the edge contour of the parent container. &lt;br&gt;Default value: **false**. &lt;br&gt;**true**: Perform clipping. **false**: Do not perform clipping. &lt;br&gt;If this parameter is set to **true**. &lt;br&gt;child components exceeding the current component's bounds will not respond to bound gesture events. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## clipShape

```TypeScript
default clipShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this
```

Clips this component based on the given shape.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default clipShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this--><!--Device-CommonMethod-default clipShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| EllipseShape \| PathShape \| RectShape \| undefined | Yes | Shape that the component to be clipped into. The clipped area remains responsive to bound gesture events. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## colorBlend

```TypeScript
default colorBlend(value: Color | string | Resource | undefined): this
```

Applies a color blend effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default colorBlend(value: Color | string | Resource | undefined): this--><!--Device-CommonMethod-default colorBlend(value: Color | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Color](arkts-arkui-color-e.md) \| string \| Resource \| undefined | Yes | Color to blend with the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## compositingFilter

```TypeScript
default compositingFilter(filter: Filter | undefined): this
```

Sets the visual effect of the compositing filter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default compositingFilter(filter: Filter | undefined): this--><!--Device-CommonMethod-default compositingFilter(filter: Filter | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) \| undefined | Yes | Filter effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## constraintSize

```TypeScript
default constraintSize(value: ConstraintSizeOptions | undefined): this
```

Sets the constraint size of the component, which is used to limit the size range during component layout.Default value: **{minWidth: 0, maxWidth: Infinity, minHeight: 0, maxHeight: Infinity}**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default constraintSize(value: ConstraintSizeOptions | undefined): this--><!--Device-CommonMethod-default constraintSize(value: ConstraintSizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contrast

```TypeScript
default contrast(value: double | undefined): this
```

Applies a contrast effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default contrast(value: double | undefined): this--><!--Device-CommonMethod-default contrast(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Contrast of the component. The input parameter is a contrast value. If the value is **1**, the source image is displayed. If the value is greater than 1, a larger value indicates a higher contrast and a clearer image. If the value is less than 1, a smaller value indicates a lower contrast is. If the value is **0**, the image becomes all gray. The unit is percentage. &lt;br&gt;Default value: **1.0**. &lt;br&gt;Recommended value range: [0, 10). &lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the value **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## customProperty

```TypeScript
default customProperty(name: string, value: CustomProperty): this
```

Sets the custom property of the current component.This API does not work for custom components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default customProperty(name: string, value: CustomProperty): this--><!--Device-CommonMethod-default customProperty(name: string, value: CustomProperty): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | the name of the custom property. |
| value | [CustomProperty](arkts-arkui-customproperty-t.md) | Yes | the value of the custom property. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default debugLine(sourceLine: string, moduleName?: string): this--><!--Device-CommonMethod-default debugLine(sourceLine: string, moduleName?: string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceLine | string | Yes | the source code line. |
| moduleName | string | No | module to which the component belongs. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## defaultFocus

```TypeScript
default defaultFocus(value: boolean | undefined): this
```

Set default focused component when a page create.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default defaultFocus(value: boolean | undefined): this--><!--Device-CommonMethod-default defaultFocus(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | True means to set the component as the default focus, and the value false has no effect. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## direction

```TypeScript
default direction(value: Direction | undefined): this
```

Sets how elements are laid out along the main axis of the container.Default value: **Direction.Auto**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default direction(value: Direction | undefined): this--><!--Device-CommonMethod-default direction(value: Direction | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Direction](arkts-arkui-direction-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## displayPriority

```TypeScript
default displayPriority(value: double | undefined): this
```

Sets the display priority for the component in the layout container.&lt;br&gt;This parameter is only effective in Row, Column, and Flex (single-line) container components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default displayPriority(value: double | undefined): this--><!--Device-CommonMethod-default displayPriority(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## doubleSided

```TypeScript
default doubleSided(value: boolean | undefined): this
```

Sets whether to component is double-sided.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default doubleSided(value: boolean | undefined): this--><!--Device-CommonMethod-default doubleSided(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to component is double-sided. **true**: Both front and back sides are visible (default). **false**: Only to front side is visible, to back side is hidden when rotated. When **value** is **undefined**, the component reverts to default double-sided setting (**true**). |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## dragPreview

```TypeScript
default dragPreview(preview: CustomBuilder | DragItemInfo | string | undefined, config?: PreviewConfiguration): this
```

Set preview of the component for dragging process

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default dragPreview(preview: CustomBuilder | DragItemInfo | string | undefined, config?: PreviewConfiguration): this--><!--Device-CommonMethod-default dragPreview(preview: CustomBuilder | DragItemInfo | string | undefined, config?: PreviewConfiguration): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| preview | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| DragItemInfo \| string \| undefined | Yes | preview of the component for dragging process |
| config | [PreviewConfiguration](arkts-arkui-common-previewconfiguration-i.md) | No | drag preview configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## dragPreviewOptions

```TypeScript
default dragPreviewOptions(value: DragPreviewOptions | undefined, options?: DragInteractionOptions): this
```

Set the selectable area drag preview options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default dragPreviewOptions(value: DragPreviewOptions | undefined, options?: DragInteractionOptions): this--><!--Device-CommonMethod-default dragPreviewOptions(value: DragPreviewOptions | undefined, options?: DragInteractionOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [DragPreviewOptions](../arkts-components/arkts-arkui-dragpreviewoptions-i.md) \| undefined | Yes | preview options value. |
| options | [DragInteractionOptions](../arkts-components/arkts-arkui-draginteractionoptions-i.md) | No | drag interaction options value. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

Enable the selectable area can be dragged.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default draggable(value: boolean | undefined): this--><!--Device-CommonMethod-default draggable(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | true means the area can be dragged, false means the area can't be dragged. The default value is false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## drawModifier

```TypeScript
default drawModifier(modifier: DrawModifier | undefined): this
```

Sets the drawModifier of the current component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default drawModifier(modifier: DrawModifier | undefined): this--><!--Device-CommonMethod-default drawModifier(modifier: DrawModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [DrawModifier](../arkts-components/arkts-arkui-drawmodifier-c.md) \| undefined | Yes | drawModifier used to draw, or undefined if it is not available. Default value: undefined A custom modifier applies only to the FrameNode of the currently bound component, not to its subnodes. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableClickSoundEffect

```TypeScript
default enableClickSoundEffect(enabled: boolean | undefined): this
```

Set whether this component should have sound effects enabled for clicking.

Sound effects playback is affected by the audio-related settings in the device system settings.When the user sets the device to silent mode, sound effects cannot be played.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default enableClickSoundEffect(enabled: boolean | undefined): this--><!--Device-CommonMethod-default enableClickSoundEffect(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | indicates whether this component should have sound effects enabled for clicking. &lt;br&gt;Pass in undefined to reset the default value, default value is true, but even it's true, the sound effect is only supported in some specific devices. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enabled

```TypeScript
default enabled(value: boolean | undefined): this
```

If the value is true, the component is available and can respond to operations such as clicking.If it is set to false, click operations are not responded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default enabled(value: boolean | undefined): this--><!--Device-CommonMethod-default enabled(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## expandSafeArea

```TypeScript
default expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): this
```

Sets the safe area to be expanded to.&lt;br&gt;default:{types: [SafeAreaType.SYSTEM, SafeAreaType.CUTOUT, SafeAreaType.KEYBOARD],edges: [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM, SafeAreaEdge.START, SafeAreaEdge.END]}

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): this--><!--Device-CommonMethod-default expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;SafeAreaType&gt; | No | Indicates the types of the safe area. |
| edges | Array&lt;SafeAreaEdge&gt; | No | Indicates the edges of the safe area. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The component instance. |

## flexBasis

```TypeScript
default flexBasis(value: double | string | undefined): this
```

Sets the base size of the component in the main axis of the parent container.Default value: **'auto'**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default flexBasis(value: double | string | undefined): this--><!--Device-CommonMethod-default flexBasis(value: double | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## flexGrow

```TypeScript
default flexGrow(value: double | undefined): this
```

Sets the percentage of the parent container's remaining space that is allocated to the component.Default value: **0**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default flexGrow(value: double | undefined): this--><!--Device-CommonMethod-default flexGrow(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## flexShrink

```TypeScript
default flexShrink(value: double | undefined): this
```

Sets the percentage of the parent container's shrink size that is allocated to the component.Default value: 0 when the parent container is Column or Row, 1 when the parent container is Flex..

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default flexShrink(value: double | undefined): this--><!--Device-CommonMethod-default flexShrink(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## focusBox

```TypeScript
default focusBox(style: FocusBoxStyle | undefined): this
```

Set the component's focusBox style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default focusBox(style: FocusBoxStyle | undefined): this--><!--Device-CommonMethod-default focusBox(style: FocusBoxStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [FocusBoxStyle](arkts-arkui-focusboxstyle-i.md) \| undefined | Yes | Component's focusBox style. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## focusOnTouch

```TypeScript
default focusOnTouch(value: boolean | undefined): this
```

Set a component focused when the component be touched.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default focusOnTouch(value: boolean | undefined): this--><!--Device-CommonMethod-default focusOnTouch(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | True means the component is focusable on touch, false means the component is not focusable on touch. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## focusScopeId

```TypeScript
default focusScopeId(id: string | undefined, isGroup?: boolean, arrowStepOut?: boolean): this
```

Set container as a focus group with a specific identifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default focusScopeId(id: string | undefined, isGroup?: boolean, arrowStepOut?: boolean): this--><!--Device-CommonMethod-default focusScopeId(id: string | undefined, isGroup?: boolean, arrowStepOut?: boolean): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| undefined | Yes | focus scope identifier. |
| isGroup | boolean | No | whether this scope is a focus group, the default value is false. |
| arrowStepOut | boolean | No | whether the arrow keys can move focus from inside the focus group to outside, only effective when isGroup is true, the default value is true. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## focusScopePriority

```TypeScript
default focusScopePriority(scopeId: string | undefined, priority?: FocusPriority): this
```

Set the focus priority of component in a specific focus scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default focusScopePriority(scopeId: string | undefined, priority?: FocusPriority): this--><!--Device-CommonMethod-default focusScopePriority(scopeId: string | undefined, priority?: FocusPriority): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scopeId | string \| undefined | Yes |  |
| priority | [FocusPriority](arkts-arkui-focuspriority-e.md) | No | the default value is AUTO |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## focusable

```TypeScript
default focusable(value: boolean | undefined): this
```

Set focusable.Components that have default interaction logic, such as Button and TextInput, are focusable by default. Other components, such as Text and Image, are not focusable by default. Only focusable components can trigger a focus event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default focusable(value: boolean | undefined): this--><!--Device-CommonMethod-default focusable(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## foregroundBlurStyle

```TypeScript
default foregroundBlurStyle(style: BlurStyle | undefined, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this
```

Applies a foreground blur style to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default foregroundBlurStyle(style: BlurStyle | undefined, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this--><!--Device-CommonMethod-default foregroundBlurStyle(style: BlurStyle | undefined, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | Yes | Settings of the foreground blur style. |
| options | [ForegroundBlurStyleOptions](arkts-arkui-common-foregroundblurstyleoptions-i.md) | No |  |
| sysOptions | [SystemAdaptiveOptions](../arkts-components/arkts-arkui-systemadaptiveoptions-i.md) | No | system adaptive options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## foregroundColor

```TypeScript
default foregroundColor(value: ResourceColor | ColoringStrategy | undefined): this
```

Sets the foreground color of the component.If the component does not have a foreground color set, it inherits the color from its parent component by default.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default foregroundColor(value: ResourceColor | ColoringStrategy | undefined): this--><!--Device-CommonMethod-default foregroundColor(value: ResourceColor | ColoringStrategy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| ColoringStrategy \| undefined | Yes | Foreground color. &lt;br&gt;The value can be a specific color or a coloring strategy. Property animations are supported. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## foregroundEffect

```TypeScript
default foregroundEffect(options: ForegroundEffectOptions | undefined): this
```

Foreground effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default foregroundEffect(options: ForegroundEffectOptions | undefined): this--><!--Device-CommonMethod-default foregroundEffect(options: ForegroundEffectOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ForegroundEffectOptions](arkts-arkui-common-foregroundeffectoptions-i.md) \| undefined | Yes | options indicates the effect options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## foregroundFilter

```TypeScript
default foregroundFilter(filter: Filter | undefined): this
```

Sets the visual effect of the foreground (content) filter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default foregroundFilter(filter: Filter | undefined): this--><!--Device-CommonMethod-default foregroundFilter(filter: Filter | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) \| undefined | Yes | Filter effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## freeze

```TypeScript
default freeze(value: boolean | undefined): this
```

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default freeze(value: boolean | undefined): this--><!--Device-CommonMethod-default freeze(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. If the opacity of the component is not 1, the drawing effect may vary depending on the value. &lt;br&gt;Default value: **false**. &lt;br&gt; **true**: Freeze the component. &lt;br&gt;**false**: Do not freeze the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## geometryTransition

```TypeScript
default geometryTransition(id: string | undefined, options?: GeometryTransitionOptions): this
```

Shared geometry transition

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default geometryTransition(id: string | undefined, options?: GeometryTransitionOptions): this--><!--Device-CommonMethod-default geometryTransition(id: string | undefined, options?: GeometryTransitionOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| undefined | Yes | geometry transition id |
| options | [GeometryTransitionOptions](../arkts-components/arkts-arkui-geometrytransitionoptions-i.md) | No | Indicates the options of geometry transition. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## gesture

```TypeScript
default gesture(gesture: GestureType, mask?: GestureMask): this
```

Bind gesture recognition.gesture:Bound Gesture Type,mask:GestureMask;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default gesture(gesture: GestureType, mask?: GestureMask): this--><!--Device-CommonMethod-default gesture(gesture: GestureType, mask?: GestureMask): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureType](arkts-arkui-gesturetype-t.md) | Yes |  |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## gestureModifier

```TypeScript
default gestureModifier(modifier: GestureModifier | undefined): this
```

Sets the gesture modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default gestureModifier(modifier: GestureModifier | undefined): this--><!--Device-CommonMethod-default gestureModifier(modifier: GestureModifier | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [GestureModifier](arkts-arkui-common-gesturemodifier-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## grayscale

```TypeScript
default grayscale(value: double | undefined): this
```

Applies a grayscale effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default grayscale(value: double | undefined): this--><!--Device-CommonMethod-default grayscale(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Grayscale conversion ratio of the component. &lt;br&gt;If the value is **1.0**, the component is completely converted to grayscale. &lt;br&gt;If the value is **0.0**, the component remains unchanged. Between **0** and **1**, &lt;br&gt;the value applies a linear multiplier on the grayscale effect. The unit is percentage. &lt;br&gt;Default value: **0.0**. &lt;br&gt;Value range: [0.0, 1.0]. &lt;p&gt;**NOTE：**: &lt;br&gt;A value less than **0.0** evaluates to the value **0.0**. &lt;br&gt;A value greater than **1.0** evaluates to the value **1.0**. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## groupDefaultFocus

```TypeScript
default groupDefaultFocus(value: boolean | undefined): this
```

Set default focused component when focus on a focus group.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default groupDefaultFocus(value: boolean | undefined): this--><!--Device-CommonMethod-default groupDefaultFocus(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | True means the component is the default focus of the parent container, and false means the component is not the default focus of the parent container. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## height

```TypeScript
default height(heightValue: Length | LayoutPolicy | undefined): this
```

Sets the height of the component or its vertical layout policy. By default, the component uses the height required for its content. If the height of the component is greater than that of the parent container, the component will be drawn beyond the parent container scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default height(heightValue: Length | LayoutPolicy | undefined): this--><!--Device-CommonMethod-default height(heightValue: Length | LayoutPolicy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| heightValue | [Length](arkts-arkui-length-t.md) \| LayoutPolicy \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hitTestBehavior

```TypeScript
default hitTestBehavior(value: HitTestMode | undefined): this
```

Sets how the component behaves during hit testing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default hitTestBehavior(value: HitTestMode | undefined): this--><!--Device-CommonMethod-default hitTestBehavior(value: HitTestMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [HitTestMode](arkts-arkui-hittestmode-e.md) \| undefined | Yes | the hit test mode. @default HitTestMode.default - Both the node and its child nodes respond to the hit test of a touch event, but its sibling nodes are blocked from the hit test. The hit test for ancestor nodes is not affected. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hoverEffect

```TypeScript
default hoverEffect(value: HoverEffect | undefined): this
```

Set hover effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default hoverEffect(value: HoverEffect | undefined): this--><!--Device-CommonMethod-default hoverEffect(value: HoverEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [HoverEffect](arkts-arkui-hovereffect-e.md) \| undefined | Yes | Hover effect of the component in hover state. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hueRotate

```TypeScript
default hueRotate(value: double | string | undefined): this
```

Rotates the hue of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default hueRotate(value: double | string | undefined): this--><!--Device-CommonMethod-default hueRotate(value: double | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| undefined | Yes | Hue rotation angle of the component. &lt;br&gt;A rotation of 360 degrees leaves the color unchanged. &lt;br&gt;A rotation of 180 degrees and then -180 degrees also leaves the color unchanged. &lt;br&gt;When the data type is number, the value **90** is equivalent to **'90deg'**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## id

```TypeScript
default id(value: string | undefined): this
```

Id. User can set an id to the component to identify it.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default id(value: string | undefined): this--><!--Device-CommonMethod-default id(value: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## ignoreLayoutSafeArea

```TypeScript
default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

Expands the layout safe area of a component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this--><!--Device-CommonMethod-default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| types | Array&lt;LayoutSafeAreaType&gt; \| undefined | No | The region type to expand the component's layout safe area into. The default value is LayoutSafeAreaType.SYSTEM. |
| edges | Array&lt;LayoutSafeAreaEdge&gt; \| undefined | No | The set of edges for which to ignore layout safe area. The default value is LayoutSafeAreaEdge.ALL. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## inspectorLabel

```TypeScript
default inspectorLabel(label: string | undefined): this
```

Set the component's inspector label which only display on DevEco Studio.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default inspectorLabel(label: string | undefined): this--><!--Device-CommonMethod-default inspectorLabel(label: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string \| undefined | Yes | the inspector label. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## invert

```TypeScript
default invert(value: double | InvertOptions | undefined): this
```

Invert the input image. Value defines the scale of the conversion. 100% of the value is a complete reversal.A value of 0% does not change the image. (Percentage)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default invert(value: double | InvertOptions | undefined): this--><!--Device-CommonMethod-default invert(value: double | InvertOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| InvertOptions \| undefined | Yes | value indicates the scale of the conversion or the options of invert. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## key

```TypeScript
default key(value: string | undefined): this
```

Key. User can set an key to the component to identify it.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default key(value: string | undefined): this--><!--Device-CommonMethod-default key(value: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## keyboardShortcut

```TypeScript
default keyboardShortcut(value: string | FunctionKey | undefined, keys: Array<ModifierKey> | undefined, action?: () => void): this
```

Sets hot keys

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default keyboardShortcut(value: string | FunctionKey | undefined, keys: Array<ModifierKey> | undefined, action?: () => void): this--><!--Device-CommonMethod-default keyboardShortcut(value: string | FunctionKey | undefined, keys: Array<ModifierKey> | undefined, action?: () => void): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| FunctionKey \| undefined | Yes | Character of the combination key. |
| keys | Array&lt;[ModifierKey](arkts-arkui-modifierkey-e.md)&gt; \| undefined | Yes | The modifier keys modify the action of key when the key are pressed at the same time. |
| action | () =&gt; void | No | Callback function, triggered when the shortcut keyboard is pressed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## layoutGravity

```TypeScript
default layoutGravity(alignment: LocalizedAlignment | undefined): this
```

Defines the align rules of child component in Stack container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default layoutGravity(alignment: LocalizedAlignment | undefined): this--><!--Device-CommonMethod-default layoutGravity(alignment: LocalizedAlignment | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| alignment | [LocalizedAlignment](arkts-arkui-localizedalignment-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## layoutWeight

```TypeScript
default layoutWeight(value: double | string | undefined): this
```

Sets the weight of the component during layout. A component with this attribute is allocated space along the main axis of its parent container (Row, Column, or Flex) based on its specified weight.Default value: **0**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default layoutWeight(value: double | string | undefined): this--><!--Device-CommonMethod-default layoutWeight(value: double | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## lightUpEffect

```TypeScript
default lightUpEffect(value: double | undefined): this
```

Applies a light up effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default lightUpEffect(value: double | undefined): this--><!--Device-CommonMethod-default lightUpEffect(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Light up degree of the component. &lt;br&gt;The value ranges from 0 to 1. &lt;br&gt;If the value is **0**, the component is dark. If the value is **1**, the component is fully illuminated. &lt;br&gt;Between **0** and **1**, a larger value indicates higher luminance. &lt;br&gt;A value less than 0 is handled as the value **0**. &lt;br&gt;A value greater than 1 is handled as the value **1**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## linearGradient

```TypeScript
default linearGradient(value: LinearGradientOptions | undefined): this
```

Linear Gradient angle: Angle of Linear Gradient. The default value is 180;direction: Direction of Linear Gradient. The default value is GradientDirection.Bottom;colors: Color description for gradients.repeating: repeating. The default value is false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default linearGradient(value: LinearGradientOptions | undefined): this--><!--Device-CommonMethod-default linearGradient(value: LinearGradientOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LinearGradientOptions](../arkts-components/arkts-arkui-lineargradientoptions-i.md) \| undefined | Yes | Linear gradient. &lt;br&gt;If **options** is **undefined**, the linear gradient is disabled. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## linearGradientBlur

```TypeScript
default linearGradientBlur(value: double | undefined, options: LinearGradientBlurOptions | undefined): this
```

Applies a linear gradient foreground blur effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default linearGradientBlur(value: double | undefined, options: LinearGradientBlurOptions | undefined): this--><!--Device-CommonMethod-default linearGradientBlur(value: double | undefined, options: LinearGradientBlurOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | the blurring radius. The larger the blurring radius, the more blurring the content, and if the value is 0, the content blurring effect is not blurring. |
| options | [LinearGradientBlurOptions](arkts-arkui-common-lineargradientbluroptions-i.md) \| undefined | Yes | the linear gradient blur options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## margin

```TypeScript
default margin(value: Margin | Length | LocalizedMargin | undefined): this
```

Sets the margin of the component.Default value: **0**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default margin(value: Margin | Length | LocalizedMargin | undefined): this--><!--Device-CommonMethod-default margin(value: Margin | Length | LocalizedMargin | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Margin](arkts-arkui-margin-t.md) \| Length \| LocalizedMargin \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## markAnchor

```TypeScript
default markAnchor(value: Position | LocalizedPosition | undefined): this
```

Sets the anchor for locating the component, which is used to move the component further away from the position specified by position or offset.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default markAnchor(value: Position | LocalizedPosition | undefined): this--><!--Device-CommonMethod-default markAnchor(value: Position | LocalizedPosition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| LocalizedPosition \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mask

```TypeScript
default mask(value: ProgressMask | undefined): this
```

Adds a mask to the component to indicate the progress.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default mask(value: ProgressMask | undefined): this--><!--Device-CommonMethod-default mask(value: ProgressMask | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ProgressMask](../arkts-components/arkts-arkui-progressmask-c.md) \| undefined | Yes | Mask to add to the component, which allows for dynamic adjustment of progress, maximum value, and color settings. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## maskShape

```TypeScript
default maskShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this
```

Adds a mask of the specified shape to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default maskShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this--><!--Device-CommonMethod-default maskShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| EllipseShape \| PathShape \| RectShape \| undefined | Yes | Mask of the specified shape to add to the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## materialFilter

```TypeScript
default materialFilter(filter: Filter | undefined): this
```

Sets the visual effect of the material filter. The effects it contains are rendered at a level before the shadow.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default materialFilter(filter: Filter | undefined): this--><!--Device-CommonMethod-default materialFilter(filter: Filter | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) \| undefined | Yes | Filter effect parameters. Undefined means to none material filter. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## monopolizeEvents

```TypeScript
default monopolizeEvents(monopolize: boolean | undefined): this
```

Sets whether the component exclusively handles events.true: The component exclusively handles events. false: The component does not exclusively handle events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default monopolizeEvents(monopolize: boolean | undefined): this--><!--Device-CommonMethod-default monopolizeEvents(monopolize: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| monopolize | boolean \| undefined | Yes | indicate the monopoly of events @default false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## motionBlur

```TypeScript
default motionBlur(value: MotionBlurOptions | undefined): this
```

Apply a motion blur effect to the component being scaled or moved.1.Do not use this API in intra-component transitions, shared element transitions,implicit element transitions, or particle animations. Doing so may cause unexpected results.2.The **radius** parameter of **motionBlur** must be set to **0** for the initial state.Otherwise, there may be unexpected results during a cold start.3.This API must be used together with the **onFinish** parameter of **AnimateParam**.Its **radius** parameter must be set to **0** when the animation ends; otherwise, there may be unexpected results.4.When using this API, do not frequently change the blur radius of the same component;otherwise, there may be unexpected results.For example, if you frequently click the image in the example, the blur effect may not work sometimes.5.To avoid unexpected results, make sure the coordinates of the motion blur anchor point are the same as those of the animation scaling anchor point.6.To avoid unexpected results, set the blur radius to a value less than 1.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default motionBlur(value: MotionBlurOptions | undefined): this--><!--Device-CommonMethod-default motionBlur(value: MotionBlurOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MotionBlurOptions](arkts-arkui-common-motionbluroptions-i.md) \| undefined | Yes | Motion blur options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## motionPath

```TypeScript
default motionPath(value: MotionPathOptions | undefined): this
```

Set the motion path of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default motionPath(value: MotionPathOptions | undefined): this--><!--Device-CommonMethod-default motionPath(value: MotionPathOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MotionPathOptions](arkts-arkui-common-motionpathoptions-i.md) \| undefined | Yes | Motion path of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mouseResponseRegion

```TypeScript
default mouseResponseRegion(value: Array<Rectangle> | Rectangle | undefined): this
```

Sets the mouse response region of current component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default mouseResponseRegion(value: Array<Rectangle> | Rectangle | undefined): this--><!--Device-CommonMethod-default mouseResponseRegion(value: Array<Rectangle> | Rectangle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;Rectangle&gt; \| Rectangle \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute |

## nextFocus

```TypeScript
default nextFocus(nextStep: FocusMovement | undefined): this
```

Set nextFocus.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default nextFocus(nextStep: FocusMovement | undefined): this--><!--Device-CommonMethod-default nextFocus(nextStep: FocusMovement | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nextStep | [FocusMovement](../arkts-components/arkts-arkui-focusmovement-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## obscured

```TypeScript
default obscured(reasons: Array<ObscuredReasons> | undefined): this
```

Sets obscured

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default obscured(reasons: Array<ObscuredReasons> | undefined): this--><!--Device-CommonMethod-default obscured(reasons: Array<ObscuredReasons> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reasons | Array&lt;[ObscuredReasons](arkts-arkui-obscuredreasons-e.md)&gt; \| undefined | Yes | reasons of obscuration |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## offset

```TypeScript
default offset(value: Position | Edges | LocalizedEdges | undefined): this
```

Sets the offset of the component relative to its original position.&lt;br&gt;The offset attribute does not affect the layout of the parent container.It adjusts the component position only during drawing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default offset(value: Position | Edges | LocalizedEdges | undefined): this--><!--Device-CommonMethod-default offset(value: Position | Edges | LocalizedEdges | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| Edges \| LocalizedEdges \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAccessibilityActionIntercept

```TypeScript
default onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback | undefined): this
```

Register accessibility action intercept callback,when accessibility action is to be executed,the callback will be executed

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback | undefined): this--><!--Device-CommonMethod-default onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AccessibilityActionInterceptCallback](../arkts-components/arkts-arkui-accessibilityactioninterceptcallback-t.md) \| undefined | Yes | accessibility action intercept callback function |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAccessibilityFocus

```TypeScript
default onAccessibilityFocus(callback: AccessibilityFocusCallback | undefined): this
```

Register accessibility focus callback,when the component is focused or out of focus,the callback will be executed

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAccessibilityFocus(callback: AccessibilityFocusCallback | undefined): this--><!--Device-CommonMethod-default onAccessibilityFocus(callback: AccessibilityFocusCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AccessibilityFocusCallback](../arkts-components/arkts-arkui-accessibilityfocuscallback-t.md) \| undefined | Yes | accessibility focus callback function |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAccessibilityHover

```TypeScript
default onAccessibilityHover(callback: AccessibilityCallback | undefined): this
```

Trigger a accessibility hover event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAccessibilityHover(callback: AccessibilityCallback | undefined): this--><!--Device-CommonMethod-default onAccessibilityHover(callback: AccessibilityCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) \| undefined | Yes | A callback instance used when the component is touched after accessibility mode is enabled. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAccessibilityHoverTransparent

```TypeScript
default onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback | undefined): this
```

prompt for current component and descendants unable to handle accessibility hover event

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback | undefined): this--><!--Device-CommonMethod-default onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) \| undefined | Yes | A callback instance used when current component and descendants not handled accessibility hover event |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAppear

```TypeScript
default onAppear(event: (() => void) | undefined): this
```

This callback is triggered when a component mounts a display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAppear(event: (() => void) | undefined): this--><!--Device-CommonMethod-default onAppear(event: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAreaChange

```TypeScript
default onAreaChange(event: ((oldValue: Area, newValue: Area) => void) | undefined): this
```

This callback is triggered when the size or position of this component change finished.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAreaChange(event: ((oldValue: Area, newValue: Area) => void) | undefined): this--><!--Device-CommonMethod-default onAreaChange(event: ((oldValue: Area, newValue: Area) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((oldValue: Area, newValue: Area) =&gt; void) \| undefined | Yes | event callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAreaChange

```TypeScript
default onAreaChange (event: AreaChangeCallback, options?: AreaChangeOptions): this
```

This callback is triggered when the size or position of this component has finished changing.The interval between two area change callbacks will not be less than the expected update interval.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAreaChange (event: AreaChangeCallback, options?: AreaChangeOptions): this--><!--Device-CommonMethod-default onAreaChange (event: AreaChangeCallback, options?: AreaChangeOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [AreaChangeCallback](../arkts-components/arkts-arkui-areachangecallback-t.md) | Yes | Callback invoked when the area of the component changes. |
| options | [AreaChangeOptions](arkts-arkui-common-areachangeoptions-i.md) | No | The options for the area change event. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAttach

```TypeScript
default onAttach(callback: VoidCallback | undefined): this
```

This callback is triggered when a component mounts to view tree.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAttach(callback: VoidCallback | undefined): this--><!--Device-CommonMethod-default onAttach(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAxisEvent

```TypeScript
default onAxisEvent(event: Callback<AxisEvent> | undefined): this
```

Handle axis events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onAxisEvent(event: Callback<AxisEvent> | undefined): this--><!--Device-CommonMethod-default onAxisEvent(event: Callback<AxisEvent> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;AxisEvent&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onBlur

```TypeScript
default onBlur(event: (() => void) | undefined): this
```

Triggered when the current component loses focus.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onBlur(event: (() => void) | undefined): this--><!--Device-CommonMethod-default onBlur(event: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChildTouchTest

```TypeScript
default onChildTouchTest(event: ((value: Array<TouchTestInfo>) => TouchResult) | undefined): this
```

Called to specify how to perform the touch test on the children of this component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onChildTouchTest(event: ((value: Array<TouchTestInfo>) => TouchResult) | undefined): this--><!--Device-CommonMethod-default onChildTouchTest(event: ((value: Array<TouchTestInfo>) => TouchResult) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((value: Array&lt;TouchTestInfo&gt;) =&gt; TouchResult) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onClick

```TypeScript
default onClick(event: ((event: ClickEvent) => void) | undefined): this
```

Called when a click event occurs.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt; Since API version 9, the following constraints apply when this API is used in service widgets:&lt;br&gt; Click events cannot be triggered if the finger is pressed for more than 800 ms.&lt;br&gt; Click events cannot be triggered if the finger moves more than 20 px after pressing down.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onClick(event: ((event: ClickEvent) => void) | undefined): this--><!--Device-CommonMethod-default onClick(event: ((event: ClickEvent) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: ClickEvent) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onClick

```TypeScript
default onClick(event: Callback<ClickEvent> | undefined, distanceThreshold: double | undefined): this
```

Trigger a click event when a click is clicked, move distance should smaller than distanceThreshold.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt; If the distanceThreshold value specified is less than or equal to 0 vp, it will be converted to the default value. Since API version 9, the following constraints apply when this API is used in service widgets:&lt;br&gt; Click events cannot be triggered if the finger is pressed for more than 800 ms.&lt;br&gt; Click events cannot be triggered if the finger moves more than 20 px after pressing down.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onClick(event: Callback<ClickEvent> | undefined, distanceThreshold: double | undefined): this--><!--Device-CommonMethod-default onClick(event: Callback<ClickEvent> | undefined, distanceThreshold: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;ClickEvent&gt; \| undefined | Yes | this function callback executed when the click action is recognized |
| distanceThreshold | double \| undefined | Yes | the distance threshold of finger's movement when detecting a click action @default (2^31-1)vp |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDetach

```TypeScript
default onDetach(callback: VoidCallback | undefined): this
```

This callback is triggered when a component is detached from view tree.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDetach(callback: VoidCallback | undefined): this--><!--Device-CommonMethod-default onDetach(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDigitalCrown

```TypeScript
default onDigitalCrown(handler: Callback<CrownEvent> | undefined): this
```

Digital crown input.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDigitalCrown(handler: Callback<CrownEvent> | undefined): this--><!--Device-CommonMethod-default onDigitalCrown(handler: Callback<CrownEvent> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;CrownEvent&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDisAppear

```TypeScript
default onDisAppear(event: (() => void) | undefined): this
```

This callback is triggered when component uninstallation disappears.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDisAppear(event: (() => void) | undefined): this--><!--Device-CommonMethod-default onDisAppear(event: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDragEnd

```TypeScript
default onDragEnd(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

This function is called when the drag event is end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragEnd(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this--><!--Device-CommonMethod-default onDragEnd(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; void) \| undefined | Yes | indicates the function to be called. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## onDragEnter

```TypeScript
default onDragEnter(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the component is dragged to the range of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragEnter(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this--><!--Device-CommonMethod-default onDragEnter(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDragLeave

```TypeScript
default onDragLeave(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the component is dragged out of the component range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragLeave(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this--><!--Device-CommonMethod-default onDragLeave(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDragMove

```TypeScript
default onDragMove(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the drag moves within the range of a placeable component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragMove(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this--><!--Device-CommonMethod-default onDragMove(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDragSpringLoading

```TypeScript
default onDragSpringLoading(callback: Callback<SpringLoadingContext> | null | undefined, configuration?: DragSpringLoadingConfiguration): this
```

Enables the component as a drag-and-drop target with spring loading functionality.

When a dragged object hovers over the target, it triggers a callback notification. Spring Loading is an enhanced feature for drag-and-drop operations, allowing users to automatically trigger view transitions during dragging by hovering (hover) without needing to use another hand.This feature is primarily designed to enhance the smoothness and efficiency of drag-and-drop operations. Below are some common scenarios suitable for supporting this feature:  
 - In a file manager, when dragging a file and hovering over a folder, the folder is automatically opened.  
 - On a desktop launcher, when dragging a file and hovering over an application icon, the application is  
 automatically opened.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragSpringLoading(callback: Callback<SpringLoadingContext> | null | undefined, configuration?: DragSpringLoadingConfiguration): this--><!--Device-CommonMethod-default onDragSpringLoading(callback: Callback<SpringLoadingContext> | null | undefined, configuration?: DragSpringLoadingConfiguration): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;SpringLoadingContext&gt; \| null \| undefined | Yes | Registers the callback for spring loading response, or sets it to null to disable the support for spring loading. |
| configuration | [DragSpringLoadingConfiguration](../arkts-components/arkts-arkui-dragspringloadingconfiguration-t.md) | No | The initialized spring loading configuration which is only used when the entire spring detecting. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## onDragStart

```TypeScript
default onDragStart(event: ((event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo) | undefined): this
```

After a listener is bound, the component can be dragged. After the drag occurs, a callback is triggered.(To be triggered, press and hold for 170 milliseconds (ms))

&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The global builder is not supported.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDragStart(event: ((event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo) | undefined): this--><!--Device-CommonMethod-default onDragStart(event: ((event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; CustomBuilder \| DragItemInfo) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDrop

```TypeScript
default onDrop(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

The component bound to this event can be used as the drag release target.This callback is triggered when the drag behavior is stopped within the scope of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDrop(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this--><!--Device-CommonMethod-default onDrop(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDrop

```TypeScript
default onDrop(eventCallback: OnDragEventCallback | undefined, dropOptions: DropOptions): this
```

The component bound to this event can be used as the drag release target.This callback is triggered when the drag behavior is stopped within the scope of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onDrop(eventCallback: OnDragEventCallback | undefined, dropOptions: DropOptions): this--><!--Device-CommonMethod-default onDrop(eventCallback: OnDragEventCallback | undefined, dropOptions: DropOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventCallback | [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) \| undefined | Yes | event callback. |
| dropOptions | [DropOptions](../arkts-components/arkts-arkui-dropoptions-i.md) | Yes | the drop handling options. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onFocus

```TypeScript
default onFocus(event: (() => void) | undefined): this
```

Trigger a event when got focus.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onFocus(event: (() => void) | undefined): this--><!--Device-CommonMethod-default onFocus(event: (() => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onFocusAxisEvent

```TypeScript
default onFocusAxisEvent(event: Callback<FocusAxisEvent> | undefined): this
```

Trigger a FocusAxisEvent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onFocusAxisEvent(event: Callback<FocusAxisEvent> | undefined): this--><!--Device-CommonMethod-default onFocusAxisEvent(event: Callback<FocusAxisEvent> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;FocusAxisEvent&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureCollectIntercept

```TypeScript
default onGestureCollectIntercept(callback: GestureCollectInterceptCallback): this
```

When the events and gestures on this node and higher-priority nodes have been collected, the callback is executed.This callback is used to intervene in the event and gesture collection results.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onGestureCollectIntercept(callback: GestureCollectInterceptCallback): this--><!--Device-CommonMethod-default onGestureCollectIntercept(callback: GestureCollectInterceptCallback): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureCollectInterceptCallback](../arkts-components/arkts-arkui-gesturecollectinterceptcallback-t.md) | Yes | A callback instance used when the component does a touch test. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureJudgeBegin

```TypeScript
default onGestureJudgeBegin(callback: ((gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult) | undefined): this
```

When a gesture bound to this component will be accepted, a user-defined callback is triggered to get the result

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onGestureJudgeBegin(callback: ((gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult) | undefined): this--><!--Device-CommonMethod-default onGestureJudgeBegin(callback: ((gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((gestureInfo: GestureInfo, event: BaseGestureEvent) =&gt; GestureJudgeResult) \| undefined | Yes | A callback instance used when a gesture bound to this component will be accepted. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureRecognizerJudgeBegin

```TypeScript
default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined): this
```

Binds a custom gesture recognizer judgment callback to the component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined): this--><!--Device-CommonMethod-default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) \| undefined | Yes | A callback instance used when a gesture bound to this component will be accepted. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureRecognizerJudgeBegin

```TypeScript
default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined, exposeInnerGesture: boolean | undefined): this
```

Binds a custom gesture recognizer judgment callback to the component.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt; For a composite component, setting exposeInnerGesture to true exposes the internal gesture recognizer of the&lt;br&gt; composite component in the current parameter callback. Currently, only the Tabs component is supported.

&lt;br&gt; Do not set exposeInnerGesture for other components. When exposeInnerGesture is set to false, this API provides the same functionality&lt;br&gt; as the onGestureRecognizerJudgeBegin API.&lt;/p&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined, exposeInnerGesture: boolean | undefined): this--><!--Device-CommonMethod-default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined, exposeInnerGesture: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) \| undefined | Yes | A callback instance used when a gesture bound to this component will be accepted. |
| exposeInnerGesture | boolean \| undefined | Yes | This parameter is a flag. This flag determines whether to expose internal gestures. @default false |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onHover

```TypeScript
default onHover(event: ((isHover: boolean, event: HoverEvent) => void) | undefined): this
```

Trigger a hover event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onHover(event: ((isHover: boolean, event: HoverEvent) => void) | undefined): this--><!--Device-CommonMethod-default onHover(event: ((isHover: boolean, event: HoverEvent) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((isHover: boolean, event: HoverEvent) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onHoverMove

```TypeScript
default onHoverMove(event: Callback<HoverEvent> | undefined): this
```

Trigger a hover move event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onHoverMove(event: Callback<HoverEvent> | undefined): this--><!--Device-CommonMethod-default onHoverMove(event: Callback<HoverEvent> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;HoverEvent&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onKeyEvent

```TypeScript
default onKeyEvent(event: Callback<KeyEvent, boolean> | undefined): this
```

Keyboard input

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onKeyEvent(event: Callback<KeyEvent, boolean> | undefined): this--><!--Device-CommonMethod-default onKeyEvent(event: Callback<KeyEvent, boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;KeyEvent, boolean&gt; \| undefined | Yes | Callback for handling the key event. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onKeyEventDispatch

```TypeScript
default onKeyEventDispatch(event: Callback<KeyEvent, boolean> | undefined): this
```

Customize the handling and distribution of key events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onKeyEventDispatch(event: Callback<KeyEvent, boolean> | undefined): this--><!--Device-CommonMethod-default onKeyEventDispatch(event: Callback<KeyEvent, boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;KeyEvent, boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onKeyPreIme

```TypeScript
default onKeyPreIme(event: Callback<KeyEvent, boolean> | undefined): this
```

Handle keyboard events before input method events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onKeyPreIme(event: Callback<KeyEvent, boolean> | undefined): this--><!--Device-CommonMethod-default onKeyPreIme(event: Callback<KeyEvent, boolean> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;KeyEvent, boolean&gt; \| undefined | Yes | Callback for handling the key event. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onMouse

```TypeScript
default onMouse(event: ((event: MouseEvent) => void) | undefined): this
```

Triggered when the component is clicked by a mouse button or the mouse pointer moves on the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onMouse(event: ((event: MouseEvent) => void) | undefined): this--><!--Device-CommonMethod-default onMouse(event: ((event: MouseEvent) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: MouseEvent) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onNeedSoftkeyboard

```TypeScript
default onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): this
```

Called when component is focused, the return value indicates whether keyboard is needed.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): this--><!--Device-CommonMethod-default onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onNeedSoftkeyboardCallback | [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onPreDrag

```TypeScript
default onPreDrag(callback: Callback<PreDragStatus> | undefined): this
```

After binding, a callback is triggered when the preDrag status change finished.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onPreDrag(callback: Callback<PreDragStatus> | undefined): this--><!--Device-CommonMethod-default onPreDrag(callback: Callback<PreDragStatus> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;PreDragStatus&gt; \| undefined | Yes | callback - The callback will be triggered when the preDrag status change. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## onSizeChange

```TypeScript
default onSizeChange(event: SizeChangeCallback | undefined): this
```

This callback is triggered when the component size changes due to layout updates.This event is not triggered for render attribute changes caused by re-rendering.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onSizeChange(event: SizeChangeCallback | undefined): this--><!--Device-CommonMethod-default onSizeChange(event: SizeChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [SizeChangeCallback](../arkts-components/arkts-arkui-sizechangecallback-t.md) \| undefined | Yes | event callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onTouch

```TypeScript
default onTouch(event: ((event: TouchEvent) => void) | undefined): this
```

Invoked when a touch event is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onTouch(event: ((event: TouchEvent) => void) | undefined): this--><!--Device-CommonMethod-default onTouch(event: ((event: TouchEvent) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | ((event: TouchEvent) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onTouchIntercept

```TypeScript
default onTouchIntercept(callback: Callback<TouchEvent, HitTestMode> | undefined): this
```

When the component does a touch test, a user-defined callback is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onTouchIntercept(callback: Callback<TouchEvent, HitTestMode> | undefined): this--><!--Device-CommonMethod-default onTouchIntercept(callback: Callback<TouchEvent, HitTestMode> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TouchEvent, [HitTestMode](arkts-arkui-hittestmode-e.md)&gt; \| undefined | Yes | A callback instance used when the component does a touch test. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onTouchTestDone

```TypeScript
default onTouchTestDone(callback: TouchTestDoneCallback | undefined): this
```

Register one callback which will be executed when all gesture recognizers are collected done, this happens when user touchs down, the system do hit test process and collect gesture recognizers base on the touch position, after this, before handling any move events, the component can use this interface to know which gesture recognizers will participate in the recognition and competing with each other.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onTouchTestDone(callback: TouchTestDoneCallback | undefined): this--><!--Device-CommonMethod-default onTouchTestDone(callback: TouchTestDoneCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) \| undefined | Yes | A callback instance used when all gesture recognizers are collected. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onVisibleAreaApproximateChange

```TypeScript
default onVisibleAreaApproximateChange(options: VisibleAreaEventOptions | undefined, event: VisibleAreaChangeCallback | undefined): this
```

Set or reset the callback which is triggered when the visibleArea of component changed.The interval between two visible area change callbacks will not be less than the expected update interval.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onVisibleAreaApproximateChange(options: VisibleAreaEventOptions | undefined, event: VisibleAreaChangeCallback | undefined): this--><!--Device-CommonMethod-default onVisibleAreaApproximateChange(options: VisibleAreaEventOptions | undefined, event: VisibleAreaChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [VisibleAreaEventOptions](arkts-arkui-common-visibleareaeventoptions-i.md) \| undefined | Yes | The options for the visibility event. |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | Yes | The callback will be triggered when the visibleArea of component changed and get close to any number in ratios defined by options. If set undefined will reset the target callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onVisibleAreaChange

```TypeScript
default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined): this
```

Trigger a visible area change event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined): this--><!--Device-CommonMethod-default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ratios | Array&lt;double&gt; \| undefined | Yes | Threshold array. Each threshold represents a ratio of the component's visible area to the component's total area. The value range of the threshold is [0.0, 1.0]. |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | Yes | Callback for visible area changes of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onVisibleAreaChange

```TypeScript
default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined, measureFromViewport: boolean | undefined): this
```

Trigger a visible area change event.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined, measureFromViewport: boolean | undefined): this--><!--Device-CommonMethod-default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined, measureFromViewport: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ratios | Array&lt;double&gt; \| undefined | Yes | Threshold array. Each threshold represents a ratio of the component's visible area to the component's total area. The value range of the threshold is [0.0, 1.0]. |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | Yes | Callback for visible area changes of the component. |
| measureFromViewport | boolean \| undefined | Yes | When this parameter is set to true, the parts of the component that exceed the parent component's area will also be included in the visible area calculation. However, this only applies if the parent component does not explicitly set the clip property to true. If the parent component sets clip to true, regardless of the value of this parameter, the parts that exceed the parent component's area will still be treated as invisible in the visible area calculation. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## opacity

```TypeScript
default opacity(value: double | Resource | undefined): this
```

Sets the opacity of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default opacity(value: double | Resource | undefined): this--><!--Device-CommonMethod-default opacity(value: double | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| Resource \| undefined | Yes | Opacity of the component. The value ranges from 0 to 1. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## outline

```TypeScript
default outline(value: OutlineOptions | undefined): this
```

Sets the outline attributes in one declaration.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default outline(value: OutlineOptions | undefined): this--><!--Device-CommonMethod-default outline(value: OutlineOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [OutlineOptions](arkts-arkui-outlineoptions-i.md) \| undefined | Yes | Outline attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## outlineColor

```TypeScript
default outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this
```

Sets the color of the outline.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this--><!--Device-CommonMethod-default outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| EdgeColors \| LocalizedEdgeColors \| undefined | Yes | Outline color. &lt;br&gt;Default value: **Color.Black**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## outlineRadius

```TypeScript
default outlineRadius(value: Dimension | OutlineRadiuses | undefined): this
```

Sets the radius of the outline corners.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default outlineRadius(value: Dimension | OutlineRadiuses | undefined): this--><!--Device-CommonMethod-default outlineRadius(value: Dimension | OutlineRadiuses | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| OutlineRadiuses \| undefined | Yes | adius of the outline corners. Percentage values are not supported. &lt;br&gt;Default value: **0**. &lt;br&gt;Maximum effective value: Component width/2 + outlineWidth or component height/2 + outlineWidth. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## outlineStyle

```TypeScript
default outlineStyle(value: OutlineStyle | EdgeOutlineStyles | undefined): this
```

Sets the style of the outline.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default outlineStyle(value: OutlineStyle | EdgeOutlineStyles | undefined): this--><!--Device-CommonMethod-default outlineStyle(value: OutlineStyle | EdgeOutlineStyles | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [OutlineStyle](arkts-arkui-common-outlinestyle-e.md) \| EdgeOutlineStyles \| undefined | Yes | Outline style. &lt;br&gt;Default value: **OutlineStyle.SOLID**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## outlineWidth

```TypeScript
default outlineWidth(value: Dimension | EdgeOutlineWidths | undefined): this
```

Sets the thickness of the outline.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default outlineWidth(value: Dimension | EdgeOutlineWidths | undefined): this--><!--Device-CommonMethod-default outlineWidth(value: Dimension | EdgeOutlineWidths | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| EdgeOutlineWidths \| undefined | Yes | Outline thickness. Percentage values are not supported. &lt;br&gt;Default value: **0**Outline thickness. Percentage values are not supported. &lt;br&gt;Default value: **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## overlay

```TypeScript
default overlay(value: string | CustomBuilder | ComponentContent<Object> | undefined, options?: OverlayOptions): this
```

Add mask text to the current component. The layout is the same as that of the current component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default overlay(value: string | CustomBuilder | ComponentContent<Object> | undefined, options?: OverlayOptions): this--><!--Device-CommonMethod-default overlay(value: string | CustomBuilder | ComponentContent<Object> | undefined, options?: OverlayOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| CustomBuilder \| ComponentContent&lt;Object&gt; \| undefined | Yes |  |
| options | [OverlayOptions](arkts-arkui-common-overlayoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## padding

```TypeScript
default padding(value: Padding | Length | LocalizedPadding | undefined): this
```

Sets the padding of the component.Default value: **0**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default padding(value: Padding | Length | LocalizedPadding | undefined): this--><!--Device-CommonMethod-default padding(value: Padding | Length | LocalizedPadding | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| Length \| LocalizedPadding \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## parallelGesture

```TypeScript
default parallelGesture(gesture: GestureType, mask?: GestureMask): this
```

Binding gestures that can be triggered simultaneously with internal component gestures gesture:Bound Gesture Type,mask:GestureMask;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default parallelGesture(gesture: GestureType, mask?: GestureMask): this--><!--Device-CommonMethod-default parallelGesture(gesture: GestureType, mask?: GestureMask): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureType](arkts-arkui-gesturetype-t.md) | Yes |  |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## pixelRound

```TypeScript
default pixelRound(value: PixelRoundPolicy | undefined): this
```

Sets the pixel rounding policy for the current component in the specified direction.&lt;br&gt;If a direction is not set, the pixels are rounded to the nearest whole number in that direction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default pixelRound(value: PixelRoundPolicy | undefined): this--><!--Device-CommonMethod-default pixelRound(value: PixelRoundPolicy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelRoundPolicy](arkts-arkui-common-pixelroundpolicy-i.md) \| undefined | Yes | indicates the rounding policy for the bounds of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## pixelStretchEffect

```TypeScript
default pixelStretchEffect(options: PixelStretchEffectOptions | undefined): this
```

Applies a pixel stretch effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default pixelStretchEffect(options: PixelStretchEffectOptions | undefined): this--><!--Device-CommonMethod-default pixelStretchEffect(options: PixelStretchEffectOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PixelStretchEffectOptions](arkts-arkui-common-pixelstretcheffectoptions-i.md) \| undefined | Yes | Pixel stretch effect options. &lt;br&gt;The value includes the length by which a pixel is stretched toward the four edges. &lt;p&gt;**NOTE：**: &lt;br&gt;1. If the length is a positive value, the original image is stretched, and the image size increases. The edge pixels grow by the set length toward the top, bottom, left, and right edges. &lt;br&gt;2. If the length is a negative value, the original image shrinks as follows, but the image size remains unchanged: &lt;br&gt;Shrinking mode: &lt;br&gt;(1) The image shrinks from the four edges by the absolute value of length set through **options**. &lt;br&gt;(2) The image is stretched back to the original size with edge pixels. &lt;br&gt;3. Constraints on **options**: &lt;br&gt;(1) The length values for the four edges must be all positive or all negative. That is, the four edges are stretched or shrink at the same time in the same direction. &lt;br&gt;(2) The length values must all be a percentage or a specific value. Combined use of the percentage and specific value is not allowed. &lt;br&gt;(3) If the input value is invalid, the image is displayed as {0, 0, 0, 0}, that is, the image is the same as the original image. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## position

```TypeScript
default position(value: Position | Edges | LocalizedEdges | undefined): this
```

Sets the absolute position of the component relative to the position of the parent component.&lt;br&gt;The attribute is not available for a layout container whose width and height are zero.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default position(value: Position | Edges | LocalizedEdges | undefined): this--><!--Device-CommonMethod-default position(value: Position | Edges | LocalizedEdges | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| Edges \| LocalizedEdges \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## priorityGesture

```TypeScript
default priorityGesture(gesture: GestureType, mask?: GestureMask): this
```

Binding Preferential Recognition Gestures gesture:Bound Gesture Type,mask:GestureMask;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default priorityGesture(gesture: GestureType, mask?: GestureMask): this--><!--Device-CommonMethod-default priorityGesture(gesture: GestureType, mask?: GestureMask): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| gesture | [GestureType](arkts-arkui-gesturetype-t.md) | Yes |  |
| mask | [GestureMask](arkts-arkui-gesturemask-e.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radialGradient

```TypeScript
default radialGradient(value: RadialGradientOptions | undefined): this
```

Creates a radial gradient.

Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default radialGradient(value: RadialGradientOptions | undefined): this--><!--Device-CommonMethod-default radialGradient(value: RadialGradientOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RadialGradientOptions](../arkts-components/arkts-arkui-radialgradientoptions-i.md) \| undefined | Yes | Radial gradient. &lt;br&gt;- **center**: center of the radial gradient, that is, the coordinates relative to the upper left corner of the current component. &lt;br&gt;- **radius**: radius of the radial gradient. &lt;br&gt; Value range: [0, +∞). &lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 is treated as **0**. &lt;br&gt;- colors: array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped. &lt;br&gt;- **repeating**: whether the colors are repeated. &lt;br&gt; Default value: **false**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## renderFit

```TypeScript
default renderFit(fitMode: RenderFit | undefined): this
```

How the final state of the component's content is rendered during its width and height animation process.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default renderFit(fitMode: RenderFit | undefined): this--><!--Device-CommonMethod-default renderFit(fitMode: RenderFit | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fitMode | [RenderFit](arkts-arkui-renderfit-e.md) \| undefined | Yes | How the final state of the component's content is rendered during. &lt;br&gt;its width and height animation process. &lt;br&gt;If **renderFit** is not set, the default value **RenderFit.TOP_LEFT** is used. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## renderGroup

```TypeScript
default renderGroup(value: boolean | undefined): this
```

Sets whether the component and its child components are rendered off the screen as a whole before being blended with its parent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default renderGroup(value: boolean | undefined): this--><!--Device-CommonMethod-default renderGroup(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether the component and its child components are rendered off the screen as a whole before being blended with its parent. If the opacity of the component is not 1, the drawing effect may vary depending on the value. &lt;br&gt;Default value: **false**. &lt;br&gt; The value **true** means the component and its child components are rendered off the screen as a whole, and **false** means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## responseRegion

```TypeScript
default responseRegion(value: Array<Rectangle> | Rectangle | undefined): this
```

Sets the response region of the current component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default responseRegion(value: Array<Rectangle> | Rectangle | undefined): this--><!--Device-CommonMethod-default responseRegion(value: Array<Rectangle> | Rectangle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;Rectangle&gt; \| Rectangle \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## responseRegionList

```TypeScript
default responseRegionList(regions: Array<ResponseRegion> | undefined): this
```

Sets the response region list of the current component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default responseRegionList(regions: Array<ResponseRegion> | undefined): this--><!--Device-CommonMethod-default responseRegionList(regions: Array<ResponseRegion> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regions | Array&lt;ResponseRegion&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute |

## restoreId

```TypeScript
default restoreId(value: int | undefined): this
```

id for distribute identification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default restoreId(value: int | undefined): this--><!--Device-CommonMethod-default restoreId(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## reuse

```TypeScript
default reuse(options: ReuseOptions | undefined): this
```

Reuse id is used for identify the reuse type of each @ComponentV2 custom component, which can give user control of sub-component recycle and reuse.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default reuse(options: ReuseOptions | undefined): this--><!--Device-CommonMethod-default reuse(options: ReuseOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ReuseOptions](../arkts-components/arkts-arkui-reuseoptions-i.md) \| undefined | Yes | The configuration parameter for reusable custom component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## reuseId

```TypeScript
default reuseId(id: string | undefined): this
```

Reuse id is used for identify the reuse type for each custom node.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default reuseId(id: string | undefined): this--><!--Device-CommonMethod-default reuseId(id: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| undefined | Yes | The id for reusable custom node. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## rotate

```TypeScript
default rotate(value: RotateOptions | RotateAngleOptions | undefined): this
```

Set component rotation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default rotate(value: RotateOptions | RotateAngleOptions | undefined): this--><!--Device-CommonMethod-default rotate(value: RotateOptions | RotateAngleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RotateOptions](../arkts-components/arkts-arkui-rotateoptions-i.md) \| RotateAngleOptions \| undefined | Yes | default:{x:0,y:0,z:0,centerX:'50%',centerY:'50%',centerZ:0,perspective:0} |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## safeAreaPadding

```TypeScript
default safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding | undefined): this
```

Sets the safe area padding. It enables a container to add a component-level safe area for child components to expand into.Default value: **LengthMetrics.vp(0)**

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding | undefined): this--><!--Device-CommonMethod-default safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| paddingValue | [Padding](arkts-arkui-units-padding-i.md) \| LengthMetrics \| LocalizedPadding \| undefined | Yes | Indicates safeArea padding values |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## saturate

```TypeScript
default saturate(value: double | undefined): this
```

Applies a saturation effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default saturate(value: double | undefined): this--><!--Device-CommonMethod-default saturate(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Saturation of the component. The saturation is the ratio of the chromatic component to the achromatic component (gray) in a color. If the value is **1**, the original image is displayed. If the value is greater than **1**, a higher percentage of the chromatic component indicates a higher saturation. If the value is less than **1**, a higher percentage of the achromatic component indicates a lower saturation. The unit is percentage. &lt;br&gt;Default value: **1.0**. &lt;br&gt;Recommended value range: [0, 50). &lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 evaluates to the value **0**. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## scale

```TypeScript
default scale(value: ScaleOptions | undefined): this
```

Scales the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default scale(value: ScaleOptions | undefined): this--><!--Device-CommonMethod-default scale(value: ScaleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScaleOptions](../arkts-components/arkts-arkui-scaleoptions-i.md) \| undefined | Yes | Scale ratio along the x-, y-, and z-axis. The default value is **1**. &lt;br&gt;**centerX** and **centerY** are used to set the scale center point. &lt;br&gt;default:{x:1,y:1,z:1,centerX:'50%',centerY:'50%'} |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sepia

```TypeScript
default sepia(value: double | undefined): this
```

Sepia conversion ratio of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default sepia(value: double | undefined): this--><!--Device-CommonMethod-default sepia(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Sepia conversion ratio of the component. If the value is **1**, the image is completely sepia. If the value is **0**, the component remains unchanged. The unit is percentage. &lt;br&gt; Value range: [0, +∞). |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## shadow

```TypeScript
default shadow(value: ShadowOptions | ShadowStyle | undefined): this
```

Applies a shadow effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default shadow(value: ShadowOptions | ShadowStyle | undefined): this--><!--Device-CommonMethod-default shadow(value: ShadowOptions | ShadowStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-common-shadowoptions-i.md) \| ShadowStyle \| undefined | Yes | Shadow of the component. &lt;br&gt;When the value type is **ShadowOptions**, the blur radius, shadow color, and offset along the x-axis and y-axis can be specified. &lt;br&gt;When the value type is **ShadowStyle**, the shadow style can be specified. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sharedTransition

```TypeScript
default sharedTransition(id: string | undefined, options?: sharedTransitionOptions): this
```

If the components of the two pages are configured with the same ID.The shared element transition is performed during transition.If the parameter is set to an empty string, the shared element transition does not occur.For details about the options parameter, see the options parameter description.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default sharedTransition(id: string | undefined, options?: sharedTransitionOptions): this--><!--Device-CommonMethod-default sharedTransition(id: string | undefined, options?: sharedTransitionOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| undefined | Yes | Transition of the shared element. &lt;br&gt;If the same **id** value is configured for a component on the two pages, &lt;br&gt;this component is considered as a shared element of the pages. &lt;br&gt;If the **id** value is an empty string, no transition will be applied to the component. |
| options | [sharedTransitionOptions](arkts-arkui-common-sharedtransitionoptions-i.md) | No | Parameters of the shared element transition animation. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## shouldBuiltInRecognizerParallelWith

```TypeScript
default shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback | undefined): this
```

Provides a callback to set the parallel relationship between built-in gestures and gestures of other components in the response chain.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback | undefined): this--><!--Device-CommonMethod-default shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) \| undefined | Yes | A callback instance used when a component is doing touch test. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## shouldRecognizerParallelWith

```TypeScript
default shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback | undefined): this
```

Provides a callback to set the parallel relationship between gestures of current component and gestures of other components in the response chain.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback | undefined): this--><!--Device-CommonMethod-default shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ShouldRecognizerParallelWithCallback](../arkts-components/arkts-arkui-shouldrecognizerparallelwithcallback-t.md) \| undefined | Yes | A callback instance used when a component is doing touch test. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## size

```TypeScript
default size(value: SizeOptions | undefined): this
```

Sets the size of the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default size(value: SizeOptions | undefined): this--><!--Device-CommonMethod-default size(value: SizeOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## smartGestureShortcut

```TypeScript
default smartGestureShortcut(options?: SmartGestureShortcutOptions): this
```

Enable or disable specific smart gesture shortcuts, and set response priorities for them.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default smartGestureShortcut(options?: SmartGestureShortcutOptions): this--><!--Device-CommonMethod-default smartGestureShortcut(options?: SmartGestureShortcutOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SmartGestureShortcutOptions](arkts-arkui-common-smartgestureshortcutoptions-i.md) | No | Options for configuring smart gesture shortcuts. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return component instance who call the method. |

## sphericalEffect

```TypeScript
default sphericalEffect(value: double | undefined): this
```

Applies a spherical effect to the component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default sphericalEffect(value: double | undefined): this--><!--Device-CommonMethod-default sphericalEffect(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | Spherical degree of the component. &lt;br&gt;The value ranges from 0 to 1. &lt;p&gt;**NOTE：**: &lt;br&gt;1. If the value is **0**, the component remains unchanged. If the value is 1, the component is completely spherical. Between **0** and **1**, a larger value indicates a higher spherical degree. A value less than 0 is handled as the value **0**. A value greater than 1 is handled as the value **1**. &lt;br&gt;2. The component's shadow and outer stroke do not support spherical effects. &lt;br&gt;3. If the value is greater than 0, the component is frozen and not updated, and its content is drawn to the transparent offscreen buffer. To update the component attributes, set the value to **0**. &lt;/p&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stateStyles

```TypeScript
default stateStyles(value: StateStyles | undefined): this
```

Sets styles for component state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default stateStyles(value: StateStyles | undefined): this--><!--Device-CommonMethod-default stateStyles(value: StateStyles | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [StateStyles](../arkts-components/arkts-arkui-statestyles-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## sweepGradient

```TypeScript
default sweepGradient(value: SweepGradientOptions | undefined): this
```

Creates a sweep gradient.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default sweepGradient(value: SweepGradientOptions | undefined): this--><!--Device-CommonMethod-default sweepGradient(value: SweepGradientOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SweepGradientOptions](arkts-arkui-common-sweepgradientoptions-i.md) \| undefined | Yes | Sweep gradient, which can sweep around the specified center point in the 0–360 degree range. If the rotation angle exceeds the range, a monochrome color instead of a gradient will be drawn.&lt;br&gt;- **center**: center of the sweep gradient, that is, the coordinates relative to the upper left corner of the current component. &lt;br&gt;- **start**: start angle of the sweep gradient. &lt;br&gt; Default value: **0**&lt;br&gt;If the angle is specified with a string, only the deg, grad, rad, and turn types are supported.&lt;br&gt;- **end**: end angle of the sweep gradient. &lt;br&gt; Default value: **0**&lt;br&gt;If the angle is specified with a string, only the deg, grad, rad, and turn types are supported.&lt;br&gt;- **rotation**: rotation angle of the sweep gradient. &lt;br&gt; Default value: **0**&lt;br&gt;If the angle is specified with a string, only the deg, grad, rad, and turn types are supported.&lt;br&gt;- colors: array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped. &lt;br&gt;- **repeating**: whether the colors are repeated. &lt;br&gt; Default value: **false**. &lt;br&gt;**NOTE：**&lt;br&gt;A value less than 0 is treated as **0**. A value greater than 360 is treated as **360**. &lt;br&gt;When **start**, **end**, or **rotation** is specified with a string, the string must be a number or a number followed by one of the following units: deg, rad, grad, and turn. Valid value examples are "90", "90deg", and "1.57rad". |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## systemBarEffect

```TypeScript
default systemBarEffect(): this
```

Applies a system bar effect to the component, which means to invert colors based on the background and add a blur.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default systemBarEffect(): this--><!--Device-CommonMethod-default systemBarEffect(): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## systemMaterial

```TypeScript
default systemMaterial(material: SystemUiMaterial | undefined): this
```

Set system-styled materials for the component. The material effect behaves differently on devices with different level of computing powers. On devices with lower computing power, it affects attributes such as the backgroundColor, borderWidth, borderColor, shadow. On devices with higher computing power, it adds a filter effect at the system material layer, which can produce an effect similar to glass.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default systemMaterial(material: SystemUiMaterial | undefined): this--><!--Device-CommonMethod-default systemMaterial(material: SystemUiMaterial | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| material | [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md) \| undefined | Yes | System-styled material. Undefined indicates reverting to the effect of no system material. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## tabIndex

```TypeScript
default tabIndex(index: int | undefined): this
```

Set focus index by key tab.The tabIndex and focusScopeId cannot be used together.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default tabIndex(index: int | undefined): this--><!--Device-CommonMethod-default tabIndex(index: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## tabStop

```TypeScript
default tabStop(isTabStop: boolean | undefined): this
```

Set TabStop on component focus

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default tabStop(isTabStop: boolean | undefined): this--><!--Device-CommonMethod-default tabStop(isTabStop: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isTabStop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## toolbar

```TypeScript
default toolbar(value: CustomBuilder | undefined): this
```

Config toolbar for current component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default toolbar(value: CustomBuilder | undefined): this--><!--Device-CommonMethod-default toolbar(value: CustomBuilder | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## transform

```TypeScript
default transform(value: Matrix4Transit | undefined): this
```

Sets the transformation matrix of the component. Set undefined value to reset the transform matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default transform(value: Matrix4Transit | undefined): this--><!--Device-CommonMethod-default transform(value: Matrix4Transit | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) \| undefined | Yes | Transformation matrix of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## transform3D

```TypeScript
default transform3D(transform: Matrix4Transit | undefined): this
```

Sets the transformation matrix for the current component.The interface can display the effect of three-dimensional natrix transformation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default transform3D(transform: Matrix4Transit | undefined): this--><!--Device-CommonMethod-default transform3D(transform: Matrix4Transit | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) \| undefined | Yes | transform3D natrix |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## transition

```TypeScript
default transition(value: TransitionEffect | undefined): this
```

Set the transition effect of component when it appears and disappears.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default transition(value: TransitionEffect | undefined): this--><!--Device-CommonMethod-default transition(value: TransitionEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) \| undefined | Yes | transition effect |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## transition

```TypeScript
default transition(effect: TransitionEffect | undefined, onFinish: TransitionFinishCallback | undefined): this
```

Set the transition effect of component when it appears and disappears.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default transition(effect: TransitionEffect | undefined, onFinish: TransitionFinishCallback | undefined): this--><!--Device-CommonMethod-default transition(effect: TransitionEffect | undefined, onFinish: TransitionFinishCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) \| undefined | Yes | transition effect |
| onFinish | [TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md) \| undefined | Yes | transition finish callback. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## translate

```TypeScript
default translate(value: TranslateOptions | undefined): this
```

Sets the translation effect for page transitions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default translate(value: TranslateOptions | undefined): this--><!--Device-CommonMethod-default translate(value: TranslateOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TranslateOptions](arkts-arkui-common-translateoptions-i.md) \| undefined | Yes | Translation effect for page transitions &lt;br&gt;specifying the start value for entrance and the end value for exit. default:{x:0,y:0,z:0} |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## useEffect

```TypeScript
default useEffect(useEffect: boolean | undefined, effectType: EffectType | undefined): this
```

Specifies whether to apply the effect defined by &lt;!--Del--&gt;the parent  
[EffectComponent](ts-container-effectcomponent-sys.md) or &lt;!--DelEnd--&gt;the window.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default useEffect(useEffect: boolean | undefined, effectType: EffectType | undefined): this--><!--Device-CommonMethod-default useEffect(useEffect: boolean | undefined, effectType: EffectType | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useEffect | boolean \| undefined | Yes | Whether to apply the effect defined by &lt;!--Del--&gt;the parent **EffectComponent** or &lt;!--DelEnd--&gt;the window. &lt;br&gt;The value **true** means to apply the effect defined by &lt;!--Del--&gt;the parent **EffectComponent** or &lt;!--DelEnd--&gt;the window. &lt;br&gt;Default value: **false**. |
| effectType | [EffectType](arkts-arkui-common-effecttype-e.md) \| undefined | Yes | Type of effect to apply to the component, which is defined by &lt;!--Del--&gt;the parent **EffectComponent** or &lt;!--DelEnd--&gt;the window. &lt;br&gt;Default value: **EffectType.DEFAULT**. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## useEffect

```TypeScript
default useEffect(value: boolean | undefined): this
```

Specifies whether to combine the drawing of special effects, such as background blur.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default useEffect(value: boolean | undefined): this--><!--Device-CommonMethod-default useEffect(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether the component inherits the special effect settings of the **EffectComponent** component.&lt;br&gt;The value **true** means that the component inherits the special effect settings of the **EffectComponent** component, and **false** means the opposite. &lt;br&gt;Default value: **false**. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## useShadowBatching

```TypeScript
default useShadowBatching(value: boolean | undefined): this
```

Sets whether to draw shadows of child nodes in the component at the same layer,so that the shadows of elements at the same layer overlap.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default useShadowBatching(value: boolean | undefined): this--><!--Device-CommonMethod-default useShadowBatching(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to draw shadows of child nodes in the component at the same layer, so that the shadows of elements at the same layer overlap. &lt;br&gt;Default value: **false**. &lt;br&gt;**NOTE：**&lt;br&gt;1. When this feature is disabled (default), if the shadow radius of a child node is large, the shadows of the child nodes may overlap. This overlap issue does not occur when the feature is enabled. &lt;br&gt;2. Avoid nesting **useShadowBatching**. When used in nested mode, **useShadowBatching** takes effect for the current child node only and cannot be recursively used. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## visibility

```TypeScript
default visibility(value: Visibility | undefined): this
```

Controls the display or hide of the current component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default visibility(value: Visibility | undefined): this--><!--Device-CommonMethod-default visibility(value: Visibility | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Visibility](arkts-arkui-visibility-e.md) \| undefined | Yes | Whether the component is visible. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## visualEffect

```TypeScript
default visualEffect(effect: VisualEffect | undefined): this
```

Sets a visual effect that is not a filter effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default visualEffect(effect: VisualEffect | undefined): this--><!--Device-CommonMethod-default visualEffect(effect: VisualEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [VisualEffect](../arkts-components/arkts-arkui-visualeffect-t.md) \| undefined | Yes | Visual effect parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## width

```TypeScript
default width(widthValue: Length | LayoutPolicy | undefined): this
```

Sets the width of the component or its horizontal layout policy. By default, the component uses the width required for its content. If the width of the component is greater than that of the parent container, the component will be drawn beyond the parent container scope.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default width(widthValue: Length | LayoutPolicy | undefined): this--><!--Device-CommonMethod-default width(widthValue: Length | LayoutPolicy | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| widthValue | [Length](arkts-arkui-length-t.md) \| LayoutPolicy \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## zIndex

```TypeScript
default zIndex(value: int | undefined): this
```

The sibling components in the same container are hierarchically displayed. A larger value of z indicates a higher display level.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonMethod-default zIndex(value: int | undefined): this--><!--Device-CommonMethod-default zIndex(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

