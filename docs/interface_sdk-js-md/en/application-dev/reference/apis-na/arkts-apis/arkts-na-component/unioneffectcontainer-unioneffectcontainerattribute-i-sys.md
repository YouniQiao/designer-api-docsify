# UnionEffectContainerAttribute (System API)

Defines the UnionEffectContainer attribute functions.

**Inheritance/Implementation:** UnionEffectContainerAttribute extends [CommonMethod](common-commonmethod-i.md)

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
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

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
| light | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The point light style. |

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
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The options to create an UnionEffectContainer. |

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
| mode | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The Union mode. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

