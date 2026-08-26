# BundleOptions


> **说明：**
> 
> 从API version 7开始支持，从API version 9开始废弃，暂无替代接口。
查询选项，包含userId。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework

## 导入模块

```TypeScript
import appControl from '@kit.AbilityKit.appControl';
import bundleManager from '@kit.AbilityKit.bundleManager';
import bundleMonitor from '@kit.AbilityKit.bundleMonitor';
import bundleResourceManager from '@kit.AbilityKit.bundleResourceManager';
import bundle from '@kit.AbilityKit';
import defaultAppManager from '@kit.AbilityKit.defaultAppManager';
import distributedBundleManager from '@kit.AbilityKit.distributedBundleManager';
import freeInstall from '@kit.AbilityKit.freeInstall';
import innerBundleManager, { BundleStatusCallback } from '@kit.AbilityKit.innerBundleManager';
import installer from '@kit.AbilityKit.installer';
import launcherBundleManager from '@kit.AbilityKit.launcherBundleManager';
import overlay from '@kit.AbilityKit.overlay';
import shortcutManager from '@kit.AbilityKit.shortcutManager';
import skillManager from '@kit.AbilityKit.skillManager';
import appDomainVerify from '@kit.AbilityKit.appDomainVerify';
import pluginBundleManager from '@kit.AbilityKit.pluginBundleManager';
```

## userId

```TypeScript
userId?: number
```

用户ID。默认值：调用方所在用户，取值范围：大于等于0。

**类型：** number

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.BundleManager.BundleFramework
