# Parcelable

Writes an object to a **MessageSequence** and reads it from the **MessageSequence** during IPC.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## marshalling

```TypeScript
marshalling(dataOut: MessageSequence): boolean
```

Marshals this **Parcelable** object into a **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataOut | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## unmarshalling

```TypeScript
unmarshalling(dataIn: MessageSequence): boolean
```

Unmarshals this **Parcelable** object from a **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
