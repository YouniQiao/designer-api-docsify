# getState

## 导入模块

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getState

```TypeScript
function getState(): RouterState
```

获取栈顶页面的状态信息。

> **说明：**&gt;
> - 从API version 8开始支持，从API version 18开始废弃，建议使用[getState](arkts-arkui-arkui-uicontext-router-c.md#getstate)替代。getLength需
> 先通过[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getRouter](arkts-arkui-arkui-uicontext-uicontext-c.md#getrouter)获取
> [Router](arkts-arkui-arkui-uicontext-uicontext-c.md)实例，然后通过该实例进行调用。&gt;
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md)中的
> [getRouter](arkts-arkui-arkui-uicontext-uicontext-c.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-arkui-uicontext-uicontext-c.md)对象。

**起始版本：** 8

**废弃版本：** 18

**替代接口：** [getState](arkts-arkui-arkui-uicontext-router-c.md#getstate)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [RouterState](arkts-arkui-system-router-routerstate-i.md) |
