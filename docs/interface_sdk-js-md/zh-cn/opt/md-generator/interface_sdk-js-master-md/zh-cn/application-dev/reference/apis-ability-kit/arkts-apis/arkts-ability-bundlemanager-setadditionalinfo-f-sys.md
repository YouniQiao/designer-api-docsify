# setAdditionalInfo（系统接口）

## setAdditionalInfo

```TypeScript
function setAdditionalInfo(bundleName: string, additionalInfo: string): void
```

设置指定应用的额外信息。此接口仅供应用市场调用。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function setAdditionalInfo(bundleName: string, additionalInfo: string): void--><!--Device-bundleManager-function setAdditionalInfo(bundleName: string, additionalInfo: string): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| additionalInfo | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700053](../errorcode-bundle.md#17700053-非应用市场调用) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let additionalInfo = "xxxxxxxxx,formUpdateLevel:4";

try {
  bundleManager.setAdditionalInfo(bundleName, additionalInfo);
  hilog.info(0x0000, 'testTag', 'setAdditionalInfo successfully.');
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'setAdditionalInfo failed. Cause: %{public}s', message);
}
```
