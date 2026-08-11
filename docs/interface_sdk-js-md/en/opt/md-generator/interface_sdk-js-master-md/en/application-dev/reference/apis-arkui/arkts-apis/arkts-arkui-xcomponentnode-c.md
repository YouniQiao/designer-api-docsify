# XComponentNode

Defines XComponent Node.

**Inheritance/Implementation:** XComponentNode extends [FrameNode](arkts-arkui-framenode-c.md)

**Since:** 11

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/typeNode#XComponent

<!--Device-unnamed-export declare class XComponentNode extends FrameNode--><!--Device-unnamed-export declare class XComponentNode extends FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeRenderType

```TypeScript
changeRenderType(type: NodeRenderType): boolean
```

Set the render type of the builderNode.

**Since:** 11

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/FrameNode#appendChild

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean--><!--Device-XComponentNode-changeRenderType(type: NodeRenderType): boolean-End-->

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

**Deprecated since:** 12

**Substitutes:** ohos.arkui.node/typeNode#createNode

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)--><!--Device-XComponentNode-constructor(uiContext: UIContext, options: RenderOptions,    id: string, type: XComponentType, libraryName?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| options | [RenderOptions](arkts-arkui-buildernode-renderoptions-i.md) | Yes |
| id | string | Yes |
| type | [XComponentType](arkts-arkui-xcomponenttype-e.md) | Yes |
| libraryName | string | No |

## onCreate

```TypeScript
onCreate(event?: Object): void
```

Called when the XComponent surface has been created.

**Since:** 11

**Deprecated since:** 12

**Substitutes:** XComponent/XComponentAttribute#onLoad

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-onCreate(event?: Object): void--><!--Device-XComponentNode-onCreate(event?: Object): void-End-->

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

**Deprecated since:** 12

**Substitutes:** XComponent/XComponentAttribute#onDestroy

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentNode-onDestroy(): void--><!--Device-XComponentNode-onDestroy(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
