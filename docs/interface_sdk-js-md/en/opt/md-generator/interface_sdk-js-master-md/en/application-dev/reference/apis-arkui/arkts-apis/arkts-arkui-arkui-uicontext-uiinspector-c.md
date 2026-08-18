# UIInspector

Provides APIs for registering the component layout and drawing display completion callbacks.

**Since:** 10

<!--Device-unnamed-export class UIInspector--><!--Device-unnamed-export class UIInspector-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## createComponentObserver

```TypeScript
createComponentObserver(id: string): inspector.ComponentObserver
```

Registers a callback for layout and drawing display completion notifications for a specific component.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIInspector-createComponentObserver(id: string): inspector.ComponentObserver--><!--Device-UIInspector-createComponentObserver(id: string): inspector.ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| inspector.ComponentObserver |

## createComponentObserver

```TypeScript
createComponentObserver(id: string | number): inspector.ComponentObserver
```

Registers a callback for layout and drawing display completion notifications for a specific component. <br>Display refers to the process of sending the drawing command of a node to the graphics service and completing <br>the display. Compared with createComponentObserver, this API supports the input of **UniqueID** (the unique ID <br>allocated by the system to a node).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIInspector-createComponentObserver(id: string | number): inspector.ComponentObserver--><!--Device-UIInspector-createComponentObserver(id: string | number): inspector.ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | string \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| inspector.ComponentObserver |
