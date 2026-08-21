# TreeListenerManager

Implements a **TreeListenerManager** object, which can be bound to a **TreeView** component to listen for changes of tree nodes. One **TreeListenerManager** object can be bound to only one tree view component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class TreeListenerManager--><!--Device-unnamed-export declare class TreeListenerManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getInstance

```TypeScript
static getInstance(): TreeListenerManager
```

Obtains a **TreeListenerManager** singleton object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerManager-static getInstance(): TreeListenerManager--><!--Device-TreeListenerManager-static getInstance(): TreeListenerManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TreeListenerManager](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtreeview-treelistenermanager-c.md) | TreeListenerManager** singleton object. |

## getTreeListener

```TypeScript
public getTreeListener(): TreeListener
```

Obtains a listener.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerManager-public getTreeListener(): TreeListener--><!--Device-TreeListenerManager-public getTreeListener(): TreeListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TreeListener](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedtreeview-treelistener-c.md) | Obtained listener. |

