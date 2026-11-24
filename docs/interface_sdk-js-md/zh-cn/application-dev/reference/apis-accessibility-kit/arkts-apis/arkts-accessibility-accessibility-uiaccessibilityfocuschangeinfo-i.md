# UIAccessibilityFocusChangeInfo

```TypeScript
interface UIAccessibilityFocusChangeInfo
```

应用内无障碍焦点变化信息。

**起始版本：** 26.0.1

<!--Device-accessibility-interface UIAccessibilityFocusChangeInfo--><!--Device-accessibility-interface UIAccessibilityFocusChangeInfo-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## 导入模块

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType, UIRect, UIAccessibilityElement } from '@kit.AccessibilityKit';
```

## focusedElement

```TypeScript
focusedElement?: UIAccessibilityElement
```

当前聚焦节点的信息。

**类型：** [UIAccessibilityElement](arkts-accessibility-accessibility-uiaccessibilityelement-i.md)

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAccessibilityFocusChangeInfo-focusedElement?: UIAccessibilityElement--><!--Device-UIAccessibilityFocusChangeInfo-focusedElement?: UIAccessibilityElement-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

## unfocusedElement

```TypeScript
unfocusedElement?: UIAccessibilityElement
```

上一个聚焦节点的信息。

**类型：** [UIAccessibilityElement](arkts-accessibility-accessibility-uiaccessibilityelement-i.md)

**起始版本：** 26.0.1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAccessibilityFocusChangeInfo-unfocusedElement?: UIAccessibilityElement--><!--Device-UIAccessibilityFocusChangeInfo-unfocusedElement?: UIAccessibilityElement-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core
