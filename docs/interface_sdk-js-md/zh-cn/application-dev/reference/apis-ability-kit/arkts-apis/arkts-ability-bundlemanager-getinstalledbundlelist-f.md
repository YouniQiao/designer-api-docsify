# getInstalledBundleList

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getInstalledBundleList

```TypeScript
function getInstalledBundleList(bundleFlags: number): Promise<Array<BundleInfo>>
```

根据给定的bundleFlags获取系统中所有的BundleInfo。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_GET_INSTALLED_BUNDLE_LIST

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleFlags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;BundleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
