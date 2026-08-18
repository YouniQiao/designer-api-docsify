# @ohos.data.preferences

The **Preferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs. The key is of string type, and the value can be a number, string, boolean value, or an array of numbers, strings, or boolean values. The user preference persistent files are stored in the [preferencesDir](../../../application-models/application-context-stage.md#obtaining-application-file-paths) directory. Before creating a preferences object, ensure that the **preferencesDir** directory is readable and writeable. The [encryption level](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md#areamode) of the persistent file directory determines the access to the files. For details, see [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path) . > **NOTE：**> > Preferences are not thread-safe and may cause file damage and data loss when used in multi-process scenarios. Do > not use preferences in multi-process scenarios.

**Since:** 23

<!--Device-unnamed-declare namespace preferences--><!--Device-unnamed-declare namespace preferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences) |
| [getPreferencesSync](arkts-arkdata-preferences-getpreferencessync-f.md#getpreferencessync) |
| [isStorageTypeSupported](arkts-arkdata-preferences-isstoragetypesupported-f.md#isstoragetypesupported) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removepreferencesfromcachesync) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removepreferencesfromcachesync) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Options](arkts-arkdata-preferences-options-i.md) |
| [Preferences](arkts-arkdata-preferences-preferences-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [StorageType](arkts-arkdata-preferences-storagetype-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RecordData](arkts-arkdata-preferences-recorddata-t.md) |
| [ValueType](arkts-arkdata-preferences-valuetype-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-preferences-con.md#maxkeylength) |
| [MAX_VALUE_LENGTH](arkts-arkdata-preferences-con.md#maxvaluelength) |
