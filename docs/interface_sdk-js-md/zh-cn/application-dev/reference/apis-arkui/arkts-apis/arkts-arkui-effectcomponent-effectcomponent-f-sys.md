# EffectComponent（系统接口）

## EffectComponent

```TypeScript
export declare function EffectComponent(
    options?: EffectComponentOptions,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent Component

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-export declare function EffectComponent(    options?: EffectComponentOptions,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EffectComponentOptions](../arkts-components/arkts-arkui-effectcomponentoptions-i-sys.md) | 否 | The options to create an EffectComponent. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | Subcomponents of EffectComponent |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EffectComponentAttribute](../arkts-components/arkts-arkui-effectcomponent-attribute.md) |  |


## EffectComponent

```TypeScript
export declare function EffectComponent(
    style_: CustomBuilderT<EffectComponentAttribute>,
    content_?: CustomBuilder,
): EffectComponentAttribute
```

Defines EffectComponent

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute--><!--Device-unnamed-export declare function EffectComponent(    style_: CustomBuilderT<EffectComponentAttribute>,    content_?: CustomBuilder,): EffectComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;EffectComponentAttribute&gt; | 是 | EffectComponent attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 否 | container |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EffectComponentAttribute](../arkts-components/arkts-arkui-effectcomponent-attribute.md) |  |

