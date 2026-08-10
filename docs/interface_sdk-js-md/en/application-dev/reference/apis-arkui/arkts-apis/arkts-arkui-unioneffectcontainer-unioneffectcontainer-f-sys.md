# UnionEffectContainer (System API)

## UnionEffectContainer

```TypeScript
export declare function UnionEffectContainer(
    options?:UnionEffectContainerOptions,
    content_?:CustomBuilder,
): UnionEffectContainerAttribute
```

Provides a UnionEffectContainer Component that generates a component fusion effect for descendant components with"useUnionEffect(true)" set inside it, when their distance is less than a certain threshold.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-export declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-arkui-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | No | The options to create a UnionEffectContainer. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Subcomponents of UnionEffectContainer |

**Return value:**

| Type | Description |
| --- | --- |
| [UnionEffectContainerAttribute](../arkts-components/arkts-arkui-unioneffectcontainer-attribute.md) |  |


## UnionEffectContainer

```TypeScript
export declare function UnionEffectContainer(
  style_: CustomBuilderT<UnionEffectContainerAttribute>,
  content_?: CustomBuilder,
): UnionEffectContainerAttribute
```

Defines UnionEffectContainer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-export declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;UnionEffectContainerAttribute&gt; | Yes | UnionEffectContainer attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [UnionEffectContainerAttribute](../arkts-components/arkts-arkui-unioneffectcontainer-attribute.md) |  |

