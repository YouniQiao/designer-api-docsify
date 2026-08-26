# setWantAgentMultithreading (System API)

## Modules to Import

```TypeScript
import wantAgent, { WantAgent } from '@kit.AbilityKit';
```

## setWantAgentMultithreading

```TypeScript
function setWantAgentMultithreading(isMultithreadingSupported: boolean) : void
```

Enables or disables the WantAgent multithreading feature.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isMultithreadingSupported | boolean | Yes | Whether to enable the multithreading feature. The value & lt;code & gt;true & lt;/code & gt; means to enable multithreading, and & lt;code & gt;false & lt;/code & gt; means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Examples**

```TypeScript
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define a wantAgent object.
let wantAgentData: _WantAgent;
// Define a WantAgentInfo object.
let wantAgentInfo: wantAgent.WantAgentInfo = {
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
  actionType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// Define a getWantAgent callback.
function getWantAgentCallback(err: BusinessError, data: _WantAgent) {
  if (err) {
    console.error(`Failed to call getWantAgentCallback. Code is ${err.code}. Message is ${err.message}.`);
  } else {
    wantAgentData = data;
  }

  try {
    wantAgent.setWantAgentMultithreading(true);
  } catch (err) {
    console.error(`Failed to set wantAgentMultithreading. Code is ${err.code}. Message is ${err.message}.`);
  }
}

try {
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  console.error(`Failed to get wantAgent. Code is ${err.code}. Message is ${err.message}.`);
}
```
