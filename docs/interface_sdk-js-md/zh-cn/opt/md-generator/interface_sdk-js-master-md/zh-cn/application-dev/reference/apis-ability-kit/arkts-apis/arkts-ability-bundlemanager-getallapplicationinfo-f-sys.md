# getAllApplicationInfo（系统接口）

## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

根据给定的appFlags获取系统中所有的ApplicationInfo。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllApplicationInfo(appFlags: int, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundleManager-function getAllApplicationInfo(appFlags: int, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ApplicationInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let appFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;

try {
  bundleManager.getAllApplicationInfo(appFlags, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getAllApplicationInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed: %{public}s', message);
}
```


## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number,
    userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

根据给定的appFlags和userId获取系统中所有的ApplicationInfo。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllApplicationInfo(appFlags: int,    userId: int, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundleManager-function getAllApplicationInfo(appFlags: int,    userId: int, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ApplicationInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let appFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;
let userId = 100;

try {
  bundleManager.getAllApplicationInfo(appFlags, userId, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getAllApplicationInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed: %{public}s', message);
}
```


## getAllApplicationInfo

```TypeScript
function getAllApplicationInfo(appFlags: number, userId?: number): Promise<Array<ApplicationInfo>>
```

根据给定的appFlags和userId获取系统中所有的ApplicationInfo。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.GET_INSTALLED_BUNDLE_LIST

<!--Device-bundleManager-function getAllApplicationInfo(appFlags: int, userId?: int): Promise<Array<ApplicationInfo>>--><!--Device-bundleManager-function getAllApplicationInfo(appFlags: int, userId?: int): Promise<Array<ApplicationInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appFlags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;ApplicationInfo&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let appFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;

try {
  bundleManager.getAllApplicationInfo(appFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getAllApplicationInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllApplicationInfo failed. Cause: %{public}s', message);
}
```
