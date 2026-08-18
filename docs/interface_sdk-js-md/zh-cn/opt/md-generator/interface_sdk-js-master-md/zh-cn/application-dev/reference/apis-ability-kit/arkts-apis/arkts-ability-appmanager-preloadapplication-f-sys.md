# preloadApplication（系统接口）

## 导入模块

```TypeScript
```

## preloadApplication

```TypeScript
function preloadApplication(bundleName: string, userId: number, mode: PreloadMode, appIndex?: number): Promise<void>
```

预加载应用进程。接口返回成功并不代表预加载成功，具体结果以目标应用进程是否创建成功为准。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRELOAD_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-appManager-function preloadApplication(bundleName: string, userId: int, mode: PreloadMode, appIndex?: int): Promise<void>--><!--Device-appManager-function preloadApplication(bundleName: string, userId: int, mode: PreloadMode, appIndex?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| userId | number | 是 |
| mode | [PreloadMode](arkts-ability-appmanager-preloadmode-e-sys.md) | 是 |
| appIndex | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16300005](../errorcode-ability.md#16300005-指定的包信息不存在) |

**示例**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let bundleName = 'ohos.samples.etsclock';
  let userId = 100;
  let mode = appManager.PreloadMode.PRESS_DOWN;
  let appIndex = 0;
  appManager.preloadApplication(bundleName, userId, mode, appIndex)
    .then(() => {
      hilog.info(0x0000, 'testTag', `preloadApplication success`);
    })
    .catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `preloadApplication error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `preloadApplication error, code: ${(err as BusinessError).code}, msg:${(err as BusinessError).message}`);
}
```
