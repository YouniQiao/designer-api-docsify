# getAllPreinstalledApplicationInfo（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllPreinstalledApplicationInfo

```TypeScript
function getAllPreinstalledApplicationInfo(): Promise<Array<PreinstalledApplicationInfo>>
```

获取所有预置应用信息。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;PreinstalledApplicationInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
