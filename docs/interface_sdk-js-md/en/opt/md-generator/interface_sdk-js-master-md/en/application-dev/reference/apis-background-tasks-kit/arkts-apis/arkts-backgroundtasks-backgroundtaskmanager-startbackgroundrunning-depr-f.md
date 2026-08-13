# startBackgroundRunning

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void
```

Requests a continuous task from the system. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning)(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void--><!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | Yes |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

FA model:

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation startBackgroundRunning succeeded");
  }
}

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility"
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
});
```

Stage model:

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

function callback(err: BusinessError, data: void) {
  if (err) {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  } else {
    console.info("Operation startBackgroundRunning succeeded");
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo : wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      operationType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback)
    });
  }
};
```


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>
```

Requests a continuous task from the system. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning)(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent)

**Required permissions:** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>--><!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>-End-->

**System capability:** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | Yes |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

FA model (JS code is required for development):

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility"
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
    console.info("Operation startBackgroundRunning succeeded");
  }).catch((err: BusinessError) => {
    console.error("Operation startBackgroundRunning failed Cause: " + err);
  });
});
```

Stage model:

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo : wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: "com.example.myapplication",
          abilityName: "EntryAbility"
        }
      ],
      // Type of the operation to perform after the notification is clicked.
      operationType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      // Execution attribute of the operation to perform after the notification is clicked.
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
        console.info("Operation startBackgroundRunning succeeded");
      }).catch((err: BusinessError) => {
        console.error("Operation startBackgroundRunning failed Cause: " + err);
      });
    });
  }
};
```
