# getExtResource（系统接口）

## 导入模块

```TypeScript
```

## getExtResource

```TypeScript
function getExtResource(bundleName: string): Promise<Array<string>>
```

根据给定的bundleName获得扩展资源对应的moduleNames。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getExtResource(bundleName: string): Promise<Array<string>>--><!--Device-bundleManager-function getExtResource(bundleName: string): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700303](../errorcode-bundle.md#17700303-扩展资源查询失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

**示例**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName: string = 'com.ohos.demo';

try {
  bundleManager.getExtResource(bundleName).then((modules: Array<string>) => {
    for (let i = 0; i < modules.length; i++) {
      hilog.info(0x0000, 'testTag', 'getExtResource item: %{public}s', modules[i]);
    }
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getExtResource failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getExtResource failed. Cause: %{public}s', message);
}
```
