# Parcelable

在进程间通信（IPC）期间，将类的对象写入MessageSequence并从MessageSequence中恢复它们。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## marshalling

```TypeScript
marshalling(dataOut: MessageSequence): boolean
```

将此可序列对象封送到MessageSequence中。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataOut | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## unmarshalling

```TypeScript
unmarshalling(dataIn: MessageSequence): boolean
```

从MessageSequence中解封此可序列对象。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dataIn | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
