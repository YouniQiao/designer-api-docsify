# SelectionExtensionContext

**SelectionExtensionContext** is the context of   
[SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md), which inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md).

When a **SelectionExtensionAbility** component is instantiated, the system automatically creates the corresponding   
**SelectionExtensionContext**. You can call the [startAbility](#startability) API in **SelectionExtensionContext** to start other abilities in the same app. This is applicable when you need to redirect to another ability in the same app in word selection extension, helping users quickly obtain the functions or information associated with the selected word.

> **NOTE：**
> 
> - This module is supported only on PCs/2-in-1 devices. You can use
> **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this
> function.

**Inheritance/Implementation:** SelectionExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 24

<!--Device-unnamed-declare class SelectionExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class SelectionExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { SelectionExtensionContext } from 'kits/@kit.BasicServicesKit';
```

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

Starts the target ability in the same app. This method is applicable when you need to redirect to another ability in the app in word selection extension. The system matches and starts the target ability based on the values of   
**bundleName** and **abilityName** specified in the **Want** object. This API uses a promise to return the result. For details about the ability startup mechanism, see   
[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionContext-startAbility(want: Want): Promise<void>--><!--Device-SelectionExtensionContext-startAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000083](../../apis-ability-kit/errorcode-ability.md#16000083-specified-ability-cannot-be-started-by-this-type-of-extensionability) |
| [16000061](../../apis-ability-kit/errorcode-ability.md#16000061-unsupported-operation) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../../apis-ability-kit/errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../../apis-ability-kit/errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-caller-released) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { SelectionExtensionAbility, BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class SelectionAbilityStub extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption
  ): boolean | Promise<boolean> {
    console.info(`onRemoteMessageRequest code: ${code}`);
    return true;
  }
}

class SelectionExtAbility extends SelectionExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    try {
      // Construct a Want object to specify the target ability to start.
      let wantAbility: Want = {
        bundleName: 'com.selection.selectionapplication',
        abilityName: 'EntryAbility',
      };
      // Start the target ability. this.context is automatically provided by the SelectionExtensionAbility instance and does not need to be obtained separately.
      this.context.startAbility(wantAbility).then(() => {
        console.info(`startAbility success`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to startAbility. Error code: ${err.code}, error message: ${err.message}`);
      });
    } catch (err) {
      console.error(`Failed to startAbility. Error code: ${err.code}, error message: ${err.message}`);
    }
    return new SelectionAbilityStub('remote');
  }
}
```
