# UnionEffectContainerAttribute (System API)

Defines the UnionEffectContainer attribute functions.

**Inheritance/Implementation:** UnionEffectContainerAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface UnionEffectContainerAttribute extends CommonMethod--><!--Device-unnamed-export declare interface UnionEffectContainerAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier for UnionEffectContainer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionEffectContainerAttribute-default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>        | AttributeModifier<CommonMethod> | undefined): this--><!--Device-UnionEffectContainerAttribute-default attributeModifier(modifier: AttributeModifier<UnionEffectContainerAttribute>        | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[UnionEffectContainerAttribute](arkts-arkui-unioneffectcontainer-unioneffectcontainerattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## pointLight

```TypeScript
default pointLight(light: PointLightStyle): this
```

Sets up point light source effects.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionEffectContainerAttribute-default pointLight(light: PointLightStyle): this--><!--Device-UnionEffectContainerAttribute-default pointLight(light: PointLightStyle): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| light | [PointLightStyle](../arkts-components/arkts-arkui-pointlightstyle-i-sys.md) | Yes | The point light style. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setUnionEffectContainerOptions

```TypeScript
default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this
```

Set UnionEffectContainer options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionEffectContainerAttribute-default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this--><!--Device-UnionEffectContainerAttribute-default setUnionEffectContainerOptions(options?: UnionEffectContainerOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UnionEffectContainerOptions](arkts-arkui-unioneffectcontainer-unioneffectcontaineroptions-i-sys.md) | No | The options to create an UnionEffectContainer. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of UnionEffectContainerAttribute. |

## unionMode

```TypeScript
default unionMode(mode: UnionMode | undefined): this
```

Sets union Mode of the UnionEffectContainer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionEffectContainerAttribute-default unionMode(mode: UnionMode | undefined): this--><!--Device-UnionEffectContainerAttribute-default unionMode(mode: UnionMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [UnionMode](arkts-arkui-unioneffectcontainer-unionmode-e-sys.md) \| undefined | Yes | The Union mode. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

