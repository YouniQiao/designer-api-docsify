# Task

上传或下载任务。使用该方法前需要先获取Task对象，promise形式通过 [request.agent.create](arkts-basicservices-agent-create-f.md)获取， callback形式通过 [request.agent.create](arkts-basicservices-agent-create-f.md)获取。

> **说明：**
> 
> Task对象及其挂载回调函数会在调用remove方法后释放并被系统自动回收。

**起始版本：** 23

<!--Device-agent-interface Task--><!--Device-agent-interface Task-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
import { cacheDownload } from '@kit.BasicServicesKit';
```

## off_completed

```TypeScript
off(event: 'completed', callback?: (progress: Progress) => void): void
```

取消订阅任务完成事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'completed', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'completed' | 是 | 取消订阅的事件类型。<br>- 取值为'completed'，表示任务完成。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有完成回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |

## off_failed

```TypeScript
off(event: 'failed', callback?: (progress: Progress) => void): void
```

取消订阅任务失败事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'failed', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'failed' | 是 | 取消订阅的事件类型。<br>- 取值为'failed'，表示任务失败。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有失败回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |

## off_faultOccur

```TypeScript
off(event: 'faultOccur', callback?: Callback<Faults>): void
```

取消订阅任务失败原因相关的事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

<!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void--><!--Device-Task-off(event: 'faultOccur', callback?: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'faultOccur' | 是 | 订阅的事件类型。<br>- 取值为'faultOccur'，表示任务失败。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 否 | 需要取消订阅的回调函数。若无此参数，则默认取消订阅当前类型的所有回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_pause

```TypeScript
off(event: 'pause', callback?: (progress: Progress) => void): void
```

取消订阅任务暂停事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'pause', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'pause' | 是 | 取消订阅的事件类型。<br>- 取值为'pause'，表示任务暂停。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有暂停回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_progress

```TypeScript
off(event: 'progress', callback?: (progress: Progress) => void): void
```

取消订阅任务进度事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'progress', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'progress' | 是 | 取消订阅的事件类型。<br>- 取值为'progress'，表示任务进度。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有进度回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | task mode error.<br>**适用版本：** 10+ |

## off_remove

```TypeScript
off(event: 'remove', callback?: (progress: Progress) => void): void
```

取消订阅任务移除事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'remove', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'remove' | 是 | 取消订阅的事件类型。<br>- 取值为'remove'，表示任务被移除。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有移除回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. <br> 3. Parameter verification failed. |

## off_response

```TypeScript
off(event: 'response', callback?: Callback<HttpResponse>): void
```

取消订阅任务响应事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void--><!--Device-Task-off(event: 'response', callback?: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'response' | 是 | 取消订阅的事件类型。<br>- 取值为'response'，表示任务响应。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | 否 | 需要取消订阅的回调函数。若无此参数，则取消订阅当前类型的所有回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_resume

```TypeScript
off(event: 'resume', callback?: (progress: Progress) => void): void
```

取消订阅任务恢复事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void--><!--Device-Task-off(event: 'resume', callback?: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'resume' | 是 | 取消订阅的事件类型。<br>- 取值为'resume'，表示任务恢复。 |
| callback | (progress: Progress) =&gt; void | 否 | 回调函数，发生相关的事件时触发该回调方法。若无此参数，则取消订阅的所有恢复回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## off_wait

```TypeScript
off(event: 'wait', callback?: Callback<WaitingReason>): void
```

取消订阅任务等待原因相关的事件。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

<!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void--><!--Device-Task-off(event: 'wait', callback?: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'wait' | 是 | 订阅的事件类型。<br>- 取值为'wait'，表示任务等待。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 否 | 需要取消订阅的回调函数。若无此参数，则默认取消订阅当前类型的所有回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## offCompleted

```TypeScript
offCompleted(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offCompleted(callback?: ProgressCallback): void--><!--Device-Task-offCompleted(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onCompleted(createOffCallback1);
  task.onCompleted(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offCompleted(createOffCallback1);
  // 表示取消订阅任务完成的所有回调
  task.offCompleted();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offFailed

```TypeScript
offFailed(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offFailed(callback?: ProgressCallback): void--><!--Device-Task-offFailed(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onFailed(createOffCallback1);
  task.onFailed(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offFailed(createOffCallback1);
  // 表示取消订阅任务失败的所有回调
  task.offFailed();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offFaultOccur

```TypeScript
offFaultOccur(callback?: Callback<Faults>): void
```

Disables the 'faultOccur' callback.

**起始版本：** 23

<!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void--><!--Device-Task-offFaultOccur(callback?: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 否 | callback function with a `Faults` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let faultOffCallback1 = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
let faultOffCallback2 = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onFaultOccur(faultOffCallback1);
  task.onFaultOccur(faultOffCallback2);
  // 表示取消faultOffCallback1的订阅
  task.offFaultOccur(faultOffCallback1);
  // 表示取消订阅任务移除的所有回调
  task.offFaultOccur();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offPause

```TypeScript
offPause(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offPause(callback?: ProgressCallback): void--><!--Device-Task-offPause(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback1 = () => {
      console.info('Download delete complete notification.');
    };
    let completeCallback2 = () => {
      console.info('Download delete complete notification.');
    };
    downloadTask.onComplete(completeCallback1);
    downloadTask.onComplete(completeCallback2);
    // 表示取消completeCallback1的订阅
    downloadTask.offComplete(completeCallback1);
    // 表示取消订阅下载任务完成的所有回调
    downloadTask.offComplete();

    let pauseCallback1 = () => {
      console.info('Download delete pause notification.');
    };
    let pauseCallback2 = () => {
      console.info('Download delete pause notification.');
    };
    downloadTask.onPause(pauseCallback1);
    downloadTask.onPause(pauseCallback2);
    // 表示取消pauseCallback1的订阅
    downloadTask.offPause(pauseCallback1);
    // 表示取消订阅下载任务暂停的所有回调
    downloadTask.offPause();

    let removeCallback1 = () => {
      console.info('Download delete remove notification.');
    };
    let removeCallback2 = () => {
      console.info('Download delete remove notification.');
    };
    downloadTask.onRemove(removeCallback1);
    downloadTask.onRemove(removeCallback2);
    // 表示取消removeCallback1的订阅
    downloadTask.offRemove(removeCallback1);
    // 表示取消订阅下载任务移除的所有回调
    downloadTask.offRemove();
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onPause(createOffCallback1);
  task.onPause(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offPause(createOffCallback1);
  // 表示取消订阅任务暂停的所有回调
  task.offPause();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offProgress

```TypeScript
offProgress(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offProgress(callback?: ProgressCallback): void--><!--Device-Task-offProgress(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: "POST",
  files: [{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: "name123", value: "123" }],
};
let upProgressCallback1 = (uploadedSize: long, totalSize: long) => {
  console.info('Upload delete progress notification.' + 'totalSize:' + totalSize + 'uploadedSize:' + uploadedSize);
};
let upProgressCallback2 = (uploadedSize: long, totalSize: long) => {
  console.info('Upload delete progress notification.' + 'totalSize:' + totalSize + 'uploadedSize:' + uploadedSize);
};
try {
  request.uploadFile(context, uploadConfig, (err: Error, uploadTask: request.UploadTask): void => {
    if (err) {
      console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    uploadTask.onProgress(upProgressCallback1);
    uploadTask.onProgress(upProgressCallback2);
    // 表示取消upProgressCallback1的订阅
    uploadTask.offProgress(upProgressCallback1);
    // 表示取消订阅上传任务进度事件的所有回调
    uploadTask.offProgress();
  });
} catch (err) {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let progressCallback1 = (receivedSize: long, totalSize: long) => {
      console.info('Download delete progress notification.' + 'receivedSize:' + receivedSize + 'totalSize:' + totalSize);
    };
    let progressCallback2 = (receivedSize: long, totalSize: long) => {
      console.info('Download delete progress notification.' + 'receivedSize:' + receivedSize + 'totalSize:' + totalSize);
    };
    downloadTask.onProgress(progressCallback1);
    downloadTask.onProgress(progressCallback2);
    // 表示取消progressCallback1的订阅
    downloadTask.offProgress(progressCallback1);
    // 表示取消订阅下载任务进度事件的所有回调
    downloadTask.offProgress();
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onProgress(createOffCallback1);
  task.onProgress(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offProgress(createOffCallback1);
  // 表示取消订阅任务进度的所有回调
  task.offProgress();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offRemove

```TypeScript
offRemove(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offRemove(callback?: ProgressCallback): void--><!--Device-Task-offRemove(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback1 = () => {
      console.info('Download delete complete notification.');
    };
    let completeCallback2 = () => {
      console.info('Download delete complete notification.');
    };
    downloadTask.onComplete(completeCallback1);
    downloadTask.onComplete(completeCallback2);
    // 表示取消completeCallback1的订阅
    downloadTask.offComplete(completeCallback1);
    // 表示取消订阅下载任务完成的所有回调
    downloadTask.offComplete();

    let pauseCallback1 = () => {
      console.info('Download delete pause notification.');
    };
    let pauseCallback2 = () => {
      console.info('Download delete pause notification.');
    };
    downloadTask.onPause(pauseCallback1);
    downloadTask.onPause(pauseCallback2);
    // 表示取消pauseCallback1的订阅
    downloadTask.offPause(pauseCallback1);
    // 表示取消订阅下载任务暂停的所有回调
    downloadTask.offPause();

    let removeCallback1 = () => {
      console.info('Download delete remove notification.');
    };
    let removeCallback2 = () => {
      console.info('Download delete remove notification.');
    };
    downloadTask.onRemove(removeCallback1);
    downloadTask.onRemove(removeCallback2);
    // 表示取消removeCallback1的订阅
    downloadTask.offRemove(removeCallback1);
    // 表示取消订阅下载任务移除的所有回调
    downloadTask.offRemove();
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onRemove(createOffCallback1);
  task.onRemove(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offRemove(createOffCallback1);
  // 表示取消订阅任务移除的所有回调
  task.offRemove();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offResponse

```TypeScript
offResponse(callback?: Callback<HttpResponse>): void
```

Disables the response callback.

**起始版本：** 23

<!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void--><!--Device-Task-offResponse(callback?: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | 否 | callback function with an `HttpResponse` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
let createOffCallback2 = (progress: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onResponse(createOffCallback1);
  task.onResponse(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offResponse(createOffCallback1);
  // 表示取消订阅任务移除的所有回调
  task.offResponse();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offResume

```TypeScript
offResume(callback?: ProgressCallback): void
```

Disables the specified callback.

**起始版本：** 23

<!--Device-Task-offResume(callback?: ProgressCallback): void--><!--Device-Task-offResume(callback?: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 否 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: {
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOffCallback1 = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
let createOffCallback2 = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onResume(createOffCallback1);
  task.onResume(createOffCallback2);
  // 表示取消createOffCallback1的订阅
  task.offResume(createOffCallback1);
  // 表示取消订阅任务恢复的所有回调
  task.offResume();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## offWait

```TypeScript
offWait(callback?: Callback<WaitingReason>): void
```

Disables the wait callback.

**起始版本：** 23

<!--Device-Task-offWait(callback?: Callback<WaitingReason>): void--><!--Device-Task-offWait(callback?: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 否 | callback function with an `WaitingReason` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOffTest",
  value: [{
    filename: "taskOffTest.avi",
    path: "./taskOffTest.avi",
  }]
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOffTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let waitOffCallback1 = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
let waitOffCallback2 = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onWait(waitOffCallback1);
  task.onWait(waitOffCallback2);
  // 表示取消waitOffCallback1的订阅
  task.offWait(waitOffCallback1);
  // 表示取消订阅任务移除的所有回调
  task.offWait();
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## on_completed

```TypeScript
on(event: 'completed', callback: (progress: Progress) => void): void
```

订阅任务完成事件，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'completed', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'completed' | 是 | 订阅的事件类型。<br>- 取值为'completed'，表示任务完成，任务完成时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | task mode error.<br>**适用版本：** 10+ |

## on_failed

```TypeScript
on(event: 'failed', callback: (progress: Progress) => void): void
```

订阅任务失败事件，使用callback异步回调。可通过调用 [request.agent.show](arkts-basicservices-agent-show-f.md)查看错误原因 。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'failed', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'failed' | 是 | 订阅的事件类型。<br>- 取值为'failed'，表示任务失败，任务失败时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |

## on_faultOccur

```TypeScript
on(event: 'faultOccur', callback: Callback<Faults>): void
```

订阅任务失败原因，使用callback形式返回结果。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

<!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void--><!--Device-Task-on(event: 'faultOccur', callback: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'faultOccur' | 是 | 订阅的事件类型。<br>- 取值为'faultOccur'，表示任务失败。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 是 | 发生相关的事件时触发该回调方法，返回任务失败的原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_pause

```TypeScript
on(event: 'pause', callback: (progress: Progress) => void): void
```

订阅任务暂停事件，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'pause', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'pause' | 是 | 订阅的事件类型。<br>- 取值为'pause'，表示任务已暂停，任务暂停时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_progress

```TypeScript
on(event: 'progress', callback: (progress: Progress) => void): void
```

订阅任务进度的事件，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'progress', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'progress' | 是 | 订阅的事件类型。<br>- 取值为'progress'，表示任务进度，任务进度有进展时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | task mode error.<br>**适用版本：** 10+ |

## on_remove

```TypeScript
on(event: 'remove', callback: (progress: Progress) => void): void
```

订阅任务移除事件，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'remove', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'remove' | 是 | 订阅的事件类型。<br>- 取值为'remove'，表示任务被移除，任务移除时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_response

```TypeScript
on(event: 'response', callback: Callback<HttpResponse>): void
```

订阅任务响应头，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void--><!--Device-Task-on(event: 'response', callback: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'response' | 是 | 订阅的事件类型。<br>- 取值为'response'，表示任务响应，请求接收到响应时触发该事件。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | 是 | 回调函数，发生相关的事件时触发该回调方法，返回任务响应头的数据结构。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_resume

```TypeScript
on(event: 'resume', callback: (progress: Progress) => void): void
```

订阅任务恢复事件，使用callback异步回调。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 11

<!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void--><!--Device-Task-on(event: 'resume', callback: (progress: Progress) => void): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'resume' | 是 | 订阅的事件类型。<br>- 取值为'resume'，表示任务恢复，任务恢复时触发该事件。 |
| callback | (progress: Progress) =&gt; void | 是 | 回调函数，发生相关的事件时触发该回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## on_wait

```TypeScript
on(event: 'wait', callback: Callback<WaitingReason>): void
```

订阅任务等待原因，使用callback形式返回结果。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 20

<!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void--><!--Device-Task-on(event: 'wait', callback: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | 'wait' | 是 | 订阅的事件类型。<br>- 取值为'wait'，表示任务等待。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 是 | 发生相关的事件时触发该回调方法，返回任务等待的原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |

## onCompleted

```TypeScript
onCompleted(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onCompleted(callback: ProgressCallback): void--><!--Device-Task-onCompleted(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task completed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onCompleted(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onFailed

```TypeScript
onFailed(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onFailed(callback: ProgressCallback): void--><!--Device-Task-onFailed(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onFailed(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onFaultOccur

```TypeScript
onFaultOccur(callback: Callback<Faults>): void
```

Enables the 'faultOccur' callback. This callback is triggered when the task failed. The returned `Faults` will contain the reason why the task failed.

**起始版本：** 23

<!--Device-Task-onFaultOccur(callback: Callback<Faults>): void--><!--Device-Task-onFaultOccur(callback: Callback<Faults>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[Faults](arkts-basicservices-agent-faults-e.md)&gt; | 是 | callback function with a `Faults` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let faultOnCallback = (faults: request.agent.Faults) => {
  console.info('upload task failed.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onFaultOccur(faultOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onPause

```TypeScript
onPause(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onPause(callback: ProgressCallback): void--><!--Device-Task-onPause(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback = () => {
      console.info('Download task completed.');
    };
    downloadTask.onComplete(completeCallback);

    let pauseCallback = () => {
      console.info('Download task pause.');
    };
    downloadTask.onPause(pauseCallback);

    let removeCallback = () => {
      console.info('Download task remove.');
    };
    downloadTask.onRemove(removeCallback);
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "POST",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task pause.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.onPause(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
  task.pause();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onProgress

```TypeScript
onProgress(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onProgress(callback: ProgressCallback): void--><!--Device-Task-onProgress(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: "POST",
  files: [{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: "name123", value: "123" }],
};
let upProgressCallback = (uploadedSize: long, totalSize: long) => {
  console.info("upload totalSize:" + totalSize + "  uploadedSize:" + uploadedSize);
};
try {
  request.uploadFile(context, uploadConfig, (err: Error, uploadTask: request.UploadTask): void => {
    if (err) {
      console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    uploadTask.onProgress(upProgressCallback);
  });
} catch (err) {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let progressCallback = (receivedSize: long, totalSize: long) => {
      console.info("download receivedSize:" + receivedSize + " totalSize:" + totalSize);
    };
    downloadTask.onProgress(progressCallback);
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task progress.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onProgress(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onRemove

```TypeScript
onRemove(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onRemove(callback: ProgressCallback): void--><!--Device-Task-onRemove(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  // 需要手动将url替换为真实服务器的HTTP协议地址
  request.downloadFile(context, { url: 'https://xxxx/xxxx.hap' }).then((data: request.DownloadTask) => {
    let downloadTask: request.DownloadTask = data;
    let completeCallback = () => {
      console.info('Download task completed.');
    };
    downloadTask.onComplete(completeCallback);

    let pauseCallback = () => {
      console.info('Download task pause.');
    };
    downloadTask.onPause(pauseCallback);

    let removeCallback = () => {
      console.info('Download task remove.');
    };
    downloadTask.onRemove(removeCallback);
  }).catch((err: Error) => {
    console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
  })
} catch (err) {
  console.error(`Failed to request the download. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task remove.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.onRemove(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
  request.agent.remove(task.tid);
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onResponse

```TypeScript
onResponse(callback: Callback<HttpResponse>): void
```

Enables the response callback.

**起始版本：** 23

<!--Device-Task-onResponse(callback: Callback<HttpResponse>): void--><!--Device-Task-onResponse(callback: Callback<HttpResponse>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;HttpResponse&gt; | 是 | callback function with an `HttpResponse` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (response: request.agent.HttpResponse) => {
  console.info('upload task response.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onResponse(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onResume

```TypeScript
onResume(callback: ProgressCallback): void
```

Enables the specified callback.

**起始版本：** 23

<!--Device-Task-onResume(callback: ProgressCallback): void--><!--Device-Task-onResume(callback: ProgressCallback): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ProgressCallback](arkts-basicservices-agent-progresscallback-t.md) | 是 | callback function with a `Progress` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let createOnCallback = (progress: request.agent.Progress) => {
  console.info('upload task resume.');
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.onResume(createOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
  task.pause();
  task.resume();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## onWait

```TypeScript
onWait(callback: Callback<WaitingReason>): void
```

Enables the wait callback. This callback is triggered when the task changes from other states to the waiting state. The returned `WaitingReason` will contain the reason why the task enters waiting state.

**起始版本：** 23

<!--Device-Task-onWait(callback: Callback<WaitingReason>): void--><!--Device-Task-onWait(callback: Callback<WaitingReason>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[WaitingReason](arkts-basicservices-agent-waitingreason-e.md)&gt; | 是 | callback function with an `WaitingReason` argument. |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let attachments: Array<request.agent.FormItem> = [{
  name: "taskOnTest",
  value: {
    filename: "taskOnTest.avi",
    path: "./taskOnTest.avi",
  }
}];
let config: request.agent.Config = {
  action: request.agent.Action.UPLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskOnTest',
  description: 'Sample code for event listening',
  mode: request.agent.Mode.FOREGROUND,
  overwrite: false,
  method: "PUT",
  data: attachments,
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
let waitOnCallback = (reason: request.agent.WaitingReason) => {
  console.info('upload task waiting.');
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.onWait(waitOnCallback);
  console.info(`Succeeded in creating a upload task. result: ${task.tid}`);
  task.start();
}).catch((err: Error) => {
  console.error(`Failed to create a upload task, Code: ${err.code}, message: ${err.message}`);
});
```

## pause

```TypeScript
pause(callback: AsyncCallback<void>): void
```

暂停任务，可以暂停正在等待/正在运行/正在重试的任务，已暂停的任务可被 [resume](#resume)恢复。使用callback异步回调。

**起始版本：** 23

<!--Device-Task-pause(callback: AsyncCallback<void>): void--><!--Device-Task-pause(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当暂停任务成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

```TypeScript
downloadTask.pause().then(() => {    
  console.info('Succeeded in pausing the download task.');
}).catch((err: BusinessError) => {
  console.error(`Failed to pause the download task. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
downloadTask.pause((err: BusinessError) => {
  if(err) {
    console.error(`Failed to pause the download task. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in pausing the download task.');
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.pause((err: BusinessError) => {
    if (err) {
      console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in pausing a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.pause(err => {
    if (err) {
      console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in pausing a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.pause().then(() => {
    console.info(`Succeeded in pausing a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskPauseTest',
  description: 'Sample code for pause the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.pause().then(() => {
    console.info(`Succeeded in pausing a download task. `);
  }).catch((err: Error) => {
    console.error(`Failed to pause the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## pause

```TypeScript
pause(): Promise<void>
```

暂停任务，可以暂停正在等待/正在运行/正在重试的任务，已暂停的任务可被 [resume](#resume)恢复。使用Promise异步回调。

**起始版本：** 23

<!--Device-Task-pause(): Promise<void>--><!--Device-Task-pause(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

参见 [pause](#pause)

## resume

```TypeScript
resume(callback: AsyncCallback<void>): void
```

重新启动任务，可以恢复被暂停的任务。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

<!--Device-Task-resume(callback: AsyncCallback<void>): void--><!--Device-Task-resume(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当重新启动任务成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

```TypeScript
downloadTask.resume().then(() => {
  console.info('Succeeded in resuming the download task.')
}).catch((err: BusinessError) => {
  console.error(`Failed to resume the download task. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
downloadTask.resume((err: BusinessError) => {
  if (err) {
    console.error(`Failed to resume the download task. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in resuming the download task.');
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.pause();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.resume((err: BusinessError) => {
    if (err) {
      console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in resuming a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.pause();
  task.resume(err => {
    if (err) {
      console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in resuming a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.pause();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.resume().then(() => {
    console.info(`Succeeded in resuming a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskResumeTest',
  description: 'Sample code for resume the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.pause();
  task.resume().then(() => {
    console.info(`Succeeded in resuming a download task. `);
  }).catch((err: Error) => {
    console.error(`Failed to resume the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## resume

```TypeScript
resume(): Promise<void>
```

重新启动任务，可以恢复被暂停的任务。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

<!--Device-Task-resume(): Promise<void>--><!--Device-Task-resume(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900005](../errorcode-request.md#21900005-任务模式错误) | Operation with wrong task mode.<br>**适用版本：** 10+ |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

参见 [resume](#resume)

## setMaxSpeed

```TypeScript
setMaxSpeed(speed: long): Promise<void>
```

设置任务每秒能传输的字节数上限。使用Promise异步回调。

**起始版本：** 23

<!--Device-Task-setMaxSpeed(speed: long): Promise<void>--><!--Device-Task-setMaxSpeed(speed: long): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | long | 是 | 设置任务每秒能传输的字节数上限，单位为字节（B），最小值为16384字节，同时该值不得低于 [MinSpeed](arkts-basicservices-agent-minspeed-i.md)设置的最低速度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: <br> 1. Missing mandatory parameters. <br> 2. Incorrect parameter type. <br> 3. Parameter verification failed. |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  saveas: "./",
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  // 设置任务速度上限。
  task.setMaxSpeed(10 * 1024 * 1024).then(() => {
    console.info(`Succeeded in setting the max speed of the task. result: ${task.tid}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the max speed of the task. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  saveas: "./",
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  // 设置任务速度上限。
  task.setMaxSpeed(10 * 1024 * 1024).then(() => {
    console.info(`Succeeded in setting the max speed of the task. result: ${task.tid}`);
  }).catch((err: Error) => {
    console.error(`Failed to set the max speed of the task. result: ${task.tid}`);
  });
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## start

```TypeScript
start(callback: AsyncCallback<void>): void
```

启动一个任务。使用callback异步回调。

以下状态的任务可以被启动：

1. 刚被request.agent.create接口创建的任务。 2. 使用request.agent.create接口创建的已经失败或者停止的下载任务。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-start(callback: AsyncCallback<void>): void--><!--Device-Task-start(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当开启任务成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start((err: BusinessError) => {
    if (err) {
      console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in starting a download task.`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start(err => {
    if (err) {
      console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in starting a download task.`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start().then(() => {
    console.info(`Succeeded in starting a download task.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStartTest',
  description: 'Sample code for start the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then((task: request.agent.Task) => {
  task.start().then(() => {
    console.info(`Succeeded in starting a download task.`);
  }).catch((err: Error) => {
    console.error(`Failed to start the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## start

```TypeScript
start(): Promise<void>
```

启动一个任务。使用Promise异步回调。

以下状态的任务可以被启动：

1. 刚被request.agent.create接口创建的任务。 2. 使用request.agent.create接口创建的已经失败或者停止的下载任务。

> **说明：**
> 
> 示例中context的获取方式请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

**起始版本：** 23

**需要权限：** ohos.permission.INTERNET

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-start(): Promise<void>--><!--Device-Task-start(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

参见 [start](#start)

## stop

```TypeScript
stop(callback: AsyncCallback<void>): void
```

停止任务，可以停止正在运行/正在等待/正在重试的任务，已停止的任务可被 [start](#start)恢复。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-stop(callback: AsyncCallback<void>): void--><!--Device-Task-stop(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 回调函数。当停止任务成功，err为undefined，否则为错误对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.stop((err: BusinessError) => {
    if (err) {
      console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in stopping a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.stop(err => {
    if (err) {
      console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in stopping a download task. `);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  // 等待1秒再执行下一步操作，以防异步乱序
  await new Promise<void>((resolve) => {
    setTimeout(() => resolve(), 1000);
  })
  task.stop().then(() => {
    console.info(`Succeeded in stopping a download task. `);
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let config: request.agent.Config = {
  action: request.agent.Action.DOWNLOAD,
  url: 'http://127.0.0.1', // 需要手动将url替换为真实服务器的HTTP协议地址
  title: 'taskStopTest',
  description: 'Sample code for stop the download task',
  mode: request.agent.Mode.BACKGROUND,
  overwrite: false,
  method: "GET",
  data: "",
  saveas: "./",
  network: request.agent.Network.CELLULAR,
  metered: false,
  roaming: true,
  retry: true,
  redirect: true,
  index: 0,
  begins: 0,
  ends: -1,
  gauge: false,
  precise: false,
  token: "it is a secret"
};
request.agent.create(context, config).then(async (task: request.agent.Task) => {
  task.start();
  task.stop().then(() => {
    console.info(`Succeeded in stopping a download task. `);
  }).catch((err: Error) => {
    console.error(`Failed to stop the download task, Code: ${err.code}, message: ${err.message}`);
  });
  console.info(`Succeeded in creating a download task. result: ${task.tid}`);
}).catch((err: Error) => {
  console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
});
```

## stop

```TypeScript
stop(): Promise<void>
```

停止任务，可以停止正在运行/正在等待/正在重试的任务，已停止的任务可被 [start](#start)恢复。使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-stop(): Promise<void>--><!--Device-Task-stop(): Promise<void>-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [13400003](../errorcode-request.md#13400003-服务异常) | Task service ability error. |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) | Operation with wrong task state. |

**示例**

参见 [stop](#stop)

## config

```TypeScript
config: Config
```

任务的配置信息。

**类型：** Config

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-config: Config--><!--Device-Task-config: Config-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## tid

```TypeScript
readonly tid: string
```

任务id，由系统自动生成且唯一。

**类型：** string

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Task-readonly tid: string--><!--Device-Task-readonly tid: string-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

