# IRemoteBroker

远端对象的代理持有者。用于获取代理对象。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## asObject

```TypeScript
asObject(): IRemoteObject
```

需派生类实现，获取代理或远端对象。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |
