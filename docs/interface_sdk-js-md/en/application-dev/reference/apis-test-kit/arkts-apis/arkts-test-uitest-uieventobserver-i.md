# UIEventObserver

Defines a UI event listener, which is used to listen for various events on the UI, including the display of the **Toast** and **Dialog** components, window change event, and component operation event. An instance can be created using [createUIEventObserver](arkts-test-uitest-driver-c.md#createuieventobserver).

**Since:** 10

**System capability:** SystemCapability.Test.UiTest

## Modules to Import

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## once('toastShow')

```TypeScript
once(type: 'toastShow', callback: Callback<UIElementInfo>): void
```

Subscribes to events of the toast component. This API uses a callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'toastShow' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## once('dialogShow')

```TypeScript
once(type: 'dialogShow', callback: Callback<UIElementInfo>): void
```

Subscribes to events of the dialog component. This API uses a callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dialogShow' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## once('windowChange')

```TypeScript
once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void
```

Starts listening for window change events of the specified type with extended configuration supported. This API triggers a callback when a specified window change event is detected. This API can be used only in [free windows](../../../windowmanager/window-terminology.md#free-windows) mode.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'windowChange' | Yes |
| [windowChangeType](arkts-test-uitest-uielementinfo-i.md) | [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) | Yes |
| options | [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |

## once('componentEventOccur')

```TypeScript
once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void
```

Starts listening for component operation events of the specified type with extended configuration supported. This API triggers a callback when a specified component operation event is detected.

**Since:** 22

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'componentEventOccur' | Yes |
| [componentEventType](arkts-test-uitest-uielementinfo-i.md) | [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) | Yes |
| options | [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[UIElementInfo](arkts-test-uitest-uielementinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [17000005](../errorcode-uitest.md#17000005-operation-not-supported) |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
