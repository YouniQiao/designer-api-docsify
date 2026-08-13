# canOpenLink

## canOpenLink

```TypeScript
function canOpenLink(link: string): boolean
```

根据给定的链接判断目标应用是否可访问，链接中的scheme需要在[module.json5文件](../../../quick-start/module-configuration-file.md)的querySchemes字段 下配置。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-bundleManager-function canOpenLink(link: string): boolean--><!--Device-bundleManager-function canOpenLink(link: string): boolean-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| link | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [17700056](../errorcode-bundle.md#17700056-指定link的scheme未在queryschemes字段下配置) |
| [17700055](../errorcode-bundle.md#17700055-指定的link无效) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let link = 'welink://';
  let data = bundleManager.canOpenLink(link);
  hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
}
```
