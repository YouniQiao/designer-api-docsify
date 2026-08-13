# getAllLauncherAbilityInfo（系统接口）

## getAllLauncherAbilityInfo

```TypeScript
function getAllLauncherAbilityInfo(userId: number, callback: AsyncCallback<Array<LauncherAbilityInfo>>) : void
```

查询指定用户下所有应用的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md#LauncherAbilityInfo)。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-launcherBundleManager-function getAllLauncherAbilityInfo(userId: int, callback: AsyncCallback<Array<LauncherAbilityInfo>>) : void--><!--Device-launcherBundleManager-function getAllLauncherAbilityInfo(userId: int, callback: AsyncCallback<Array<LauncherAbilityInfo>>) : void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;LauncherAbilityInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  launcherBundleManager.getAllLauncherAbilityInfo(100,
    (errData: BusinessError, data: launcherBundleManager.LauncherAbilityInfo[]) => {
      if (errData !== null) {
        console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
      } else {
        console.info('data is ' + JSON.stringify(data));
      }
    });
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```


## getAllLauncherAbilityInfo

```TypeScript
function getAllLauncherAbilityInfo(userId: number) : Promise<Array<LauncherAbilityInfo>>
```

查询指定用户下所有应用的[LauncherAbilityInfo](arkts-ability-launcherabilityinfo-i.md#LauncherAbilityInfo)。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-launcherBundleManager-function getAllLauncherAbilityInfo(userId: int) : Promise<Array<LauncherAbilityInfo>>--><!--Device-launcherBundleManager-function getAllLauncherAbilityInfo(userId: int) : Promise<Array<LauncherAbilityInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Launcher

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;LauncherAbilityInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |

## 示例

```TypeScript
import { launcherBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  launcherBundleManager.getAllLauncherAbilityInfo(100)
    .then((data: launcherBundleManager.LauncherAbilityInfo[]) => {
      console.info('data is ' + JSON.stringify(data));
    }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  });
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
