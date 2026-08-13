# @ohos.data.sendablePreferences

共享用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。 数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括number、string、boolean、bigint以及可序列化的object。 共享用户首选项的持久化文件存储在[preferencesDir](../../../application-models/application-context-stage.md#获取应用文件路径)路径下，创建preferences 对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md#AreaMode)会影响文件的 可读写状态，路径访问限制详见[应用文件目录与应用文件路径](../../../file-management/app-sandbox-directory.md#应用文件目录与应用文件路径)。 共享用户首选项可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，性能优于普通的[用户首选项](arkts-data-preferences.md#@ohos.data.preferences) ，可参考[Sendable使用场景](../../../arkts-utils/sendable-guide.md)。 > **说明：** > > 共享用户首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare namespace sendablePreferences--><!--Device-unnamed-declare namespace sendablePreferences-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 汇总

### 函数

| 名称 |
| --- |
| [deletePreferences](arkts-arkdata-sendablepreferences-deletepreferences-f.md#deletePreferences) |
| [getPreferences](arkts-arkdata-sendablepreferences-getpreferences-f.md#getPreferences) |
| [getPreferencesSync](arkts-arkdata-sendablepreferences-getpreferencessync-f.md#getPreferencesSync) |
| [removePreferencesFromCache](arkts-arkdata-sendablepreferences-removepreferencesfromcache-f.md#removePreferencesFromCache) |
| [removePreferencesFromCacheSync](arkts-arkdata-sendablepreferences-removepreferencesfromcachesync-f.md#removePreferencesFromCacheSync) |

### 接口

| 名称 |
| --- |
| [Options](arkts-arkdata-sendablepreferences-options-i.md) |
| [Preferences](arkts-arkdata-sendablepreferences-preferences-i.md) |

### 常量

| 名称 |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-sendablepreferences-con.md#MAX_KEY_LENGTH) |
| [MAX_VALUE_LENGTH](arkts-arkdata-sendablepreferences-con.md#MAX_VALUE_LENGTH) |
