# getLaunchWant

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getLaunchWant

```TypeScript
function getLaunchWant(): Want
```

Obtains the **Want** parameters of the [entry UIAbility](../../../quick-start/application-package-glossary.md#uiability) of the current application.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Want](arkts-ability-app-ability-want-want-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [17700072](../errorcode-bundle.md#17700072-launch-want-does-not-exist) |
