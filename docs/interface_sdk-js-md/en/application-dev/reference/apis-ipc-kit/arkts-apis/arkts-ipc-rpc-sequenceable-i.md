# Sequenceable

Writes objects of classes to a **MessageParcel** and reads them from the **MessageParcel** during IPC.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [Parcelable](arkts-ipc-rpc-parcelable-i.md)

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## marshalling

```TypeScript
marshalling(dataOut: MessageParcel): boolean
```

Marshals the sequenceable object into a **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [marshalling](arkts-ipc-rpc-parcelable-i.md#marshalling)(dataOut: MessageSequence)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataOut | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## unmarshalling

```TypeScript
unmarshalling(dataIn: MessageParcel): boolean
```

Unmarshals this sequenceable object from a **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unmarshalling](arkts-ipc-rpc-parcelable-i.md#unmarshalling)(dataIn: MessageSequence)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
