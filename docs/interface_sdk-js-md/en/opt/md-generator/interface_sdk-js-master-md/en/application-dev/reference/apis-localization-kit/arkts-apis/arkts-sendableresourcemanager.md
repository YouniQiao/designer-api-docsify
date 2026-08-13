# @ohos.sendableResourceManager

This module provides the mutual conversion between [Resource](arkts-localization-sendableresourcemanager-resource-t.md#Resource) objects and [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md#SendableResource) objects. `SendableResource` implements the [ISendable](../../../arkts-utils/arkts-sendable.md#isendable) API and supports cross-thread transmission. After cross-thread transmission, the `SendableResource` object can be converted back to a `Resource` object and passed as a parameter to the [resource management](arkts-resourcemanager.md#@ohos.resourceManager) APIs to obtain resources.

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sendableResourceManager--><!--Device-unnamed-declare namespace sendableResourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { sendableResourceManager } from '@kit.LocalizationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [resourceToSendableResource](arkts-localization-sendableresourcemanager-resourcetosendableresource-f.md#resourceToSendableResource) |
| [sendableResourceToResource](arkts-localization-sendableresourcemanager-sendableresourcetoresource-f.md#sendableResourceToResource) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Resource](arkts-localization-sendableresourcemanager-resource-t.md) |
| [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) |
