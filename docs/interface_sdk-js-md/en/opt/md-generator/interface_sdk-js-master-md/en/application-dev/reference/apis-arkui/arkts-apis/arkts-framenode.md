# FrameNode

Provides APIs for creating a specific type of FrameNode, which can be mounted through the basic API of the FrameNode and be displayed using a placeholder container.

When **typeNode** is used to create [Text](../@internal/component/ets/text),  
[Image](../@internal/component/ets/image), [Select](../@internal/component/ets/select), or  
[Toggle](../@internal/component/ets/toggle) nodes, if the UI instance corresponding to the input  
[UIContext](@ohos.arkui.UIContext) is destroyed, this API returns an invalid FrameNode that cannot be properly mounted or displayed.

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FrameNode](arkts-arkui-framenode-c.md) |
| [NodeAdapter](arkts-arkui-framenode-nodeadapter-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CrossLanguageOptions](arkts-arkui-framenode-crosslanguageoptions-i.md) |
| [InteractionEventBindingInfo](arkts-arkui-framenode-interactioneventbindinginfo-i.md) |
| [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) |
| [TypedFrameNode](arkts-arkui-framenode-typedframenode-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ChildrenCountMode](arkts-arkui-framenode-childrencountmode-e.md) |
| [ExpandMode](arkts-arkui-framenode-expandmode-e.md) |
| [UIState](arkts-arkui-framenode-uistate-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UIStatesChangeHandler](arkts-arkui-uistateschangehandler-t.md) |
