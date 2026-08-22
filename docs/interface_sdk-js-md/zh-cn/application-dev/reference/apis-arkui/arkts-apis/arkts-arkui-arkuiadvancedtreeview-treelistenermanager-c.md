# TreeListenerManager

树视图组件的监听管理器，可以获取监听器实例并绑定至树视图组件，用于管理树的节点监听，同一个监听器不可以控制多个树视图组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class TreeListenerManager--><!--Device-unnamed-export declare class TreeListenerManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { CallbackParam, NodeParam, TreeController, TreeListenType, TreeListener, TreeListenerManager, TreeView } from '@kit.ArkUI';
import { CallbackParamV2, NodeParamV2, TreeControllerV2, TreeListenerV2, TreeListenerManagerV2, TreeViewV2 } from '@kit.ArkUI';
```

## getInstance

```TypeScript
static getInstance(): TreeListenerManager
```

获取监听管理器单例对象。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TreeListenerManager-static getInstance(): TreeListenerManager--><!--Device-TreeListenerManager-static getInstance(): TreeListenerManager-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TreeListenerManager](arkts-arkui-arkuiadvancedtreeview-treelistenermanager-c.md) | 返回获取到的监听管理器单例对象。 |

## getTreeListener

```TypeScript
public getTreeListener(): TreeListener
```

获取监听器。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TreeListenerManager-public getTreeListener(): TreeListener--><!--Device-TreeListenerManager-public getTreeListener(): TreeListener-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TreeListener](arkts-arkui-arkuiadvancedtreeview-treelistener-c.md) | 返回获取到的监听器。 |

