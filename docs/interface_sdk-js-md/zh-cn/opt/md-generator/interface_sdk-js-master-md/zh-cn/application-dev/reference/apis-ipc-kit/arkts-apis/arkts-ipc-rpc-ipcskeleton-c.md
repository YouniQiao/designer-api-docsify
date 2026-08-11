# IPCSkeleton

用于获取IPC上下文信息，包括获取UID和PID、获取本端和对端设备ID、检查接口调用是否在同一设备上。

**起始版本：** 7

<!--Device-rpc-class IPCSkeleton--><!--Device-rpc-class IPCSkeleton-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

## flushCmdBuffer

```TypeScript
static flushCmdBuffer(object: IRemoteObject): void
```

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

**起始版本：** 9

<!--Device-IPCSkeleton-static flushCmdBuffer(object: IRemoteObject): void--><!--Device-IPCSkeleton-static flushCmdBuffer(object: IRemoteObject): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  rpc.IPCSkeleton.flushCmdBuffer(remoteObject);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}
```

## flushCommands

```TypeScript
static flushCommands(object: IRemoteObject): number
```

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** static

<!--Device-IPCSkeleton-static flushCommands(object: IRemoteObject): number--><!--Device-IPCSkeleton-static flushCommands(object: IRemoteObject): number-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // 根据业务实际逻辑，进行相应处理
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  let ret = rpc.IPCSkeleton.flushCommands(remoteObject);
  hilog.info(0x0000, 'testTag', 'RpcServer: flushCommands result: ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}
```

## getCallingDeviceID

```TypeScript
static getCallingDeviceID(): string
```

静态方法，获取调用者进程所在的设备ID。

**起始版本：** 7

<!--Device-IPCSkeleton-static getCallingDeviceID(): string--><!--Device-IPCSkeleton-static getCallingDeviceID(): string-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerDeviceID = rpc.IPCSkeleton.getCallingDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: callerDeviceID is ' + callerDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## getCallingPid

```TypeScript
static getCallingPid(): number
```

静态方法，获取调用者的PID。此方法由[RemoteObject](arkts-ipc-rpc-remoteobject-c.md)对象在IPC上下文环境（  
[onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中调用，不在则返回本进程的PID。

**起始版本：** 7

<!--Device-IPCSkeleton-static getCallingPid(): int--><!--Device-IPCSkeleton-static getCallingPid(): int-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerPid = rpc.IPCSkeleton.getCallingPid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid result: ' + callerPid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## getCallingTokenId

```TypeScript
static getCallingTokenId(): number
```

静态方法，获取调用者的TokenId，用于被调用方对调用方的身份校验。

**起始版本：** 8

<!--Device-IPCSkeleton-static getCallingTokenId(): long--><!--Device-IPCSkeleton-static getCallingTokenId(): long-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingTokenId result: ' + callerTokenId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## getCallingUid

```TypeScript
static getCallingUid(): number
```

静态方法，获取调用者的UID。此方法由[RemoteObject](arkts-ipc-rpc-remoteobject-c.md)对象在IPC上下文环境（  
[onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中调用，不在则返回本进程的UID。

**起始版本：** 7

<!--Device-IPCSkeleton-static getCallingUid(): int--><!--Device-IPCSkeleton-static getCallingUid(): int-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerUid = rpc.IPCSkeleton.getCallingUid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid result: ' + callerUid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## getContextObject

```TypeScript
static getContextObject(): IRemoteObject
```

静态方法，获取系统服务管理器（SAMGR）对象。

**起始版本：** 7

<!--Device-IPCSkeleton-static getContextObject(): IRemoteObject--><!--Device-IPCSkeleton-static getContextObject(): IRemoteObject-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let samgr = rpc.IPCSkeleton.getContextObject();
  hilog.info(0x0000, 'testTag', 'RpcServer: getContextObject result: ' + samgr);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## getLocalDeviceID

```TypeScript
static getLocalDeviceID(): string
```

静态方法，获取本端设备ID。

**起始版本：** 7

<!--Device-IPCSkeleton-static getLocalDeviceID(): string--><!--Device-IPCSkeleton-static getLocalDeviceID(): string-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let localDeviceID = rpc.IPCSkeleton.getLocalDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: localDeviceID is ' + localDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## isLocalCalling

```TypeScript
static isLocalCalling(): boolean
```

静态方法，检查当前通信对端是否是本设备的进程。

**起始版本：** 7

<!--Device-IPCSkeleton-static isLocalCalling(): boolean--><!--Device-IPCSkeleton-static isLocalCalling(): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let isLocalCalling = rpc.IPCSkeleton.isLocalCalling();
      hilog.info(0x0000, 'testTag', 'RpcServer: isLocalCalling is ' + isLocalCalling);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## resetCallingIdentity

```TypeScript
static resetCallingIdentity(): string
```

静态方法，将远程用户的UID和PID替换为本地用户的UID和PID。它可以用于身份验证等场景。

**起始版本：** 7

<!--Device-IPCSkeleton-static resetCallingIdentity(): string--><!--Device-IPCSkeleton-static resetCallingIdentity(): string-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## restoreCallingIdentity

```TypeScript
static restoreCallingIdentity(identity: string): void
```

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。该接口仅支持在IPC上下文（  
[onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中使用，否则直接返回。

**起始版本：** 9

<!--Device-IPCSkeleton-static restoreCallingIdentity(identity: string): void--><!--Device-IPCSkeleton-static restoreCallingIdentity(identity: string): void-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identity | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      rpc.IPCSkeleton.restoreCallingIdentity(callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```

## setCallingIdentity

```TypeScript
static setCallingIdentity(identity: string): boolean
```

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** static

<!--Device-IPCSkeleton-static setCallingIdentity(identity: string): boolean--><!--Device-IPCSkeleton-static setCallingIdentity(identity: string): boolean-End-->

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identity | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      let ret = rpc.IPCSkeleton.setCallingIdentity(callingIdentity);
      hilog.info(0x0000, 'testTag', 'RpcServer: setCallingIdentity is ' + ret);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}
```
