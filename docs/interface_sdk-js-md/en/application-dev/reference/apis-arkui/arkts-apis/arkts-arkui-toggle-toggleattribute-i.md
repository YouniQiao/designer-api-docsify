# ToggleAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**Inheritance/Implementation:** ToggleAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ToggleAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ToggleAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of toggle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ToggleAttribute-default attributeModifier(modifier: AttributeModifier<ToggleAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ToggleAttribute](arkts-arkui-toggle-toggleattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of toggle. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this
```

定制Toggle内容区的方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this--><!--Device-ToggleAttribute-default contentModifier(modifier: ContentModifier<ToggleConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;ToggleConfiguration&gt; \| undefined | Yes | 在Toggle组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改器，开发 者需要自定义class实现ContentModifier接口。取值为undefined时，则不使用contentModifier。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: ((isOn: boolean) => void) | undefined): this
```

开关状态切换时触发该事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default onChange(callback: ((isOn: boolean) => void) | undefined): this--><!--Device-ToggleAttribute-default onChange(callback: ((isOn: boolean) => void) | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((isOn: boolean) =&gt; void) \| undefined | Yes | 为true时，代表状态从关切换为开。false时，代表状态从开切换为关。为undefined时，则不使用事 件。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

设置组件在打开状态下的背景颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-ToggleAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | 组件打开状态的背景颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：&lt;br/&gt;当ToggleType为Switch时，默 认值为`\\$r('sys.color.ohos_id_color_emphasize')`。&lt;br/&gt;当ToggleType为Checkbox时，默认值为 `\\$r('sys.color.ohos_id_color_emphasize')`。&lt;br/&gt;当ToggleType为Button时，默认值为 `\\$r('sys.color.ohos_id_color_emphasize')`混合`\\$r('sys.float.ohos_id_alpha_highlight_bg')`的透明度。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## switchPointColor

```TypeScript
default switchPointColor(color: ResourceColor | undefined): this
```

设置Switch类型的圆形滑块颜色。仅当type为ToggleType.Switch生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default switchPointColor(color: ResourceColor | undefined): this--><!--Device-ToggleAttribute-default switchPointColor(color: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | Switch类型的圆形滑块颜色。取值为undefined时，按默认值处理。&lt;br/&gt;默认值：\\$r(' sys.color.ohos_id_color_foreground_contrary')&lt;br/&gt;**说明：**&lt;br/&gt;同时设置了systemMaterial新材质时，设置此属性后会出现点光源效果，点光源颜色跟随此 属性的设置。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## switchStyle

```TypeScript
default switchStyle(value: SwitchStyle | undefined): this
```

设置Switch类型的样式。仅当type为ToggleType.Switch生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToggleAttribute-default switchStyle(value: SwitchStyle | undefined): this--><!--Device-ToggleAttribute-default switchStyle(value: SwitchStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwitchStyle](../arkts-components/arkts-arkui-switchstyle-i.md) \| undefined | Yes | Switch样式风格。取值为undefined时，按各属性的默认值处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

