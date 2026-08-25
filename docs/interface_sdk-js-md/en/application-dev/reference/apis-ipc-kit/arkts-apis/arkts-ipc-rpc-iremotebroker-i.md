# IRemoteBroker

Represents the holder of a remote proxy object. It is used to obtain a proxy object.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## asObject

```TypeScript
asObject(): IRemoteObject
```

Obtains a proxy or remote object. This API must be implemented by its derived classes.

**Since:** 7

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |
