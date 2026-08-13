# originalText

## Modules to Import

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from '@kit.TestKit';
```

## originalText

```TypeScript
export function originalText(text: string, pattern?: MatchPattern): On
```

Specifies the original text for the target Component. If the accessibility property [accessibilityLevel](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#accessibilityLevel) of a component is set to 'no' or 'no-hide-descendants', you will not be able to use [text](arkts-test-uitest-on-c.md#text) to match the component with the specified original text, but you can use this method to achieve it; if the component does not set the above accessibility property, this method has no difference with [text](arkts-test-uitest-on-c.md#text)

**Since:** 23

**Deprecated since:** -1

<!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On--><!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On-End-->

**System capability:** SystemCapability.Test.UiTest

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [On](arkts-test-uitest-on-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17000007](../errorcode-uitest.md#17000007-parameters-are-invalid) |
