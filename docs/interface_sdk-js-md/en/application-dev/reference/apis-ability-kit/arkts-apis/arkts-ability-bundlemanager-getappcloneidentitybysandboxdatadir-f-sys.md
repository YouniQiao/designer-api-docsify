# getAppCloneIdentityBySandboxDataDir (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAppCloneIdentityBySandboxDataDir

```TypeScript
function getAppCloneIdentityBySandboxDataDir(sandboxDataDir: string): AppCloneIdentity
```

Obtains the identity information of an application, including the bundle name and clone index, based on the given sandbox directory name.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sandboxDataDir | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AppCloneIdentity](arkts-ability-bundlemanager-appcloneidentity-t.md) |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Main application.
let dataDir = 'com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(dataDir);
  console.info('getAppCloneIdentityBySandboxDataDir successfully. res = ' + JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('getAppCloneIdentityBySandboxDataDir failed. Cause = ' + message);
}

// Application clone.
let cloneDataDir = '+clone-1+com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(cloneDataDir);
  console.info('getAppCloneIdentityBySandboxDataDir successfully. res = ' + JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('getAppCloneIdentityBySandboxDataDir failed. Cause = ' + message);
}

// Atomic service.
let atomicDataDir = '+auid-20000000+com.example.myapplication';
try {
  let res = bundleManager.getAppCloneIdentityBySandboxDataDir(atomicDataDir);
  console.info('getAppCloneIdentityBySandboxDataDir successfully. res = ' + JSON.stringify(res));
} catch (err) {
  let message = (err as BusinessError).message;
  console.error('getAppCloneIdentityBySandboxDataDir failed. Cause = ' + message);
}
```
