# UIExtensionComponent (System API)

## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    want: Want, options?: UIExtensionOptions
): UIExtensionComponentAttribute
```

定义UIExtensionComponent组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIExtensionComponent(    want: Want, options?: UIExtensionOptions): UIExtensionComponentAttribute--><!--Device-unnamed-export declare function UIExtensionComponent(    want: Want, options?: UIExtensionOptions): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 要加载的Ability，必须是带UI的Ability扩展。 Want的parameters中需设置ability.want.params.uiExtensionType字段，取值需与扩展Ability在module.json5中配置的type一致。 |
| options | [UIExtensionOptions](arkts-arkui-uiextensioncomponent-uiextensionoptions-i-sys.md) | No | 需要传递的构造参数，用于自定义UIExtensionComponent的配置（如设置占位符、DPI跟随策略、窗口Mode跟随策略等）。 当需要自定义上述配置时传入此参数，不传入时使用默认配置。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIExtensionComponentAttribute](../arkts-components/arkts-arkui-uiextensioncomponent-attribute.md) |  |


## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    style: CustomBuilderT<UIExtensionComponentAttribute>
): UIExtensionComponentAttribute
```

定义UIExtensionComponent组件。它要求在组件属性设置开始时调用setUIExtensionComponentOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIExtensionComponent(    style: CustomBuilderT<UIExtensionComponentAttribute>): UIExtensionComponentAttribute--><!--Device-unnamed-export declare function UIExtensionComponent(    style: CustomBuilderT<UIExtensionComponentAttribute>): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;UIExtensionComponentAttribute&gt; | Yes | 用于设置uiextensioncomponent属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UIExtensionComponentAttribute](../arkts-components/arkts-arkui-uiextensioncomponent-attribute.md) | UIExtensionComponent的属性。 |

