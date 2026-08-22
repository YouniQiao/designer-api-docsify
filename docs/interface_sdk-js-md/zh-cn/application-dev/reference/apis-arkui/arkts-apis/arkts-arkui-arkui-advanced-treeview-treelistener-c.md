# TreeListener

树视图组件的监听器，可以将此对象绑定至树视图组件，然后通过它监听树的节点的变化，同一个监听器不可以控制多个树视图组件。监听器内部维护事件类型与回调函数的映射关系，当用户在TreeView上进行节点操作时，TreeView会通知监听器触 发相应的回调函数，开发者可在回调中获取节点信息并进行业务处理。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class TreeListener--><!--Device-unnamed-export declare class TreeListener-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { CallbackParam, NodeParam, TreeController, TreeListenType, TreeListener, TreeListenerManager, TreeView } from '@kit.ArkUI';
import { CallbackParamV2, NodeParamV2, TreeControllerV2, TreeListenerV2, TreeListenerManagerV2, TreeViewV2 } from '@kit.ArkUI';
```

## off_TreeListenType

```TypeScript
public off(type: TreeListenType, callback?: OnChangedCallback): void
```

取消监听。需要先注册监听后才能取消。同一监听器不可控制多个树视图组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TreeListener-public off(type: TreeListenType, callback?: OnChangedCallback): void--><!--Device-TreeListener-public off(type: TreeListenType, callback?: OnChangedCallback): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | 是 | 监听事件类型，用于指定要取消的监听事件。 |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | 否 | 回调函数，在对应监听事件触发时调用。默认值：undefined。传入时取消对应的节点信息的监听，不传时取消该类型的所有节点信息的监听。 |

## on_TreeListenType

```TypeScript
public on(type: TreeListenType, callback: OnChangedCallback): void
```

注册树视图节点事件的监听，监听成功后，当节点发生对应事件时会触发回调函数。同一监听器不可控制多个树视图组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TreeListener-public on(type: TreeListenType, callback: OnChangedCallback): void--><!--Device-TreeListener-public on(type: TreeListenType, callback: OnChangedCallback): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | 是 | 监听事件类型，用于指定要注册的监听事件。 |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | 是 | 回调函数，在对应监听事件触发时调用。回调参数callbackParam包含currentNodeId、parentNodeId和 childIndex等信息。 |

## once_TreeListenType

```TypeScript
public once(type: TreeListenType, callback: OnChangedCallback): void
```

注册一次树视图节点事件的监听，监听成功后，当节点首次发生对应事件时会触发回调函数，触发后自动移除监听。同一监听器不可控制多个树视图组件。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TreeListener-public once(type: TreeListenType, callback: OnChangedCallback): void--><!--Device-TreeListener-public once(type: TreeListenType, callback: OnChangedCallback): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [TreeListenType](arkts-arkui-arkui-advanced-treeview-treelistentype-e.md) | 是 | 监听事件类型，用于指定要注册的监听事件。 |
| callback | [OnChangedCallback](arkts-arkui-onchangedcallback-t.md) | 是 | 回调函数，在对应监听事件触发时调用。回调参数callbackParam包含currentNodeId、parentNodeId和 childIndex等信息。 |

