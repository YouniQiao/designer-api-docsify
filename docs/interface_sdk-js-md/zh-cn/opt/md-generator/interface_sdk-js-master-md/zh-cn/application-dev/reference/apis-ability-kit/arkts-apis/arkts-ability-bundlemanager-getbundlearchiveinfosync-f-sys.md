# getBundleArchiveInfoSync（系统接口）

## getBundleArchiveInfoSync

```TypeScript
function getBundleArchiveInfoSync(hapFilePath: string, bundleFlags: number): BundleInfo
```

以同步方法根据给定的hapFilePath和bundleFlags获取BundleInfo对象。

**起始版本：** 10

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getBundleArchiveInfoSync(hapFilePath: string, bundleFlags: int): BundleInfo--><!--Device-bundleManager-function getBundleArchiveInfoSync(hapFilePath: string, bundleFlags: int): BundleInfo-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hapFilePath | string | 是 |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [17700022](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700022-输入的待解析源文件无效) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let hapFilePath = "/data/xxx/test.hap";
let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT;

try {
  let data = bundleManager.getBundleArchiveInfoSync(hapFilePath, bundleFlags)
  hilog.info(0x0000, 'testTag', 'getBundleArchiveInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleArchiveInfoSync failed. Cause: %{public}s', message);
}
```
