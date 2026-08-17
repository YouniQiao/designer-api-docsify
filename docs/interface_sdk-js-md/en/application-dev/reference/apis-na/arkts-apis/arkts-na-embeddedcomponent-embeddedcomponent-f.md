# EmbeddedComponent

## EmbeddedComponent

```TypeScript
@ComponentBuilder
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | indicates initialization parameter. |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | No | indicates type of the EmbeddedComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| EmbeddedComponentAttribute |  |


## EmbeddedComponent

```TypeScript
@ComponentBuilder
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | indicates initialization parameter. |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | No | indicates type of the EmbeddedComponent. |
| options | [EmbeddedOptions](arkts-na-embeddedcomponent-embeddedoptions-i.md) | No | indicates type of the EmbeddedComponent options. |

**Return value:**

| Type | Description |
| --- | --- |
| EmbeddedComponentAttribute |  |


## EmbeddedComponent

```TypeScript
@Builder
export declare function EmbeddedComponent(
    style: CustomBuilderT<EmbeddedComponentAttribute>
): EmbeddedComponentAttribute
```

Defines EmbeddedComponent Component.It requires call setEmbeddedComponentOptions at start of the component attribute set-up, and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute--><!--Device-unnamed-@Builderexport declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;EmbeddedComponentAttribute&gt; | Yes | the callback to set up embeddedcomponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| EmbeddedComponentAttribute | The attribute of the EmbeddedComponent. |

