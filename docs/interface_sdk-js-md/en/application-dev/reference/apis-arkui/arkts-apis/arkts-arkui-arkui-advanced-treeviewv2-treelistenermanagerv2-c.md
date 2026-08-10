# TreeListenerManagerV2

树视图组件的监听管理器，可以将此对象绑定至树视图组件，然后通过它管理树视图监听器的变化，同一个监听管理器不可以控制多个树视图组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class TreeListenerManagerV2--><!--Device-unnamed-export declare class TreeListenerManagerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TreeListenerManagerV2, NodeParamV2, CallbackParamV2, TreeControllerV2, TreeViewV2, TreeListenerV2 } from 'kits/@kit.ArkUI';
```

## getInstance

```TypeScript
static getInstance(): TreeListenerManagerV2
```

获取树视图组件的监听管理器单例对象。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerManagerV2-static getInstance(): TreeListenerManagerV2--><!--Device-TreeListenerManagerV2-static getInstance(): TreeListenerManagerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TreeListenerManagerV2](arkts-arkui-arkui-advanced-treeviewv2-treelistenermanagerv2-c.md) | 返回获取到的树视图组件的监听管理器单例对象。 |

## getTreeListener

```TypeScript
getTreeListener(): TreeListenerV2
```

获取树视图监听器实例。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TreeListenerManagerV2-getTreeListener(): TreeListenerV2--><!--Device-TreeListenerManagerV2-getTreeListener(): TreeListenerV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [TreeListenerV2](arkts-arkui-arkui-advanced-treeviewv2-treelistenerv2-c.md) | 返回获取到的树视图监听器实例。 |

