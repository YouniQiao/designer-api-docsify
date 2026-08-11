# GestureInterface

Defines the gesture API.

**Since:** 11

<!--Device-unnamed-interface GestureInterface<T>--><!--Device-unnamed-interface GestureInterface<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): T
```

Sets the input types that can trigger the gesture response.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-GestureInterface-allowedTypes(types: Array<SourceTool>): T--><!--Device-GestureInterface-allowedTypes(types: Array<SourceTool>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;SourceTool&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## tag

```TypeScript
tag(tag: string): T
```

Sets a gesture tag.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-GestureInterface-tag(tag: string): T--><!--Device-GestureInterface-tag(tag: string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [tag](#tag) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
