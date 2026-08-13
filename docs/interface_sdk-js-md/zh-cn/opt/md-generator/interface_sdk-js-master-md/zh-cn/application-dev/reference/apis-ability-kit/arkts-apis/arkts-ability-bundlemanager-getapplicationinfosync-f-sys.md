# getApplicationInfoSync（系统接口）

## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: number, userId: number) : ApplicationInfo
```

以同步方法根据给定的bundleName、applicationFlags和userId获取ApplicationInfo。 获取调用方自身的信息时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| applicationFlags | number | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;
let userId = 100;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags, userId);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```


## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: number) : ApplicationInfo
```

以同步方法根据给定的bundleName、applicationFlags获取ApplicationInfo。 获取调用方自身的信息时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| applicationFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700026](../errorcode-bundle.md#17700026-指定应用被禁用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```
