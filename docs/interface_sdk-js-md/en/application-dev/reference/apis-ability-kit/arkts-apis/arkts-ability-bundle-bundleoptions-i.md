# BundleOptions

> **NOTE：**> > This API has been supported since API version 7 and deprecated since API version 9. No substitute is provided. Options that contain the user ID.

**Since:** 7

**Deprecated since:** 9

<!--Device-bundle-export interface BundleOptions--><!--Device-bundle-export interface BundleOptions-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
import { appControl } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { bundleMonitor } from '@kit.AbilityKit';
import { bundleMonitor } from '@kit.AbilityKit';
import { bundleResourceManager } from '@kit.AbilityKit';
import { bundleResourceManager } from '@kit.AbilityKit';
import { bundle } from '@kit.AbilityKit';
import { defaultAppManager } from '@kit.AbilityKit';
import { defaultAppManager } from '@kit.AbilityKit';
import { distributedBundleManager } from '@kit.AbilityKit';
import { distributedBundleManager } from '@kit.AbilityKit';
import { freeInstall } from '@kit.AbilityKit';
import { freeInstall } from '@kit.AbilityKit';
import { innerBundleManager, BundleStatusCallback } from '@kit.AbilityKit';
import { installer } from '@kit.AbilityKit';
import { installer } from '@kit.AbilityKit';
import { launcherBundleManager } from '@kit.AbilityKit';
import { launcherBundleManager } from '@kit.AbilityKit';
import { overlay } from '@kit.AbilityKit';
import { overlay } from '@kit.AbilityKit';
import { shortcutManager } from '@kit.AbilityKit';
import { shortcutManager } from '@kit.AbilityKit';
import { skillManager } from '@kit.AbilityKit';
import { appDomainVerify } from '@kit.AbilityKit';
import { pluginBundleManager } from '@kit.AbilityKit';
import { pluginBundleManager } from '@kit.AbilityKit';
```

## userId

```TypeScript
userId?: number
```

User ID. The default value is the user ID of the caller. The value must be greater than or equal to 0.

**Type:** number

**Since:** 7

**Deprecated since:** 9

<!--Device-BundleOptions-userId?: number--><!--Device-BundleOptions-userId?: number-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

