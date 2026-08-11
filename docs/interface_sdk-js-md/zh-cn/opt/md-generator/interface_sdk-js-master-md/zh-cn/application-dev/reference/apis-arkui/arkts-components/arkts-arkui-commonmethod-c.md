# CommonMethod

CommonMethod.

**起始版本：** 11

<!--Device-unnamed-declare class CommonMethod<T>--><!--Device-unnamed-declare class CommonMethod<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityActionOptions

```TypeScript
accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T
```

设置组件的无障碍操作的可选参数，用于限制或修改屏幕朗读等辅助应用发起的操作行为。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T--><!--Device-CommonMethod-accessibilityActionOptions(option: AccessibilityActionOptions | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AccessibilityActionOptions](../arkts-apis/arkts-arkui-accessibilityactionoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityChecked

```TypeScript
accessibilityChecked(isCheck: boolean): T
```

无障碍节点是否选中的状态维护，用于支持多选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本13开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityChecked(isCheck: boolean): T--><!--Device-CommonMethod-accessibilityChecked(isCheck: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isCheck | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityCustomActions

```TypeScript
accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T
```

设置组件的自定义无障碍操作，支持开发者设置一个自定义actions的数组，用于给组件按操作名进行自定义操作的回调绑定。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T--><!--Device-CommonMethod-accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| actions | Array&lt;AccessibilityCustomAction&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityDefaultFocus

```TypeScript
accessibilityDefaultFocus(focus: boolean): T
```

为页面设置屏幕朗读初始焦点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityDefaultFocus(focus: boolean): T--><!--Device-CommonMethod-accessibilityDefaultFocus(focus: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| focus | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityDescription

```TypeScript
accessibilityDescription(value: string): T
```

设置无障碍说明。该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityDescription(value: string): T--><!--Device-CommonMethod-accessibilityDescription(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityDescription

```TypeScript
accessibilityDescription(description: Resource): T
```

设置无障碍说明，支持通过Resource引用资源文件。该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;Reference resource of the accessibility description. You can specify further explanation&lt;br&gt;of the current component, for example, possible operation consequences, especially those that&lt;br&gt;cannot be learned from component attributes and accessibility text. If a component contains&lt;br&gt;both text information and the accessibility description, the text is read first and then the&lt;br&gt;accessibility description, when the component is selected.&lt;/p&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityDescription(description: Resource): T--><!--Device-CommonMethod-accessibilityDescription(description: Resource): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| description | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityFocusDrawLevel

```TypeScript
accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T
```

无障碍焦点绿框的绘制层级设置功能。默认层级是跟随组件。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T--><!--Device-CommonMethod-accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawLevel | [FocusDrawLevel](../arkts-apis/arkts-arkui-focusdrawlevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityGroup

```TypeScript
accessibilityGroup(value: boolean): T
```

Sets whether to enable accessibility grouping.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;Whether to enable accessibility grouping. When accessibility grouping is enabled,&lt;br&gt;the component and all its children are treated as a single selectable unit, and the accessibility&lt;br&gt;service will no longer focus on the individual child components.&lt;/p&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityGroup(value: boolean): T--><!--Device-CommonMethod-accessibilityGroup(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityGroup

```TypeScript
accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T
```

Sets whether to enable accessibility grouping.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;If accessibility grouping is enabled and the component does not contain a universal text attribute&lt;br&gt;or an accessibility text attribute, the system will concatenate the universal text attributes of&lt;br&gt;its child components to form a merged text for the component. If a child component lacks a universal&lt;br&gt;text attribute, it will be ignored in the concatenation process.

&lt;br&gt;When accessibilityPreferred is set to true, the system will prioritize concatenating the accessibility&lt;br&gt;text attributes of the child components to form the merged text. If a child component lacks an&lt;br&gt;accessibility text attribute, the system will continue to concatenate its universal text attribute.&lt;br&gt;If a child component lacks both, it will be ignored.&lt;/p&gt;

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本14开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T--><!--Device-CommonMethod-accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isGroup | boolean | 是 |
| accessibilityOptions | [AccessibilityOptions](../arkts-apis/arkts-arkui-accessibilityoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityLevel

```TypeScript
accessibilityLevel(value: string): T
```

Sets the accessibility level.This property determines whether the component can be recognized by accessibility services.&lt;p&gt;Accessibility level, which is used to decide whether a component can be identified by the accessibility service.&lt;br&gt;The options are as follows:&lt;br&gt;"auto": The component's recognizability is determined by the accessibility grouping service and ArkUI.&lt;br&gt;"yes": The component can be recognized by accessibility services.&lt;br&gt;"no": The component cannot be recognized by accessibility services.&lt;br&gt;"no-hide-descendants": Neither the component nor its child components can be recognized by accessibility services.&lt;strong&gt;NOTE&lt;/strong&gt;&lt;br&gt;When accessibilityLevel is set to "auto", the component's recognizability depends on the following factors:&lt;br&gt;1. The accessibility service internally determines whether the component can be recognized.&lt;br&gt;2. If the parent component's accessibilityGroup property has isGroup set to true, the accessibility service will&lt;br&gt;not focus on its child components, making them unrecognizable.&lt;br&gt;3. If the parent component's accessibilityLevel is set to "no-hide-descendants", the component will not be&lt;br&gt;recognized by accessibility services.&lt;/p&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityLevel(value: string): T--><!--Device-CommonMethod-accessibilityLevel(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string): T
```

指定屏幕朗读扫动走焦过程中组件的下一个焦点。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityNextFocusId(nextId: string): T--><!--Device-CommonMethod-accessibilityNextFocusId(nextId: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextId | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityNextFocusId

```TypeScript
accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T
```

指定屏幕朗读扫动走焦过程中组件的下一个焦点，并支持配置详细参数。&lt;br&gt;通过AccessibilityNextFocusParams参数，可以配置是否在无障碍下一个焦点处理过程中查找后代节点中的焦点。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T--><!--Device-CommonMethod-accessibilityNextFocusId(nextId: string, nextFocusParams : AccessibilityNextFocusParams | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextId | string | 是 |
| nextFocusParams | [AccessibilityNextFocusParams](../arkts-apis/arkts-arkui-accessibilitynextfocusparams-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityRole

```TypeScript
accessibilityRole(role: AccessibilityRoleType): T
```

设置无障碍组件类型，特定组件类型有特定的朗读方式，可以根据应用诉求，修改组件类型，用于控制无障碍模式下对组件的朗读方式和朗读内容。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityRole(role: AccessibilityRoleType): T--><!--Device-CommonMethod-accessibilityRole(role: AccessibilityRoleType): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| role | [AccessibilityRoleType](arkts-arkui-accessibilityroletype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityScrollTriggerable

```TypeScript
accessibilityScrollTriggerable(isTriggerable: boolean): T
```

设置无障碍节点是否支持屏幕朗读滚动操作。当屏幕朗读在扫动走焦时，若容器内当前页面无可聚焦的组件，会发起一次自动滚动操作。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityScrollTriggerable(isTriggerable: boolean): T--><!--Device-CommonMethod-accessibilityScrollTriggerable(isTriggerable: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTriggerable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilitySelected

```TypeScript
accessibilitySelected(isSelect: boolean): T
```

无障碍节点是否选中的状态维护，用于支持单选的情况使用，表示组件是否被选中。此接口只影响屏幕朗读场景下的组件状态播报信息。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本13开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilitySelected(isSelect: boolean): T--><!--Device-CommonMethod-accessibilitySelected(isSelect: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isSelect | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityStateDescription

```TypeScript
accessibilityStateDescription(description: string | Resource | undefined): T
```

设置组件的状态播报文本，用于屏幕朗读场景下清晰说明组件当前的实时状态。屏幕朗读时会优先播报该状态文本。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityStateDescription(description: string | Resource | undefined): T--><!--Device-CommonMethod-accessibilityStateDescription(description: string | Resource | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| description | string \| Resource \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityText

```TypeScript
accessibilityText(value: string): T
```

Sets the accessibility text.When a component does not contain a text attribute, you can use this API to set an accessibility text attribute, so that accessibility services can announce the specified content for the component.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityText(value: string): T--><!--Device-CommonMethod-accessibilityText(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityText

```TypeScript
accessibilityText(text: Resource): T
```

Sets the accessibility text.&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;If a component has both text content and accessibility text, only the accessibility text is announced.&lt;br&gt;If a component is grouped for accessibility purposes but lacks both text content and accessibility&lt;br&gt;text, the screen reader will concatenate text from its child components (depth-first traversal).&lt;br&gt;To prioritize accessibility text concatenation, set accessibilityPreferred in accessibilityGroup.&lt;/p&gt;

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityText(text: Resource): T--><!--Device-CommonMethod-accessibilityText(text: Resource): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityTextHint

```TypeScript
accessibilityTextHint(value: string): T
```

设置组件的文本提示信息，供无障碍辅助应用查询。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityTextHint(value: string): T--><!--Device-CommonMethod-accessibilityTextHint(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityUseSamePage

```TypeScript
accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T
```

设置当前组件和宿主应用为同page模式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T--><!--Device-CommonMethod-accessibilityUseSamePage(pageMode: AccessibilitySamePageMode): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageMode | [AccessibilitySamePageMode](arkts-arkui-accessibilitysamepagemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## accessibilityVirtualNode

```TypeScript
accessibilityVirtualNode(builder: CustomBuilder): T
```

设置无障碍虚拟子节点。对自绘制组件传入一个自定义的CustomBuilder，该CustomBuilder中的组件在后端仅做布局不做显示，辅助应用获取无障碍节点信息时会返回CustomBuilder中的节点信息。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-accessibilityVirtualNode(builder: CustomBuilder): T--><!--Device-CommonMethod-accessibilityVirtualNode(builder: CustomBuilder): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## align

```TypeScript
align(value: Alignment): T
```

设置当前组件绘制区域内的子组件的对齐方式，支持 [attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-align(value: Alignment): T--><!--Device-CommonMethod-align(value: Alignment): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## align

```TypeScript
align(alignment: Alignment | LocalizedAlignment): T
```

设置当前组件绘制区域内的子组件的对齐方式，增加支持镜像的能力，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-align(alignment: Alignment | LocalizedAlignment): T--><!--Device-CommonMethod-align(alignment: Alignment | LocalizedAlignment): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignment | [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) \| [LocalizedAlignment](../arkts-apis/arkts-arkui-enums-localizedalignment-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## alignRules

```TypeScript
alignRules(value: AlignRuleOption): T
```

指定设置在相对布局组件中子组件的对齐规则，仅当父组件为[RelativeContainer](RelativeContainer)时生效，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-alignRules(value: AlignRuleOption): T--><!--Device-CommonMethod-alignRules(value: AlignRuleOption): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AlignRuleOption](arkts-arkui-alignruleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## alignRules

```TypeScript
alignRules(alignRule: LocalizedAlignRuleOptions): T
```

指定设置在相对布局组件中子组件的对齐规则，仅当父组件为[RelativeContainer](RelativeContainer)时生效。该方法水平方向上以start和end分别替代原方法的left和right，以便在RTL模式下能镜像显示，建议使用该方法指定设置在相对布局组件中子组件的对齐规则，支持  
[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T--><!--Device-CommonMethod-alignRules(alignRule: LocalizedAlignRuleOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignRule | [LocalizedAlignRuleOptions](arkts-arkui-localizedalignruleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## alignSelf

```TypeScript
alignSelf(value: ItemAlign): T
```

子组件在父容器交叉轴的对齐格式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-alignSelf(value: ItemAlign): T--><!--Device-CommonMethod-alignSelf(value: ItemAlign): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ItemAlign](../arkts-apis/arkts-arkui-itemalign-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## allowDrop

```TypeScript
allowDrop(value: Array<UniformDataType> | null | Array<string>): T
```

设置该组件上允许落入的数据类型。如果未设置allowDrop，组件将默认接受所有数据类型。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-allowDrop(value: Array<UniformDataType> | null | Array<string>): T--><!--Device-CommonMethod-allowDrop(value: Array<UniformDataType> | null | Array<string>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;UniformDataType&gt; \| null \| Array&lt;string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## allowForceDark

```TypeScript
allowForceDark(value: boolean): T
```

Set whether the component enables the ability to invert colors.This interface needs to be set as the first attribute of the component.

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-allowForceDark(value: boolean): T--><!--Device-CommonMethod-allowForceDark(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## animation

```TypeScript
animation(value: AnimateParam): T
```

设置组件的属性动画。

> **说明：**
> 
> - 在单一页面上存在大量应用动效的组件时，可以使用[renderGroup](arkts-arkui-commonmethod-c.md#rendergroup)方法来解决卡顿问题，从而提升动画性能。最佳实践请参考
> [动画使用指导-使用renderGroup](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fair-use-animation#section1223162922415)。
> 
> 
> - 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-animation(value: AnimateParam): T--><!--Device-CommonMethod-animation(value: AnimateParam): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-animateparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## aspectRatio

```TypeScript
aspectRatio(value: number): T
```

指定当前组件的宽高比，aspectRatio=width/height。  
- 仅设置width、aspectRatio时，height=width/aspectRatio。  
- 仅设置height、aspectRatio时，width=height*aspectRatio。  
- 同时设置width、height和aspectRatio时，height不生效，height=width/aspectRatio。

设置aspectRatio属性后，组件宽高会受父组件内容区大小限制，[constraintSize](arkts-arkui-commonmethod-c.md#constraintsize)的优先级高于aspectRatio。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-aspectRatio(value: number): T--><!--Device-CommonMethod-aspectRatio(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<T>): T
```

Sets the attribute modifier.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-attributeModifier(modifier: AttributeModifier<T>): T--><!--Device-CommonMethod-attributeModifier(modifier: AttributeModifier<T>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](arkts-arkui-attributemodifier-i.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(value: number, options?: BlurOptions): T
```

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backdropBlur(value: number, options?: BlurOptions): T--><!--Device-CommonMethod-backdropBlur(value: number, options?: BlurOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(radius: Optional<number>, options?: BlurOptions): T
```

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。与[backdropBlur](arkts-arkui-commonmethod-c.md#backdropblur)相比，radius参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions): T--><!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backdropBlur

```TypeScript
backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T
```

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。与  
[backdropBlur&lt;sup&gt;18+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backdropblur)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## background

```TypeScript
background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T
```

Add a background for the component.

Anonymous Object Rectification.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T--><!--Device-CommonMethod-background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |
| options | [BackgroundOptions](arkts-arkui-backgroundoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T
```

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | 是 |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T
```

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。与  
[backgroundBlurStyle&lt;sup&gt;9+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backgroundblurstyle)相比，style参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | 是 |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T
```

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。与  
[backgroundBlurStyle&lt;sup&gt;18+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backgroundblurstyle)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | 是 |
| options | [BackgroundBlurStyleOptions](arkts-arkui-backgroundblurstyleoptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundBrightness

```TypeScript
backgroundBrightness(params: BackgroundBrightnessOptions): T
```

设置组件背景提亮效果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundBrightness(params: BackgroundBrightnessOptions): T--><!--Device-CommonMethod-backgroundBrightness(params: BackgroundBrightnessOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [BackgroundBrightnessOptions](arkts-arkui-backgroundbrightnessoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundBrightness

```TypeScript
backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T
```

设置组件背景提亮效果。与  
[backgroundBrightness&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backgroundbrightness)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T--><!--Device-CommonMethod-backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;BackgroundBrightnessOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(value: ResourceColor): T
```

Background color

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundColor(value: ResourceColor): T--><!--Device-CommonMethod-backgroundColor(value: ResourceColor): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(color: Optional<ResourceColor>): T
```

Background color

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor>): T--><!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;ResourceColor&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundColor

```TypeScript
backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T
```

Background color

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T--><!--Device-CommonMethod-backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;ResourceColor \| [ColorMetrics&gt;](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: BackgroundEffectOptions): T
```

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundEffect(options: BackgroundEffectOptions): T--><!--Device-CommonMethod-backgroundEffect(options: BackgroundEffectOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: Optional<BackgroundEffectOptions>): T
```

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。与  
[backgroundEffect&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backgroundeffect)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>): T--><!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;BackgroundEffectOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundEffect

```TypeScript
backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T
```

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。与  
[backgroundEffect&lt;sup&gt;18+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#backgroundeffect)相比，新增了sysOptions参数，即支持系统自适应调节参数。

> **说明：**
> 
> backgroundEffect接口为实时接口，每帧对模糊等效果执行实时渲染，性能负载较大。当组件背景模糊效果无需变动时，推荐采用静态模糊接口
> [blur](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-effectkit-filter-i.md/arkts-arkgraphics2d-effectkit-filter-i.md#blur)实现模糊效果。最佳实践请参考：
> [图像模糊动效优化-使用场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519)。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;BackgroundEffectOptions&gt; | 是 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundFilter

```TypeScript
backgroundFilter(filter: Filter): T
```

设置背景滤镜视觉效果。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundFilter(filter: Filter): T--><!--Device-CommonMethod-backgroundFilter(filter: Filter): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundImage

```TypeScript
backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T
```

Background image src: Image address url

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T--><!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-apis/arkts-arkui-pixelmap-t.md) | 是 |
| repeat | [ImageRepeat](../arkts-apis/arkts-arkui-imagerepeat-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundImage

```TypeScript
backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T
```

Background image

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T--><!--Device-CommonMethod-backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-apis/arkts-arkui-pixelmap-t.md) | 是 |
| options | [BackgroundImageOptions](arkts-arkui-backgroundimageoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundImagePosition

```TypeScript
backgroundImagePosition(value: Position | Alignment): T
```

Background image position x:Horizontal coordinate;y:Vertical axis coordinate.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundImagePosition(value: Position | Alignment): T--><!--Device-CommonMethod-backgroundImagePosition(value: Position | Alignment): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) \| [Alignment](../arkts-apis/arkts-arkui-alignment-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundImageResizable

```TypeScript
backgroundImageResizable(value: ResizableOptions): T
```

Background image resizable.value:resizable options

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-backgroundImageResizable(value: ResizableOptions): T--><!--Device-CommonMethod-backgroundImageResizable(value: ResizableOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-resizableoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## backgroundImageSize

```TypeScript
backgroundImageSize(value: SizeOptions | ImageSize): T
```

Background image size

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-backgroundImageSize(value: SizeOptions | ImageSize): T--><!--Device-CommonMethod-backgroundImageSize(value: SizeOptions | ImageSize): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) \| [ImageSize](../arkts-apis/arkts-arkui-imagesize-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContentCover

```TypeScript
bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T
```

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，显示方式可设置无动画过渡，上下切换过渡以及透明渐变过渡。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T--><!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, type?: ModalTransition): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| type | [ModalTransition](arkts-arkui-modaltransition-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContentCover

```TypeScript
bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T
```

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，可自定义设置转场方式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T--><!--Device-CommonMethod-bindContentCover(isShow: boolean, builder: CustomBuilder, options?: ContentCoverOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [ContentCoverOptions](arkts-arkui-contentcoveroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenu

```TypeScript
bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenu(content: CustomBuilder, responseType: ResponseType, options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| responseType | [ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md) | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenu

```TypeScript
bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T
```

ContextMenu control

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenu(isShown: boolean, content: CustomBuilder, options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShown | boolean | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenuByIsShow

```TypeScript
bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T
```

将上下文菜单绑定到组件，组件的可见性受isShow设置的约束。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuByIsShow(isShow: boolean, content: CustomBuilder | Array<MenuElement>, options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;MenuElement&gt; | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenuByResponseType

```TypeScript
bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,
      options?: ContextMenuOptions): T
```

将上下文菜单绑定到此组件，当用户长按或右键单击组件，支持自定义或固定样式的菜单项。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,      options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement>, responseType: ResponseType,      options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;MenuElement&gt; | 是 |
| responseType | [ResponseType](../arkts-apis/arkts-arkui-responsetype-e.md) | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenuWithResponse

```TypeScript
bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T
```

将上下文菜单绑定到组件上，当用户长按或右键该组件时显示。仅支持自定义菜单项。鼠标设备不支持长按操作。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;ResponseType&gt; \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindContextMenuWithResponse

```TypeScript
bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,
    options?: ContextMenuOptions): T
```

将上下文菜单绑定到此组件，当用户长按或右键单击组件，支持自定义或固定样式的菜单项。不支持使用鼠标设备长按。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,    options?: ContextMenuOptions): T--><!--Device-CommonMethod-bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,    options?: ContextMenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;ResponseType&gt; \| Array&lt;MenuElement&gt; \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindMenu

```TypeScript
bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T
```

Menu control

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T--><!--Device-CommonMethod-bindMenu(content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | Array&lt;MenuElement&gt; \| [CustomBuilder](../arkts-apis/arkts-arkui-custombuilder-t.md) | 是 |
| options | [MenuOptions](arkts-arkui-menuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindMenu

```TypeScript
bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T
```

Menu control

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T--><!--Device-CommonMethod-bindMenu(isShow: boolean, content: Array<MenuElement> | CustomBuilder, options?: MenuOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean | 是 |
| content | Array&lt;MenuElement&gt; \| [CustomBuilder](../arkts-apis/arkts-arkui-custombuilder-t.md) | 是 |
| options | [MenuOptions](arkts-arkui-menuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindPopup

```TypeScript
bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T
```

Popup control&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;The popup can be displayed only after the entire page is fully constructed. Therefore, to avoid incorrect display positions and shapes, do not set this parameter to true while the page is still being constructed.&lt;/p&gt;

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T--><!--Device-CommonMethod-bindPopup(show: boolean, popup: PopupOptions | CustomPopupOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| show | boolean | 是 | @param { PopupOptions \|
| popup | [PopupOptions](arkts-arkui-popupoptions-i.md) \| [CustomPopupOptions](../arkts-apis/arkts-arkui-common-custompopupoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## bindSheet

```TypeScript
bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T
```

给组件绑定半模态页面，点击后显示模态页面。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T--><!--Device-CommonMethod-bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |
| options | [SheetOptions](arkts-arkui-sheetoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## bindTips

```TypeScript
bindTips(message: TipsMessageType, options?: TipsOptions): T
```

Tips control

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-bindTips(message: TipsMessageType, options?: TipsOptions): T--><!--Device-CommonMethod-bindTips(message: TipsMessageType, options?: TipsOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) | 是 |
| options | [TipsOptions](arkts-arkui-tipsoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## blendMode

```TypeScript
blendMode(value: BlendMode, type?: BlendApplyType): T
```

将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-blendMode(value: BlendMode, type?: BlendApplyType): T--><!--Device-CommonMethod-blendMode(value: BlendMode, type?: BlendApplyType): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlendMode](arkts-arkui-blendmode-e.md) | 是 |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## blendMode

```TypeScript
blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T
```

将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。与  
[blendMode&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#blendmode)相比，mode参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T--><!--Device-CommonMethod-blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [Optional](arkts-arkui-optional-t.md)&lt;BlendMode&gt; | 是 |
| type | [BlendApplyType](arkts-arkui-blendapplytype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## blur

```TypeScript
blur(value: number, options?: BlurOptions): T
```

为组件添加内容模糊效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-blur(value: number, options?: BlurOptions): T--><!--Device-CommonMethod-blur(value: number, options?: BlurOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## blur

```TypeScript
blur(blurRadius: Optional<number>, options?: BlurOptions): T
```

为组件添加内容模糊效果。与[blur](arkts-arkui-commonmethod-c.md#blur)相比，blurRadius参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions): T--><!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurRadius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## blur

```TypeScript
blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T
```

为组件添加内容模糊效果。与[blur&lt;sup&gt;18+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#blur)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本19开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurRadius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
| options | [BlurOptions](arkts-arkui-bluroptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## border

```TypeScript
border(value: BorderOptions): T
```

设置边框样式。

> **说明：**
> 
> color、radius缺省时，为了保证[borderColor](arkts-arkui-commonmethod-c.md#bordercolor)、[borderRadius](arkts-arkui-commonmethod-c.md#borderradius)生效，需要将[borderColor](arkts-arkui-commonmethod-c.md#bordercolor)、[borderRadius](arkts-arkui-commonmethod-c.md#borderradius)设置在[border](arkts-arkui-commonmethod-c.md#border)后。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-border(value: BorderOptions): T--><!--Device-CommonMethod-border(value: BorderOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderOptions](../arkts-apis/arkts-arkui-borderoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## borderColor

```TypeScript
borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T
```

设置边框的颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T--><!--Device-CommonMethod-borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| EdgeColors \| [LocalizedEdgeColors](../arkts-apis/arkts-arkui-localizededgecolors-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## borderImage

```TypeScript
borderImage(value: BorderImageOption): T
```

Sets the border image of the component.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderImage(value: BorderImageOption): T--><!--Device-CommonMethod-borderImage(value: BorderImageOption): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderImageOption](arkts-arkui-borderimageoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T
```

设置边框的圆角半径。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T--><!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](../arkts-apis/arkts-arkui-localizedborderradiuses-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## borderRadius

```TypeScript
borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T
```

设置边框的圆角半径和绘制圆角的模式。

**注意**1. **RenderStrategy.FAST**：当前组件及其子组件将直接以圆角效果绘制到画布上。2. **RenderStrategy.OFFSCREEN**：当前组件及其子组件将首先渲染到一个离屏画布，然后进行圆角裁剪，最后绘制到主画布上。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T--><!--Device-CommonMethod-borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](../arkts-apis/arkts-arkui-localizedborderradiuses-i.md) | 是 |
| type | [RenderStrategy](../arkts-apis/arkts-arkui-renderstrategy-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## borderStyle

```TypeScript
borderStyle(value: BorderStyle | EdgeStyles): T
```

设置元素的边框线条样式。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderStyle(value: BorderStyle | EdgeStyles): T--><!--Device-CommonMethod-borderStyle(value: BorderStyle | EdgeStyles): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderStyle](../arkts-apis/arkts-arkui-borderstyle-e.md) \| [EdgeStyles](../arkts-apis/arkts-arkui-units-edgestyles-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## borderWidth

```TypeScript
borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T
```

设置边框的宽度。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T--><!--Device-CommonMethod-borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) \| EdgeWidths \| [LocalizedEdgeWidths](../arkts-apis/arkts-arkui-units-localizededgewidths-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## brightness

```TypeScript
brightness(value: number): T
```

为组件添加高光效果。不通过该接口设置时，默认无变化。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-brightness(value: number): T--><!--Device-CommonMethod-brightness(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## brightness

```TypeScript
brightness(brightness: Optional<number>): T
```

为组件添加高光效果。不通过该接口设置时，默认无变化。与[brightness](arkts-arkui-commonmethod-c.md#brightness)相比，brightness参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-brightness(brightness: Optional<number>): T--><!--Device-CommonMethod-brightness(brightness: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [brightness](#brightness) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## chainMode

```TypeScript
chainMode(direction: Axis, style: ChainStyle): T
```

指定以该组件为链头所构成的链的参数，仅当父组件为RelativeContainer时生效。链头指满足成链规则时链的第一个组件（水平方向从左边起始，镜像语言下从右边起始；竖直方向从上边起始）。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-chainMode(direction: Axis, style: ChainStyle): T--><!--Device-CommonMethod-chainMode(direction: Axis, style: ChainStyle): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [direction](#direction) | [Axis](../arkts-apis/arkts-arkui-axis-e.md) | 是 |
| style | [ChainStyle](arkts-arkui-chainstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## chainWeight

```TypeScript
chainWeight(chainWeight: ChainWeightOptions): T
```

对形成链的组件进行重新布局。仅当父组件为[RelativeContainer](RelativeContainer)时生效。

> **说明：**
> 
> 从API version 23开始，支持 [attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-chainWeight(chainWeight: ChainWeightOptions): T--><!--Device-CommonMethod-chainWeight(chainWeight: ChainWeightOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [chainWeight](#chainweight) | [ChainWeightOptions](../arkts-apis/arkts-arkui-chainweightoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clickEffect

```TypeScript
clickEffect(value: ClickEffect | null): T
```

设置当前组件的点击回弹效果。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-clickEffect(value: ClickEffect | null): T--><!--Device-CommonMethod-clickEffect(value: ClickEffect | null): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ClickEffect](arkts-arkui-clickeffect-i.md) \| null | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clickEffect

```TypeScript
clickEffect(effect: Optional<ClickEffect | null>): T
```

设置当前组件的点击回弹效果。与[clickEffect](arkts-arkui-commonmethod-c.md#clickeffect)相比，新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-clickEffect(effect: Optional<ClickEffect | null>): T--><!--Device-CommonMethod-clickEffect(effect: Optional<ClickEffect | null>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [Optional](arkts-arkui-optional-t.md)&lt;ClickEffect \| null&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clip

```TypeScript
clip(value: boolean): T
```

是否对子组件超出当前组件范围外的区域进行裁剪。不设置该接口时，默认不对子组件超出当前组件范围外的区域进行裁剪。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-clip(value: boolean): T--><!--Device-CommonMethod-clip(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clip

```TypeScript
clip(clip: Optional<boolean>): T
```

是否对子组件超出当前组件范围外的区域进行裁剪。不设置该接口时，默认不对子组件超出当前组件范围外的区域进行裁剪。与  
[clip&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#clip)相比，新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-clip(clip: Optional<boolean>): T--><!--Device-CommonMethod-clip(clip: Optional<boolean>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [clip](#clip) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clip

```TypeScript
clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T
```

按指定的形状对当前组件进行裁剪。

> **说明：**

**起始版本：** 7

**废弃版本：** 12

**替代接口：** [CommonMethod#clipShape](arkts-arkui-commonmethod-c.md#clipshape)(value:

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T--><!--Device-CommonMethod-clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| CircleAttribute \| EllipseAttribute \| PathAttribute \| [RectAttribute](arkts-arkui-rect-attribute.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clipShape

```TypeScript
clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T
```

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。

> **说明：**
> 
> 不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。
> 
> 路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。
> 
> 形状中的[fill](arkts-arkui-commonshapemethod-c.md#fill)属性对clipShape接口不生效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T--><!--Device-CommonMethod-clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-circleshape-t.md) \| EllipseShape \| PathShape \| [RectShape](../arkts-apis/arkts-arkui-arkui-shape-rectshape-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## clipShape

```TypeScript
clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T
```

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。与  
[clipShape&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#clipshape)相比，新增了对undefined类型的支持。

> **说明：**
> 
> 不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。
> 
> 路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。
> 
> 形状中的[fill](arkts-arkui-commonshapemethod-c.md#fill)属性对clipShape接口不生效。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T--><!--Device-CommonMethod-clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shape | [Optional](arkts-arkui-optional-t.md)&lt;CircleShape \| EllipseShape \| PathShape \| [RectShape&gt;](../arkts-apis/arkts-arkui-arkui-shape-rectshape-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## colorBlend

```TypeScript
colorBlend(value: Color | string | Resource): T
```

为组件添加颜色叠加效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-colorBlend(value: Color | string | Resource): T--><!--Device-CommonMethod-colorBlend(value: Color | string | Resource): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## colorBlend

```TypeScript
colorBlend(color: Optional<Color | string | Resource>): T
```

为组件添加颜色叠加效果。与[colorBlend](arkts-arkui-commonmethod-c.md#colorblend)相比，color参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-colorBlend(color: Optional<Color | string | Resource>): T--><!--Device-CommonMethod-colorBlend(color: Optional<Color | string | Resource>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;Color \| string \| [Resource&gt;](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## compositingFilter

```TypeScript
compositingFilter(filter: Filter): T
```

设置合成滤镜视觉效果。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-compositingFilter(filter: Filter): T--><!--Device-CommonMethod-compositingFilter(filter: Filter): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## constraintSize

```TypeScript
constraintSize(value: ConstraintSizeOptions): T
```

设置约束尺寸，组件布局时进行尺寸范围限制。设置后组件的宽度和高度将被限制在指定的最小值和最大值范围内，constraintSize的优先级高于width和height属性。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-constraintSize(value: ConstraintSizeOptions): T--><!--Device-CommonMethod-constraintSize(value: ConstraintSizeOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ConstraintSizeOptions](../arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## contrast

```TypeScript
contrast(value: number): T
```

为组件添加对比度效果。不通过该接口设置时，默认无变化。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-contrast(value: number): T--><!--Device-CommonMethod-contrast(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## contrast

```TypeScript
contrast(contrast: Optional<number>): T
```

为组件添加对比度效果。不通过该接口设置时，默认无变化。与[contrast](arkts-arkui-commonmethod-c.md#contrast)相比，contrast参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-contrast(contrast: Optional<number>): T--><!--Device-CommonMethod-contrast(contrast: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [contrast](#contrast) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## customProperty

```TypeScript
customProperty(name: string, value: Optional<Object>): T
```

设置组件的自定义属性。

API版本26.0.0之前，[自定义组件](../../../ui/state-management/arkts-create-custom-components.md)不支持设置自定义属性。

从API版本26.0.0开始，自定义组件支持设置并读取自定义属性。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-customProperty(name: string, value: Optional<Object>): T--><!--Device-CommonMethod-customProperty(name: string, value: Optional<Object>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | [Optional](arkts-arkui-optional-t.md)&lt;Object&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## defaultFocus

```TypeScript
defaultFocus(value: boolean): T
```

设置当前组件是否为当前[层级页面](../../../ui/arkts-common-events-focus-event.md#基础概念)上的默认焦点。当未设置defaultFocus时，组件默认不为当前层级页面的默认焦点。

> **说明：**
> 
> 可以设置默认焦点的页面指的是支持页面路由或是弹窗类的容器组件，例如Page、NaviDestination、NavBar、PopUp、Dialog等。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-defaultFocus(value: boolean): T--><!--Device-CommonMethod-defaultFocus(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## direction

```TypeScript
direction(value: Direction): T
```

设置当前组件绘制区域内主轴方向上的布局，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-direction(value: Direction): T--><!--Device-CommonMethod-direction(value: Direction): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Direction](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-direction-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## displayPriority

```TypeScript
displayPriority(value: number): T
```

设置当前组件在布局容器中显示的优先级。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-displayPriority(value: number): T--><!--Device-CommonMethod-displayPriority(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## doubleSided

```TypeScript
doubleSided(value: Optional<boolean>): T
```

是否绘制组件的双面。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-doubleSided(value: Optional<boolean>): T--><!--Device-CommonMethod-doubleSided(value: Optional<boolean>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## dragPreview

```TypeScript
dragPreview(value: CustomBuilder | DragItemInfo | string): T
```

设置组件浮起和拖拽过程中的预览图。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-dragPreview(value: CustomBuilder | DragItemInfo | string): T--><!--Device-CommonMethod-dragPreview(value: CustomBuilder | DragItemInfo | string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| DragItemInfo \| string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## dragPreview

```TypeScript
dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T
```

自定义组件拖拽过程中的预览图，仅用于设置浮起效果或者禁用浮起效果。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T--><!--Device-CommonMethod-dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preview | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| DragItemInfo \| string | 是 |
| config | [PreviewConfiguration](arkts-arkui-previewconfiguration-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## dragPreviewOptions

```TypeScript
dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T
```

设置拖拽过程中预览图处理模式，数量角标的显示以及预览图浮起的交互模式。不支持onItemDragStart拖拽方式。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T--><!--Device-CommonMethod-dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DragPreviewOptions](arkts-arkui-dragpreviewoptions-i.md) | 是 |
| options | [DragInteractionOptions](arkts-arkui-draginteractionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## draggable

```TypeScript
draggable(value: boolean): T
```

设置该组件是否允许拖拽。默认情况下，组件不允许拖拽。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-draggable(value: boolean): T--><!--Device-CommonMethod-draggable(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## drawModifier

```TypeScript
drawModifier(modifier: DrawModifier | undefined): T
```

Sets the drawModifier of the current component.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-drawModifier(modifier: DrawModifier | undefined): T--><!--Device-CommonMethod-drawModifier(modifier: DrawModifier | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [DrawModifier](arkts-arkui-drawmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## enableClickSoundEffect

```TypeScript
enableClickSoundEffect(enabled: boolean | undefined): T
```

设置组件是否启用默认点击音效。是否能够发音依赖设备声音相关的设置，如静音模式下不会播放音效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-enableClickSoundEffect(enabled: boolean | undefined): T--><!--Device-CommonMethod-enableClickSoundEffect(enabled: boolean | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [enabled](#enabled) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## enabled

```TypeScript
enabled(value: boolean): T
```

设置组件是否可交互。当未设置enabled时，组件默认可交互。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-enabled(value: boolean): T--><!--Device-CommonMethod-enabled(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## expandSafeArea

```TypeScript
expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T
```

控制组件扩展其安全区域。

> **说明：**
> 
> - 设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高（包括设置'auto'）时，扩展安全区域的方向只支持[SafeAreaEdge.TOP,
SafeAreaEdge.START]，扩展后的组件尺寸保持不变。  
> 
> - 安全区域不会限制内部组件的布局和大小，不会裁剪内部组件。
> 
> - 当父容器为滚动容器时，组件设置expandSafeArea属性后，自身不会延伸，但仍可触发其子节点中设置了expandSafeArea的延伸范围更新。
> 
> - 设置expandSafeArea()时，不传参，走默认值处理；设置expandSafeArea([],[])时，相当于入参是空数组，此时expandSafeArea属性设置无效。
> 
> - 组件设置expandSafeArea生效的条件为：
> 1.type为SafeAreaType.KEYBOARD时默认生效，表现为组件不避让键盘。&lt;br/&gt;
> 2.设置其他type，组件的边界与安全区域重合时组件能够延伸到安全区域下。例如：设备顶部状态栏高度100，那么组件在屏幕中的绝对位置需要为0 &lt;= y <= 100。
> 
&gt;&lt;= 100。
&gt; 
> - 组件延伸到避让区时，在避让区的事件如点击事件等可能会被系统拦截，优先给状态栏等系统组件响应。
> 
> -
滚动类容器内的组件不建议设置expandSafeArea属性，如果设置，需要按照组件嵌套关系，将当前节点到滚动类祖先容器间所有直接节点设置expandSafeArea属性，否则expandSafeArea属性在滚动后可能会失效，写法参考[示例7](#示例7滚动类容器扩展安全区)。  
> 
> - expandSafeArea属性仅作用于当前组件，不会向父组件或子组件传递，因此使用过程中，所有相关组件均需配置。
> 
> -
同时设置expandSafeArea和position属性时，position属性会优先生效，expandSafeArea属性会后生效。对于未设置position、offset等绘制属性的组件，如果其边界未与避让区重叠，设置exp andSafeArea属性将不生效，如弹窗和半模态组件。  
> 
> - 对于expandSafeArea属性无法生效的场景，若要将组件部署在避让区，需要手动调整组件的坐标。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T--><!--Device-CommonMethod-expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;SafeAreaType&gt; | 否 |
| edges | Array&lt;SafeAreaEdge&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## flexBasis

```TypeScript
flexBasis(value: number | string): T
```

设置组件的基准尺寸。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-flexBasis(value: number | string): T--><!--Device-CommonMethod-flexBasis(value: number | string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## flexGrow

```TypeScript
flexGrow(value: number): T
```

设置组件在父容器的剩余空间所占比例。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-flexGrow(value: number): T--><!--Device-CommonMethod-flexGrow(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## flexShrink

```TypeScript
flexShrink(value: number): T
```

设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。

使用[getInspectorByKey](ts-universal-attributes-component-id.md#getinspectorbykey9)获取flexShrink属性时，如果该节点未设置flexShrink属性，默认返回1。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-flexShrink(value: number): T--><!--Device-CommonMethod-flexShrink(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## focusBox

```TypeScript
focusBox(style: FocusBoxStyle): T
```

设置当前组件系统焦点框样式。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusBox(style: FocusBoxStyle): T--><!--Device-CommonMethod-focusBox(style: FocusBoxStyle): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [FocusBoxStyle](../arkts-apis/arkts-arkui-focusboxstyle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## focusOnTouch

```TypeScript
focusOnTouch(value: boolean): T
```

设置当前组件是否支持点击获焦能力。当组件未设置focusOnTouch时，组件默认不支持点击获焦能力。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusOnTouch(value: boolean): T--><!--Device-CommonMethod-focusOnTouch(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## focusScopeId

```TypeScript
focusScopeId(id: string, isGroup?: boolean): T
```

设置当前容器组件的id标识，以及是否为焦点组。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean): T--><!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |
| isGroup | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## focusScopeId

```TypeScript
focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T
```

设置当前容器组件的id标识，以及是否为焦点组。新增参数arrowStepOut，用于设置能否使用方向键走焦出当前焦点组。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T--><!--Device-CommonMethod-focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |
| isGroup | boolean | 否 |
| arrowStepOut | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## focusScopePriority

```TypeScript
focusScopePriority(scopeId: string, priority?: FocusPriority): T
```

设置当前组件在指定容器内获焦的优先级。需要配合[focusScopeId](arkts-arkui-commonmethod-c.md#focusscopeid)一起使用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusScopePriority(scopeId: string, priority?: FocusPriority): T--><!--Device-CommonMethod-focusScopePriority(scopeId: string, priority?: FocusPriority): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scopeId | string | 是 |
| priority | [FocusPriority](../arkts-apis/arkts-arkui-focuspriority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## focusable

```TypeScript
focusable(value: boolean): T
```

设置当前组件是否可以获焦。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-focusable(value: boolean): T--><!--Device-CommonMethod-focusable(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T
```

为当前组件提供内容模糊能力。

> **说明：**
> 
> 从API version 18开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | 是 |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T
```

为当前组件提供内容模糊能力。与  
[foregroundBlurStyle](arkts-arkui-commonmethod-c.md#foregroundblurstyle)相比，style参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | 是 |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundBlurStyle

```TypeScript
foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T
```

为当前组件提供内容模糊能力。与  
[foregroundBlurStyle&lt;sup&gt;18+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#foregroundblurstyle)相比，新增了sysOptions参数，即支持系统自适应调节参数。

> **说明：**
> 
> foregroundBlurStyle接口为实时模糊接口，每帧执行实时渲染，性能负载较大。当模糊内容与模糊半径均无需变动时，推荐采用静态模糊接口
> [blur](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-effectkit-filter-i.md/arkts-arkgraphics2d-effectkit-filter-i.md#blur)。最佳实践请参考：
> [图像模糊动效优化-使用场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519)。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T--><!--Device-CommonMethod-foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | 是 |
| options | [ForegroundBlurStyleOptions](arkts-arkui-foregroundblurstyleoptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundColor

```TypeScript
foregroundColor(value: ResourceColor | ColoringStrategy): T
```

设置组件的前景色。当组件未设置前景色，默认继承父组件。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundColor(value: ResourceColor | ColoringStrategy): T--><!--Device-CommonMethod-foregroundColor(value: ResourceColor | ColoringStrategy): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColoringStrategy](../arkts-apis/arkts-arkui-enums-coloringstrategy-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundColor

```TypeScript
foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T
```

设置组件的前景色。当组件未设置前景色，默认继承父组件。与  
[foregroundColor](arkts-arkui-commonmethod-c.md#foregroundcolor)相比，color参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T--><!--Device-CommonMethod-foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;ResourceColor \| [ColoringStrategy&gt;](../arkts-apis/arkts-arkui-enums-coloringstrategy-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundEffect

```TypeScript
foregroundEffect(options: ForegroundEffectOptions): T
```

设置组件的前景属性。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundEffect(options: ForegroundEffectOptions): T--><!--Device-CommonMethod-foregroundEffect(options: ForegroundEffectOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ForegroundEffectOptions](arkts-arkui-foregroundeffectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## foregroundFilter

```TypeScript
foregroundFilter(filter: Filter): T
```

设置前景滤镜（内容）视觉效果。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-foregroundFilter(filter: Filter): T--><!--Device-CommonMethod-foregroundFilter(filter: Filter): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## freeze

```TypeScript
freeze(value: boolean): T
```

设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-freeze(value: boolean): T--><!--Device-CommonMethod-freeze(value: boolean): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## freeze

```TypeScript
freeze(freeze: Optional<boolean>): T
```

设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。与[freeze](arkts-arkui-commonmethod-c.md#freeze)相比，freeze参数新增了对undefined类型的支持。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-freeze(freeze: Optional<boolean>): T--><!--Device-CommonMethod-freeze(freeze: Optional<boolean>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [freeze](#freeze) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## geometryTransition

```TypeScript
geometryTransition(id: string): T
```

组件内隐式共享元素转场。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-geometryTransition(id: string): T--><!--Device-CommonMethod-geometryTransition(id: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## geometryTransition

```TypeScript
geometryTransition(id: string, options?: GeometryTransitionOptions): T
```

组件内隐式共享元素转场。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-geometryTransition(id: string, options?: GeometryTransitionOptions): T--><!--Device-CommonMethod-geometryTransition(id: string, options?: GeometryTransitionOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |
| options | [GeometryTransitionOptions](arkts-arkui-geometrytransitionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## gesture

```TypeScript
gesture(gesture: GestureType, mask?: GestureMask): T
```

绑定手势。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-gesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-gesture(gesture: GestureType, mask?: GestureMask): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## gestureModifier

```TypeScript
gestureModifier(modifier: GestureModifier): T
```

动态设置组件绑定的手势。

说明：gestureModifier不支持自定义组件。该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-gestureModifier(modifier: GestureModifier): T--><!--Device-CommonMethod-gestureModifier(modifier: GestureModifier): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [GestureModifier](arkts-arkui-gesturemodifier-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## grayscale

```TypeScript
grayscale(value: number): T
```

为组件添加灰度效果。上层渲染灰度会覆盖下层子组件渲染。不通过该接口设置时，默认无变化。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-grayscale(value: number): T--><!--Device-CommonMethod-grayscale(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## grayscale

```TypeScript
grayscale(grayscale: Optional<number>): T
```

为组件添加灰度效果。上层渲染灰度会覆盖下层子组件渲染。不通过该接口设置时，默认无变化。与[grayscale](arkts-arkui-commonmethod-c.md#grayscale)相比，grayscale参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-grayscale(grayscale: Optional<number>): T--><!--Device-CommonMethod-grayscale(grayscale: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [grayscale](#grayscale) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## gridOffset

```TypeScript
gridOffset(value: number): T
```

The default offset column number indicates the number of offset columns of the current component in the start direction of the parent component when the useSizeType attribute does not set the offset of the corresponding dimension. That is,the current component is located in the nth column.

**起始版本：** 11

**废弃版本：** 14

**替代接口：** grid_col/GridColInterface

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-gridOffset(value: number): T--><!--Device-CommonMethod-gridOffset(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## gridSpan

```TypeScript
gridSpan(value: number): T
```

Default number of occupied columns, indicating the number of occupied grid columns when the number of columns (span) of the corresponding size is not set in the useSizeType attribute.

**起始版本：** 11

**废弃版本：** 14

**替代接口：** grid_col/GridColInterface

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-gridSpan(value: number): T--><!--Device-CommonMethod-gridSpan(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## groupDefaultFocus

```TypeScript
groupDefaultFocus(value: boolean): T
```

设置当前组件是否为当前组件所在容器获焦时的默认焦点。当组件未设置groupDefaultFocus时，组件默认不为当前组件所在容器获焦时的默认焦点。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-groupDefaultFocus(value: boolean): T--><!--Device-CommonMethod-groupDefaultFocus(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## height

```TypeScript
height(value: Length): T
```

设置组件自身的高度，缺省时使用子组件自身内容需要的高度。若子组件的高大于父组件的高，则子组件会溢出显示在父组件外部。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-height(value: Length): T--><!--Device-CommonMethod-height(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## height

```TypeScript
height(heightValue: Length | LayoutPolicy): T
```

设置组件自身的高度或垂直方向布局策略，缺省时使用子组件自身内容需要的高度。若子组件的高大于父组件的高，则子组件会溢出显示在父组件外部。

从API version 15开始，当参数为Length类型时，该接口支持calc计算特性。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本15开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-height(heightValue: Length | LayoutPolicy): T--><!--Device-CommonMethod-height(heightValue: Length | LayoutPolicy): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| heightValue | [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LayoutPolicy](../arkts-apis/arkts-arkui-common-layoutpolicy-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## hitTestBehavior

```TypeScript
hitTestBehavior(value: HitTestMode): T
```

设置组件的触摸测试类型。如果组件不设置hitTestBehavior，其默认触摸测试类型为HitTestMode.Default。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-hitTestBehavior(value: HitTestMode): T--><!--Device-CommonMethod-hitTestBehavior(value: HitTestMode): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [HitTestMode](../arkts-apis/arkts-arkui-hittestmode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## hoverEffect

```TypeScript
hoverEffect(value: HoverEffect): T
```

设置组件的鼠标悬浮态显示效果。当未设置hoverEffect时，组件默认鼠标悬浮态效果为HoverEffect.Auto。对于应用了悬浮态效果的组件，当鼠标悬浮于组件上并按下时，悬浮态效果会消失；当鼠标松开时，悬浮态效果会恢复。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-hoverEffect(value: HoverEffect): T--><!--Device-CommonMethod-hoverEffect(value: HoverEffect): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [HoverEffect](../arkts-apis/arkts-arkui-hovereffect-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## hueRotate

```TypeScript
hueRotate(value: number | string): T
```

色相旋转效果。不通过该接口设置时，默认无变化。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-hueRotate(value: number | string): T--><!--Device-CommonMethod-hueRotate(value: number | string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## hueRotate

```TypeScript
hueRotate(rotation: Optional<number | string>): T
```

色相旋转效果。不通过该接口设置时，默认无变化。与[hueRotate](arkts-arkui-commonmethod-c.md#huerotate)相比，rotation参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-hueRotate(rotation: Optional<number | string>): T--><!--Device-CommonMethod-hueRotate(rotation: Optional<number | string>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rotation | [Optional](arkts-arkui-optional-t.md)&lt;number \| string&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## id

```TypeScript
id(value: string): T
```

Id. User can set an id to the component to identify it.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-id(value: string): T--><!--Device-CommonMethod-id(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T
```

扩展组件布局时的安全区。

> **说明：**
> 
> 
忽略布局安全区边缘的组件，如果其宽度或高度设置了 [LayoutPolicy.matchParent](arkts-arkui-layoutpolicy-c.md#matchparent)，其大小和位置都会改变，否则仅改变其位置。  
> 
> 依据safeAreaPadding累积功能，组件可扩展其安全区边缘到所有能感知的连续安全区域。
> 
> 滚动类组件的子元素忽略布局安全区边缘时在滚动方向不考虑滚动组件自身及其父组件的安全区域，包括：List、ArcListItem、Grid、WaterFlow、Swiper和Tabs。
> 
> 忽略布局安全区属性.ignoreLayoutSafeArea和忽略渲染安全区属性.expandSafeArea都设置时，.ignoreLayoutSafeArea先生效，.expandSafeArea在前者基础上再生效。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T--><!--Device-CommonMethod-ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;LayoutSafeAreaType&gt; | 否 |
| edges | Array&lt;LayoutSafeAreaEdge&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## inspectorLabel

```TypeScript
inspectorLabel(label: string | undefined): T
```

设置组件的检查器标签，该标签仅在DevEco Studio上显示。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-inspectorLabel(label: string | undefined): T--><!--Device-CommonMethod-inspectorLabel(label: string | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## invert

```TypeScript
invert(value: number | InvertOptions): T
```

反转输入的图像。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-invert(value: number | InvertOptions): T--><!--Device-CommonMethod-invert(value: number | InvertOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| [InvertOptions](../arkts-apis/arkts-arkui-common-invertoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## invert

```TypeScript
invert(options: Optional<number | InvertOptions>): T
```

反转输入的图像。与[invert](arkts-arkui-commonmethod-c.md#invert)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-invert(options: Optional<number | InvertOptions>): T--><!--Device-CommonMethod-invert(options: Optional<number | InvertOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;number \| [InvertOptions&gt;](../arkts-apis/arkts-arkui-common-invertoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## key

```TypeScript
key(value: string): T
```

控件标识，开发者可以通过标识来区分不同控件

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-key(value: string): T--><!--Device-CommonMethod-key(value: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## keyboardShortcut

```TypeScript
keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T
```

设置组件的自定义组合键。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T--><!--Device-CommonMethod-keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [FunctionKey](../../apis-input-kit/arkts-apis/arkts-input-inputdevice-functionkey-e.md) | 是 |
| keys | Array&lt;ModifierKey&gt; | 是 |
| action | () =&gt; void | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## layoutGravity

```TypeScript
layoutGravity(alignment: LocalizedAlignment): T
```

单独设置Stack组件中子组件的对齐规则，仅当父组件为Stack时生效。与align属性同时使用时，layoutGravity优先级更高，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-layoutGravity(alignment: LocalizedAlignment): T--><!--Device-CommonMethod-layoutGravity(alignment: LocalizedAlignment): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignment | [LocalizedAlignment](../arkts-apis/arkts-arkui-localizedalignment-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## layoutWeight

```TypeScript
layoutWeight(value: number | string): T
```

设置组件的布局权重，使组件在父容器（[Row](./row)/[Column](./column)/[Flex](./flex)）的主轴方向按照权重分配尺寸。适用于父容器尺寸确定、需要多个子组件按比例分配剩余空间的场景。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-layoutWeight(value: number | string): T--><!--Device-CommonMethod-layoutWeight(value: number | string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## lightUpEffect

```TypeScript
lightUpEffect(value: number): T
```

设置组件图像亮起程度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-lightUpEffect(value: number): T--><!--Device-CommonMethod-lightUpEffect(value: number): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## lightUpEffect

```TypeScript
lightUpEffect(degree: Optional<number>): T
```

设置组件图像亮起程度。与[lightUpEffect&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#lightupeffect)相比，degree参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-lightUpEffect(degree: Optional<number>): T--><!--Device-CommonMethod-lightUpEffect(degree: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## linearGradient

```TypeScript
linearGradient(value: LinearGradientOptions): T
```

线性渐变。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-linearGradient(value: LinearGradientOptions): T--><!--Device-CommonMethod-linearGradient(value: LinearGradientOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LinearGradientOptions](arkts-arkui-lineargradientoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## linearGradient

```TypeScript
linearGradient(options: Optional<LinearGradientOptions>): T
```

线性渐变。与[linearGradient](arkts-arkui-commonmethod-c.md#lineargradient)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-linearGradient(options: Optional<LinearGradientOptions>): T--><!--Device-CommonMethod-linearGradient(options: Optional<LinearGradientOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;LinearGradientOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## linearGradientBlur

```TypeScript
linearGradientBlur(value: number, options: LinearGradientBlurOptions): T
```

为组件添加内容线性渐变模糊效果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-linearGradientBlur(value: number, options: LinearGradientBlurOptions): T--><!--Device-CommonMethod-linearGradientBlur(value: number, options: LinearGradientBlurOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| options | [LinearGradientBlurOptions](arkts-arkui-lineargradientbluroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## linearGradientBlur

```TypeScript
linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T
```

为组件添加内容线性渐变模糊效果。与  
[linearGradientBlur&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#lineargradientblur)相比，新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T--><!--Device-CommonMethod-linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurRadius | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |
| options | [Optional](arkts-arkui-optional-t.md)&lt;LinearGradientBlurOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## margin

```TypeScript
margin(value: Margin | Length | LocalizedMargin): T
```

设置组件的外边距属性。在计算位置时外边距视为组件大小的一部分，从而影响组件位置。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-margin(value: Margin | Length | LocalizedMargin): T--><!--Device-CommonMethod-margin(value: Margin | Length | LocalizedMargin): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Margin](../arkts-apis/arkts-arkui-margin-t.md) \| Length \| [LocalizedMargin](../arkts-apis/arkts-arkui-localizedmargin-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## markAnchor

```TypeScript
markAnchor(value: Position | LocalizedPosition): T
```

设置元素在位置定位时的锚点，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-markAnchor(value: Position | LocalizedPosition): T--><!--Device-CommonMethod-markAnchor(value: Position | LocalizedPosition): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) \| [LocalizedPosition](../arkts-apis/arkts-arkui-units-localizedposition-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## mask

```TypeScript
mask(value: ProgressMask): T
```

为组件上添加可调节进度的遮罩。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-mask(value: ProgressMask): T--><!--Device-CommonMethod-mask(value: ProgressMask): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ProgressMask](arkts-arkui-progressmask-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## mask

```TypeScript
mask(mask: Optional<ProgressMask>): T
```

为组件上添加可调节进度的遮罩。与[mask&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#mask)相比，新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-mask(mask: Optional<ProgressMask>): T--><!--Device-CommonMethod-mask(mask: Optional<ProgressMask>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mask](#mask) | [Optional](arkts-arkui-optional-t.md)&lt;ProgressMask&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## mask

```TypeScript
mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T
```

为组件上添加指定形状的遮罩。

> **说明：**

**起始版本：** 7

**废弃版本：** 12

**替代接口：** [CommonMethod#maskShape](arkts-arkui-commonmethod-c.md#maskshape)(value:

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T--><!--Device-CommonMethod-mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CircleAttribute](arkts-arkui-circle-attribute.md) \| EllipseAttribute \| PathAttribute \| RectAttribute \| [ProgressMask](arkts-arkui-progressmask-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## maskShape

```TypeScript
maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T
```

为组件上添加指定形状的遮罩。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T--><!--Device-CommonMethod-maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-circleshape-t.md) \| EllipseShape \| PathShape \| [RectShape](../arkts-apis/arkts-arkui-arkui-shape-rectshape-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## maskShape

```TypeScript
maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T
```

为组件上添加指定形状的遮罩。与  
[maskShape&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#maskshape)相比，新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T--><!--Device-CommonMethod-maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shape | [Optional](arkts-arkui-optional-t.md)&lt;CircleShape \| EllipseShape \| PathShape \| [RectShape&gt;](../arkts-apis/arkts-arkui-arkui-shape-rectshape-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## materialFilter

```TypeScript
materialFilter(filter: Filter | undefined): T
```

设置系统材质滤镜效果，系统材质滤镜的绘制早于[backgroundFilter](arkts-arkui-commonmethod-c.md#backgroundfilter)绘制，即位于backgroundFilter的更底层。

> **说明：**
> 
> 该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-materialFilter(filter: Filter | undefined): T--><!--Device-CommonMethod-materialFilter(filter: Filter | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## monopolizeEvents

```TypeScript
monopolizeEvents(monopolize: boolean): T
```

设置组件是否独占事件。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-monopolizeEvents(monopolize: boolean): T--><!--Device-CommonMethod-monopolizeEvents(monopolize: boolean): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monopolize | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## motionBlur

```TypeScript
motionBlur(value: MotionBlurOptions):T
```

在当前组件由缩放大小或位移变化引起的运动过程中，增加动态模糊效果。

> **说明：**
> 
> - 不建议在组件内转场、共享元素转场、组件内隐式元素转场和粒子动画场景中使用该属性，否则会产生非预期效果。
> 
> - 该属性需要在开始状态将motionBlur的参数radius设置为0，否则冷启动时会有非预期效果。
> 
> - 该属性需要与动画的AnimateParam的onFinish参数配合使用，需要在运动模糊动画结束后将motionBlur的参数radius置为0，否则会产生非预期效果。
> 
> - 在使用该属性过程中，不要在使用过程中频繁更改同一个组件的模糊半径，否则会产生非预期效果。比如示例中的动画，频繁点击会出现模糊效果偶尔失效的情况。
> 
> - 运动模糊锚点坐标需要与动画缩放的锚点保持一致，否则会产生非预期效果。
> 
> - 模糊半径建议设置1以内，否则会产生非预期效果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-motionBlur(value: MotionBlurOptions):T--><!--Device-CommonMethod-motionBlur(value: MotionBlurOptions):T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MotionBlurOptions](arkts-arkui-motionbluroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## motionBlur

```TypeScript
motionBlur(motionBlur: Optional<MotionBlurOptions>):T
```

在当前组件由缩放大小或位移变化引起的运动过程中，增加动态模糊效果。与[motionBlur](arkts-arkui-commonmethod-c.md#motionblur)相比，motionBlur参数新增了对undefined类型的支持。

1、不建议在组件内转场、共享元素转场、组件内隐式元素转场、粒子动画场景下使用该属性，否则会产生非预期效果。

2、该属性需要在开始状态将motionBlur的参数radius设置为0，否则冷启动时会有非预期效果。

3、该属性需要与动画的AnimateParam的onFinish参数配合使用，需要在运动模糊动画结束后将motionBlur的参数radius置为0，否则会产生非预期效果。

4、在使用该属性过程中，不要在使用过程中频繁更改同一个组件的模糊半径，否则会产生非预期效果。比如示例中的动画，频繁点击会出现模糊效果偶尔失效的情况。

5、运动模糊锚点坐标需要与动画缩放的锚点保持一致，否则会产生非预期效果。

6、模糊半径建议设置1以内，否则会产生非预期效果。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-motionBlur(motionBlur: Optional<MotionBlurOptions>):T--><!--Device-CommonMethod-motionBlur(motionBlur: Optional<MotionBlurOptions>):T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [motionBlur](#motionblur) | [Optional](arkts-arkui-optional-t.md)&lt;MotionBlurOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## motionPath

```TypeScript
motionPath(value: MotionPathOptions): T
```

设置组件的路径动画。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-motionPath(value: MotionPathOptions): T--><!--Device-CommonMethod-motionPath(value: MotionPathOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MotionPathOptions](arkts-arkui-motionpathoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## mouseResponseRegion

```TypeScript
mouseResponseRegion(value: Array<Rectangle> | Rectangle): T
```

设置一个或多个鼠标触摸热区。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-mouseResponseRegion(value: Array<Rectangle> | Rectangle): T--><!--Device-CommonMethod-mouseResponseRegion(value: Array<Rectangle> | Rectangle): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;Rectangle&gt; \| [Rectangle](../arkts-apis/arkts-arkui-common-rectangle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## nextFocus

```TypeScript
nextFocus(nextStep: Optional<FocusMovement>): T
```

设置组件的自定义焦点走焦逻辑。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-nextFocus(nextStep: Optional<FocusMovement>): T--><!--Device-CommonMethod-nextFocus(nextStep: Optional<FocusMovement>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextStep | [Optional](arkts-arkui-optional-t.md)&lt;FocusMovement&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## obscured

```TypeScript
obscured(reasons: Array<ObscuredReasons>): T
```

Sets obscured

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-obscured(reasons: Array<ObscuredReasons>): T--><!--Device-CommonMethod-obscured(reasons: Array<ObscuredReasons>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reasons | Array&lt;ObscuredReasons&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## offset

```TypeScript
offset(value: Position | Edges | LocalizedEdges): T
```

相对偏移，组件相对原本的布局位置进行偏移。和position一起使用时，position生效，offset不生效，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-offset(value: Position | Edges | LocalizedEdges): T--><!--Device-CommonMethod-offset(value: Position | Edges | LocalizedEdges): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) \| Edges \| [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAccessibilityActionIntercept

```TypeScript
onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T
```

注册可访问性操作拦截回调，当要执行可访问性操作时，将执行回调

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T--><!--Device-CommonMethod-onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityActionInterceptCallback](arkts-arkui-accessibilityactioninterceptcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAccessibilityFocus

```TypeScript
onAccessibilityFocus(callback: AccessibilityFocusCallback): T
```

Register accessibility focus callback,when the component is focused or out of focus,the callback will be executed

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onAccessibilityFocus(callback: AccessibilityFocusCallback): T--><!--Device-CommonMethod-onAccessibilityFocus(callback: AccessibilityFocusCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityFocusCallback](arkts-arkui-accessibilityfocuscallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAccessibilityHover

```TypeScript
onAccessibilityHover(callback: AccessibilityCallback): T
```

Trigger a accessibility hover event.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAccessibilityHover(callback: AccessibilityCallback): T--><!--Device-CommonMethod-onAccessibilityHover(callback: AccessibilityCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAccessibilityHoverTransparent

```TypeScript
onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T
```

prompt for current component and descendants unable to handle accessibility hover event

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T--><!--Device-CommonMethod-onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAppear

```TypeScript
onAppear(event: () => void): T
```

组件挂载后触发此回调。

> **说明：**
> 
> 回调的调用时机有可能发生在组件布局渲染后。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onAppear(event: () => void): T--><!--Device-CommonMethod-onAppear(event: () => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAreaChange

```TypeScript
onAreaChange(event: (oldValue: Area, newValue: Area) => void): T
```

组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

由绘制变化所导致的渲染属性变化不会响应回调，如[translate](arkts-arkui-commonmethod-c.md#translate)、  
[offset](arkts-arkui-commonmethod-c.md#offset)、[markAnchor](arkts-arkui-commonmethod-c.md#markanchor)、  
[scale](arkts-arkui-commonmethod-c.md#scale)、[transform](arkts-arkui-commonmethod-c.md#transform)。若组件自身位置由绘制变化决定也不会响应回调，如[bindSheet](arkts-arkui-commonmethod-c.md#bindsheet)。

> **说明：**
> 
> 当组件同时绑定onAreaChange事件和[position](arkts-arkui-commonmethod-c.md#position)属性时，onAreaChange事件响应设置
> [Position](../arkts-apis/arkts-arkui-position-t.md/arkts-arkui-position-t.md)类型的position属性变化，不响应设置[Edges](../arkts-apis/arkts-arkui-graphics-edges-i.md/arkts-arkui-graphics-edges-i.md)和[LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md/arkts-arkui-localizededges-i.md)
> 类型的position属性变化。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAreaChange(event: (oldValue: Area, newValue: Area) => void): T--><!--Device-CommonMethod-onAreaChange(event: (oldValue: Area, newValue: Area) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (oldValue: Area, newValue: Area) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAreaChange

```TypeScript
onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T
```

组件区域变化时触发该回调，可通过[AreaChangeOptions](arkts-arkui-areachangeoptions-i.md)中的expectedUpdateInterval设置触发回调的间隔。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T--><!--Device-CommonMethod-onAreaChange(event: AreaChangeCallback, options?: AreaChangeOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [AreaChangeCallback](arkts-arkui-areachangecallback-t.md) | 是 |
| options | [AreaChangeOptions](arkts-arkui-areachangeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## onAttach

```TypeScript
onAttach(callback: Callback<void>): T
```

组件挂载到组件树时触发此回调。由于以下说明中的限制，建议使用[onAppear](arkts-arkui-commonmethod-c.md#onappear)替代此接口。

> **说明：**
> 
> - 回调在组件布局渲染前调用。
> 
> - 不允许在回调中对组件树进行变更，例如启动动画或使用if-else变更组件树结构。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAttach(callback: Callback<void>): T--><!--Device-CommonMethod-onAttach(callback: Callback<void>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onAxisEvent

```TypeScript
onAxisEvent(event: Callback<AxisEvent>): T
```

鼠标滚轮滚动或触控板双指轻触滑动、双指捏合时触发该回调。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onAxisEvent(event: Callback<AxisEvent>): T--><!--Device-CommonMethod-onAxisEvent(event: Callback<AxisEvent>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AxisEvent&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onBlur

```TypeScript
onBlur(event: () => void): T
```

当前组件失去焦点时触发的回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onBlur(event: () => void): T--><!--Device-CommonMethod-onBlur(event: () => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onChildTouchTest

```TypeScript
onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T
```

当前组件通过设置回调，可自定义触摸测试并控制触摸测试中的子节点行为。

> **说明：**
> 
> - 子节点信息数组中仅包含命名节点的信息，即开发者通过id属性设置了id的节点。
> 
> - 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T--><!--Device-CommonMethod-onChildTouchTest(event: (value: Array<TouchTestInfo>) => TouchResult): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (value: Array&lt;TouchTestInfo&gt;) =&gt; TouchResult | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onClick

```TypeScript
onClick(event: (event: ClickEvent) => void): T
```

点击动作触发该回调。

触发点击事件的设备类型为键盘或手柄时，事件的SourceTool值为Unknown，事件的[SourceType](arkts-arkui-sourcetype-e.md)值为KEY，JOYSTICK。

> **说明：**
> 
> 从API version 9开始，使用卡片能力时存在以下限制：
> 
> 1. 如果手指按下的持续时间超过800ms，不能触发点击事件。
> 
> 2. 如果手指按下后移动位移超过20px，不能触发点击事件。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onClick(event: (event: ClickEvent) => void): T--><!--Device-CommonMethod-onClick(event: (event: ClickEvent) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: ClickEvent) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onClick

```TypeScript
onClick(event: Callback<ClickEvent>, distanceThreshold: number): T
```

点击动作触发该回调。

当触发点击事件的设备类型为键盘或手柄时，事件的[SourceTool](arkts-arkui-sourcetool-e.md)值为Unknown，事件的[SourceType](arkts-arkui-sourcetype-e.md)值为KEY或JOYSTICK。

新增distanceThreshold参数，设置点击手势移动阈值。手指移动超出阈值时，点击手势识别失败。

对于无手指移动距离限制的点击场景，建议使用原有接口。若需限制点击时手指移动范围，建议使用该接口。

> **说明：**
> 
> - 从API version 12开始，在使用卡片能力时，存在以下限制：
> > 1. 如果手指按下的持续时间超过800ms，不能触发点击事件。
> > 2. 如果手指按下后移动位移超过20px，不能触发点击事件。
> 
> - 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onClick(event: Callback<ClickEvent>, distanceThreshold: number): T--><!--Device-CommonMethod-onClick(event: Callback<ClickEvent>, distanceThreshold: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ClickEvent&gt; | 是 |
| distanceThreshold | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDetach

```TypeScript
onDetach(callback: Callback<void>): T
```

组件从组件树卸载时触发此回调。建议使用[onDisAppear](arkts-arkui-commonmethod-c.md#ondisappear)替代此接口。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDetach(callback: Callback<void>): T--><!--Device-CommonMethod-onDetach(callback: Callback<void>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDigitalCrown

```TypeScript
onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T
```

组件获焦以后旋转表冠时触发该回调。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T--><!--Device-CommonMethod-onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;Callback&lt;CrownEvent&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDisAppear

```TypeScript
onDisAppear(event: () => void): T
```

组件从组件树卸载时触发此回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onDisAppear(event: () => void): T--><!--Device-CommonMethod-onDisAppear(event: () => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragEnd

```TypeScript
onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T
```

绑定此事件的组件触发的拖拽结束后，触发回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragEnd(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragEnter

```TypeScript
onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T
```

拖拽进入组件范围内时，触发回调，当监听了[onDrop](arkts-arkui-commonmethod-c.md#ondrop)事件时，此事件才有效。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragEnter(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragLeave

```TypeScript
onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T
```

拖拽离开组件范围内时，触发回调，当监听了[onDrop](arkts-arkui-commonmethod-c.md#ondrop)事件时，此事件才有效。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragLeave(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragMove

```TypeScript
onDragMove(event: (event: DragEvent, extraParams?: string) => void): T
```

拖拽在组件范围内移动时，触发回调，当监听了[onDrop](arkts-arkui-commonmethod-c.md#ondrop)事件时，此事件才有效。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragMove(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDragMove(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragSpringLoading

```TypeScript
onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T
```

绑定此事件的组件可作为具有悬停检测功能的拖拽响应目标。当拖拽对象悬停在目标上时，触发回调通知。此时只有一个目标可以成为响应方，并且子组件始终具有更高的响应优先级。

关于悬停检测的触发机制及详细使用方法，请参考开发指南[支持悬停检测](../../../ui/arkts-common-events-drag-event.md#支持悬停检测)。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T--><!--Device-CommonMethod-onDragSpringLoading(callback: Callback<SpringLoadingContext> | null, configuration?: DragSpringLoadingConfiguration): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SpringLoadingContext&gt; \| null | 是 |
| configuration | [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## onDragStart

```TypeScript
onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T
```

在手势拖拽场景中，在可拖拽的组件上长按时间超过500ms，然后手指移动距离大于10vp时触发此回调；在鼠标拖拽场景中，鼠标左键在可拖拽的组件上按下并移动超过1vp时，即可触发此回调。

针对默认支持拖拽能力的组件，如果开发者设置了onDragStart，优先执行onDragStart，并根据执行情况决定是否使用系统默认的拖拽能力，具体规则为：

- 如果开发者返回了自定义预览图，则不再使用系统默认的拖拽预览图；  
- 如果开发者设置了拖拽数据，则不再使用系统默认填充的拖拽数据。

文本类组件[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)、[Search](search)、[TextInput](text_input)、[TextArea](text_area)、  
[RichEditor](rich_editor)对选中的文本内容进行拖拽时，不支持自定义预览图。当onDragStart与菜单预览一起使用或使用了默认支持拖拽能力的组件时，预览及菜单项上的自定义内容不支持拖拽。

> **说明：**
> 
> 从API version 13开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T--><!--Device-CommonMethod-onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; CustomBuilder \| [DragItemInfo](../arkts-apis/arkts-arkui-common-dragiteminfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDrop

```TypeScript
onDrop(event: (event: DragEvent, extraParams?: string) => void): T
```

绑定此事件的组件可作为释放目标。当在本组件范围内停止拖放行为时，将触发回调。如果开发者未在onDrop中主动调用event.setResult()来设置拖拽接收的结果，对于系统支持的默认可拖入组件，处理结果将以系统实际处理的数据为准。对于其他组件，系统将默认视为数据接收成功。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDrop(event: (event: DragEvent, extraParams?: string) => void): T--><!--Device-CommonMethod-onDrop(event: (event: DragEvent, extraParams?: string) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: DragEvent, extraParams?: string) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onDrop

```TypeScript
onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T
```

绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。如果开发者没有在onDrop中主动调用event.[setResult](arkts-arkui-dragevent-i.md#setresult)()设置拖拽接收的结果，若拖拽组件为系统支持默认拖入的组件，以系统实际处理数据结果为准，其它组件则系统按照数据接收成功处理。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T--><!--Device-CommonMethod-onDrop(eventCallback: OnDragEventCallback, dropOptions?: DropOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventCallback | [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) | 是 |
| dropOptions | [DropOptions](arkts-arkui-dropoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## onFocus

```TypeScript
onFocus(event: () => void): T
```

当前组件获取焦点时触发的回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onFocus(event: () => void): T--><!--Device-CommonMethod-onFocus(event: () => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onFocusAxisEvent

```TypeScript
onFocusAxisEvent(event: Callback<FocusAxisEvent>): T
```

给组件绑定焦点轴事件回调。绑定该方法的组件获焦后，游戏手柄上的摇杆、十字键等的操作会触发该回调。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onFocusAxisEvent(event: Callback<FocusAxisEvent>): T--><!--Device-CommonMethod-onFocusAxisEvent(event: Callback<FocusAxisEvent>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FocusAxisEvent&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onGestureCollectIntercept

```TypeScript
onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T
```

在当前节点及更高优先级节点上的事件和手势被收集完成后触发该回调。该回调可用于干预事件和手势的收集结果。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T--><!--Device-CommonMethod-onGestureCollectIntercept(callback: GestureCollectInterceptCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onGestureJudgeBegin

```TypeScript
onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T
```

为组件绑定自定义手势判定回调。当手势即将成功时，触发用户定义的回调获取结果。

> **说明：**
> 
> 在Text组件中使用该接口时，不支持对点击事件进行自定义手势判定。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T--><!--Device-CommonMethod-onGestureJudgeBegin(callback: (gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (gestureInfo: GestureInfo, event: BaseGestureEvent) =&gt; GestureJudgeResult | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onGestureRecognizerJudgeBegin

```TypeScript
onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T
```

给组件绑定自定义手势识别器判定回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T--><!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onGestureRecognizerJudgeBegin

```TypeScript
onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T
```

给组件绑定自定义手势识别器判定回调。

新增exposeInnerGesture参数作为是否将ArkUI系统组合组件的内置组件的手势暴露给开发者的标识。当该标识置为true时，将ArkUI系统组合组件的内置组件的手势暴露给开发者。

对于不需要将ArkUI系统组合组件的内置组件的手势暴露给开发者的场景，建议采用原有  
[onGestureRecognizerJudgeBegin](arkts-arkui-commonmethod-c.md#ongesturerecognizerjudgebegin)接口。若要求将ArkUI系统组合组件的内置组件的手势暴露给开发者，建议使用该接口并将exposeInnerGesture设置为true。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T--><!--Device-CommonMethod-onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback, exposeInnerGesture: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) | 是 |
| exposeInnerGesture | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onHover

```TypeScript
onHover(event: (isHover: boolean, event: HoverEvent) => void): T
```

鼠标或手写笔进入或退出组件时，触发hover事件。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onHover(event: (isHover: boolean, event: HoverEvent) => void): T--><!--Device-CommonMethod-onHover(event: (isHover: boolean, event: HoverEvent) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (isHover: boolean, event: HoverEvent) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onHoverMove

```TypeScript
onHoverMove(event: Callback<HoverEvent>): T
```

手写笔悬浮于组件上方时触发悬浮移动事件。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onHoverMove(event: Callback<HoverEvent>): T--><!--Device-CommonMethod-onHoverMove(event: Callback<HoverEvent>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;HoverEvent&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onKeyEvent

```TypeScript
onKeyEvent(event: (event: KeyEvent) => void): T
```

绑定该方法的组件获焦后，按键动作触发该回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onKeyEvent(event: (event: KeyEvent) => void): T--><!--Device-CommonMethod-onKeyEvent(event: (event: KeyEvent) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: KeyEvent) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onKeyEvent

```TypeScript
onKeyEvent(event: Callback<KeyEvent, boolean>): T
```

当绑定该方法的组件获焦后，按键操作将触发此回调。若此回调的返回值为`true`，则视为按键事件已被处理。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onKeyEvent(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyEvent(event: Callback<KeyEvent, boolean>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyEvent, boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onKeyEventDispatch

```TypeScript
onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T
```

对应组件收到按键事件时，会触发该回调，该按键事件不会分发给其子组件。不支持构造KeyEvent进行分发，只支持分发已有的按键事件。

该回调的返回值为`true`时，视作该按键事件已被消费，不会[冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)给父组件处理。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyEvent, boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onKeyPreIme

```TypeScript
onKeyPreIme(event: Callback<KeyEvent, boolean>): T
```

绑定该方法的组件获焦后，按键动作优先触发该回调。

该回调的返回值为`true`时，视作该按键事件已被消费，后续的事件回调（`keyboardShortcut`、输入法事件、`onKeyEventDispatch`、`onKeyEvent`）会被拦截，不再触发。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onKeyPreIme(event: Callback<KeyEvent, boolean>): T--><!--Device-CommonMethod-onKeyPreIme(event: Callback<KeyEvent, boolean>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;KeyEvent, boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onMouse

```TypeScript
onMouse(event: (event: MouseEvent) => void): T
```

当前组件被鼠标按键点击时或者鼠标在组件上悬浮移动时，触发该回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onMouse(event: (event: MouseEvent) => void): T--><!--Device-CommonMethod-onMouse(event: (event: MouseEvent) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: MouseEvent) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onNeedSoftkeyboard

```TypeScript
onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T
```

设置组件判断是否需要键盘时触发的回调。主要用于键盘接续场景，当焦点从输入框切换到其他组件时，如果切换后的组件回调函数[OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md)的返回值设置为`true`，则表示该组件需要键盘，此时键盘将不会收起，如果返回值设置为`false`，则表示该组件不需要键盘，此时键盘将收起。

对于不能获焦的组件，本接口不生效。

输入框组件使用该接口并将返回值设置为`false`时，点击输入框将不会拉起键盘。

Web组件使用该方法时，如果返回值为`true`，Web组件会判断组件中是否有可编辑节点，如果有可编辑节点才会保留键盘，如果返回值为`false`，无论是否有可编辑节点，键盘都不会保留。

XComponent组件使用该方法时，如果返回值为`true`且XComponent组件使用 [OH_ArkUI_XComponent_SetNeedSoftKeyboard()](../../../reference/apis-arkui/capi-native-interface-xcomponent-h.md#oh_arkui_xcomponent_setneedsoftkeyboard)设置了需要键盘，才会保留键盘，如果返回值为`false`，无论组件如何设置，键盘都不会保留。

当返回值为`true`时，应用的自绘制输入框需要在获焦时主动调用 [attach](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-inputmethodcontroller-i.md/arkts-ime-inputmethod-inputmethodcontroller-i.md#attach)方法，建立输入法框架和输入法应用的通信，否则点击键盘会失去响应。说明：失焦时输入法框架和输入法应用的通信会断开，获焦时需要重新建立通信。

该接口只适用于对输入法应用接续的场景，对自定义键盘不生效。自定义键盘接续详见[setCustomKeyboardContinueFeature](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#setcustomkeyboardcontinuefeature)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T--><!--Device-CommonMethod-onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onNeedSoftkeyboardCallback | [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onPreDrag

```TypeScript
onPreDrag(callback: Callback<PreDragStatus>): T
```

绑定此事件的组件，当处于手势拖拽发起前的不同阶段时，触发回调。拖拽发起前的各阶段可参考[PreDragStatus](arkts-arkui-predragstatus-e.md)。此接口不支持在鼠标拖拽中触发。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onPreDrag(callback: Callback<PreDragStatus>): T--><!--Device-CommonMethod-onPreDrag(callback: Callback<PreDragStatus>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PreDragStatus&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onSizeChange

```TypeScript
onSizeChange(event: SizeChangeCallback): T
```

组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。

> **说明：**
> 
> 1. 该接口在布局发生变化时触发，由于计算精度的关系，其返回值可能与真实物理尺寸存在细微的差异。
> 
> 2. onSizeChange是布局过程中触发的同步回调，直接在其中更改状态变量存在被纳入动画闭包的风险。具体而言，动画会对比动画前的布局与动画闭包后的布局，若onSizeChange的回调在动画前的布局中同步触发，那么
> onSizeChange回调中所做的变更将与动画闭包中的变更一同纳入动画过程。为了避免此类问题，可在onSizeChange中使用延迟时间为0的
> [setTimeout](../arkts-apis/arkts-arkui-global-settimeout-f.md/arkts-arkui-global-settimeout-f.md#settimeout)或
> [postFrameCallback](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md/arkts-arkui-arkui-uicontext-uicontext-c.md#postframecallback)，将UI处理逻辑
> 延后至异步执行。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-onSizeChange(event: SizeChangeCallback): T--><!--Device-CommonMethod-onSizeChange(event: SizeChangeCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onTouch

```TypeScript
onTouch(event: (event: TouchEvent) => void): T
```

手指触摸动作触发该回调。触摸事件默认[冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)，会被多个组件消费，如果需阻止冒泡，可参考  
[TouchEvent](arkts-arkui-touchevent-i.md)的stopPropagation方法。鼠标左键按下时，对应的事件也会转换成触摸事件并触发该回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onTouch(event: (event: TouchEvent) => void): T--><!--Device-CommonMethod-onTouch(event: (event: TouchEvent) => void): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (event: TouchEvent) =&gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onTouchIntercept

```TypeScript
onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T
```

给组件绑定自定义事件拦截回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T--><!--Device-CommonMethod-onTouchIntercept(callback: Callback<TouchEvent, HitTestMode>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TouchEvent, HitTestMode&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onTouchTestDone

```TypeScript
onTouchTestDone(callback: TouchTestDoneCallback): T
```

提供在[触摸测试](../../../ui/arkts-interaction-basic-principles.md#触摸测试)结束后，指定手势识别器是否参与后续处理的能力。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onTouchTestDone(callback: TouchTestDoneCallback): T--><!--Device-CommonMethod-onTouchTestDone(callback: TouchTestDoneCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onVisibleAreaApproximateChange

```TypeScript
onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T
```

设置onVisibleAreaApproximateChange事件的回调参数，限制它的执行间隔。

> **说明：**
> 
> 从API version 23开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 17

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本17开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T--><!--Device-CommonMethod-onVisibleAreaApproximateChange(options: VisibleAreaEventOptions, event: VisibleAreaChangeCallback | undefined): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VisibleAreaEventOptions](arkts-arkui-visibleareaeventoptions-i.md) | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onVisibleAreaChange

```TypeScript
onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T
```

组件可见区域变化时触发该回调。开发指导及常见问题请参考[感知组件可见性](../../../ui/arkts-manage-components-visibility.md)指南。

> **说明：**
> 
> - 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。
> 
> - 仅提供自身节点相对于所有祖先节点（直到window边界）的相对裁切面积与自身面积的比值及其变化趋势。
> 
> - 不支持兄弟组件对自身节点的遮挡计算，不支持所有祖先的兄弟节点对自身节点的遮挡计算，不支持窗口遮挡计算，不支持组件旋转计算，如[Stack](../../apis-arkts/arkts-apis/arkts-arkts-util-stack-stack-c.md/arkts-arkts-util-stack-stack-c.md)、[Z序控制](arkts-arkui-commonmethod-c.md#zindex)、
> [rotate](arkts-arkui-commonmethod-c.md#rotate)等。
> 
> - 不支持非挂树节点的可见面积变化计算。例如，预加载的节点、通过[overlay](arkts-arkui-commonmethod-c.md#overlay)能力挂载的自定义节点。
> 
> - 不支持[scale](arkts-arkui-commonmethod-c.md#scale)属性，如果想要支持
> [scale](arkts-arkui-commonmethod-c.md#scale)，则需使用
> [onVisibleAreaChange&lt;sup&gt;22+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#onvisibleareachange)
> ，将measureFromViewport设置为true。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T--><!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ratios | Array&lt;number&gt; | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## onVisibleAreaChange

```TypeScript
onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T
```

组件可见区域变化时触发该回调。可以通过measureFromViewport设置可见区域计算模式。开发指导及常见问题请参考  
[感知组件可见性](../../../ui/arkts-manage-components-visibility.md)指南。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T--><!--Device-CommonMethod-onVisibleAreaChange(ratios: Array<number>, event: VisibleAreaChangeCallback, measureFromViewport: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ratios | Array&lt;number&gt; | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) | 是 |
| measureFromViewport | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## opacity

```TypeScript
opacity(value: number | Resource): T
```

设置组件的不透明度。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-opacity(value: number | Resource): T--><!--Device-CommonMethod-opacity(value: number | Resource): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## opacity

```TypeScript
opacity(opacity: Optional<number | Resource>): T
```

设置组件的不透明度。与[opacity](arkts-arkui-commonmethod-c.md#opacity)相比，opacity参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-opacity(opacity: Optional<number | Resource>): T--><!--Device-CommonMethod-opacity(opacity: Optional<number | Resource>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [opacity](#opacity) | [Optional](arkts-arkui-optional-t.md)&lt;number \| [Resource&gt;](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outline

```TypeScript
outline(value: OutlineOptions): T
```

统一外描边样式设置接口。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outline(value: OutlineOptions): T--><!--Device-CommonMethod-outline(value: OutlineOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OutlineOptions](../arkts-apis/arkts-arkui-outlineoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outline

```TypeScript
outline(options: Optional<OutlineOptions>): T
```

统一外描边样式设置接口。与[outline](arkts-arkui-commonmethod-c.md#outline)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outline(options: Optional<OutlineOptions>): T--><!--Device-CommonMethod-outline(options: Optional<OutlineOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;OutlineOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineColor

```TypeScript
outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T
```

设置元素的外描边颜色。不设置该接口时，默认显示为黑色。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T--><!--Device-CommonMethod-outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| EdgeColors \| [LocalizedEdgeColors](../arkts-apis/arkts-arkui-localizededgecolors-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineColor

```TypeScript
outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T
```

设置元素的外描边颜色。不设置该接口时，默认显示为黑色。与  
[outlineColor](arkts-arkui-commonmethod-c.md#outlinecolor)相比，color参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T--><!--Device-CommonMethod-outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](arkts-arkui-optional-t.md)&lt;ResourceColor \| EdgeColors \| [LocalizedEdgeColors&gt;](../arkts-apis/arkts-arkui-localizededgecolors-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineRadius

```TypeScript
outlineRadius(value: Dimension | OutlineRadiuses): T
```

设置元素的外描边圆角半径。不设置该接口时，默认无变化。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineRadius(value: Dimension | OutlineRadiuses): T--><!--Device-CommonMethod-outlineRadius(value: Dimension | OutlineRadiuses): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [OutlineRadiuses](../arkts-apis/arkts-arkui-units-outlineradiuses-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineRadius

```TypeScript
outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T
```

设置元素的外描边圆角半径。不设置该接口时，默认无变化。与[outlineRadius](arkts-arkui-commonmethod-c.md#outlineradius)相比，radius参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T--><!--Device-CommonMethod-outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | [Optional](arkts-arkui-optional-t.md)&lt;Dimension \| [OutlineRadiuses&gt;](../arkts-apis/arkts-arkui-units-outlineradiuses-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineStyle

```TypeScript
outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T
```

设置元素的外描边样式。不设置该接口时，默认显示为一条实线。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T--><!--Device-CommonMethod-outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OutlineStyle](arkts-arkui-outlinestyle-e.md) \| [EdgeOutlineStyles](../arkts-apis/arkts-arkui-units-edgeoutlinestyles-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineStyle

```TypeScript
outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T
```

设置元素的外描边样式。不设置该接口时，默认显示为一条实线。与  
[outlineStyle](arkts-arkui-commonmethod-c.md#outlinestyle)相比，style参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T--><!--Device-CommonMethod-outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;OutlineStyle \| [EdgeOutlineStyles&gt;](../arkts-apis/arkts-arkui-units-edgeoutlinestyles-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineWidth

```TypeScript
outlineWidth(value: Dimension | EdgeOutlineWidths): T
```

设置元素的外描边宽度。不设置该接口时，默认无变化。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineWidth(value: Dimension | EdgeOutlineWidths): T--><!--Device-CommonMethod-outlineWidth(value: Dimension | EdgeOutlineWidths): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) \| [EdgeOutlineWidths](../arkts-apis/arkts-arkui-units-edgeoutlinewidths-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## outlineWidth

```TypeScript
outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T
```

设置元素的外描边宽度。不设置该接口时，默认无变化。与[outlineWidth](arkts-arkui-commonmethod-c.md#outlinewidth)相比，width参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T--><!--Device-CommonMethod-outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [width](#width) | [Optional](arkts-arkui-optional-t.md)&lt;Dimension \| [EdgeOutlineWidths&gt;](../arkts-apis/arkts-arkui-units-edgeoutlinewidths-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## overlay

```TypeScript
overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T
```

在当前组件上，增加遮罩文本或者叠加自定义组件以及[ComponentContent](arkts-arkui-componentcontent-t.md)作为该组件的浮层。浮层的定位同样基于当前组件进行计算。浮层不通过组件树进行渲染，部分接口（例如  
[getRectangleById](api\@ohos.arkui.ComponentUtils#getRectangleById)）不支持获取浮层中的组件。

> **说明：**
> 
> - overlay会将浮层组件覆盖在所绑定的组件上方，阻塞用户对浮层下方组件的所有交互操作。
> - 多次调用overlay接口时，如果同时传入string类型和
> [CustomBuilder](arkts-arkui-custombuilder-t.md)类型，或者同时传入string类型和
> [ComponentContent](arkts-arkui-componentcontent-t.md)类型，浮层内容会叠加显示。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T--><!--Device-CommonMethod-overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| CustomBuilder \| [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | 是 |
| options | [OverlayOptions](arkts-arkui-overlayoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## padding

```TypeScript
padding(value: Padding | Length | LocalizedPadding): T
```

设置组件的内边距属性。设置后会在组件内容和边框之间创建额外空间，影响组件内部内容的布局区域。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-padding(value: Padding | Length | LocalizedPadding): T--><!--Device-CommonMethod-padding(value: Padding | Length | LocalizedPadding): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Padding \| Length \| [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## parallelGesture

```TypeScript
parallelGesture(gesture: GestureType, mask?: GestureMask): T
```

绑定可与子组件手势同时触发的手势。手势事件为非冒泡事件。父组件设置parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-parallelGesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-parallelGesture(gesture: GestureType, mask?: GestureMask): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## pixelRound

```TypeScript
pixelRound(value: PixelRoundPolicy): T
```

指定当前组件在指定方向上的像素取整对齐方式，某方向不设置时默认在该方向进行四舍五入取整。

> **说明：**
> 
> - 在API version 11，本接口采用半像素对齐方式（即0\~0.25取0，0.25\~0.75取0.5，0.75\~1.0取1）。从API version
12开始，本接口采用四舍五入的取整方式，并支持组件级关闭像素取整的能力。  
> 
> - 从API version
12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

正常计算时，上下方向与组件高度相对应，左右方向（镜像的起始方向称为左）与宽度相对应。为方便描述将两组方向称为左上和右下。

- 计算当前组件左上角坐标： 左上角相对父容器偏移量。  
- 计算当前组件右下角坐标： 左上角相对于父容器偏移量 + 组件自身尺寸。  
- 重新计算当前组件尺寸： 右下角坐标四舍五入取整 - 左上角坐标四舍五入取整。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-pixelRound(value: PixelRoundPolicy): T--><!--Device-CommonMethod-pixelRound(value: PixelRoundPolicy): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PixelRoundPolicy](arkts-arkui-pixelroundpolicy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## pixelStretchEffect

```TypeScript
pixelStretchEffect(options: PixelStretchEffectOptions): T
```

设置组件的图像边缘像素扩展距离。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-pixelStretchEffect(options: PixelStretchEffectOptions): T--><!--Device-CommonMethod-pixelStretchEffect(options: PixelStretchEffectOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PixelStretchEffectOptions](arkts-arkui-pixelstretcheffectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## pixelStretchEffect

```TypeScript
pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T
```

设置组件的图像边缘像素扩展距离。与  
[pixelStretchEffect&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#pixelstretcheffect)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T--><!--Device-CommonMethod-pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;PixelStretchEffectOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## position

```TypeScript
position(value: Position | Edges | LocalizedEdges): T
```

绝对定位，确定子组件相对父组件内容区的位置，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。

> **说明：**
> 
> - position对位置的影响作用在组件的尺寸测量完成之后。
> - 当父组件为[Row](Row)、[Column](Column)或[Flex](Flex)时，设置position的子组件不占位。在上述场景中，如果父组件包含的所有子组件均设置了position，此时父组件尺寸无法通过其他子组件确定，将基于尺寸(0, 0)进行布局测算。
> -
Position类型基于父组件内容区左上角确定位置；Edges类型基于父组件内容区四边确定位置，top/left/right/bottom分别为组件各边距离父组件内容区相应边的边距，通过边距来确定组件相对于父组件内容区的位置；Lo calizedEdges类型基于父组件内容区四边确定位置，支持镜像模式。  
> - 本属性适用于置顶显示、悬浮按钮等组件在父组件中位置固定的场景。
> - 本属性不支持在宽高为零的布局组件上设置。
> - 当父组件为[RelativeContainer](RelativeContainer)，且子组件设置了alignRules属性时，子组件的position属性不生效。
> - 若本属性所在组件的父组件未设置固定宽高，那么本组件会参考第一个设置固定宽高的祖先组件进行绝对定位。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-position(value: Position | Edges | LocalizedEdges): T--><!--Device-CommonMethod-position(value: Position | Edges | LocalizedEdges): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](../arkts-apis/arkts-arkui-display-position-i.md) \| Edges \| [LocalizedEdges](../arkts-apis/arkts-arkui-localizededges-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## priorityGesture

```TypeScript
priorityGesture(gesture: GestureType, mask?: GestureMask): T
```

绑定优先识别手势。

1. 默认情况下，子组件优先识别通过gesture绑定的手势，当父组件配置priorityGesture时，父组件优先识别priorityGesture绑定的手势。2. 绑定长按手势时，设置触发长按的最短时间小的组件会优先响应，会忽略priorityGesture设置。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-priorityGesture(gesture: GestureType, mask?: GestureMask): T--><!--Device-CommonMethod-priorityGesture(gesture: GestureType, mask?: GestureMask): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](../arkts-apis/arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## radialGradient

```TypeScript
radialGradient(value: RadialGradientOptions): T
```

径向渐变。

Anonymous Object Rectification.

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-radialGradient(value: RadialGradientOptions): T--><!--Device-CommonMethod-radialGradient(value: RadialGradientOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RadialGradientOptions](arkts-arkui-radialgradientoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## radialGradient

```TypeScript
radialGradient(options: Optional<RadialGradientOptions>): T
```

径向渐变。与[radialGradient](arkts-arkui-commonmethod-c.md#radialgradient)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-radialGradient(options: Optional<RadialGradientOptions>): T--><!--Device-CommonMethod-radialGradient(options: Optional<RadialGradientOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;RadialGradientOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## renderFit

```TypeScript
renderFit(fitMode: RenderFit): T
```

设置宽高动画过程中的组件内容填充方式。不通过该接口设置，保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-renderFit(fitMode: RenderFit): T--><!--Device-CommonMethod-renderFit(fitMode: RenderFit): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fitMode | [RenderFit](../arkts-apis/arkts-arkui-renderfit-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## renderFit

```TypeScript
renderFit(fitMode: Optional<RenderFit>): T
```

设置宽高动画过程中的组件内容填充方式。不通过该接口设置，保持动画终态的内容大小，并且内容始终与组件保持左上角对齐。与  
[renderFit](arkts-arkui-commonmethod-c.md#renderfit)相比，fitMode参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-renderFit(fitMode: Optional<RenderFit>): T--><!--Device-CommonMethod-renderFit(fitMode: Optional<RenderFit>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fitMode | [Optional](arkts-arkui-optional-t.md)&lt;RenderFit&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## renderGroup

```TypeScript
renderGroup(value: boolean): T
```

设置是否组成节点组。节点组表示当前组件和子组件组成的子树先在离屏画布中渲染，再与父组件融合绘制。设置为节点组后，系统会缓存绘制结果，提升性能。但如果节点组内的组件频繁更新，缓存失效，可能导致性能下降。此外，设置为节点组后，当前组件的不透明度不为1时，绘制效果可能有差异。

不设置该属性时，默认不组成节点组。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-renderGroup(value: boolean): T--><!--Device-CommonMethod-renderGroup(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## renderGroup

```TypeScript
renderGroup(isGroup: Optional<boolean>): T
```

设置是否组成节点组。节点组表示当前组件和子组件组成的子树先在离屏画布中渲染，再与父组件融合绘制。设置为节点组后，系统会缓存绘制结果，提升性能。但如果节点组内的组件频繁更新，缓存失效，可能导致性能下降。此外，设置为节点组后，当前组件的不透明度不为1时，绘制效果可能有差异。

与[renderGroup&lt;sup&gt;10+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#rendergroup)相比，isGroup参数新增了对undefined类型的支持。

不设置该属性时，默认不组成节点组。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-renderGroup(isGroup: Optional<boolean>): T--><!--Device-CommonMethod-renderGroup(isGroup: Optional<boolean>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isGroup | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## responseRegion

```TypeScript
responseRegion(value: Array<Rectangle> | Rectangle): T
```

设置一个或多个触摸热区。从API版本26.0.0开始，未主动设置时[Button](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-button-e.md/arkts-input-multimodalinput-mouseevent-button-e.md)、[Button模式的Toggle](toggle)、[Select](select)、  
[Chip](../arkts-apis/arkts-arkui-advanced-chip.md/arkts-arkui-advanced-chip.md)和[ChipGroup](../arkts-apis/arkts-arkui-advanced-chipgroup.md/arkts-arkui-advanced-chipgroup.md)组件的触摸热区默认最小高度从28vp变更为32vp。该变更仅影响触摸命中范围，不影响组件实际显示高度。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-responseRegion(value: Array<Rectangle> | Rectangle): T--><!--Device-CommonMethod-responseRegion(value: Array<Rectangle> | Rectangle): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;Rectangle&gt; \| [Rectangle](../arkts-apis/arkts-arkui-common-rectangle-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## responseRegionList

```TypeScript
responseRegionList(regions: Array<ResponseRegion>): T
```

设置组件的触摸热区列表。调用该接口时，[responseRegion](arkts-arkui-commonmethod-c.md#responseregion)与  
[mouseResponseRegion](arkts-arkui-commonmethod-c.md#mouseresponseregion)接口不再生效。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-responseRegionList(regions: Array<ResponseRegion>): T--><!--Device-CommonMethod-responseRegionList(regions: Array<ResponseRegion>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| regions | Array&lt;ResponseRegion&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## restoreId

```TypeScript
restoreId(value: number): T
```

id for distribute identification.

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-restoreId(value: number): T--><!--Device-CommonMethod-restoreId(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reuse

```TypeScript
reuse(options: ReuseOptions): T
```

Reuse id is used for identify the reuse type of each @ComponentV2 custom component, which can give user control of sub-component recycle and reuse.

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-reuse(options: ReuseOptions): T--><!--Device-CommonMethod-reuse(options: ReuseOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ReuseOptions](arkts-arkui-reuseoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## reuseId

```TypeScript
reuseId(id: string): T
```

Reuse id is used for identify the reuse type for each custom node.

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-reuseId(id: string): T--><!--Device-CommonMethod-reuseId(id: string): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## rotate

```TypeScript
rotate(value: RotateOptions): T
```

设置组件旋转。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-rotate(value: RotateOptions): T--><!--Device-CommonMethod-rotate(value: RotateOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RotateOptions](arkts-arkui-rotateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## rotate

```TypeScript
rotate(options: Optional<RotateOptions>): T
```

设置组件旋转。与[rotate](arkts-arkui-commonmethod-c.md#rotate)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-rotate(options: Optional<RotateOptions>): T--><!--Device-CommonMethod-rotate(options: Optional<RotateOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;RotateOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## rotate

```TypeScript
rotate(options: Optional<RotateOptions | RotateAngleOptions>): T
```

设置组件旋转效果。与[rotate](arkts-arkui-commonmethod-c.md#rotate)相比，options参数新增了对RotateAngleOptions类型的支持。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-rotate(options: Optional<RotateOptions | RotateAngleOptions>): T--><!--Device-CommonMethod-rotate(options: Optional<RotateOptions | RotateAngleOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;RotateOptions \| [RotateAngleOptions&gt;](../arkts-apis/arkts-arkui-common-rotateangleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## safeAreaPadding

```TypeScript
safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T
```

设置安全区边距属性。允许容器向自身添加组件级安全区域，供子组件延伸，支持[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)动态设置属性方法。与padding不同，safeAreaPadding用于设置组件级安全区域供子组件延伸使用，而padding用于设置组件内容区域的内边距，两者可同时设置、分别生效。

> **说明：**
> 
> 从API version 18开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本14开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T--><!--Device-CommonMethod-safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| paddingValue | Padding \| LengthMetrics \| [LocalizedPadding](../arkts-apis/arkts-arkui-localizedpadding-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## saturate

```TypeScript
saturate(value: number): T
```

为组件添加饱和度效果。不通过该接口设置时，默认无变化。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-saturate(value: number): T--><!--Device-CommonMethod-saturate(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## saturate

```TypeScript
saturate(saturate: Optional<number>): T
```

为组件添加饱和度效果。不通过该接口设置时，默认无变化。与[saturate](arkts-arkui-commonmethod-c.md#saturate)相比，saturate参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-saturate(saturate: Optional<number>): T--><!--Device-CommonMethod-saturate(saturate: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [saturate](#saturate) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## scale

```TypeScript
scale(value: ScaleOptions): T
```

设置组件缩放。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-scale(value: ScaleOptions): T--><!--Device-CommonMethod-scale(value: ScaleOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## scale

```TypeScript
scale(options: Optional<ScaleOptions>): T
```

设置组件缩放。与[scale](arkts-arkui-commonmethod-c.md#scale)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-scale(options: Optional<ScaleOptions>): T--><!--Device-CommonMethod-scale(options: Optional<ScaleOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;ScaleOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sepia

```TypeScript
sepia(value: number): T
```

将图像转换为深褐色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-sepia(value: number): T--><!--Device-CommonMethod-sepia(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sepia

```TypeScript
sepia(sepia: Optional<number>): T
```

将图像转换为深褐色。与[sepia](arkts-arkui-commonmethod-c.md#sepia)相比，sepia参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-sepia(sepia: Optional<number>): T--><!--Device-CommonMethod-sepia(sepia: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sepia](#sepia) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## shadow

```TypeScript
shadow(value: ShadowOptions | ShadowStyle): T
```

为组件添加阴影效果。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-shadow(value: ShadowOptions | ShadowStyle): T--><!--Device-CommonMethod-shadow(value: ShadowOptions | ShadowStyle): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-shadowoptions-i.md) \| [ShadowStyle](../arkts-apis/arkts-arkui-common-shadowstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## shadow

```TypeScript
shadow(options: Optional<ShadowOptions | ShadowStyle>): T
```

为组件添加阴影效果。与[shadow](arkts-arkui-commonmethod-c.md#shadow)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-shadow(options: Optional<ShadowOptions | ShadowStyle>): T--><!--Device-CommonMethod-shadow(options: Optional<ShadowOptions | ShadowStyle>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;ShadowOptions \| [ShadowStyle&gt;](../arkts-apis/arkts-arkui-common-shadowstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sharedTransition

```TypeScript
sharedTransition(id: string, options?: sharedTransitionOptions): T
```

设置共享元素转场动效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-sharedTransition(id: string, options?: sharedTransitionOptions): T--><!--Device-CommonMethod-sharedTransition(id: string, options?: sharedTransitionOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string | 是 |
| options | [sharedTransitionOptions](arkts-arkui-sharedtransitionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## shouldBuiltInRecognizerParallelWith

```TypeScript
shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T
```

提供系统内置手势与响应链上其他组件的手势设置并行关系的回调事件。此接口对应的C API接口为  
[setInnerGestureParallelTo](../../../reference/apis-arkui/capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T--><!--Device-CommonMethod-shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## shouldRecognizerParallelWith

```TypeScript
shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T
```

提供手势与响应链上其他组件的手势设置并行关系的回调事件。使用callback异步回调。此接口对应的C API接口为  
[setGestureParallelTo](../../../reference/apis-arkui/capi-arkui-nativemodule-arkui-nativegestureapi-3.md#setgestureparallelto)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T--><!--Device-CommonMethod-shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ShouldRecognizerParallelWithCallback](arkts-arkui-shouldrecognizerparallelwithcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## size

```TypeScript
size(value: SizeOptions): T
```

设置组件自身的宽高尺寸。设置后会影响组件在父容器中的布局和显示大小。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-size(value: SizeOptions): T--><!--Device-CommonMethod-size(value: SizeOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](../arkts-apis/arkts-arkui-sizeoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## smartGestureShortcut

```TypeScript
smartGestureShortcut(options?: SmartGestureShortcutOptions): T
```

设置组件智慧手势响应行为配置。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-smartGestureShortcut(options?: SmartGestureShortcutOptions): T--><!--Device-CommonMethod-smartGestureShortcut(options?: SmartGestureShortcutOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SmartGestureShortcutOptions](arkts-arkui-smartgestureshortcutoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## sphericalEffect

```TypeScript
sphericalEffect(value: number): T
```

设置组件的图像球面化程度。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-sphericalEffect(value: number): T--><!--Device-CommonMethod-sphericalEffect(value: number): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sphericalEffect

```TypeScript
sphericalEffect(effect: Optional<number>): T
```

设置组件的图像球面化程度。与[sphericalEffect&lt;sup&gt;12+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#sphericaleffect)相比，effect参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-sphericalEffect(effect: Optional<number>): T--><!--Device-CommonMethod-sphericalEffect(effect: Optional<number>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## stateStyles

```TypeScript
stateStyles(value: StateStyles): T
```

设置组件不同状态下的样式。

> **说明：**
> 
> 该接口不支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-stateStyles(value: StateStyles): T--><!--Device-CommonMethod-stateStyles(value: StateStyles): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [StateStyles](arkts-arkui-statestyles-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sweepGradient

```TypeScript
sweepGradient(value: SweepGradientOptions): T
```

角度渐变。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-sweepGradient(value: SweepGradientOptions): T--><!--Device-CommonMethod-sweepGradient(value: SweepGradientOptions): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SweepGradientOptions](arkts-arkui-sweepgradientoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## sweepGradient

```TypeScript
sweepGradient(options: Optional<SweepGradientOptions>): T
```

角度渐变。与[sweepGradient](arkts-arkui-commonmethod-c.md#sweepgradient)相比，options参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-sweepGradient(options: Optional<SweepGradientOptions>): T--><!--Device-CommonMethod-sweepGradient(options: Optional<SweepGradientOptions>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Optional](arkts-arkui-optional-t.md)&lt;SweepGradientOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## systemBarEffect

```TypeScript
systemBarEffect(): T
```

根据背景进行智能反色并且带有模糊效果。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-systemBarEffect(): T--><!--Device-CommonMethod-systemBarEffect(): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| T |

## systemMaterial

```TypeScript
systemMaterial(material: SystemUiMaterial | undefined): T
```

Set system-styled materials for the component. The material effect behaves differently on devices with different level of computing powers. On devices with lower computing power, it affects attributes such as the backgroundColor, borderWidth, borderColor, shadow. On devices with higher computing power, it adds a filter effect at the system material layer, which can produce an effect similar to glass.

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-systemMaterial(material: SystemUiMaterial | undefined): T--><!--Device-CommonMethod-systemMaterial(material: SystemUiMaterial | undefined): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| material | [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## tabIndex

```TypeScript
tabIndex(index: number): T
```

自定义组件tab键走焦能力。当组件未设置tabIndex时，默认按照预设的焦点移动规则进行焦点移动。

> **说明：**
> 
> - tabIndex只能够自定义Tab键走焦，若想同时自定义方向键等走焦能力，建议使用[nextFocus](arkts-arkui-commonmethod-c.md#nextfocus)。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-tabIndex(index: number): T--><!--Device-CommonMethod-tabIndex(index: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## tabStop

```TypeScript
tabStop(isTabStop: boolean): T
```

设置当前容器组件的tabStop，可决定焦点在走焦时是否会停留在当前容器。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-tabStop(isTabStop: boolean): T--><!--Device-CommonMethod-tabStop(isTabStop: boolean): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTabStop | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## toolbar

```TypeScript
toolbar(value: CustomBuilder): T
```

Config toolbar for current component.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CommonMethod-toolbar(value: CustomBuilder): T--><!--Device-CommonMethod-toolbar(value: CustomBuilder): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## touchable

```TypeScript
touchable(value: boolean): T
```

设置当前组件是否可以响应点击事件、触摸事件等手指交互事件。

> **说明：**

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [hitTestBehavior](arkts-arkui-commonmethod-c.md#hittestbehavior)

<!--Device-CommonMethod-touchable(value: boolean): T--><!--Device-CommonMethod-touchable(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## transform

```TypeScript
transform(value: object): T
```

可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](arkts-arkui-commonmethod-c.md#transform3d)接口。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-transform(value: object): T--><!--Device-CommonMethod-transform(value: object): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | object | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## transform

```TypeScript
transform(transform: Optional<object>): T
```

可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](arkts-arkui-commonmethod-c.md#transform3d)接口。与  
[transform](arkts-arkui-commonmethod-c.md#transform)相比，transform&lt;sup&gt;18+&lt;/sup&gt;参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-transform(transform: Optional<object>): T--><!--Device-CommonMethod-transform(transform: Optional<object>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transform](#transform) | [Optional](arkts-arkui-optional-t.md)&lt;object&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## transform3D

```TypeScript
transform3D(transform: Optional<Matrix4Transit>): T
```

设置组件的三维变换矩阵。当涉及包含透视效果的三维变换时，transform接口显示效果可能有误，推荐使用transform3D接口。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-transform3D(transform: Optional<Matrix4Transit>): T--><!--Device-CommonMethod-transform3D(transform: Optional<Matrix4Transit>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transform](#transform) | [Optional](arkts-arkui-optional-t.md)&lt;Matrix4Transit&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## transition

```TypeScript
transition(value: TransitionOptions | TransitionEffect): T
```

组件插入显示和删除隐藏的过渡效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-transition(value: TransitionOptions | TransitionEffect): T--><!--Device-CommonMethod-transition(value: TransitionOptions | TransitionEffect): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TransitionOptions](arkts-arkui-transitionoptions-i.md) \| [TransitionEffect](arkts-arkui-transitioneffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## transition

```TypeScript
transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T
```

组件插入显示和删除隐藏的过渡效果。同[transition](arkts-arkui-commonmethod-c.md#transition)相比，增加了转场动画结束的回调。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T--><!--Device-CommonMethod-transition(effect: TransitionEffect, onFinish: Optional<TransitionFinishCallback>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [TransitionEffect](arkts-arkui-transitioneffect-c.md) | 是 |
| onFinish | [Optional](arkts-arkui-optional-t.md)&lt;TransitionFinishCallback&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## translate

```TypeScript
translate(value: TranslateOptions): T
```

设置组件平移。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-translate(value: TranslateOptions): T--><!--Device-CommonMethod-translate(value: TranslateOptions): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TranslateOptions](arkts-arkui-translateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## translate

```TypeScript
translate(translate: Optional<TranslateOptions>): T
```

设置组件平移。与[translate](arkts-arkui-commonmethod-c.md#translate)相比，translate参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-translate(translate: Optional<TranslateOptions>): T--><!--Device-CommonMethod-translate(translate: Optional<TranslateOptions>): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [translate](#translate) | [Optional](arkts-arkui-optional-t.md)&lt;TranslateOptions&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useEffect

```TypeScript
useEffect(useEffect: boolean, effectType: EffectType): T
```

用于设置组件是否应用&lt;!--Del--&gt;父级[EffectComponent](effect_component)或&lt;!--DelEnd--&gt;窗口定义的效果模板。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-useEffect(useEffect: boolean, effectType: EffectType): T--><!--Device-CommonMethod-useEffect(useEffect: boolean, effectType: EffectType): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [useEffect](#useeffect) | boolean | 是 |
| effectType | [EffectType](arkts-arkui-effecttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useEffect

```TypeScript
useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T
```

用于设置组件是否应用&lt;!--Del--&gt;父级[EffectComponent](effect_component)或&lt;!--DelEnd--&gt;窗口定义的效果模板。与  
[useEffect&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#useeffect)相比，useEffect参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T--><!--Device-CommonMethod-useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [useEffect](#useeffect) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |
| effectType | [EffectType](arkts-arkui-effecttype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## useEffect

```TypeScript
useEffect(value: boolean): T
```

用于对背景模糊等特效进行绘制合并。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-useEffect(value: boolean): T--><!--Device-CommonMethod-useEffect(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useShadowBatching

```TypeScript
useShadowBatching(value: boolean): T
```

控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-useShadowBatching(value: boolean): T--><!--Device-CommonMethod-useShadowBatching(value: boolean): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## useShadowBatching

```TypeScript
useShadowBatching(use: Optional<boolean>): T
```

控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。与[useShadowBatching&lt;sup&gt;11+&lt;/sup&gt;](arkts-arkui-commonmethod-c.md#useshadowbatching)相比，use参数新增了对undefined类型的支持。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-useShadowBatching(use: Optional<boolean>): T--><!--Device-CommonMethod-useShadowBatching(use: Optional<boolean>): T-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| use | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
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

**起始版本：** 7

**废弃版本：** 9

**替代接口：** grid_col/GridColColumnOption

<!--Device-CommonMethod-useSizeType(value: {    xs?: number | { span: number; offset: number };    sm?: number | { span: number; offset: number };    md?: number | { span: number; offset: number };    lg?: number | { span: number; offset: number };  }): T--><!--Device-CommonMethod-useSizeType(value: {    xs?: number | { span: number; offset: number };    sm?: number | { span: number; offset: number };    md?: number | { span: number; offset: number };    lg?: number | { span: number; offset: number };  }): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | {     xs?: number \| { span: number; offset: number };     sm?: number \| { span: number; offset: number };     md?: number \| { span: number; offset: number };     lg?: number \| { span: number; offset: number };   } | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## visibility

```TypeScript
visibility(value: Visibility): T
```

控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-visibility(value: Visibility): T--><!--Device-CommonMethod-visibility(value: Visibility): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Visibility](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-visibility-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## visualEffect

```TypeScript
visualEffect(effect: VisualEffect): T
```

设置非滤镜视觉效果。

> **说明：**
> 
> 从API version 20开始，该接口支持在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-CommonMethod-visualEffect(effect: VisualEffect): T--><!--Device-CommonMethod-visualEffect(effect: VisualEffect): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [VisualEffect](arkts-arkui-visualeffect-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## width

```TypeScript
width(value: Length): T
```

设置组件自身的宽度，缺省时使用子组件自身内容需要的宽度。若子组件的宽大于父组件的宽，则子组件会溢出显示在父组件外部。

从API version 10开始，该接口支持calc计算特性。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-width(value: Length): T--><!--Device-CommonMethod-width(value: Length): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## width

```TypeScript
width(widthValue: Length | LayoutPolicy): T
```

设置组件自身的宽度或水平方向布局策略，缺省时使用子组件自身内容需要的宽度。若子组件的宽大于父组件的宽，则子组件会溢出显示在父组件外部。

从API version 15开始，当参数为Length类型时，该接口支持calc计算特性。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本15开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-width(widthValue: Length | LayoutPolicy): T--><!--Device-CommonMethod-width(widthValue: Length | LayoutPolicy): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| widthValue | [Length](../arkts-apis/arkts-arkui-length-t.md) \| [LayoutPolicy](../arkts-apis/arkts-arkui-common-layoutpolicy-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## zIndex

```TypeScript
zIndex(value: number): T
```

设置组件的堆叠顺序。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonMethod-zIndex(value: number): T--><!--Device-CommonMethod-zIndex(value: number): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |
