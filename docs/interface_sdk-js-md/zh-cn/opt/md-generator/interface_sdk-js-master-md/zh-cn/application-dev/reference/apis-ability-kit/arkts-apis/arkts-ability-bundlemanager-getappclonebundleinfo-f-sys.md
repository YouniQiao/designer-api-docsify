# getAppCloneBundleInfo（系统接口）

## getAppCloneBundleInfo

```TypeScript
function getAppCloneBundleInfo(bundleName: string, appIndex: number, bundleFlags: number, userId?: number): Promise<BundleInfo>
```

根据bundleName、分身索引、[bundleFlags](arkts-ability-bundlemanager-bundleflag-e.md)以及用户ID查询主应用或分身应用的BundleInfo。使用Promise异步回调。

获取调用方自身的信息时不需要权限。

**起始版本：** 12

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAppCloneBundleInfo(bundleName: string, appIndex: int, bundleFlags: int, userId?: int): Promise<BundleInfo>--><!--Device-bundleManager-function getAppCloneBundleInfo(bundleName: string, appIndex: int, bundleFlags: int, userId?: int): Promise<BundleInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appIndex | number | 是 |
| bundleFlags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;BundleInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17700061](../errorcode-bundle.md#17700061-指定的应用分身索引无效) |
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
let appIndex = 1;
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE |
bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY;

try {
  bundleManager.getAppCloneBundleInfo(bundleName, appIndex, bundleFlags).then((res: bundleManager.BundleInfo) => {
    hilog.info(0x0000, 'testTag', 'getAppCloneBundleInfo res: BundleInfo = %{public}s', JSON.stringify(res));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAppCloneBundleInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneBundleInfo failed. Cause: %{public}s', message);
}
```
