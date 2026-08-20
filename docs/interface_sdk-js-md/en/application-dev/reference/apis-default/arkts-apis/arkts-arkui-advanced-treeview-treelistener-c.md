# TreeListener

Listener of the tree view component. You can bind it to the **TreeView** component and use it to listen for changes of tree nodes. One listener can be bound to only one **TreeView** component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class TreeListener--><!--Device-unnamed-export declare class TreeListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## off_TreeListenType

```TypeScript
public off(type: TreeListenType, callback?: OnChangedCallback): void
```

Unregisters a listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListener-public off(type: TreeListenType, callback?: OnChangedCallback): void--><!--Device-TreeListener-public off(type: TreeListenType, callback?: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TreeListenType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes | Listening type. |
| callback | [OnChangedCallback](arkts-onchangedcallback-t.md) | No | Node information. |

## on_TreeListenType

```TypeScript
public on(type: TreeListenType, callback: OnChangedCallback): void
```

Register a listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListener-public on(type: TreeListenType, callback: OnChangedCallback): void--><!--Device-TreeListener-public on(type: TreeListenType, callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TreeListenType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes | Listening type. |
| callback | [OnChangedCallback](arkts-onchangedcallback-t.md) | Yes | Node information. |

## once_TreeListenType

```TypeScript
public once(type: TreeListenType, callback: OnChangedCallback): void
```

Registers a one-off listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListener-public once(type: TreeListenType, callback: OnChangedCallback): void--><!--Device-TreeListener-public once(type: TreeListenType, callback: OnChangedCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [TreeListenType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | Yes | Listening type. |
| callback | [OnChangedCallback](arkts-onchangedcallback-t.md) | Yes | Node information. |

