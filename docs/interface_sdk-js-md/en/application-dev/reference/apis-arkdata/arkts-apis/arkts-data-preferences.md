# @ohos.data.preferences

The **Preferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs. The key is of string type, and the value can be a number, string, boolean value, or an array of numbers, strings, or boolean values. The user preference persistent files are stored in the [preferencesDir](../../../application-models/application-context-stage.md#obtaining-application-file-paths) directory. Before creating a preferences object, ensure that the **preferencesDir** directory is readable and writeable. The [encryption level](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md) of the persistent file directory determines the access to the files. For details, see [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path).

> **NOTE：**&gt;
> Preferences are not thread-safe and may cause file damage and data loss when used in multi-process scenarios. Do
> not use preferences in multi-process scenarios.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { preferences } from 'kits/@kit.ArkData';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md) |
| [getPreferencesSync](arkts-arkdata-preferences-getpreferencessync-f.md) |
| [isStorageTypeSupported](arkts-arkdata-preferences-isstoragetypesupported-f.md) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md) |

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
| [ValueType](arkts-arkdata-preferences-valuetype-t.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-preferences-con.md#max_key_length) |
| [MAX_VALUE_LENGTH](arkts-arkdata-preferences-con.md#max_value_length) |
