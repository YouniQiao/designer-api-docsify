# UnionEffectContainer（系统接口）

## UnionEffectContainer

```TypeScript
@ComponentBuilder
export declare function UnionEffectContainer(
    options?:UnionEffectContainerOptions,
    content_?:CustomBuilder,
): UnionEffectContainerAttribute
```

Provides a UnionEffectContainer Component that generates a component fusion effect for descendant components with "useUnionEffect(true)" set inside it, when their distance is less than a certain threshold.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@ComponentBuilderexport declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function UnionEffectContainer(    options?:UnionEffectContainerOptions,    content_?:CustomBuilder,): UnionEffectContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | 否 | The options to create a UnionEffectContainer. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | Subcomponents of UnionEffectContainer |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnionEffectContainerAttribute](arkts-unioneffectcontainer-attribute.md) |  |


## UnionEffectContainer

```TypeScript
@Builder
export declare function UnionEffectContainer(
  style_: CustomBuilderT<UnionEffectContainerAttribute>,
  content_?: CustomBuilder,
): UnionEffectContainerAttribute
```

Defines UnionEffectContainer

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute--><!--Device-unnamed-@Builderexport declare function UnionEffectContainer(  style_: CustomBuilderT<UnionEffectContainerAttribute>,  content_?: CustomBuilder,): UnionEffectContainerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[UnionEffectContainerAttribute](arkts-unioneffectcontainer-attribute.md)&gt; | 是 | UnionEffectContainer attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnionEffectContainerAttribute](arkts-unioneffectcontainer-attribute.md) |  |

