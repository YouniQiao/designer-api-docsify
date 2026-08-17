# DynamicComponent (System API)

## DynamicComponent

```TypeScript
@ComponentBuilder
export declare function DynamicComponent(
    options: DynamicOptions
): DynamicComponentAttribute
```

Defines DynamicComponent Component.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function DynamicComponent(    options: DynamicOptions): DynamicComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function DynamicComponent(    options: DynamicOptions): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-na-dynamiccomponent-dynamicoptions-i-sys.md) | Yes | The options |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicComponentAttribute](arkts-na-dynamiccomponent-dynamiccomponentattribute-i.md) |  |


## DynamicComponent

```TypeScript
@Builder
export declare function DynamicComponent(
    style: CustomBuilderT<DynamicComponentAttribute>
): DynamicComponentAttribute
```

Defines DynamicComponent Component.It requires call setDynamicComponentOptions at start of the component attribute set-up and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function DynamicComponent(    style: CustomBuilderT<DynamicComponentAttribute>): DynamicComponentAttribute--><!--Device-unnamed-@Builderexport declare function DynamicComponent(    style: CustomBuilderT<DynamicComponentAttribute>): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;[DynamicComponentAttribute](arkts-na-dynamiccomponent-dynamiccomponentattribute-i.md)&gt; | Yes | the callback to set up DynamicComponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicComponentAttribute](arkts-na-dynamiccomponent-dynamiccomponentattribute-i.md) | The attribute of the DynamicComponent. |

