# startBackgroundRunning

## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void
```

向系统申请长时任务，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning)(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void--><!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | 是 |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

FA模型示例：

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

const callback = (err: BusinessError, data: void) => {
  if (err) {
    console.error(`Operation startBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
  } else {
    console.info('Operation startBackgroundRunning succeeded');
  }
}

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback);
});
```

Stage模型示例：

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

const callback = (err: BusinessError, data: void) => {
  if (err) {
    console.error(`Operation startBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
  } else {
    console.info('Operation startBackgroundRunning succeeded');
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let wantAgentInfo : wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: 'com.example.myapplication',
          abilityName: 'EntryAbility'
        }
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj, callback);
    });
  }
};
```


## startBackgroundRunning

```TypeScript
function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>
```

向系统申请长时任务，使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [startBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-startbackgroundrunning-f.md#startBackgroundRunning)(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent)

**需要权限：** ohos.permission.KEEP_BACKGROUND_RUNNING

<!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>--><!--Device-backgroundTaskManager-function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| bgMode | [BackgroundMode](arkts-backgroundtasks-backgroundtaskmanager-backgroundmode-e.md) | 是 |
| wantAgent | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

FA模型示例（需使用js代码开发）：

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import wantAgent, { WantAgent } from '@ohos.app.ability.wantAgent';
import { BusinessError } from '@ohos.base';

let wantAgentInfo : wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
  backgroundTaskManager.startBackgroundRunning(featureAbility.getContext(),
    backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
    console.info('Operation startBackgroundRunning succeeded');
  }).catch((err: BusinessError) => {
    console.error(`Operation startBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
  });
});
```

Stage模型示例：

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
          bundleName: 'com.example.myapplication',
          abilityName: 'EntryAbility'
        }
      ],
      // 点击通知后，动作类型
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 0,
      // 点击通知后，动作执行属性
      wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
    };

    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj : WantAgent) => {
      backgroundTaskManager.startBackgroundRunning(this.context,
        backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
        console.info('Operation startBackgroundRunning succeeded');
      }).catch((err: BusinessError) => {
        console.error(`Operation startBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
      });
    });
  }
};
```
