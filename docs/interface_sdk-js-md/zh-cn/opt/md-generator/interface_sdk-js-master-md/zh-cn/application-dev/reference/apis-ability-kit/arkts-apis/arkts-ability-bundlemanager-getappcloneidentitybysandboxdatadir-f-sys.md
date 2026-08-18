# getAppCloneIdentityBySandboxDataDir（系统接口）

## 导入模块

```TypeScript
```

## getAppCloneIdentityBySandboxDataDir

```TypeScript
function getAppCloneIdentityBySandboxDataDir(sandboxDataDir: string): AppCloneIdentity
```

根据应用的沙箱目录名称获取应用的身份信息，包括应用包名和分身索引信息。

**起始版本：** 23

<!--Device-bundleManager-function getAppCloneIdentityBySandboxDataDir(sandboxDataDir: string): AppCloneIdentity--><!--Device-bundleManager-function getAppCloneIdentityBySandboxDataDir(sandboxDataDir: string): AppCloneIdentity-End-->

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

**示例**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 主应用
let dataDir = 'com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(dataDir);
  hilog.info(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir successfully. res:%{public}s',
    JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir failed. Cause: %{public}s',
    message);
}

// 分身应用
let cloneDataDir = '+clone-1+com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(cloneDataDir);
  hilog.info(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir successfully. res:%{public}s',
    JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir failed. Cause: %{public}s',
    message);
}

// 原子化服务
let atomicDataDir = '+auid-20000000+com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(atomicDataDir);
  hilog.info(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir successfully. res:%{public}s',
    JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppCloneIdentityBySandboxDataDir failed. Cause: %{public}s',
    message);
}
```
