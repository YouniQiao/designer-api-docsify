# Sequenceable

在进程间通信（IPC）期间，将类的对象写入MessageParcel并从MessageParcel中恢复它们。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [Parcelable](arkts-ipc-rpc-parcelable-i.md)

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## marshalling

```TypeScript
marshalling(dataOut: MessageParcel): boolean
```

将此可序列对象封送到MessageParcel中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [marshalling](arkts-ipc-rpc-parcelable-i.md#marshalling)(dataOut: MessageSequence)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataOut | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## unmarshalling

```TypeScript
unmarshalling(dataIn: MessageParcel): boolean
```

从MessageParcel中解封此可序列对象。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unmarshalling](arkts-ipc-rpc-parcelable-i.md#unmarshalling)(dataIn: MessageSequence)

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
