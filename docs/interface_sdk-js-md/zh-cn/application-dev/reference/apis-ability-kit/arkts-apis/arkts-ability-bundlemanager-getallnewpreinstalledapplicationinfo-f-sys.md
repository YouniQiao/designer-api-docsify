# getAllNewPreinstalledApplicationInfo（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllNewPreinstalledApplicationInfo

```TypeScript
function getAllNewPreinstalledApplicationInfo(): Promise<Array<PreinstalledApplicationInfo>>
```

获取设备OTA升级期间当前用户下新增的所有预置应用信息。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

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
