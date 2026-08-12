# createComponentObserver

## createComponentObserver

```TypeScript
function createComponentObserver(id: string): ComponentObserver
```

绑定指定组件，返回对应的监听句柄。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** [createComponentObserver](ohos.arkui.UIContext.UIInspector#createComponentObserver)

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-inspector-function createComponentObserver(id: string): ComponentObserver--><!--Device-inspector-function createComponentObserver(id: string): ComponentObserver-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [ComponentObserver](arkts-arkui-inspector-componentobserver-i.md) |

## 示例

```TypeScript
let listener: inspector.ComponentObserver = inspector.createComponentObserver('COMPONENT_ID'); // 监听id为COMPONENT_ID的组件回调事件
```
