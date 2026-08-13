# @ohos.data.preferences

The **Preferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs. The key is of string type, and the value can be a number, string, boolean value, or an array of numbers, strings, or boolean values. The user preference persistent files are stored in the [preferencesDir](../../../application-models/application-context-stage.md#obtaining-application-file-paths) directory. Before creating a preferences object, ensure that the **preferencesDir** directory is readable and writeable. The [encryption level](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md#AreaMode) of the persistent file directory determines the access to the files. For details, see [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path) . > **NOTE：**> > Preferences are not thread-safe and may cause file damage and data loss when used in multi-process scenarios. Do > not use preferences in multi-process scenarios.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace preferences--><!--Device-unnamed-declare namespace preferences-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { preferences } from '@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletePreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletePreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletePreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletePreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getPreferences) |
| [getPreferencesSync](arkts-arkdata-preferences-getpreferencessync-f.md#getPreferencesSync) |
| [isStorageTypeSupported](arkts-arkdata-preferences-isstoragetypesupported-f.md#isStorageTypeSupported) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removePreferencesFromCache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removePreferencesFromCache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removePreferencesFromCache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removePreferencesFromCache) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removePreferencesFromCacheSync) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removePreferencesFromCacheSync) |

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
| [MAX_KEY_LENGTH](arkts-arkdata-preferences-con.md#MAX_KEY_LENGTH) |
| [MAX_VALUE_LENGTH](arkts-arkdata-preferences-con.md#MAX_VALUE_LENGTH) |
