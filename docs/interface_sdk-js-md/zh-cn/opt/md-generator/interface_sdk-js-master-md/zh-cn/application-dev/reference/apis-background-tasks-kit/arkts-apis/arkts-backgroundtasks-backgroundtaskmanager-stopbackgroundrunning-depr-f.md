# stopBackgroundRunning

## stopBackgroundRunning

```TypeScript
function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void
```

向系统申请取消长时任务，使用callback异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning)(context: Context, callback: AsyncCallback&lt;void&gt;)

<!--Device-backgroundTaskManager-function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void--><!--Device-backgroundTaskManager-function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

FA模型示例（需使用js代码开发）：

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

const callback = (err: BusinessError, data: void) => {
  if (err) {
    console.error(`Operation stopBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
  } else {
    console.info('Operation stopBackgroundRunning succeeded');
  }
}

backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext(), callback);
```

Stage模型示例：

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

const callback = (err: BusinessError, data: void) => {
  if (err) {
    console.error(`Operation stopBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
  } else {
    console.info('Operation stopBackgroundRunning succeeded');
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    backgroundTaskManager.stopBackgroundRunning(this.context, callback);
  }
};
```


## stopBackgroundRunning

```TypeScript
function stopBackgroundRunning(context: Context): Promise<void>
```

向系统申请取消长时任务，使用promise异步回调。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [stopBackgroundRunning](arkts-backgroundtasks-backgroundtaskmanager-stopbackgroundrunning-f.md#stopBackgroundRunning)(context: Context)

<!--Device-backgroundTaskManager-function stopBackgroundRunning(context: Context): Promise<void>--><!--Device-backgroundTaskManager-function stopBackgroundRunning(context: Context): Promise<void>-End-->

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

FA模型示例：

```TypeScript
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import featureAbility from '@ohos.ability.featureAbility';
import { BusinessError } from '@ohos.base';

// 取消长时任务
backgroundTaskManager.stopBackgroundRunning(featureAbility.getContext()).then(() => {
  console.info('Operation stopBackgroundRunning succeeded');
}).catch((err: BusinessError) => {
  console.error(`Operation stopBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
});
```

Stage模型示例：

```TypeScript
import UIAbility from '@ohos.app.ability.UIAbility';
import backgroundTaskManager from '@ohos.backgroundTaskManager';
import Want from '@ohos.app.ability.Want';
import AbilityConstant from '@ohos.app.ability.AbilityConstant';
import { BusinessError } from '@ohos.base';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 取消长时任务
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      console.info('Operation stopBackgroundRunning succeeded');
    }).catch((err: BusinessError) => {
      console.error(`Operation stopBackgroundRunning failed. code is ${err.code} message is ${err.message}`);
    });
  }
};
```
