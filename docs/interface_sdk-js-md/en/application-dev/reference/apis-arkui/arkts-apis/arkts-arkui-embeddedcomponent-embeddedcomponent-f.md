# EmbeddedComponent

## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType
): EmbeddedComponentAttribute
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | No | 提供方的类型，当前支持值为EmbeddedType.EMBEDDED_UI_EXTENSION， 表示嵌入的是EmbeddedUIExtensionAbility提供的UI。 |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](../arkts-components/arkts-arkui-embeddedcomponent-attribute.md) |  |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions
): EmbeddedComponentAttribute
```

创建跨进程嵌入式组件，用于显示同包名或满足跨应用权限条件的EmbeddedUIExtensionAbility的UI。相对于API version 12的接口，新增options参数用于传递构造参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 要加载的EmbeddedUIExtensionAbility。 |
| type | [EmbeddedType](arkts-arkui-embeddedtype-e.md) | No | 提供方的类型，当前支持值为EmbeddedType.EMBEDDED_UI_EXTENSION， 表示嵌入的是EmbeddedUIExtensionAbility提供的UI。 |
| options | [EmbeddedOptions](arkts-arkui-embeddedcomponent-embeddedoptions-i.md) | No | 嵌入式组件的可选配置项，用于设置占位符、DPI跟随策略、窗口模式跟随策略等。详见EmbeddedOptions。 |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](../arkts-components/arkts-arkui-embeddedcomponent-attribute.md) |  |


## EmbeddedComponent

```TypeScript
export declare function EmbeddedComponent(
    style: CustomBuilderT<EmbeddedComponentAttribute>
): EmbeddedComponentAttribute
```

定义EmbeddedComponent组件。需要在组件属性设置开始时调用setEmbeddedComponentOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute--><!--Device-unnamed-export declare function EmbeddedComponent(    style: CustomBuilderT<EmbeddedComponentAttribute>): EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;EmbeddedComponentAttribute&gt; | Yes | 用于设置embeddedcomponent属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](../arkts-components/arkts-arkui-embeddedcomponent-attribute.md) | EmbeddedComponent的属性。 |

