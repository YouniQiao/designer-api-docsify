# createComponentObserver

## 导入模块

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## createComponentObserver

```TypeScript
function createComponentObserver(id: string): ComponentObserver
```

绑定指定组件，返回对应的监听句柄。

**起始版本：** 10

**废弃版本：** 18

**替代接口：** createComponentObserver

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

**返回值：**

| 类型 |
| --- |
| [ComponentObserver](arkts-arkui-inspector-componentobserver-i.md) |
