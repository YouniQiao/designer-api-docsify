# WindowSceneAttribute (System API)

The WindowSceneAttribute

**Inheritance/Implementation:** WindowSceneAttribute extends [CommonMethod](common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface WindowSceneAttribute extends CommonMethod--><!--Device-unnamed-export declare interface WindowSceneAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## attractionEffect

```TypeScript
default attractionEffect(destination: Position | undefined, fraction: double | undefined): this
```

Set the attraction deformation effect of WindowScene.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSceneAttribute-default attractionEffect(destination: Position | undefined, fraction: double | undefined): this--><!--Device-WindowSceneAttribute-default attractionEffect(destination: Position | undefined, fraction: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| destination | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The position of the attraction target point in the component coordinate system. |
| fraction | double \| undefined | Yes | indicates the fraction of WindowScene. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier:
    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSceneAttribute-default attributeModifier(modifier:    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this--><!--Device-WindowSceneAttribute-default attributeModifier(modifier:    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this-End-->

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

