# isLocalWantAgent (System API)

## Modules to Import

```TypeScript
import { WantAgent } from '@kit.AbilityKit';
```

## isLocalWantAgent

```TypeScript
function isLocalWantAgent(agent: WantAgent): boolean
```

Checks whether the specified WantAgent is local.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-wantAgent-function isLocalWantAgent(agent: WantAgent): boolean--><!--Device-wantAgent-function isLocalWantAgent(agent: WantAgent): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { wantAgent } from '@kit.AbilityKit';
import type { WantAgent } from '@kit.AbilityKit';

// Declare a wantAgent object.
let wantAgentData: WantAgent;
// Create a LocalWantAgentInfo object.
let localWantAgentInfo: wantAgent.LocalWantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0
};

// Create a WantAgent object and check whether it is local.
try {
  wantAgentData = wantAgent.createLocalWantAgent(localWantAgentInfo);
  let isLocal: boolean = wantAgent.isLocalWantAgent(wantAgentData);
} catch (err) {
  console.error('call isLocalWantAgent failed');
}
```
