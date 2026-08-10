# TaskState

上传任务的任务信息，是  
[on('complete' | 'fail')](request.UploadTask.on(type: 'complete' | 'fail', callback: Callback&lt;Array<TaskState>&gt;&lt;TaskState&gt;>))和  
[off('complete' | 'fail')](request.UploadTask.off(type: 'complete' | 'fail', callback?: Callback&lt;Array<TaskState>&gt;&lt;TaskState&gt;>))接口的回调参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-request-interface TaskState--><!--Device-request-interface TaskState-End-->

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## message

```TypeScript
message: string
```

上传任务结果描述信息。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-message: string--><!--Device-TaskState-message: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## path

```TypeScript
path: string
```

文件路径。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-path: string--><!--Device-TaskState-path: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## responseCode

```TypeScript
responseCode: int
```

上传任务返回码。返回0表示上传任务成功，返回其它值表示上传任务失败，具体请参见message参数中的上传任务结果描述信息。

此处推荐使用  
[request.agent.create](arkts-basicservices-agent-create-f.md#create)创建上传任务，并获取标准错误码处理异常分支。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-TaskState-responseCode: int--><!--Device-TaskState-responseCode: int-End-->

**System capability:** SystemCapability.MiscServices.Upload

