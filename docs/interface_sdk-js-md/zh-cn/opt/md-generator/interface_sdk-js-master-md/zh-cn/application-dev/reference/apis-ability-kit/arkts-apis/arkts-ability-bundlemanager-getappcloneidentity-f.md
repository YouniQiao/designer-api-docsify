# getAppCloneIdentity

## getAppCloneIdentity

```TypeScript
function getAppCloneIdentity(uid: number): Promise<AppCloneIdentity>
```

根据uid查询分身应用的包名和分身索引。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getAppCloneIdentity(uid: int): Promise<AppCloneIdentity>--><!--Device-bundleManager-function getAppCloneIdentity(uid: int): Promise<AppCloneIdentity>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;AppCloneIdentity & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700021](../errorcode-bundle.md#17700021-指定的uid无效) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005;

try {
  bundleManager.getAppCloneIdentity(uid).then((res) => {
    hilog.info(0x0000, 'testTag', 'getAppCloneIdentity res = %{public}s', JSON.stringify(res));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneIdentity failed. Cause: %{public}s', message);
}
```
