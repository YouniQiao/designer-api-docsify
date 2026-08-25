# getAllPluginInfo（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllPluginInfo

```TypeScript
function getAllPluginInfo(hostBundleName: string, userId?: number): Promise<Array<PluginBundleInfo>>
```

根据给定的hostBundleName和userId获取所有的PluginBundleInfo。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;PluginBundleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
