# UnionEffectContainer (System API)

## UnionEffectContainer

```TypeScript
@ComponentBuilder
export declare function UnionEffectContainer(
    options?:UnionEffectContainerOptions,
    content_?:CustomBuilder,
): UnionEffectContainerAttribute
```

Provides a UnionEffectContainer Component that generates a component fusion effect for descendant components with "useUnionEffect(true)" set inside it, when their distance is less than a certain threshold.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-na-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | No | The options to create a UnionEffectContainer. |
| content_ | CustomBuilder | No | Subcomponents of UnionEffectContainer |

**Return value:**

| Type | Description |
| --- | --- |
| [UnionEffectContainerAttribute](arkts-na-unioneffectcontainer-unioneffectcontainerattribute-i.md) |  |


## UnionEffectContainer

```TypeScript
@Builder
export declare function UnionEffectContainer(
  style_: CustomBuilderT<UnionEffectContainerAttribute>,
  content_?: CustomBuilder,
): UnionEffectContainerAttribute
```

Defines UnionEffectContainer

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-@Builderexport declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[UnionEffectContainerAttribute](arkts-na-unioneffectcontainer-unioneffectcontainerattribute-i.md)&gt; | Yes | UnionEffectContainer attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [UnionEffectContainerAttribute](arkts-na-unioneffectcontainer-unioneffectcontainerattribute-i.md) |  |

