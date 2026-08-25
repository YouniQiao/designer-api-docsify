# @ohos.rpc(RPC通信)

本模块提供进程间通信能力，包括设备内的进程间通信（IPC）和设备间的进程间通信（RPC），前者基于Binder驱动，后者基于软总线驱动。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from '@kit.IPCKit';
```

## 汇总

### 类

| 名称 |
| --- |
| [Ashmem(RPC通信)](arkts-ipc-rpc-ashmem-c.md) |
| [CallingInfo(RPC通信)](arkts-ipc-rpc-callinginfo-c.md) |
| [IPCSkeleton(RPC通信)](arkts-ipc-rpc-ipcskeleton-c.md) |
| [IRemoteObject(RPC通信)](arkts-ipc-rpc-iremoteobject-c.md) |
| [MessageOption(RPC通信)](arkts-ipc-rpc-messageoption-c.md) |
| [MessageParcel(RPC通信)](arkts-ipc-rpc-messageparcel-c.md) |
| [MessageSequence(RPC通信)](arkts-ipc-rpc-messagesequence-c.md) |
| [RemoteObject(RPC通信)](arkts-ipc-rpc-remoteobject-c.md) |
| [RemoteProxy(RPC通信)](arkts-ipc-rpc-remoteproxy-c.md) |

### 接口

| 名称 |
| --- |
| [DeathRecipient(RPC通信)](arkts-ipc-rpc-deathrecipient-i.md) |
| [IRemoteBroker(RPC通信)](arkts-ipc-rpc-iremotebroker-i.md) |
| [Parcelable(RPC通信)](arkts-ipc-rpc-parcelable-i.md) |
| [RequestResult(RPC通信)](arkts-ipc-rpc-requestresult-i.md) |
| [SendRequestResult(RPC通信)](arkts-ipc-rpc-sendrequestresult-i.md) |
| [Sequenceable(RPC通信)](arkts-ipc-rpc-sequenceable-i.md) |

### 枚举

| 名称 |
| --- |
| [ErrorCode(RPC通信)](arkts-ipc-rpc-errorcode-e.md) |
| [TypeCode(RPC通信)](arkts-ipc-rpc-typecode-e.md) |

### 类型

| 名称 |
| --- |
| [OnRemoteDiedFunc(RPC通信)](arkts-ipc-rpc-onremotediedfunc-t.md) |
