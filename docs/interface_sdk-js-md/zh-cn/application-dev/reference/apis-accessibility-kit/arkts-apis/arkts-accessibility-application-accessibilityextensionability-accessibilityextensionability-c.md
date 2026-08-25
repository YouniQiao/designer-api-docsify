# AccessibilityExtensionAbility

AccessibilityExtensionAbility基于ExtensionAbility框架，提供无障碍扩展业务的能力，包括连接无障碍服务、断开无障碍服务、处理无障碍事件和处理无障碍按键事件等。  
**生命周期流程：** onAccessibilityConnect（连接回调，用于初始化）→ onAccessibilityEventInfo/onAccessibilityKeyEvent（处理无障碍事件和按键事件）→ onAccessibilityDisconnect（断开回调，用于资源回收）。

**起始版本：** 9

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## 导入模块

```TypeScript
import { AccessibilityExtensionAbility, AccessibilityElement, AccessibilityExtensionContext, ElementAttributeKeys, ElementAttributeValues, FocusDirection, FocusType, Rect, WindowType, AccessibilityEvent, AccessibilityEventInfo, Parameter, FocusRule, FocusCondition, FocusMoveResult, AccessibilityVirtualNode, TouchPosition } from 'kits/@kit.AccessibilityKit';
import { AccessibilityExtensionAbility, AccessibilityElement, AccessibilityExtensionContext, FocusDirection, Rect, WindowType, AccessibilityEventInfo, Parameter, FocusRule, FocusCondition, FocusMoveResult, AccessibilityVirtualNode, TouchPosition } from 'kits/@kit.AccessibilityKit';
```

## onAccessibilityEvent

```TypeScript
onAccessibilityEvent(event: AccessibilityEvent): void
```

当无障碍事件发生时回调此接口，可在该方法中根据事件信息进行业务逻辑处理。通常需要重写该方法。

**起始版本：** 9

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [AccessibilityEvent](arkts-accessibility-application-accessibilityextensionability-accessibilityevent-i.md) | 是 |

## onConnect

```TypeScript
onConnect(): void
```

用户启用AccessibilityExtensionAbility时，系统服务完成连接后回调此接口，可在该方法中执行初始化业务逻辑操作。该方法可选择性重写。

**起始版本：** 9

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## onDisconnect

```TypeScript
onDisconnect(): void
```

用户停用AccessibilityExtensionAbility时，系统服务完成断开连接后回调此接口，可在该方法中执行资源回收和退出业务操作。该方法可选择性重写。

**起始版本：** 9

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## onKeyEvent

```TypeScript
onKeyEvent(keyEvent: KeyEvent): boolean
```

在按键按下时回调此接口，可在该方法中根据业务判断是否消费事件。该方法可选择性重写。

**起始版本：** 9

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [keyEvent](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyeventdata-i-sys.md) | [KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## context

```TypeScript
context: AccessibilityExtensionContext
```

表示辅助功能扩展的上下文环境。

**类型：** [AccessibilityExtensionContext](arkts-accessibility-accessibilityextensioncontext-t.md)

**起始版本：** 9

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core
