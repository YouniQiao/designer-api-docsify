# application/AccessibilityExtensionContext

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AccessibilityExtensionContext](accessibilityextensioncontext-accessibilityextensioncontext-c.md) | The accessibility extension context. Used to configure, query information, and inject gestures. |

<!--Del-->
### Classes（系统接口）

| Name | Description |
| --- | --- |
| [AccessibilityExtensionContext](accessibilityextensioncontext-accessibilityextensioncontext-c-sys.md) | The accessibility extension context. Used to configure, query information, and inject gestures. |
| [Parameter](accessibilityextensioncontext-parameter-c-sys.md) | Sets the parameter for a specific operation when the accessibility node element executes this operation. For details, see [AccessibilityAction]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ (executable actions for accessibility node elements). |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [AccessibilityElement](accessibilityextensioncontext-accessibilityelement-i.md) | Defines the **AccessibilityElement**. Before calling APIs of **AccessibilityElement**, you must call [AccessibilityExtensionContext.getFocusElement()]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ or [AccessibilityExtensionContext.getWindowRootElement()]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to obtain an **AccessibilityElement** instance. |
| [ElementAttributeValues](accessibilityextensioncontext-elementattributevalues-i.md) | Provides attribute names and value types of a node element. |
| [Rect](accessibilityextensioncontext-rect-i.md) | Defines a rectangle. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AccessibilityElement](accessibilityextensioncontext-accessibilityelement-i-sys.md) | Defines the **AccessibilityElement**. Before calling APIs of **AccessibilityElement**, you must call [AccessibilityExtensionContext.getFocusElement()]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ or [AccessibilityExtensionContext.getWindowRootElement()]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to obtain an **AccessibilityElement** instance. |
| [AccessibilityGrid](accessibilityextensioncontext-accessibilitygrid-i-sys.md) | Defines accessibility grid information. For details, see the currentItem attribute in [AccessibilityElement]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [AccessibilitySpan](accessibilityextensioncontext-accessibilityspan-i-sys.md) | Defines the information about the hyperlink wrapped by the span tag. For details, see the spans attribute in [AccessibilityElement]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [AccessibilityVirtualNode](accessibilityextensioncontext-accessibilityvirtualnode-i-sys.md) | Defines the **AccessibilityVirtualNode**. |
| [ElementAttributeValues](accessibilityextensioncontext-elementattributevalues-i-sys.md) | Provides attribute names and value types of a node element. |
| [FocusMoveResult](accessibilityextensioncontext-focusmoveresult-i-sys.md) | Queries the return value type of the target accessibility nodes. |
| [TouchPosition](accessibilityextensioncontext-touchposition-i-sys.md) | Indicates touch position of accessibility virtual node. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [FocusDirection](arkts-accessibility-focusdirection-t.md) | Enumerates the focus directions. |
| [FocusType](arkts-accessibility-focustype-t.md) | Enumerates the focus types. |
| [WindowType](arkts-accessibility-windowtype-t.md) | Enumerates the window types. |

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [FocusCondition](arkts-accessibility-focuscondition-t-sys.md) | Defines a condition for querying the focusable node. |
| [FocusRule](arkts-accessibility-focusrule-t-sys.md) | Defines a focus rule for determining the start node and its descendants when searching for a focusable node. |
<!--DelEnd-->

