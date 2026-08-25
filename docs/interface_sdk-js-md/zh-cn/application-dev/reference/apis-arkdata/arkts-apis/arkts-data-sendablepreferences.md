# @ohos.data.sendablePreferences(共享用户首选项)

共享用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括number、string、boolean、bigint以及可序列化的object。共享用户首选项的持久化文件存储在[preferencesDir](../../../application-models/application-context-stage.md#获取应用文件路径)路径下，创建preferences 对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](../../apis-ability-kit/arkts-apis/arkts-ability-contextconstant-areamode-e.md)会影响文件的 可读写状态，路径访问限制详见[应用文件目录与应用文件路径](../../../file-management/app-sandbox-directory.md#应用文件目录与应用文件路径)。共享用户首选项可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，性能优于普通的[用户首选项](arkts-data-preferences.md) ，可参考[Sendable使用场景](../../../arkts-utils/sendable-guide.md)。

> **说明：**&gt;
> 共享用户首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 导入模块

```TypeScript
import { sendablePreferences } from '@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [deletePreferences(共享用户首选项)](arkts-arkdata-sendablepreferences-deletepreferences-f.md) |
| [getPreferences(共享用户首选项)](arkts-arkdata-sendablepreferences-getpreferences-f.md) |
| [getPreferencesSync(共享用户首选项)](arkts-arkdata-sendablepreferences-getpreferencessync-f.md) |
| [removePreferencesFromCache(共享用户首选项)](arkts-arkdata-sendablepreferences-removepreferencesfromcache-f.md) |
| [removePreferencesFromCacheSync(共享用户首选项)](arkts-arkdata-sendablepreferences-removepreferencesfromcachesync-f.md) |

### 接口

| 名称 |
| --- |
| [Options(共享用户首选项)](arkts-arkdata-sendablepreferences-options-i.md) |
| [Preferences(共享用户首选项)](arkts-arkdata-sendablepreferences-preferences-i.md) |

### 常量

| 名称 |
| --- |
| [MAX_KEY_LENGTH(共享用户首选项)](arkts-arkdata-sendablepreferences-con.md#max_key_length) |
| [MAX_VALUE_LENGTH(共享用户首选项)](arkts-arkdata-sendablepreferences-con.md#max_value_length) |
