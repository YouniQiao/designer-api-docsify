# SecurityUIExtensionComponent (System API)

## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    want: Want, options?: SecurityUIExtensionOptions, 
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

创建SecurityUIExtensionComponent组件，用于嵌入显示远程UIExtensionAbility提供的UI。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-export declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 要加载的Ability信息。 通过bundleName和abilityName共同确定被拉起的UIExtensionAbility， 同时需要在parameters中配置ability.want.params.uiExtensionType字段指定UIExtensionAbility的类型，当前仅支持'sysPicker/photoPicker'。 |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | No | 用于构造SecurityUIExtensionComponent的参数。不填时各字段使用默认值。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器内容构建器。ArkTS-Sta模式下可传入自定义内容构建器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](../arkts-components/arkts-arkui-securityuiextensioncomponent-attribute.md) |  |


## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

定义SecurityUIExtensionComponent组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-export declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SecurityUIExtensionComponentAttribute&gt; | Yes | 用于设置 SecurityUIExtensionComponent属性的回调。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器 |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](../arkts-components/arkts-arkui-securityuiextensioncomponent-attribute.md) | SecurityUIExtensionComponent的属性。 |

