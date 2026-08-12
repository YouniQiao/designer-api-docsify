# @ohos.rpc

The **RPC** module implements communication between processes, including inter-process communication (IPC) on a  single device and remote procedure call (RPC) between processes on difference devices. IPC is implemented based  on the Binder driver, and RPC is based on the DSoftBus driver.

**Since:** 7

<!--Device-unnamed-declare namespace rpc--><!--Device-unnamed-declare namespace rpc-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from '@kit.IPCKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |
| [CallingInfo](arkts-ipc-rpc-callinginfo-c.md) |
| [IPCSkeleton](arkts-ipc-rpc-ipcskeleton-c.md) |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |
| [MessageOption](arkts-ipc-rpc-messageoption-c.md) |
| [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) |
| [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) |
| [RemoteObject](arkts-ipc-rpc-remoteobject-c.md) |
| [RemoteProxy](arkts-ipc-rpc-remoteproxy-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeathRecipient](arkts-ipc-rpc-deathrecipient-i.md) |
| [IRemoteBroker](arkts-ipc-rpc-iremotebroker-i.md) |
| [Parcelable](arkts-ipc-rpc-parcelable-i.md) |
| [RequestResult](arkts-ipc-rpc-requestresult-i.md) |
| [SendRequestResult](arkts-ipc-rpc-sendrequestresult-i.md) |
| [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ErrorCode](arkts-ipc-rpc-errorcode-e.md) |
| [TypeCode](arkts-ipc-rpc-typecode-e.md) |
