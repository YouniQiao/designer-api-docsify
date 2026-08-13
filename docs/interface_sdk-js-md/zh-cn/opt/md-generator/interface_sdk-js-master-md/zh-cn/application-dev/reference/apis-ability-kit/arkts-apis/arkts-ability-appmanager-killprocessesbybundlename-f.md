# killProcessesByBundleName

## killProcessesByBundleName

```TypeScript
function killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: number): Promise<void>
```

终止指定应用包名的应用进程。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.KILL_APP_PROCESSES or ohos.permission.CLEAN_BACKGROUND_PROCESSES

<!--Device-appManager-function killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: int): Promise<void>--><!--Device-appManager-function killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| clearPageStack | boolean | 是 |
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

## 示例

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleName = 'bundleName';
let isClearPageStack = false;
let appIndex = 1;

try {
  appManager.killProcessesByBundleName(bundleName, isClearPageStack, appIndex).then((data) => {
    console.info('killProcessesByBundleName success.');
  }).catch((err: BusinessError) => {
    console.error(`killProcessesByBundleName fail, code: ${err.code}, msg:${err.message}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```
