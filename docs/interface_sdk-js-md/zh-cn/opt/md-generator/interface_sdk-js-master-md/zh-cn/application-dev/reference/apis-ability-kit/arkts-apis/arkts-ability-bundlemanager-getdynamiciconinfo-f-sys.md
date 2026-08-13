# getDynamicIconInfo（系统接口）

## getDynamicIconInfo

```TypeScript
function getDynamicIconInfo(bundleName: string): Promise<Array<DynamicIconInfo>>
```

根据指定的bundleName获取所有用户和所有分身下的动态图标信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-bundleManager-function getDynamicIconInfo(bundleName: string): Promise<Array<DynamicIconInfo>>--><!--Device-bundleManager-function getDynamicIconInfo(bundleName: string): Promise<Array<DynamicIconInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;DynamicIconInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700306](../errorcode-bundle.md#17700306-动态图标查询失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName: string = 'com.ohos.demo';

try {
  bundleManager.getDynamicIconInfo(bundleName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getDynamicIconInfo successfully %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getDynamicIconInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getDynamicIconInfo failed. Cause: %{public}s', message);
}
```
