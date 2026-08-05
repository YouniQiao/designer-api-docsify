# @ohos.data.sendableRelationalStore

The **sendableRelationalStore** module provides APIs for obtaining **ValuesBucket** of the sendable type from the query result set and transferring it between concurrent instances.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare namespace sendableRelationalStore--><!--Device-unnamed-declare namespace sendableRelationalStore-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [fromSendableAsset](arkts-arkdata-sendablerelationalstore-fromsendableasset-f.md#fromsendableasset) | Converts the asset data that can be passed across threads into the data that cannot be passed across threads. |
| [fromSendableValues](arkts-arkdata-sendablerelationalstore-fromsendablevalues-f.md#fromsendablevalues) | Converts the array data that can be passed across threads into the data that cannot be passed across threads. |
| [fromSendableValuesBucket](arkts-arkdata-sendablerelationalstore-fromsendablevaluesbucket-f.md#fromsendablevaluesbucket) | Converts a KV pair that can be passed across threads into the data that cannot be passed across threads. |
| [toSendableAsset](arkts-arkdata-sendablerelationalstore-tosendableasset-f.md#tosendableasset) | Converts the asset data that cannot be passed across threads into the data that can be passed across threads. |
| [toSendableValues](arkts-arkdata-sendablerelationalstore-tosendablevalues-f.md#tosendablevalues) | Converts the array data that cannot be passed across threads into the data that can be passed across threads. |
| [toSendableValuesBucket](arkts-arkdata-sendablerelationalstore-tosendablevaluesbucket-f.md#tosendablevaluesbucket) | Converts a key-value (KV) pair that cannot be passed across threads into the data that can be passed across threads. |

### Interfaces

| Name | Description |
| --- | --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) | Represent the asset (such as a document, image, or video). **Asset** inherits from [lang.ISendable]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and is used to implement cross-thread transfer of asset data. The asset data does not support **Datashare** APIs. Use [sendableRelationalStore.toSendableAsset]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to create an **Asset** instance. |

### Types

| Name | Description |
| --- | --- |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) | Represent an array of [Assets]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, which allows assets to be passed across threads. |
| [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | Represents the asset (such as a document, image, or video) that cannot be passed across threads. |
| [NonSendableBucket](arkts-arkdata-sendablerelationalstore-nonsendablebucket-t.md) | Represents the KV pair that cannot be passed across threads. |
| [NonSendableValues](arkts-arkdata-sendablerelationalstore-nonsendablevalues-t.md) | Represents the [ValueType]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ array that cannot be passed across threads. |
| [ValueType](arkts-arkdata-sendablerelationalstore-valuetype-t.md) | Defines the types of the value in a KV pair. The type varies with the parameter function. |
| [ValuesBucket](arkts-arkdata-sendablerelationalstore-valuesbucket-t.md) | Represents the KV pair of the [ValueType]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ data that can be passed across threads. |

