# @ohos.sendableResourceManager

This module provides the mutual conversion between [Resource]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ objects and [SendableResource]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_ objects. \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ implements the \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ API and supports cross-thread transmission. After cross-thread transmission, the \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ object can be converted back to a \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ object and passed as a parameter to the [resource management]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_ APIs to obtain resources.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare namespace sendableResourceManager--><!--Device-unnamed-declare namespace sendableResourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Summary

### Functions

| Name | Description |
| --- | --- |
| [resourceToSendableResource](arkts-localization-sendableresourcemanager-resourcetosendableresource-f.md#resourcetosendableresource) | Converts a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object to a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object that can be used for cross-thread transmission. |
| [sendableResourceToResource](arkts-localization-sendableresourcemanager-sendableresourcetoresource-f.md#sendableresourcetoresource) | Converts a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object transmitted across threads to a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_INLINE\_\_\_ESCAPED\_UNDERSCORE\_\_\_CODE\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ object. |

### Types

| Name | Description |
| --- | --- |
| [Resource](arkts-localization-sendableresourcemanager-resource-t.md) | Represents resource-related information, including the application bundle name, application module name, resource ID, resource type, and other resource parameters. |
| [SendableResource](arkts-localization-sendableresourcemanager-sendableresource-t.md) | Represents Sendable resource-related information for cross-thread transmission, including the application bundle name, application module name, resource ID, resource type, and other resource parameters. |

