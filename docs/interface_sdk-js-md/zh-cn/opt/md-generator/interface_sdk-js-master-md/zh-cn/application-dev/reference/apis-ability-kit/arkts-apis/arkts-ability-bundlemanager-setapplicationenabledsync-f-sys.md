# setApplicationEnabledSync（系统接口）

## setApplicationEnabledSync

```TypeScript
function setApplicationEnabledSync(bundleName: string, isEnabled: boolean): void
```

以同步方法设置指定应用的禁用或使能状态。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

<!--Device-bundleManager-function setApplicationEnabledSync(bundleName: string, isEnabled: boolean): void--><!--Device-bundleManager-function setApplicationEnabledSync(bundleName: string, isEnabled: boolean): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| isEnabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.ohos.myapplication";

try {
  bundleManager.setApplicationEnabledSync(bundleName, false);
  hilog.info(0x0000, 'testTag', 'setApplicationEnabledSync successfully.');
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'setApplicationEnabledSync failed: %{public}s', message);
}
```


## setApplicationEnabledSync

```TypeScript
function setApplicationEnabledSync(bundleName: string, appIndex: number, isEnabled: boolean, killProcess: boolean): void
```

设置应用程序是启用还是禁用，并控制在禁用时是否杀死进程。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.CHANGE_ABILITY_ENABLED_STATE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-bundleManager-function setApplicationEnabledSync(bundleName: string, appIndex: int, isEnabled: boolean, killProcess: boolean): void--><!--Device-bundleManager-function setApplicationEnabledSync(bundleName: string, appIndex: int, isEnabled: boolean, killProcess: boolean): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |
| isEnabled | boolean | 是 |
| killProcess | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 需要替换为要设置的应用Bundle名称、应用索引、是否启用应用和禁用应用时是否退出应用进程
let bundleName: string = 'com.example.myapplication';
let appIndex: number = 0;
let isEnabled: boolean = true;
let killProcess: boolean = false;

try {
  bundleManager.setApplicationEnabledSync(bundleName, appIndex, isEnabled, killProcess);
  hilog.info(0x0000, 'testTag', 'setApplicationEnabledSync successfully');
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'setApplicationEnabledSync failed: %{public}s', message);
}
```
