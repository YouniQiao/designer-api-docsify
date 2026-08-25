# Panel

Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## hide

```TypeScript
hide(): Promise<void>
```

Hides the word selection panel. This API is used together with [show](#show). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result. If this API is not called proactively, the panel is automatically hidden when it loses focus.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## moveToGlobalDisplay

```TypeScript
moveToGlobalDisplay(x: number, y: number): Promise<void>
```

Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## off('destroyed')

```TypeScript
off(type: 'destroyed', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel destruction event. This API is used together with on('destroyed'). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md).

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'destroyed' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## off('hidden')

```TypeScript
off(type: 'hidden', callback?: Callback<void>): void
```

Unsubscribes from the word selection panel hiding event. This API is used together with on('hidden'). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md).

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hidden' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## on('destroyed')

```TypeScript
on(type: 'destroyed', callback: Callback<void>): void
```

Subscribes to the word selection panel destruction event. This API is used together with off('destroyed'). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md).

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'destroyed' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## on('hidden')

```TypeScript
on(type: 'hidden', callback: Callback<void>): void
```

Subscribes to the word selection panel hiding event. This API is used together with off('hidden'). This event is triggered when the panel is hidden by calling [hide](#hide) or automatically hidden when it loses focus. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md).

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hidden' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

Sets the UI content for the current word selection panel, for example, to display translation results, search suggestions, or custom action buttons. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## show

```TypeScript
show(): Promise<void>
```

Shows the word selection panel. This API is used together with [hide](#hide). This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |

## startMoving

```TypeScript
startMoving(): Promise<void>
```

Sets whether the word selection panel can be dragged along with the mouse, touchpad, or touchscreen. The panel automatically stops moving after the pointer is released. This API can be called only after a **Panel** instance is obtained by calling [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md). This API uses a promise to return the result. This API must be called in the **onTouch** callback, and the event type must be **TouchType.Down**.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [33600001](../errorcode-selection.md#33600001-word-selection-service-invocation-error) |
| [33600002](../errorcode-selection.md#33600002-word-selection-panel-has-been-destroyed) |
