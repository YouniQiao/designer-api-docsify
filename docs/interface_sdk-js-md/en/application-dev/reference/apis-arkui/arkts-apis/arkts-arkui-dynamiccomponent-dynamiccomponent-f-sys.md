# DynamicComponent (System API)

## DynamicComponent

```TypeScript
export declare function DynamicComponent(
    options: DynamicOptions
): DynamicComponentAttribute
```

Defines DynamicComponent Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DynamicComponent(    options: DynamicOptions): DynamicComponentAttribute--><!--Device-unnamed-export declare function DynamicComponent(    options: DynamicOptions): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamiccomponent-dynamicoptions-i-sys.md) | Yes | The options |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md) |  |


## DynamicComponent

```TypeScript
export declare function DynamicComponent(
    style: CustomBuilderT<DynamicComponentAttribute>
): DynamicComponentAttribute
```

Defines DynamicComponent Component.It requires call setDynamicComponentOptions at start of the component attribute set-up and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function DynamicComponent(    style: CustomBuilderT<DynamicComponentAttribute>): DynamicComponentAttribute--><!--Device-unnamed-export declare function DynamicComponent(    style: CustomBuilderT<DynamicComponentAttribute>): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md)&gt; | Yes | the callback to set up DynamicComponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md) | The attribute of the DynamicComponent. |

