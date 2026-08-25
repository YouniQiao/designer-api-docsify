# @ohos.sendableResourceManager(Resource Manager)

This module provides the mutual conversion between [Resource](arkts-localization-sendableresourcemanager-resource-t.md) objects and [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) objects. `SendableResource` implements the [ISendable](../../../arkts-utils/arkts-sendable.md#isendable) API and supports cross-thread transmission. After cross-thread transmission, the `SendableResource` object can be converted back to a `Resource` object and passed as a parameter to the [resource management](arkts-resourcemanager.md) APIs to obtain resources.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { sendableResourceManager } from '@kit.LocalizationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [resourceToSendableResource(Resource Manager)](arkts-localization-sendableresourcemanager-resourcetosendableresource-f.md) |
| [sendableResourceToResource(Resource Manager)](arkts-localization-sendableresourcemanager-sendableresourcetoresource-f.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Resource(Resource Manager)](arkts-localization-sendableresourcemanager-resource-t.md) |
| [SendableResource(Resource Manager)](arkts-localization-sendableresourcemanager-sendableresource-t.md) |
