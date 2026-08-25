# getSupportedProcessCachePids（系统接口）

## 导入模块

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## getSupportedProcessCachePids

```TypeScript
function getSupportedProcessCachePids(bundleName : string): Promise<Array<int>>
```

查询当前应用中支持缓存后快速启动的进程PID。使用Promise异步回调。

> **说明：**&gt;
> 本接口仅支持获取调用者所在系统账号下的进程PID。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_RUNNING_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;Array & lt;number & gt; & gt;<br>ArkTS-Sta：Promise & lt;Array & lt;int & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = 'ohos.samples.processcache';
  appManager.getSupportedProcessCachePids(bundleName).then((pids: Array<number>) => {
      hilog.info(0x0000, 'testTag', `pids: ${JSON.stringify(pids)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.processcache";
  appManager.getSupportedProcessCachePids(bundleName).then((pids: Array<int>) => {
    hilog.info(0x0000, 'testTag', `pids: ${JSON.stringify(pids)}`);
  }).catch((e) => {
    let err = e as BusinessError;
    hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
  })
} catch (e) {
  let err = e as BusinessError;
  hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
}
```
