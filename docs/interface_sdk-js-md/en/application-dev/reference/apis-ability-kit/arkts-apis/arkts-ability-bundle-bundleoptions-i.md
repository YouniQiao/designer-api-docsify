# BundleOptions


> **NOTE：**
> 
> This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided.
Options that contain the user ID.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

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

User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0.

**Type:** number

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.BundleManager.BundleFramework
