# originalText

## 导入模块

```TypeScript
import { ResizeDirection, WindowMode, PenMode, PenKeyOperation, Driver, MatchPattern, UiDirection, TouchOptions, ComponentEventType, PointerMatrix, WindowChangeType, Component, ON, PenKey, Rect, InputTextMode, UIEventObserver, WindowFilter, WindowChangeOptions, UiWindow, TouchPadSwipeOptions, Point, KeyOptions, DisplayRotation, UIElementInfo, PenKeyOperationOptions, ComponentEventOptions, MouseButton, On } from 'kits/@kit.TestKit';
```

## originalText

```TypeScript
export function originalText(text: string, pattern?: MatchPattern): On
```

Specifies the original text for the target Component.If the accessibility property 'accessibilityLevel' of a component is set to 'no' or 'no-hide-descendants',you will not be able to use {@link On.text} to match the component with the specified original text, but you can use this method to achieve it;if the component does not set the above accessibility property, this method has no difference with {@link On.text}

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On--><!--Device-ON-export function originalText(text: string, pattern?: MatchPattern): On-End-->

**系统能力：** SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | the original text value. |
| pattern | [MatchPattern](arkts-test-uitest-matchpattern-e.md) | 否 | the {@link MatchPattern} of the text value, Set it default {@link MatchPattern.EQUALS} if null or undefined. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](arkts-test-uitest-on-c.md) | this { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 17000007 | Parameter verification failed. |

