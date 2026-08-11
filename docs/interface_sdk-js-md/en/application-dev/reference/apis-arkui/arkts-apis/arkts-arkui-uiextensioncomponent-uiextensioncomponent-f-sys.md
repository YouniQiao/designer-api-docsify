# UIExtensionComponent (System API)

## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    want: Want, options?: UIExtensionOptions
): UIExtensionComponentAttribute
```

Defines UIExtensionComponent Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIExtensionComponent(    want: Want, options?: UIExtensionOptions): UIExtensionComponentAttribute--><!--Device-unnamed-export declare function UIExtensionComponent(    want: Want, options?: UIExtensionOptions): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | The want. |
| options | [UIExtensionOptions](arkts-arkui-uiextensioncomponent-uiextensionoptions-i-sys.md) | No | The options. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIExtensionComponentAttribute](../arkts-components/arkts-arkui-uiextensioncomponent-attribute.md) | return instance of UIExtensionComponentAttribute. |


## UIExtensionComponent

```TypeScript
export declare function UIExtensionComponent(
    style: CustomBuilderT<UIExtensionComponentAttribute>
): UIExtensionComponentAttribute
```

Defines UIExtensionComponent Component.It requires call setUIExtensionComponentOptions at start of the component attribute set-up,and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIExtensionComponent(    style: CustomBuilderT<UIExtensionComponentAttribute>): UIExtensionComponentAttribute--><!--Device-unnamed-export declare function UIExtensionComponent(    style: CustomBuilderT<UIExtensionComponentAttribute>): UIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;UIExtensionComponentAttribute&gt; | Yes | the callback to set up uiextensioncomponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIExtensionComponentAttribute](../arkts-components/arkts-arkui-uiextensioncomponent-attribute.md) | The attribute of the UIExtensionComponent. |

