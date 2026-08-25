# getAllBundleCacheSize（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAllBundleCacheSize

```TypeScript
function getAllBundleCacheSize(): Promise<number>
```

获取全局缓存大小，单位：字节。使用Promise异步回调。有程序运行时的应用的缓存、或者在[应用配置指南](../../../../device-dev/subsystems/subsys-app-privilege-config-guide.md)中已配置“ AllowAppDataNotCleared”特权的应用的缓存，无法被获取。

**起始版本：** 15

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
