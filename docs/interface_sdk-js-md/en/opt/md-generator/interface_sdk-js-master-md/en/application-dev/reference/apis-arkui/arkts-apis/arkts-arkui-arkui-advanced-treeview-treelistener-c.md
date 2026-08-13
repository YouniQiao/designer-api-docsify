# TreeListener

Listener of the tree view component. You can bind it to the **TreeView** component and use it to listen for changes of tree nodes. One listener can be bound to only one **TreeView** component.

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-export declare class TreeListener--><!--Device-unnamed-export declare class TreeListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListener, NodeParam, CallbackParam, TreeListenType, TreeView, TreeController, TreeListenerManager } from '@kit.ArkUI';
```

## off_TreeListenType

```TypeScript
off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void
```

Registers a one-off listener.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TreeListener-off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void--><!--Device-TreeListener-off(type: TreeListenType, callback?: (callbackParam: CallbackParam) => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes |
| callback | (callbackParam: CallbackParam) = & gt; void | No |

## on_TreeListenType

```TypeScript
on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void
```

Declare class TreeListener

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TreeListener-on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void--><!--Device-TreeListener-on(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes |
| callback | (callbackParam: CallbackParam) = & gt; void | Yes |

## once_TreeListenType

```TypeScript
once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void
```

Declare class TreeListener

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TreeListener-once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void--><!--Device-TreeListener-once(type: TreeListenType, callback: (callbackParam: CallbackParam) => void): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes |
| callback | (callbackParam: CallbackParam) = & gt; void | Yes |
