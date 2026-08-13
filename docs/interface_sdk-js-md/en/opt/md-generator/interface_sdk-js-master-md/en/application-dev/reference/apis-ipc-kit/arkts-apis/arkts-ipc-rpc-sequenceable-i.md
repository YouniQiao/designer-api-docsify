# Sequenceable

Writes objects of classes to a **MessageParcel** and reads them from the **MessageParcel** during IPC.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [Parcelable](arkts-ipc-rpc-parcelable-i.md#Parcelable)

<!--Device-rpc-interface Sequenceable--><!--Device-rpc-interface Sequenceable-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from '@kit.IPCKit';
```

## marshalling

```TypeScript
marshalling(dataOut: MessageParcel): boolean
```

Marshals the sequenceable object into a **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [marshalling](arkts-ipc-rpc-parcelable-i.md#marshalling)(dataOut: MessageSequence)

<!--Device-Sequenceable-marshalling(dataOut: MessageParcel): boolean--><!--Device-Sequenceable-marshalling(dataOut: MessageParcel): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataOut | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```

## unmarshalling

```TypeScript
unmarshalling(dataIn: MessageParcel): boolean
```

Unmarshals this sequenceable object from a **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [unmarshalling](arkts-ipc-rpc-parcelable-i.md#unmarshalling)(dataIn: MessageSequence)

<!--Device-Sequenceable-unmarshalling(dataIn: MessageParcel): boolean--><!--Device-Sequenceable-unmarshalling(dataIn: MessageParcel): boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}
```
