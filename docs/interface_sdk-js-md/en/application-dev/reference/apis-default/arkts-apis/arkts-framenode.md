# FrameNode

Provides methods to implement FrameNode.

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [typeNode](arkts-typenode-n.md) | Provides methods to implement FrameNode. |

### Classes

| Name | Description |
| --- | --- |
| [FrameNode](arkts-framenode-c.md) | Defines FrameNode. |
| [NodeAdapter](arkts-framenode-nodeadapter-c.md) | Used for lazy loading of typeNode. |
| [TypedFrameNode](arkts-framenode-typedframenode-c.md) | Used to define the FrameNode type. |

### Interfaces

| Name | Description |
| --- | --- |
| [CrossLanguageOptions](arkts-framenode-crosslanguageoptions-i.md) | Defines the cross-language options. |
| [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | FrameNode options for configuring node creation behavior. |
| [InteractionEventBindingInfo](arkts-framenode-interactioneventbindinginfo-i.md) | The interaction event binding status information on the component. |
| [LayoutConstraint](arkts-framenode-layoutconstraint-i.md) | Layout constraint, including the max size, the min size and the reference size for children to calculate percent. |

### Enums

| Name | Description |
| --- | --- |
| [ChildrenCountMode](arkts-framenode-childrencountmode-e.md) | Enum for children count mode. Specifies how to count children when querying number of child nodes. |
| [ExpandMode](arkts-framenode-expandmode-e.md) | Enum for the expand mode. |
| [UIState](arkts-framenode-uistate-e.md) | Enum for the UI state of one component, which is used for handling of state style. |

### Types

| Name | Description |
| --- | --- |
| [UIStatesChangeHandler](arkts-uistateschangehandler-t.md) | UI state change handling function, it returns the current UI states, the value is the result of all current state enumeration values or calculations, and you can determine the state by performing the & operation as follows。 if (currentStates & UIState.PRESSED == UIState.PRESSED) But, please be awared, for the normal state check, the equal should be used directly. if (currentStates == UIState.NORMAL) |

