# @ohos.data.sendablePreferences

The **sendablePreferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs.In the KV pairs, the key must be a string, and the value can be a number, a string, a Boolean value, a bigint, or a serializable object.The persistent files of the shared user preferences are stored in the   
[preferencesDir](../../../application-models/application-context-stage.md#obtaining-application-file-paths) directory. Before creating a preferences object, ensure that the **preferencesDir** path can be read and written. The  
[encryption level](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md/arkts-ability-contextconstant-areamode-e.md) of the persistent file directory determines the access to the files. For details, see   
[Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path).Sendable preferences can be passed between concurrent ArkTS instances (including the main thread and TaskPool or Worker threads) by reference. It allows for higher performance than   
[user preferences](arkts-data-preferences.md). For more information, see   
[Using Sendable Objects](../../../arkts-utils/sendable-guide.md).

> **NOTE：**
> 
> The shared user preferences are not thread-safe and may cause file damage and data loss when used in multi-process
> scenarios. Do not use it in multi-process scenarios.

**Since:** 12

<!--Device-unnamed-declare namespace sendablePreferences--><!--Device-unnamed-declare namespace sendablePreferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { sendablePreferences } from 'kits/@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deletePreferences](arkts-arkdata-sendablepreferences-deletepreferences-f.md#deletepreferences) |
| [getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md#getpreferences) |
| [getPreferencesSync](arkts-arkdata-sendablepreferences-getpreferencessync-f.md#getpreferencessync) |
| [removePreferencesFromCache](arkts-arkdata-sendablepreferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCacheSync](arkts-arkdata-sendablepreferences-removepreferencesfromcachesync-f.md#removepreferencesfromcachesync) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Options](arkts-arkdata-sendablepreferences-options-i.md) |
| [Preferences](arkts-arkdata-sendablepreferences-preferences-i.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-sendablepreferences-con.md#max_key_length) |
| [MAX_VALUE_LENGTH](arkts-arkdata-sendablepreferences-con.md#max_value_length) |
