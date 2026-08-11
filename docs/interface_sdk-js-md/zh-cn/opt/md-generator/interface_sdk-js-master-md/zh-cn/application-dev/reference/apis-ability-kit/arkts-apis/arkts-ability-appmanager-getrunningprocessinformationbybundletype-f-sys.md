# getRunningProcessInformationByBundleType（系统接口）

## getRunningProcessInformationByBundleType

```TypeScript
function getRunningProcessInformationByBundleType(
    bundleType: bundleManager.BundleType): Promise<Array<ProcessInformation>>
```

根据包类型获取当前运行进程的有关信息。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getRunningProcessInformationByBundleType(    bundleType: bundleManager.BundleType): Promise<Array<ProcessInformation>>--><!--Device-appManager-function getRunningProcessInformationByBundleType(    bundleType: bundleManager.BundleType): Promise<Array<ProcessInformation>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleType | bundleManager.BundleType | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;ProcessInformation&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { appManager, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appManager.getRunningProcessInformationByBundleType(bundleManager.BundleType.ATOMIC_SERVICE)
    .then((data) => {
      console.info(`The running process information is: ${JSON.stringify(data)}`);
    }).catch((error: BusinessError) => {
    console.error(`error: ${JSON.stringify(error)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] error: ${code}, ${message}`);
}
```
