# getBundleInfoForSelfSync

## getBundleInfoForSelfSync

```TypeScript
function getBundleInfoForSelfSync(bundleFlags: number): BundleInfo
```

以同步方法根据给定的bundleFlags获取当前应用的BundleInfo。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-bundleManager-function getBundleInfoForSelfSync(bundleFlags: int): BundleInfo--><!--Device-bundleManager-function getBundleInfoForSelfSync(bundleFlags: int): BundleInfo-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;

try {
  let data = bundleManager.getBundleInfoForSelfSync(bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoForSelfSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelfSync failed: %{public}s', message);
}
```
