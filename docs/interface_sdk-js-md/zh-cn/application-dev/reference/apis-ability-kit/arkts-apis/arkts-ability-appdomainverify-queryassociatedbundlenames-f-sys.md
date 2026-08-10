# queryAssociatedBundleNames（系统接口）

## 导入模块

```TypeScript
import { appDomainVerify } from 'kits/@kit.AbilityKit';
```

## queryAssociatedBundleNames

```TypeScript
function queryAssociatedBundleNames(domain: string): string[]
```

query bundleNames associated with domain.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_APP_DOMAIN_BUNDLE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-appDomainVerify-function queryAssociatedBundleNames(domain: string): string[]--><!--Device-appDomainVerify-function queryAssociatedBundleNames(domain: string): string[]-End-->

**系统能力：** SystemCapability.BundleManager.AppDomainVerify

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | string | 是 | Parameters related to the function. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | Result bundleNames. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 29900001 | Internal error. |
| 202 | System API accessed by non-system app. |

## 示例

```TypeScript
import { appDomainVerify } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 获取域名"example.com"应用所关联的包名列表
let domain = "example.com";
let bundleNames = appDomainVerify.queryAssociatedBundleNames(domain);
bundleNames.forEach(bundleName => {
  hilog.info(0x0000, 'testTag', `domain:${domain} associate with app:${bundleName}`);
});
```

