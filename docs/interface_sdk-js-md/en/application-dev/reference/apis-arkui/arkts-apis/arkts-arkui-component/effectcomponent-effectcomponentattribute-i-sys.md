# EffectComponentAttribute (System API)

Define the EffectComponentAttribute.

**Inheritance/Implementation:** EffectComponentAttribute extends [CommonMethod](common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EffectComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface EffectComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## alwaysSnapshot

```TypeScript
alwaysSnapshot(enable: boolean | undefined): this
```

Use snapshot when Effect Component have no visual effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentAttribute-alwaysSnapshot(enable: boolean | undefined): this--><!--Device-EffectComponentAttribute-alwaysSnapshot(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_true indicates using the snapshot method, false indicates not using the snapshot method. undefined means the default value false. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A nonsystem application calls a system API. |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<EffectComponentAttribute>
        | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier for EffectComponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentAttribute-default attributeModifier(modifier: AttributeModifier<EffectComponentAttribute>        | AttributeModifier<CommonMethod> | undefined): this--><!--Device-EffectComponentAttribute-default attributeModifier(modifier: AttributeModifier<EffectComponentAttribute>        | AttributeModifier<CommonMethod> | undefined): this-End-->

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

## setEffectComponentOptions

```TypeScript
default setEffectComponentOptions(options?: EffectComponentOptions): this
```

Set EffectComponent options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EffectComponentAttribute-default setEffectComponentOptions(options?: EffectComponentOptions): this--><!--Device-EffectComponentAttribute-default setEffectComponentOptions(options?: EffectComponentOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The options to create an EffectComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns instance of EffectComponentAttribute. |

