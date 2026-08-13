# Callee

Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface Callee--><!--Device-unnamed-export interface Callee-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { Callee, Caller, OnReleaseCallback, OnRemoteStateChangeCallback, CalleeCallback } from '@kit.AbilityKit';
```

## off_string

```TypeScript
off(method: string): void
```

Unregisters a caller notification callback, which is invoked when the target UIAbility registers a function.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Callee-off(method: string): void--><!--Device-Callee-off(method: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200005](../errorcode-ability.md#16200005-method-not-registered) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

let method = 'call_Function';

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.off(method);
    } catch (error) {
      console.error(`Callee.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
  }
}
```

## on_string

```TypeScript
on(method: string, callback: CalleeCallback): void
```

Registers a caller notification callback, which is invoked when the target UIAbility registers a function.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-Callee-on(method: string, callback: CalleeCallback): void--><!--Device-Callee-on(method: string, callback: CalleeCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |
| callback | [CalleeCallback](arkts-ability-app-ability-uiability-calleecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200004](../errorcode-ability.md#16200004-method-registered) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class MyMessageAble implements rpc.Parcelable {
  name: string
  str: string
  num: number = 1

  constructor(name: string, str: string) {
    this.name = name;
    this.str = str;
  }

  marshalling(messageSequence: rpc.MessageSequence) {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
    return true;
  }

  unmarshalling(messageSequence: rpc.MessageSequence) {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
    return true;
  }
}

let method = 'call_Function';

function funcCallBack(pdata: rpc.MessageSequence) {
  let msg = new MyMessageAble('test', '');
  pdata.readParcelable(msg);
  return new MyMessageAble('test1', 'Callee test');
}

export default class MainUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info('Callee onCreate is called');
    try {
      this.callee.on(method, funcCallBack);
    } catch (error) {
      console.error(`Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
  }
}
```
