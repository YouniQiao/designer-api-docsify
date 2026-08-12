# @ohos.data.preferences(用户首选项)

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储采用键值对形式，键为字符串类型，值可为数字、字符串、布尔类型、数组、Uint8Array、object或bigint。

用户首选项的持久化文件存储在[preferencesDir](../../../application-models/application-context-stage.md#获取应用文件路径)路径下，创建preferences对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md#AreaMode)会影响文件的可读写状态，路径访问限制详见[应用文件目录与应用文件路径](../../../file-management/app-sandbox-directory.md#应用文件目录与应用文件路径)。

> **说明：**
> 
> 首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

**起始版本：** 9

<!--Device-unnamed-declare namespace preferences--><!--Device-unnamed-declare namespace preferences-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 汇总

### 函数

| 名称 |
| --- |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences-1) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences-2) |
| [deletePreferences](arkts-arkdata-preferences-deletepreferences-f.md#deletepreferences-3) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences-1) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences-2) |
| [getPreferences](arkts-arkdata-preferences-getpreferences-f.md#getpreferences-3) |
| [getPreferencesSync](arkts-arkdata-preferences-getpreferencessync-f.md#getpreferencessync) |
| [isStorageTypeSupported](arkts-arkdata-preferences-isstoragetypesupported-f.md#isstoragetypesupported) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache-1) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache-2) |
| [removePreferencesFromCache](arkts-arkdata-preferences-removepreferencesfromcache-f.md#removepreferencesfromcache-3) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removepreferencesfromcachesync) |
| [removePreferencesFromCacheSync](arkts-arkdata-preferences-removepreferencesfromcachesync-f.md#removepreferencesfromcachesync-1) |

### 接口

| 名称 |
| --- |
| [Options](arkts-arkdata-preferences-options-i.md) |
| [Preferences](arkts-arkdata-preferences-preferences-i.md) |

### 枚举

| 名称 |
| --- |
| [StorageType](arkts-arkdata-preferences-storagetype-e.md) |

### 类型

| 名称 |
| --- |
| [ValueType](arkts-arkdata-preferences-valuetype-t.md) |

### 常量

| 名称 |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-preferences-con.md#max_key_length) |
| [MAX_VALUE_LENGTH](arkts-arkdata-preferences-con.md#max_value_length) |
