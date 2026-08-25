# CommonMethod

CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## accessibilityActionOptions

```TypeScript
default accessibilityActionOptions(option: AccessibilityActionOptions | undefined): this
```

Sets AccessibilityActionOptions that can affect operation under accessibility.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [AccessibilityActionOptions](arkts-arkui-accessibilityactionoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityChecked

```TypeScript
default accessibilityChecked(isCheck: boolean | undefined): this
```

Sets accessibilityChecked

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isCheck | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityCustomActions

```TypeScript
default accessibilityCustomActions(actions: Array<AccessibilityCustomAction> | undefined): this
```

Sets AccessibilityCustomActions that can be processed in custom action processing under accessibility.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [actions](../../apis-ability-kit/arkts-apis/arkts-ability-skill-i.md) | Array&lt;[AccessibilityCustomAction](arkts-arkui-accessibilitycustomaction-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityDefaultFocus

```TypeScript
default accessibilityDefaultFocus(focus: boolean | undefined): this
```

Sets the accessibility default foucs flag

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [focus](../../apis-test-kit/arkts-apis/arkts-test-uitest-uiwindow-c.md) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityDescription

```TypeScript
default accessibilityDescription(description: Resource | string | undefined): this
```

Sets accessibilityDescription with support for resource references using Resource. This property provides additional context or explanation for the component, helping users understand the action or function it performs. <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Reference resource of the accessibility description. You can specify further explanation <br>of the current component, for example, possible operation consequences, especially those that <br>cannot be learned from component attributes and accessibility text. If a component contains <br>both text information and the accessibility description, the text is read first and then the <br>accessibility description, when the component is selected.</p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| description | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityFocusDrawLevel

```TypeScript
default accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel | undefined): this
```

Accessibility focus draw level, and the default value is FocusDrawLevel.SELF.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawLevel | [FocusDrawLevel](arkts-arkui-focusdrawlevel-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityGroup

```TypeScript
default accessibilityGroup(isGroup: boolean | undefined, accessibilityOptions?: AccessibilityOptions): this
```

Sets whether to enable accessibility grouping.<p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>Whether to enable accessibility grouping. When accessibility grouping is enabled, <br>the component and all its children are treated as a single selectable unit, and the accessibility <br>service will no longer focus on the individual child components.<br>If accessibility grouping is enabled and the component does not contain a universal text attribute <br>or an accessibility text attribute, the system will concatenate the universal text attributes of <br>its child components to form a merged text for the component. If a child component lacks a universal <br>text attribute, it will be ignored in the concatenation process.<br>When accessibilityPreferred is set to true, the system will prioritize concatenating the accessibility <br>text attributes of the child components to form the merged text. If a child component lacks an <br>accessibility text attribute, the system will continue to concatenate its universal text attribute. <br>If a child component lacks both, it will be ignored.</p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isGroup | boolean \| undefined | 是 |
| accessibilityOptions | [AccessibilityOptions](arkts-arkui-accessibilityoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityLevel

```TypeScript
default accessibilityLevel(value: string | undefined): this
```

Sets the accessibility level. This property determines whether the component can be recognized by accessibility services. <p> Accessibility level, which is used to decide whether a component can be identified by the accessibility service. <br>The options are as follows: <br>"auto": The component's recognizability is determined by the accessibility grouping service and ArkUI. <br>"yes": The component can be recognized by accessibility services. <br>"no": The component cannot be recognized by accessibility services. <br>"no-hide-descendants": Neither the component nor its child components can be recognized by accessibility services. &lt;strong&gt;NOTE&lt;/strong&gt; <br>When accessibilityLevel is set to "auto", the component's recognizability depends on the following factors: <br>1. The accessibility service internally determines whether the component can be recognized. <br>2. If the parent component's accessibilityGroup property has isGroup set to true, the accessibility service will <br>not focus on its child components, making them unrecognizable. <br>3. If the parent component's accessibilityLevel is set to "no-hide-descendants", the component will not be <br>recognized by accessibility services.</p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityNextFocusId

```TypeScript
default accessibilityNextFocusId(nextId: string | undefined): this
```

Sets accessibility next focus id

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextId | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityNextFocusId

```TypeScript
default accessibilityNextFocusId(nextId: string, nextFocusParams: AccessibilityNextFocusParams | undefined): this
```

Sets the next accessibility focus ID for the component, with optional detailed parameters. The detailed parameters can provide additional behavior for the accessibility focus transition.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextId | string | 是 |
| nextFocusParams | [AccessibilityNextFocusParams](arkts-arkui-accessibilitynextfocusparams-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityRole

```TypeScript
default accessibilityRole(role: AccessibilityRoleType | undefined): this
```

Sets accessibility role,role indicates the custom type of the component

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| role | [AccessibilityRoleType](arkts-arkui-common-accessibilityroletype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityScrollTriggerable

```TypeScript
default accessibilityScrollTriggerable(isTriggerable: boolean | undefined): this
```

Sets accessibilityScrollTriggerable

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTriggerable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilitySelected

```TypeScript
default accessibilitySelected(isSelect: boolean | undefined): this
```

Sets accessibilitySelected

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isSelect | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityStateDescription

```TypeScript
default accessibilityStateDescription(description: string | Resource | undefined): this
```

Sets the state anouncement text of the component under accessibility.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| description | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityText

```TypeScript
default accessibilityText(text: Resource | string | undefined): this
```

Sets the accessibility text. <p>&lt;strong&gt;NOTE&lt;/strong&gt; <br>When a component does not contain a text attribute, you can use this API to set an accessibility <br>text attribute, so that accessibility services can announce the specified content for the component. <br>If a component has both text content and accessibility text, only the accessibility text is announced. <br>If a component is grouped for accessibility purposes but lacks both text content and accessibility <br>text, the screen reader will concatenate text from its child components (depth-first traversal). <br>To prioritize accessibility text concatenation, set accessibilityPreferred in accessibilityGroup. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityTextHint

```TypeScript
default accessibilityTextHint(value: string | undefined): this
```

Sets accessibilityTextHint

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityUseSamePage

```TypeScript
default accessibilityUseSamePage(pageMode: AccessibilitySamePageMode | undefined): this
```

Sets accessibility same page mode

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pageMode | [AccessibilitySamePageMode](arkts-arkui-common-accessibilitysamepagemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## accessibilityVirtualNode

```TypeScript
default accessibilityVirtualNode(builder: CustomBuilder | undefined): this
```

Sets accessibilityVirtualNode

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## align

```TypeScript
default align(alignment: Alignment | LocalizedAlignment | undefined): this
```

Sets the alignment mode of the component content in the drawing area. Default value: **Alignment.Center**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignment | [Alignment](arkts-arkui-alignment-e.md) \| [LocalizedAlignment](arkts-arkui-localizedalignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## alignRules

```TypeScript
default alignRules(value: AlignRuleOption | LocalizedAlignRuleOptions | undefined): this
```

Sets the alignment rules in the relative container. <br>This API is valid only when the container is RelativeContainer. <br>LocalizedAlignRuleOptions takes the right-to-left scripts into account, using start and end instead of left and right for alignment in the horizontal direction. Prioritize this API in aligning child components in the relative container.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AlignRuleOption](arkts-arkui-common-alignruleoption-i.md) \| [LocalizedAlignRuleOptions](arkts-arkui-common-localizedalignruleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## alignSelf

```TypeScript
default alignSelf(value: ItemAlign | undefined): this
```

Sets the alignment mode of the child components along the cross axis of the parent container. Default value: **ItemAlign.Auto**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ItemAlign](arkts-arkui-itemalign-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## allowDrop

```TypeScript
default allowDrop(value: Array<UniformDataType> | null | Array<string> | undefined): this
```

Allowed drop uniformData type for this node.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[UniformDataType](arkts-arkui-uniformdatatype-t.md)&gt; \| null \| Array & lt;string & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## animation

```TypeScript
default animation(value: AnimateParam | undefined): this
```

animation

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-common-animateparam-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## aspectRatio

```TypeScript
default aspectRatio(value: double | undefined): this
```

Sets the aspect ratio of the component, which can be obtained using the following formula: width/height. <br>If only width and aspectRatio are set, the height is calculated using the following formula: width/aspectRatio. <br>If only height and aspectRatio are set, the width is calculated using the following formula: height x aspectRatio. <br>If width, height, and aspectRatio are all set, the explicitly set height is ignored, and the effective height is calculated using the following formula: width/aspectRatio. <br>This parameter takes effect only when a valid value greater than 0 is specified.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backdropBlur

```TypeScript
default backdropBlur(radius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this
```

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | double \| undefined | 是 |
| options | [BlurOptions](arkts-arkui-common-bluroptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## background

```TypeScript
default background(content: CustomBuilder | ResourceColor | undefined, options?: BackgroundOptions): this
```

Set the background to a given CustomBuilder, or set it to a specific ResourceColor.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |
| options | [BackgroundOptions](arkts-arkui-common-backgroundoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundBlurStyle

```TypeScript
default backgroundBlurStyle(style: BlurStyle | undefined, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this
```

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [BlurStyle](arkts-arkui-common-blurstyle-e.md) \| undefined | 是 |
| options | [BackgroundBlurStyleOptions](arkts-arkui-common-backgroundblurstyleoptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundBrightness

```TypeScript
default backgroundBrightness(params: BackgroundBrightnessOptions | undefined): this
```

设置组件背景提亮效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [BackgroundBrightnessOptions](arkts-arkui-common-backgroundbrightnessoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundColor

```TypeScript
default backgroundColor(value: ResourceColor | ColorMetrics | undefined): this
```

Background color

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundEffect

```TypeScript
default backgroundEffect(options: BackgroundEffectOptions | undefined, sysOptions?: SystemAdaptiveOptions): this
```

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。

> **说明：**&gt;
> backgroundEffect接口为实时接口，每帧对模糊等效果执行实时渲染，性能负载较大。当组件背景模糊效果无需变动时，推荐采用静态模糊接口
> [blur](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-effectkit-filter-i.md#blur)实现模糊效果。最佳实践请参考：
> [图像模糊动效优化-使用场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [BackgroundEffectOptions](arkts-arkui-common-backgroundeffectoptions-i.md) \| undefined | 是 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundFilter

```TypeScript
default backgroundFilter(filter: Filter | undefined): this
```

设置背景滤镜视觉效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined): this
```

Background image

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined, options: BackgroundImageOptions): this
```

Background image

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) \| undefined | 是 |
| options | [BackgroundImageOptions](arkts-arkui-common-backgroundimageoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImage

```TypeScript
default backgroundImage(src: ResourceStr | PixelMap | undefined, repeat: ImageRepeat): this
```

Background image src:Image address url

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](arkts-arkui-pixelmap-t.md) \| undefined | 是 |
| repeat | [ImageRepeat](arkts-arkui-imagerepeat-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImagePosition

```TypeScript
default backgroundImagePosition(value: Position | Alignment | undefined): this
```

Background image position x:Horizontal coordinate;y:Vertical axis coordinate.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| [Alignment](arkts-arkui-alignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImageResizable

```TypeScript
default backgroundImageResizable(value: ResizableOptions | undefined): this
```

Background image resizable. value:resizable options

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResizableOptions](../arkts-components/arkts-arkui-resizableoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backgroundImageSize

```TypeScript
default backgroundImageSize(value: SizeOptions | ImageSize | undefined): this
```

Background image size

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| [ImageSize](arkts-arkui-imagesize-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContentCover

```TypeScript
default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, type?: ModalTransition): this
```

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，显示方式可设置无动画过渡，上下切换过渡以及透明渐变过渡。

> **说明：**&gt;
> 该接口不支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| type | [ModalTransition](arkts-arkui-common-modaltransition-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContentCover

```TypeScript
default bindContentCover(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: ContentCoverOptions): this
```

给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，可自定义设置转场方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [ContentCoverOptions](arkts-arkui-common-contentcoveroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenu

```TypeScript
default bindContextMenu(content: CustomBuilder | undefined, responseType: ResponseType | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| responseType | [ResponseType](arkts-arkui-responsetype-e.md) \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenu

```TypeScript
default bindContextMenu(isShow: boolean | Bindable<boolean> | undefined, content: CustomBuilder | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to the component, whose visibility is subject to the isShow settings.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenuByIsShow

```TypeScript
default bindContextMenuByIsShow(isShow: boolean | Bindable<boolean> | undefined,
        content: CustomBuilder | Array<MenuElement> | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to the component, whose visibility is subject to the isShow settings.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;[MenuElement](arkts-arkui-common-menuelement-i.md)&gt; \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenuByResponseType

```TypeScript
default bindContextMenuByResponseType(content: CustomBuilder | Array<MenuElement> | undefined,
        responseType: ResponseType | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| Array&lt;[MenuElement](arkts-arkui-common-menuelement-i.md)&gt; \| undefined | 是 |
| responseType | [ResponseType](arkts-arkui-responsetype-e.md) \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenuWithResponse

```TypeScript
default bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | undefined, options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported. Long pressing with a mouse device is not supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ResponseType](arkts-arkui-responsetype-e.md)&gt; \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindContextMenuWithResponse

```TypeScript
default bindContextMenuWithResponse(content: CustomBuilderT<ResponseType> | Array<MenuElement> | undefined,
        options?: ContextMenuOptions): this
```

Binds a context menu to this component, which is displayed when the user long-presses or right-clicks the component. Only custom menu items are supported. Long pressing with a mouse device is not supported.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ResponseType](arkts-arkui-responsetype-e.md)&gt; \| Array&lt;[MenuElement](arkts-arkui-common-menuelement-i.md)&gt; \| undefined | 是 |
| options | [ContextMenuOptions](arkts-arkui-common-contextmenuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindMenu

```TypeScript
default bindMenu(content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this
```

Menu control

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | Array&lt;[MenuElement](arkts-arkui-common-menuelement-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [MenuOptions](arkts-arkui-common-menuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindMenu

```TypeScript
default bindMenu(isShow: boolean | Bindable<boolean> | undefined, content: Array<MenuElement> | CustomBuilder | undefined, options?: MenuOptions): this
```

Menu control

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| content | Array&lt;[MenuElement](arkts-arkui-common-menuelement-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [MenuOptions](arkts-arkui-common-menuoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindPopup

```TypeScript
default bindPopup(show: boolean | undefined, popup: PopupOptions | CustomPopupOptions | undefined): this
```

Popup control <p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>The popup can be displayed only after the entire page is fully constructed. Therefore, to avoid incorrect display positions and shapes, do not set this parameter to true while the page is still being constructed. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| show | boolean \| undefined | 是 |
| popup | [PopupOptions](arkts-arkui-common-popupoptions-i.md) \| [CustomPopupOptions](arkts-arkui-common-custompopupoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## bindSheet

```TypeScript
default bindSheet(isShow: boolean | Bindable<boolean> | undefined, builder: CustomBuilder | undefined, options?: SheetOptions): this
```

给组件绑定半模态页面，点击后显示模态页面。

> **说明：**&gt;
> 该接口不支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isShow | boolean \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; \| undefined | 是 |
| builder | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| options | [SheetOptions](arkts-arkui-common-sheetoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## bindTips

```TypeScript
default bindTips(message: TipsMessageType | undefined, options?: TipsOptions): this
```

Tips control

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | [TipsMessageType](arkts-arkui-tipsmessagetype-t.md) \| undefined | 是 |
| options | [TipsOptions](arkts-arkui-common-tipsoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## blendMode

```TypeScript
default blendMode(value: BlendMode | undefined, type?: BlendApplyType): this
```

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlendMode](arkts-arkui-common-blendmode-e.md) \| undefined | 是 |
| type | [BlendApplyType](arkts-arkui-common-blendapplytype-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## blur

```TypeScript
default blur(blurRadius: double | undefined, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): this
```

Adds the content blurring effect for the current component. The input parameter is the blurring radius. The larger the blurring radius, the more blurring the content. If the value is 0, the content blurring effect is not blurring.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-textshadow-i.md) | double \| undefined | 是 |
| options | [BlurOptions](arkts-arkui-common-bluroptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## border

```TypeScript
default border(value: BorderOptions | undefined): this
```

Sets the border.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderOptions](arkts-arkui-borderoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## borderColor

```TypeScript
default borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this
```

Sets the border color. Default value: **Color.Black**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [EdgeColors](arkts-arkui-units-edgecolors-i.md) \| [LocalizedEdgeColors](arkts-arkui-localizededgecolors-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## borderImage

```TypeScript
default borderImage(value: BorderImageOption | undefined): this
```

Sets the border image of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderImageOption](arkts-arkui-common-borderimageoption-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## borderRadius

```TypeScript
default borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses | undefined, type?: RenderStrategy | undefined): this
```

Sets the radius of the border rounded corners. The radius is restricted by the component size. The maximum value is half of the component width or height. NOTE
1. **RenderStrategy.FAST**: The current component and its child components will be drawn directly
onto the canvas with rounded corners applied.
2. **RenderStrategy.OFFSCREEN**: The current component and its child components will first be rendered onto
an off-screen canvas, then undergo a rounded corner clipping, and finally be drawn onto the main canvas.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| BorderRadiuses \| [LocalizedBorderRadiuses](arkts-arkui-localizedborderradiuses-i.md) \| undefined | 是 |
| type | [RenderStrategy](arkts-arkui-renderstrategy-e.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## borderStyle

```TypeScript
default borderStyle(value: BorderStyle | EdgeStyles | undefined): this
```

Sets the border style. Default value: **BorderStyle.Solid**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BorderStyle](arkts-arkui-borderstyle-e.md) \| [EdgeStyles](arkts-arkui-units-edgestyles-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## borderWidth

```TypeScript
default borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths | undefined): this
```

Sets the border width. Percentage values are not supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| [EdgeWidths](arkts-arkui-units-edgewidths-i.md) \| [LocalizedEdgeWidths](arkts-arkui-localizededgewidths-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## brightness

```TypeScript
default brightness(value: double | undefined): this
```

Applies a brightness effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## chainMode

```TypeScript
default chainMode(direction: Axis | undefined, style: ChainStyle | undefined): this
```

Sets the parameters of the chain in which the component is the head. <br>This parameter has effect only when the parent container is RelativeContainer. <br>The chain head is the first component in the chain that satisfies the chain formation rules. In a horizontal layout, it starts from the left (or from the right in a mirrored language layout). In a vertical layout, it starts from the top.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [direction](#direction) | [Axis](arkts-arkui-axis-e.md) \| undefined | 是 |
| style | [ChainStyle](arkts-arkui-common-chainstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## chainWeight

```TypeScript
default chainWeight(chainWeight: ChainWeightOptions | undefined): this
```

Sets the weight of the component in a chain, which is used to re-lay out components that form the chain. <br>This API has effect only when the parent container is RelativeContainer.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [chainWeight](#chainweight) | [ChainWeightOptions](arkts-arkui-chainweightoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## clickEffect

```TypeScript
default clickEffect(value: ClickEffect | null | undefined): this
```

设置当前组件的点击回弹效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ClickEffect](arkts-arkui-common-clickeffect-i.md) \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## clip

```TypeScript
default clip(value: boolean | undefined): this
```

是否对子组件超出当前组件范围外的区域进行裁剪。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## clipShape

```TypeScript
default clipShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this
```

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。

> **说明：**&gt;
> 不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。&gt;
> 路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。&gt;
> 形状中的[fill](arkts-arkui-arkui-shape-commonshapemethod-c.md#fill)属性对clipShape接口不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| [EllipseShape](arkts-arkui-arkui-shape-ellipseshape-c.md) \| [PathShape](arkts-arkui-arkui-shape-pathshape-c.md) \| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## colorBlend

```TypeScript
default colorBlend(value: Color | string | Resource | undefined): this
```

Applies a color blend effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Color](arkts-arkui-color-e.md) \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## compositingFilter

```TypeScript
default compositingFilter(filter: Filter | undefined): this
```

设置合成滤镜视觉效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## constraintSize

```TypeScript
default constraintSize(value: ConstraintSizeOptions | undefined): this
```

Sets the constraint size of the component, which is used to limit the size range during component layout. Default value: **{minWidth: 0, maxWidth: Infinity, minHeight: 0, maxHeight: Infinity}**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ConstraintSizeOptions](arkts-arkui-constraintsizeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## contrast

```TypeScript
default contrast(value: double | undefined): this
```

Applies a contrast effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## customProperty

```TypeScript
default customProperty(name: string, value: CustomProperty): this
```

Sets the custom property of the current component. This API does not work for custom components.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | [CustomProperty](arkts-arkui-customproperty-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## debugLine

```TypeScript
default debugLine(sourceLine: string, moduleName?: string): this
```

Set the component's source code redirection information.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sourceLine | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## defaultFocus

```TypeScript
default defaultFocus(value: boolean | undefined): this
```

Set default focused component when a page create.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## direction

```TypeScript
default direction(value: Direction | undefined): this
```

Sets how elements are laid out along the main axis of the container. Default value: **Direction.Auto**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Direction](arkts-arkui-direction-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## displayPriority

```TypeScript
default displayPriority(value: double | undefined): this
```

Sets the display priority for the component in the layout container. <br>This parameter is only effective in Row, Column, and Flex (single-line) container components.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## doubleSided

```TypeScript
default doubleSided(value: boolean | undefined): this
```

Sets whether to component is double-sided.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

Enable the selectable area can be dragged.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## dragPreview

```TypeScript
default dragPreview(preview: CustomBuilder | DragItemInfo | string | undefined, config?: PreviewConfiguration): this
```

Set preview of the component for dragging process

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| preview | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [DragItemInfo](arkts-arkui-common-dragiteminfo-i.md) \| string \| undefined | 是 |
| config | [PreviewConfiguration](arkts-arkui-common-previewconfiguration-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## dragPreviewOptions

```TypeScript
default dragPreviewOptions(value: DragPreviewOptions | undefined, options?: DragInteractionOptions): this
```

Set the selectable area drag preview options.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DragPreviewOptions](arkts-arkui-common-dragpreviewoptions-i.md) \| undefined | 是 |
| options | [DragInteractionOptions](arkts-arkui-common-draginteractionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## drawModifier

```TypeScript
default drawModifier(modifier: DrawModifier | undefined): this
```

Sets the drawModifier of the current component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [DrawModifier](arkts-arkui-common-drawmodifier-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## enableClickSoundEffect

```TypeScript
default enableClickSoundEffect(enabled: boolean | undefined): this
```

Set whether this component should have sound effects enabled for clicking.Sound effects playback is affected by the audio-related settings in the device system settings. When the user sets the device to silent mode, sound effects cannot be played.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [enabled](#enabled) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## enabled

```TypeScript
default enabled(value: boolean | undefined): this
```

If the value is true, the component is available and can respond to operations such as clicking. If it is set to false, click operations are not responded.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## expandSafeArea

```TypeScript
default expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): this
```

Sets the safe area to be expanded to. <br>default:{types: [SafeAreaType.SYSTEM, SafeAreaType.CUTOUT, SafeAreaType.KEYBOARD], edges: [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM, SafeAreaEdge.START, SafeAreaEdge.END]}

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;[SafeAreaType](arkts-arkui-common-safeareatype-e.md)&gt; | 否 |
| edges | Array&lt;[SafeAreaEdge](arkts-arkui-common-safeareaedge-e.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## flexBasis

```TypeScript
default flexBasis(value: double | string | undefined): this
```

Sets the base size of the component in the main axis of the parent container. Default value: **'auto'**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## flexGrow

```TypeScript
default flexGrow(value: double | undefined): this
```

Sets the percentage of the parent container's remaining space that is allocated to the component. Default value: **0**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## flexShrink

```TypeScript
default flexShrink(value: double | undefined): this
```

Sets the percentage of the parent container's shrink size that is allocated to the component. Default value: 0 when the parent container is Column or Row, 1 when the parent container is Flex..

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## focusable

```TypeScript
default focusable(value: boolean | undefined): this
```

Set focusable. Components that have default interaction logic, such as Button and TextInput, are focusable by default. Other components, such as Text and Image, are not focusable by default. Only focusable components can trigger a focus event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## focusBox

```TypeScript
default focusBox(style: FocusBoxStyle | undefined): this
```

Set the component's focusBox style.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [FocusBoxStyle](arkts-arkui-focusboxstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## focusOnTouch

```TypeScript
default focusOnTouch(value: boolean | undefined): this
```

Set a component focused when the component be touched.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## focusScopeId

```TypeScript
default focusScopeId(id: string | undefined, isGroup?: boolean, arrowStepOut?: boolean): this
```

Set container as a focus group with a specific identifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string \| undefined | 是 |
| isGroup | boolean | 否 |
| arrowStepOut | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## focusScopePriority

```TypeScript
default focusScopePriority(scopeId: string | undefined, priority?: FocusPriority): this
```

Set the focus priority of component in a specific focus scope.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scopeId | string \| undefined | 是 |
| priority | [FocusPriority](arkts-arkui-focuspriority-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## foregroundBlurStyle

```TypeScript
default foregroundBlurStyle(style: BlurStyle | undefined, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): this
```

Applies a foreground blur style to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [BlurStyle](arkts-arkui-common-blurstyle-e.md) \| undefined | 是 |
| options | [ForegroundBlurStyleOptions](arkts-arkui-common-foregroundblurstyleoptions-i.md) | 否 |
| sysOptions | [SystemAdaptiveOptions](arkts-arkui-common-systemadaptiveoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## foregroundColor

```TypeScript
default foregroundColor(value: ResourceColor | ColoringStrategy | undefined): this
```

设置组件的前景色。当组件未设置前景色，默认继承父组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColoringStrategy](arkts-arkui-coloringstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## foregroundEffect

```TypeScript
default foregroundEffect(options: ForegroundEffectOptions | undefined): this
```

Foreground effect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ForegroundEffectOptions](arkts-arkui-common-foregroundeffectoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## foregroundFilter

```TypeScript
default foregroundFilter(filter: Filter | undefined): this
```

设置前景滤镜（内容）视觉效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## freeze

```TypeScript
default freeze(value: boolean | undefined): this
```

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## geometryTransition

```TypeScript
default geometryTransition(id: string | undefined, options?: GeometryTransitionOptions): this
```

组件内隐式共享元素转场。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string \| undefined | 是 |
| options | [GeometryTransitionOptions](arkts-arkui-common-geometrytransitionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## gesture

```TypeScript
default gesture(gesture: GestureType, mask?: GestureMask): this
```

Bind gesture recognition. gesture:Bound Gesture Type,mask:GestureMask;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](arkts-arkui-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## gestureModifier

```TypeScript
default gestureModifier(modifier: GestureModifier | undefined): this
```

Sets the gesture modifier.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [GestureModifier](arkts-arkui-common-gesturemodifier-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## grayscale

```TypeScript
default grayscale(value: double | undefined): this
```

Applies a grayscale effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## groupDefaultFocus

```TypeScript
default groupDefaultFocus(value: boolean | undefined): this
```

Set default focused component when focus on a focus group.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## height

```TypeScript
default height(heightValue: Length | LayoutPolicy | undefined): this
```

Sets the height of the component or its vertical layout policy. By default, the component uses the height required for its content. If the height of the component is greater than that of the parent container, the component will be drawn beyond the parent container scope.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| heightValue | [Length](arkts-arkui-length-t.md) \| [LayoutPolicy](arkts-arkui-common-layoutpolicy-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## hitTestBehavior

```TypeScript
default hitTestBehavior(value: HitTestMode | undefined): this
```

Sets how the component behaves during hit testing.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [HitTestMode](arkts-arkui-hittestmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## hoverEffect

```TypeScript
default hoverEffect(value: HoverEffect | undefined): this
```

Set hover effect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [HoverEffect](arkts-arkui-hovereffect-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## hueRotate

```TypeScript
default hueRotate(value: double | string | undefined): this
```

Rotates the hue of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## id

```TypeScript
default id(value: string | undefined): this
```

Id. User can set an id to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## ignoreLayoutSafeArea

```TypeScript
default ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType> | undefined, edges?: Array<LayoutSafeAreaEdge> | undefined): this
```

Expands the layout safe area of a component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;[LayoutSafeAreaType](arkts-arkui-common-layoutsafeareatype-e.md)&gt; \| undefined | 否 |
| edges | Array&lt;[LayoutSafeAreaEdge](arkts-arkui-common-layoutsafeareaedge-e.md)&gt; \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## inspectorLabel

```TypeScript
default inspectorLabel(label: string | undefined): this
```

Set the component's inspector label which only display on DevEco Studio.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## invert

```TypeScript
default invert(value: double | InvertOptions | undefined): this
```

Invert the input image. Value defines the scale of the conversion. 100% of the value is a complete reversal. A value of 0% does not change the image. (Percentage)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| [InvertOptions](arkts-arkui-common-invertoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## key

```TypeScript
default key(value: string | undefined): this
```

Key. User can set an key to the component to identify it.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## keyboardShortcut

```TypeScript
default keyboardShortcut(value: string | FunctionKey | undefined, keys: Array<ModifierKey> | undefined, action?: () => void): this
```

Sets hot keys

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [FunctionKey](arkts-arkui-functionkey-e.md) \| undefined | 是 |
| keys | Array&lt;[ModifierKey](arkts-arkui-modifierkey-e.md)&gt; \| undefined | 是 |
| action | () = & gt; void | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## layoutGravity

```TypeScript
default layoutGravity(alignment: LocalizedAlignment | undefined): this
```

Defines the align rules of child component in Stack container.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignment | [LocalizedAlignment](arkts-arkui-localizedalignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## layoutWeight

```TypeScript
default layoutWeight(value: double | string | undefined): this
```

Sets the weight of the component during layout. A component with this attribute is allocated space along the main axis of its parent container (Row, Column, or Flex) based on its specified weight. Default value: **0**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## lightUpEffect

```TypeScript
default lightUpEffect(value: double | undefined): this
```

Applies a light up effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## linearGradient

```TypeScript
default linearGradient(value: LinearGradientOptions | undefined): this
```

Linear Gradient angle: Angle of Linear Gradient. The default value is 180; direction: Direction of Linear Gradient. The default value is GradientDirection.Bottom; colors: Color description for gradients. repeating: repeating. The default value is false

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LinearGradientOptions](arkts-arkui-common-lineargradientoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## linearGradientBlur

```TypeScript
default linearGradientBlur(value: double | undefined, options: LinearGradientBlurOptions | undefined): this
```

Applies a linear gradient foreground blur effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |
| options | [LinearGradientBlurOptions](arkts-arkui-common-lineargradientbluroptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## margin

```TypeScript
default margin(value: Margin | Length | LocalizedMargin | undefined): this
```

Sets the margin of the component. Default value: **0**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Margin](arkts-arkui-margin-t.md) \| [Length](arkts-arkui-length-t.md) \| [LocalizedMargin](arkts-arkui-localizedmargin-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## markAnchor

```TypeScript
default markAnchor(value: Position | LocalizedPosition | undefined): this
```

Sets the anchor for locating the component, which is used to move the component further away from the position specified by position or offset.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| [LocalizedPosition](arkts-arkui-localizedposition-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## mask

```TypeScript
default mask(value: ProgressMask | undefined): this
```

为组件上添加可调节进度的遮罩。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ProgressMask](arkts-arkui-common-progressmask-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## maskShape

```TypeScript
default maskShape(value: CircleShape | EllipseShape | PathShape | RectShape | undefined): this
```

为组件上添加指定形状的遮罩。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| [EllipseShape](arkts-arkui-arkui-shape-ellipseshape-c.md) \| [PathShape](arkts-arkui-arkui-shape-pathshape-c.md) \| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## materialFilter

```TypeScript
default materialFilter(filter: Filter | undefined): this
```

设置系统材质滤镜效果，系统材质滤镜的绘制早于[backgroundFilter](#backgroundfilter)绘制，即位于backgroundFilter的更底层。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [Filter](arkts-arkui-filter-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## monopolizeEvents

```TypeScript
default monopolizeEvents(monopolize: boolean | undefined): this
```

Sets whether the component exclusively handles events. true: The component exclusively handles events. false: The component does not exclusively handle events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| monopolize | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## motionBlur

```TypeScript
default motionBlur(value: MotionBlurOptions | undefined): this
```

Apply a motion blur effect to the component being scaled or moved. 1.Do not use this API in intra-component transitions, shared element transitions, implicit element transitions, or particle animations. Doing so may cause unexpected results. 2.The **radius** parameter of **motionBlur** must be set to **0** for the initial state. Otherwise, there may be unexpected results during a cold start. 3.This API must be used together with the **onFinish** parameter of **AnimateParam**. Its **radius** parameter must be set to **0** when the animation ends; otherwise, there may be unexpected results. 4.When using this API, do not frequently change the blur radius of the same component; otherwise, there may be unexpected results. For example, if you frequently click the image in the example, the blur effect may not work sometimes. 5.To avoid unexpected results, make sure the coordinates of the motion blur anchor point are the same as those of the animation scaling anchor point. 6.To avoid unexpected results, set the blur radius to a value less than 1.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MotionBlurOptions](arkts-arkui-common-motionbluroptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## motionPath

```TypeScript
default motionPath(value: MotionPathOptions | undefined): this
```

设置组件的路径动画。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MotionPathOptions](arkts-arkui-common-motionpathoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## mouseResponseRegion

```TypeScript
default mouseResponseRegion(value: Array<Rectangle> | Rectangle | undefined): this
```

Sets the mouse response region of current component

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[Rectangle](arkts-arkui-common-rectangle-i.md)&gt; \| [Rectangle](arkts-arkui-common-rectangle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## nextFocus

```TypeScript
default nextFocus(nextStep: FocusMovement | undefined): this
```

Set nextFocus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| nextStep | [FocusMovement](arkts-arkui-common-focusmovement-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## obscured

```TypeScript
default obscured(reasons: Array<ObscuredReasons> | undefined): this
```

Sets obscured

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reasons | Array&lt;[ObscuredReasons](arkts-arkui-obscuredreasons-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## offset

```TypeScript
default offset(value: Position | Edges | LocalizedEdges | undefined): this
```

Sets the offset of the component relative to its original position. <br>The offset attribute does not affect the layout of the parent container. It adjusts the component position only during drawing.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| [Edges](arkts-arkui-edges-i.md) \| [LocalizedEdges](arkts-arkui-localizededges-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAccessibilityActionIntercept

```TypeScript
default onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback | undefined): this
```

Register accessibility action intercept callback, when accessibility action is to be executed,the callback will be executed

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityActionInterceptCallback](arkts-arkui-accessibilityactioninterceptcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAccessibilityFocus

```TypeScript
default onAccessibilityFocus(callback: AccessibilityFocusCallback | undefined): this
```

Register accessibility focus callback,when the component is focused or out of focus,the callback will be executed

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityFocusCallback](arkts-arkui-accessibilityfocuscallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAccessibilityHover

```TypeScript
default onAccessibilityHover(callback: AccessibilityCallback | undefined): this
```

Trigger a accessibility hover event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityCallback](arkts-arkui-accessibilitycallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAccessibilityHoverTransparent

```TypeScript
default onAccessibilityHoverTransparent(callback: AccessibilityTransparentCallback | undefined): this
```

prompt for current component and descendants unable to handle accessibility hover event

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AccessibilityTransparentCallback](arkts-arkui-accessibilitytransparentcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAppear

```TypeScript
default onAppear(event: (() => void) | undefined): this
```

This callback is triggered when a component mounts a display.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAreaChange

```TypeScript
default onAreaChange(event: ((oldValue: Area, newValue: Area) => void) | undefined): this
```

This callback is triggered when the size or position of this component change finished.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((oldValue: Area, newValue: Area) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAreaChange

```TypeScript
default onAreaChange (event: AreaChangeCallback, options?: AreaChangeOptions): this
```

This callback is triggered when the size or position of this component has finished changing. The interval between two area change callbacks will not be less than the expected update interval.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [AreaChangeCallback](arkts-arkui-areachangecallback-t.md) | 是 |
| options | [AreaChangeOptions](arkts-arkui-common-areachangeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## onAttach

```TypeScript
default onAttach(callback: VoidCallback | undefined): this
```

This callback is triggered when a component mounts to view tree.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onAxisEvent

```TypeScript
default onAxisEvent(event: Callback<AxisEvent> | undefined): this
```

Handle axis events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[AxisEvent](arkts-arkui-common-axisevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onBlur

```TypeScript
default onBlur(event: (() => void) | undefined): this
```

Triggered when the current component loses focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onChildTouchTest

```TypeScript
default onChildTouchTest(event: ((value: Array<TouchTestInfo>) => TouchResult) | undefined): this
```

Called to specify how to perform the touch test on the children of this component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((value: Array&lt;[TouchTestInfo](arkts-arkui-common-touchtestinfo-c.md)&gt;) =&gt; TouchResult) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onClick

```TypeScript
default onClick(event: ((event: ClickEvent) => void) | undefined): this
```

Called when a click event occurs.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br> Since API version 9, the following constraints apply when this API is used in service widgets: <br> Click events cannot be triggered if the finger is pressed for more than 800 ms. <br> Click events cannot be triggered if the finger moves more than 20 px after pressing down. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: ClickEvent) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onClick

```TypeScript
default onClick(event: Callback<ClickEvent> | undefined, distanceThreshold: double | undefined): this
```

Trigger a click event when a click is clicked, move distance should smaller than distanceThreshold.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br> If the distanceThreshold value specified is less than or equal to 0 vp, it will be converted to the default value. Since API version 9, the following constraints apply when this API is used in service widgets: <br> Click events cannot be triggered if the finger is pressed for more than 800 ms. <br> Click events cannot be triggered if the finger moves more than 20 px after pressing down. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[ClickEvent](arkts-arkui-common-clickevent-i.md)&gt; \| undefined | 是 |
| distanceThreshold | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDetach

```TypeScript
default onDetach(callback: VoidCallback | undefined): this
```

This callback is triggered when a component is detached from view tree.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDigitalCrown

```TypeScript
default onDigitalCrown(handler: Callback<CrownEvent> | undefined): this
```

Digital crown input.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Callback](arkts-arkui-callback-t.md)&lt;[CrownEvent](arkts-arkui-common-crownevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDisAppear

```TypeScript
default onDisAppear(event: (() => void) | undefined): this
```

This callback is triggered when component uninstallation disappears.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragEnd

```TypeScript
default onDragEnd(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

This function is called when the drag event is end.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragEnter

```TypeScript
default onDragEnter(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the component is dragged to the range of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragLeave

```TypeScript
default onDragLeave(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the component is dragged out of the component range.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragMove

```TypeScript
default onDragMove(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

After binding, a callback is triggered when the drag moves within the range of a placeable component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragSpringLoading

```TypeScript
default onDragSpringLoading(callback: Callback<SpringLoadingContext> | null | undefined, configuration?: DragSpringLoadingConfiguration): this
```

Enables the component as a drag-and-drop target with spring loading functionality.When a dragged object hovers over the target, it triggers a callback notification. Spring Loading is an enhanced feature for drag-and-drop operations, allowing users to automatically trigger view transitions during dragging by hovering (hover) without needing to use another hand. This feature is primarily designed to enhance the smoothness and efficiency of drag-and-drop operations. Below are some common scenarios suitable for supporting this feature: - In a file manager, when dragging a file and hovering over a folder, the folder is automatically opened. - On a desktop launcher, when dragging a file and hovering over an application icon, the application is automatically opened.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-t.md)&lt;[SpringLoadingContext](arkts-arkui-springloadingcontext-t.md)&gt; \| null \| undefined | 是 |
| configuration | [DragSpringLoadingConfiguration](arkts-arkui-dragspringloadingconfiguration-t.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## onDragStart

```TypeScript
default onDragStart(event: ((event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo) | undefined): this
```

After a listener is bound, the component can be dragged. After the drag occurs, a callback is triggered. (To be triggered, press and hold for 170 milliseconds (ms))&lt;strong&gt;NOTE&lt;/strong&gt;:<br> The global builder is not supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; CustomBuilder \ | DragItemInfo) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDrop

```TypeScript
default onDrop(event: ((event: DragEvent, extraParams?: string) => void) | undefined): this
```

The component bound to this event can be used as the drag release target. This callback is triggered when the drag behavior is stopped within the scope of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: DragEvent, extraParams?: string) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDrop

```TypeScript
default onDrop(eventCallback: OnDragEventCallback | undefined, dropOptions: DropOptions): this
```

The component bound to this event can be used as the drag release target. This callback is triggered when the drag behavior is stopped within the scope of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventCallback | [OnDragEventCallback](arkts-arkui-ondrageventcallback-t.md) \| undefined | 是 |
| dropOptions | [DropOptions](arkts-arkui-common-dropoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onFocus

```TypeScript
default onFocus(event: (() => void) | undefined): this
```

Trigger a event when got focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onFocusAxisEvent

```TypeScript
default onFocusAxisEvent(event: Callback<FocusAxisEvent> | undefined): this
```

Trigger a FocusAxisEvent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[FocusAxisEvent](arkts-arkui-common-focusaxisevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onGestureCollectIntercept

```TypeScript
default onGestureCollectIntercept(callback: GestureCollectInterceptCallback): this
```

When the events and gestures on this node and higher-priority nodes have been collected, the callback is executed. This callback is used to intervene in the event and gesture collection results.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureCollectInterceptCallback](arkts-arkui-gesturecollectinterceptcallback-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onGestureJudgeBegin

```TypeScript
default onGestureJudgeBegin(callback: ((gestureInfo: GestureInfo, event: BaseGestureEvent) => GestureJudgeResult) | undefined): this
```

When a gesture bound to this component will be accepted, a user-defined callback is triggered to get the result

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((gestureInfo: GestureInfo, event: BaseGestureEvent) = & gt; GestureJudgeResult) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onGestureRecognizerJudgeBegin

```TypeScript
default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined): this
```

Binds a custom gesture recognizer judgment callback to the component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onGestureRecognizerJudgeBegin

```TypeScript
default onGestureRecognizerJudgeBegin(callback: GestureRecognizerJudgeBeginCallback | undefined, exposeInnerGesture: boolean | undefined): this
```

Binds a custom gesture recognizer judgment callback to the component.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br> For a composite component, setting exposeInnerGesture to true exposes the internal gesture recognizer of the <br> composite component in the current parameter callback. Currently, only the Tabs component is supported.<br> Do not set exposeInnerGesture for other components. When exposeInnerGesture is set to false, this API provides the same functionality <br> as the onGestureRecognizerJudgeBegin API. </p>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [GestureRecognizerJudgeBeginCallback](arkts-arkui-gesturerecognizerjudgebegincallback-t.md) \| undefined | 是 |
| exposeInnerGesture | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onHover

```TypeScript
default onHover(event: ((isHover: boolean, event: HoverEvent) => void) | undefined): this
```

Trigger a hover event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((isHover: boolean, event: HoverEvent) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onHoverMove

```TypeScript
default onHoverMove(event: Callback<HoverEvent> | undefined): this
```

Trigger a hover move event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[HoverEvent](arkts-arkui-common-hoverevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onKeyEvent

```TypeScript
default onKeyEvent(event: Callback<KeyEvent, boolean> | undefined): this
```

Keyboard input

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[KeyEvent](arkts-arkui-common-keyevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onKeyEventDispatch

```TypeScript
default onKeyEventDispatch(event: Callback<KeyEvent, boolean> | undefined): this
```

Customize the handling and distribution of key events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[KeyEvent](arkts-arkui-common-keyevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onKeyPreIme

```TypeScript
default onKeyPreIme(event: Callback<KeyEvent, boolean> | undefined): this
```

Handle keyboard events before input method events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](arkts-arkui-callback-t.md)&lt;[KeyEvent](arkts-arkui-common-keyevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onMouse

```TypeScript
default onMouse(event: ((event: MouseEvent) => void) | undefined): this
```

Triggered when the component is clicked by a mouse button or the mouse pointer moves on the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: MouseEvent) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onNeedSoftkeyboard

```TypeScript
default onNeedSoftkeyboard(onNeedSoftkeyboardCallback: OnNeedSoftkeyboardCallback | undefined): this
```

Called when component is focused, the return value indicates whether keyboard is needed.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onNeedSoftkeyboardCallback | [OnNeedSoftkeyboardCallback](arkts-arkui-onneedsoftkeyboardcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onPreDrag

```TypeScript
default onPreDrag(callback: Callback<PreDragStatus> | undefined): this
```

After binding, a callback is triggered when the preDrag status change finished.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-t.md)&lt;[PreDragStatus](arkts-arkui-common-predragstatus-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onSizeChange

```TypeScript
default onSizeChange(event: SizeChangeCallback | undefined): this
```

This callback is triggered when the component size changes due to layout updates. This event is not triggered for render attribute changes caused by re-rendering.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [SizeChangeCallback](arkts-arkui-sizechangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onTouch

```TypeScript
default onTouch(event: ((event: TouchEvent) => void) | undefined): this
```

Invoked when a touch event is triggered.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | ((event: TouchEvent) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onTouchIntercept

```TypeScript
default onTouchIntercept(callback: Callback<TouchEvent, HitTestMode> | undefined): this
```

When the component does a touch test, a user-defined callback is triggered.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-t.md)&lt;[TouchEvent](arkts-arkui-common-touchevent-i.md), [HitTestMode](arkts-arkui-hittestmode-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onTouchTestDone

```TypeScript
default onTouchTestDone(callback: TouchTestDoneCallback | undefined): this
```

Register one callback which will be executed when all gesture recognizers are collected done, this happens when user touchs down, the system do hit test process and collect gesture recognizers base on the touch position, after this, before handling any move events, the component can use this interface to know which gesture recognizers will participate in the recognition and competing with each other.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TouchTestDoneCallback](arkts-arkui-touchtestdonecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onVisibleAreaApproximateChange

```TypeScript
default onVisibleAreaApproximateChange(options: VisibleAreaEventOptions | undefined, event: VisibleAreaChangeCallback | undefined): this
```

Set or reset the callback which is triggered when the visibleArea of component changed. The interval between two visible area change callbacks will not be less than the expected update interval.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VisibleAreaEventOptions](arkts-arkui-common-visibleareaeventoptions-i.md) \| undefined | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onVisibleAreaChange

```TypeScript
default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined): this
```

Trigger a visible area change event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ratios | Array & lt;double & gt; \ | undefined | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onVisibleAreaChange

```TypeScript
default onVisibleAreaChange(ratios: Array<double> | undefined, event: VisibleAreaChangeCallback | undefined, measureFromViewport: boolean | undefined): this
```

Trigger a visible area change event.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ratios | Array & lt;double & gt; \ | undefined | 是 |
| event | [VisibleAreaChangeCallback](arkts-arkui-visibleareachangecallback-t.md) \| undefined | 是 |
| measureFromViewport | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## opacity

```TypeScript
default opacity(value: double | Resource | undefined): this
```

设置组件的不透明度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## outline

```TypeScript
default outline(value: OutlineOptions | undefined): this
```

Sets the outline attributes in one declaration.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OutlineOptions](arkts-arkui-outlineoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## outlineColor

```TypeScript
default outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors | undefined): this
```

Sets the color of the outline.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [EdgeColors](arkts-arkui-units-edgecolors-i.md) \| [LocalizedEdgeColors](arkts-arkui-localizededgecolors-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## outlineRadius

```TypeScript
default outlineRadius(value: Dimension | OutlineRadiuses | undefined): this
```

Sets the radius of the outline corners.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| [OutlineRadiuses](arkts-arkui-units-outlineradiuses-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## outlineStyle

```TypeScript
default outlineStyle(value: OutlineStyle | EdgeOutlineStyles | undefined): this
```

Sets the style of the outline.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OutlineStyle](arkts-arkui-common-outlinestyle-e.md) \| [EdgeOutlineStyles](arkts-arkui-units-edgeoutlinestyles-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## outlineWidth

```TypeScript
default outlineWidth(value: Dimension | EdgeOutlineWidths | undefined): this
```

Sets the thickness of the outline.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Dimension](arkts-arkui-dimension-t.md) \| [EdgeOutlineWidths](arkts-arkui-units-edgeoutlinewidths-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## overlay

```TypeScript
default overlay(value: string | CustomBuilder | ComponentContent<Object> | undefined, options?: OverlayOptions): this
```

Add mask text to the current component. The layout is the same as that of the current component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [ComponentContent](arkts-arkui-componentcontent-c.md)&lt;Object&gt; \| undefined | 是 |
| options | [OverlayOptions](arkts-arkui-common-overlayoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## padding

```TypeScript
default padding(value: Padding | Length | LocalizedPadding | undefined): this
```

Sets the padding of the component. Default value: **0**.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Padding](arkts-arkui-units-padding-i.md) \| [Length](arkts-arkui-length-t.md) \| [LocalizedPadding](arkts-arkui-localizedpadding-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## parallelGesture

```TypeScript
default parallelGesture(gesture: GestureType, mask?: GestureMask): this
```

Binding gestures that can be triggered simultaneously with internal component gestures gesture:Bound Gesture Type,mask:GestureMask;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](arkts-arkui-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## pixelRound

```TypeScript
default pixelRound(value: PixelRoundPolicy | undefined): this
```

Sets the pixel rounding policy for the current component in the specified direction. <br>If a direction is not set, the pixels are rounded to the nearest whole number in that direction.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PixelRoundPolicy](arkts-arkui-common-pixelroundpolicy-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## pixelStretchEffect

```TypeScript
default pixelStretchEffect(options: PixelStretchEffectOptions | undefined): this
```

Applies a pixel stretch effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PixelStretchEffectOptions](arkts-arkui-common-pixelstretcheffectoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## position

```TypeScript
default position(value: Position | Edges | LocalizedEdges | undefined): this
```

Sets the absolute position of the component relative to the position of the parent component. <br>The attribute is not available for a layout container whose width and height are zero.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Position](arkts-arkui-position-i.md) \| [Edges](arkts-arkui-edges-i.md) \| [LocalizedEdges](arkts-arkui-localizededges-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## priorityGesture

```TypeScript
default priorityGesture(gesture: GestureType, mask?: GestureMask): this
```

Binding Preferential Recognition Gestures gesture:Bound Gesture Type,mask:GestureMask;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [gesture](#gesture) | [GestureType](arkts-arkui-gesturetype-t.md) | 是 |
| [mask](#mask) | [GestureMask](arkts-arkui-gesturemask-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## radialGradient

```TypeScript
default radialGradient(value: RadialGradientOptions | undefined): this
```

Creates a radial gradient.Anonymous Object Rectification.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RadialGradientOptions](arkts-arkui-common-radialgradientoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## renderFit

```TypeScript
default renderFit(fitMode: RenderFit | undefined): this
```

设置宽高动画过程中的组件内容填充方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fitMode | [RenderFit](arkts-arkui-renderfit-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## renderGroup

```TypeScript
default renderGroup(value: boolean | undefined): this
```

Sets whether the component and its child components are rendered off the screen as a whole before being blended with its parent.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## responseRegion

```TypeScript
default responseRegion(value: Array<Rectangle> | Rectangle | undefined): this
```

Sets the response region of the current component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[Rectangle](arkts-arkui-common-rectangle-i.md)&gt; \| [Rectangle](arkts-arkui-common-rectangle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## responseRegionList

```TypeScript
default responseRegionList(regions: Array<ResponseRegion> | undefined): this
```

Sets the response region list of the current component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| regions | Array&lt;[ResponseRegion](arkts-arkui-common-responseregion-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## restoreId

```TypeScript
default restoreId(value: int | undefined): this
```

id for distribute identification.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## reuse

```TypeScript
default reuse(options: ReuseOptions | undefined): this
```

Reuse id is used for identify the reuse type of each @ComponentV2 custom component, which can give user control of sub-component recycle and reuse.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ReuseOptions](arkts-arkui-common-reuseoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## reuseId

```TypeScript
default reuseId(id: string | undefined): this
```

Reuse id is used for identify the reuse type for each custom node.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## rotate

```TypeScript
default rotate(value: RotateOptions | RotateAngleOptions | undefined): this
```

设置组件旋转。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [RotateOptions](arkts-arkui-common-rotateoptions-i.md) \| [RotateAngleOptions](arkts-arkui-common-rotateangleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## safeAreaPadding

```TypeScript
default safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding | undefined): this
```

Sets the safe area padding. It enables a container to add a component-level safe area for child components to expand into. Default value: **LengthMetrics.vp(0)**

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| paddingValue | [Padding](arkts-arkui-units-padding-i.md) \| [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| [LocalizedPadding](arkts-arkui-localizedpadding-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## saturate

```TypeScript
default saturate(value: double | undefined): this
```

Applies a saturation effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scale

```TypeScript
default scale(value: ScaleOptions | undefined): this
```

设置组件缩放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScaleOptions](arkts-arkui-common-scaleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## sepia

```TypeScript
default sepia(value: double | undefined): this
```

Sepia conversion ratio of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## shadow

```TypeScript
default shadow(value: ShadowOptions | ShadowStyle | undefined): this
```

Applies a shadow effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShadowOptions](arkts-arkui-common-shadowoptions-i.md) \| [ShadowStyle](arkts-arkui-common-shadowstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## sharedTransition

```TypeScript
default sharedTransition(id: string | undefined, options?: sharedTransitionOptions): this
```

设置共享元素转场动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [id](#id) | string \| undefined | 是 |
| options | [sharedTransitionOptions](arkts-arkui-common-sharedtransitionoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## shouldBuiltInRecognizerParallelWith

```TypeScript
default shouldBuiltInRecognizerParallelWith(callback: ShouldBuiltInRecognizerParallelWithCallback | undefined): this
```

Provides a callback to set the parallel relationship between built-in gestures and gestures of other components in the response chain.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ShouldBuiltInRecognizerParallelWithCallback](arkts-arkui-shouldbuiltinrecognizerparallelwithcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## shouldRecognizerParallelWith

```TypeScript
default shouldRecognizerParallelWith(callback: ShouldRecognizerParallelWithCallback | undefined): this
```

Provides a callback to set the parallel relationship between gestures of current component and gestures of other components in the response chain.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ShouldRecognizerParallelWithCallback](arkts-arkui-shouldrecognizerparallelwithcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## size

```TypeScript
default size(value: SizeOptions | undefined): this
```

Sets the size of the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SizeOptions](arkts-arkui-sizeoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## smartGestureShortcut

```TypeScript
default smartGestureShortcut(options?: SmartGestureShortcutOptions): this
```

Enable or disable specific smart gesture shortcuts, and set response priorities for them.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SmartGestureShortcutOptions](arkts-arkui-common-smartgestureshortcutoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## sphericalEffect

```TypeScript
default sphericalEffect(value: double | undefined): this
```

Applies a spherical effect to the component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## stateStyles

```TypeScript
default stateStyles(value: StateStyles | undefined): this
```

Sets styles for component state.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [StateStyles](arkts-arkui-common-statestyles-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## sweepGradient

```TypeScript
default sweepGradient(value: SweepGradientOptions | undefined): this
```

Creates a sweep gradient.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SweepGradientOptions](arkts-arkui-common-sweepgradientoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## systemBarEffect

```TypeScript
default systemBarEffect(): this
```

Applies a system bar effect to the component, which means to invert colors based on the background and add a blur.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| this |

## systemMaterial

```TypeScript
default systemMaterial(material: SystemUiMaterial | undefined): this
```

Set system-styled materials for the component. The material effect behaves differently on devices with different level of computing powers. On devices with lower computing power, it affects attributes such as the backgroundColor, borderWidth, borderColor, shadow. On devices with higher computing power, it adds a filter effect at the system material layer, which can produce an effect similar to glass.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- API版本23+：SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| material | [SystemUiMaterial](arkts-arkui-systemuimaterial-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## tabIndex

```TypeScript
default tabIndex(index: int | undefined): this
```

Set focus index by key tab. The tabIndex and focusScopeId cannot be used together.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## tabStop

```TypeScript
default tabStop(isTabStop: boolean | undefined): this
```

Set TabStop on component focus

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isTabStop | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## toolbar

```TypeScript
default toolbar(value: CustomBuilder | undefined): this
```

Config toolbar for current component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## transform

```TypeScript
default transform(value: Matrix4Transit | undefined): this
```

可用于显示二维变换时的矩阵变换。包含三维变换时应使用[transform3D](#transform3d)接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Matrix4Transit](arkts-arkui-matrix4transit-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## transform3D

```TypeScript
default transform3D(transform: Matrix4Transit | undefined): this
```

设置组件的三维变换矩阵。当涉及包含透视效果的三维变换时，transform接口显示效果可能有误，推荐使用transform3D接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transform](#transform) | [Matrix4Transit](arkts-arkui-matrix4transit-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## transition

```TypeScript
default transition(value: TransitionEffect | undefined): this
```

设置组件插入时显示和删除时隐藏的过渡效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## transition

```TypeScript
default transition(effect: TransitionEffect | undefined, onFinish: TransitionFinishCallback | undefined): this
```

设置组件插入时显示和删除时隐藏的过渡效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [TransitionEffect](arkts-arkui-common-transitioneffect-c.md) \| undefined | 是 |
| onFinish | [TransitionFinishCallback](arkts-arkui-transitionfinishcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## translate

```TypeScript
default translate(value: TranslateOptions | undefined): this
```

设置组件平移。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TranslateOptions](arkts-arkui-common-translateoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## useEffect

```TypeScript
default useEffect(useEffect: boolean | undefined, effectType: EffectType | undefined): this
```

Specifies whether to apply the effect defined by <!--Del-->the parent [EffectComponent](ts-container-effectcomponent-sys.md) or <!--DelEnd-->the window.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [useEffect](#useeffect) | boolean \| undefined | 是 |
| [effectType](../../apis-camera-kit/arkts-apis/arkts-camera-camera-controlcenterstatusinfo-i.md) | [EffectType](arkts-arkui-common-effecttype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## useEffect

```TypeScript
default useEffect(value: boolean | undefined): this
```

Specifies whether to combine the drawing of special effects, such as background blur.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## useShadowBatching

```TypeScript
default useShadowBatching(value: boolean | undefined): this
```

Sets whether to draw shadows of child nodes in the component at the same layer, so that the shadows of elements at the same layer overlap.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## visibility

```TypeScript
default visibility(value: Visibility | undefined): this
```

Controls the display or hide of the current component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Visibility](arkts-arkui-visibility-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## visualEffect

```TypeScript
default visualEffect(effect: VisualEffect | undefined): this
```

设置非滤镜视觉效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [VisualEffect](arkts-arkui-visualeffect-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## width

```TypeScript
default width(widthValue: Length | LayoutPolicy | undefined): this
```

Sets the width of the component or its horizontal layout policy. By default, the component uses the width required for its content. If the width of the component is greater than that of the parent container, the component will be drawn beyond the parent container scope.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| widthValue | [Length](arkts-arkui-length-t.md) \| [LayoutPolicy](arkts-arkui-common-layoutpolicy-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## zIndex

```TypeScript
default zIndex(value: int | undefined): this
```

The sibling components in the same container are hierarchically displayed. A larger value of z indicates a higher display level.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
