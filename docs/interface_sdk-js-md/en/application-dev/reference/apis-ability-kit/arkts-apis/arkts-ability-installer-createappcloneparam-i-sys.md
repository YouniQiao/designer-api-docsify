# CreateAppCloneParam (System API)

Describes the parameters used for creating an application clone.

**Since:** 23

<!--Device-installer-export interface CreateAppCloneParam--><!--Device-installer-export interface CreateAppCloneParam-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { installer } from '@kit.AbilityKit';
```

## appIndex

```TypeScript
appIndex?: int
```

Index of the clone. The default value is the currently available minimum index.

**Type:** int

**Since:** 23

<!--Device-CreateAppCloneParam-appIndex?: int--><!--Device-CreateAppCloneParam-appIndex?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

ID of the user for whom the clone is to be created. You can obtain the user ID by calling [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid). The default value is the user ID of the caller.

**Type:** int

**Since:** 23

<!--Device-CreateAppCloneParam-userId?: int--><!--Device-CreateAppCloneParam-userId?: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

