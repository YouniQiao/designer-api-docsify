# getAppCloneIdentityBySandboxDataDir（系统接口）

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAppCloneIdentityBySandboxDataDir

```TypeScript
function getAppCloneIdentityBySandboxDataDir(sandboxDataDir: string): AppCloneIdentity
```

根据应用的沙箱目录名称获取应用的身份信息，包括应用包名和分身索引信息。

**起始版本：** 20

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sandboxDataDir | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AppCloneIdentity](arkts-ability-bundlemanager-appcloneidentity-t.md) |
