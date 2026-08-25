# WindowSceneAttribute (System API)

The WindowSceneAttribute@extends CommonMethod @interface WindowSceneAttribute

**Inheritance/Implementation:** WindowSceneAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## attractionEffect

```TypeScript
default attractionEffect(destination: Position | undefined, fraction: double | undefined): this
```

Set the attraction deformation effect of WindowScene.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [destination](../../apis-network-kit/arkts-apis/arkts-network-connection-routeinfo-i.md) | [Position](arkts-arkui-position-i.md) \| undefined | Yes |
| fraction | double \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowSceneAttribute](arkts-arkui-windowscene-windowsceneattribute-i-sys.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier:
    AttributeModifier<WindowSceneAttribute> | AttributeModifier<CommonMethod> | undefined) : this
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WindowSceneAttribute](arkts-arkui-windowscene-windowsceneattribute-i-sys.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WindowSceneAttribute](arkts-arkui-windowscene-windowsceneattribute-i-sys.md) |
