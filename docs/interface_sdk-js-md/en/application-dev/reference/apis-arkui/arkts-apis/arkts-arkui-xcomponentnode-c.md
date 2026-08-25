# XComponentNode

Defines XComponent Node.@extends FrameNode

**Inheritance/Implementation:** XComponentNode extends FrameNode

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Deprecated since:** 12

**Substitutes:** XComponent

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeRenderType

```TypeScript
changeRenderType(type: NodeRenderType): boolean
```

Set the render type of the builderNode.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Deprecated since:** 12

**Substitutes:** appendChild

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [NodeRenderType](arkts-arkui-buildernode-noderendertype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## constructor

```TypeScript
constructor(uiContext: UIContext, options: RenderOptions,
    id: string, type: XComponentType, libraryName?: string)
```

constructor.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Deprecated since:** 12

**Substitutes:** createNode

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | Yes |
| id | string | Yes |
| type | [XComponentType](arkts-arkui-enums-xcomponenttype-e.md) | Yes |
| libraryName | string | No |

## onCreate

```TypeScript
onCreate(event?: Object): void
```

Called when the XComponent surface has been created.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Deprecated since:** 12

**Substitutes:** onLoad

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Object | No |

## onDestroy

```TypeScript
onDestroy(): void
```

Called when the XComponent surface has been destroyed.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Deprecated since:** 12

**Substitutes:** onDestroy

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
