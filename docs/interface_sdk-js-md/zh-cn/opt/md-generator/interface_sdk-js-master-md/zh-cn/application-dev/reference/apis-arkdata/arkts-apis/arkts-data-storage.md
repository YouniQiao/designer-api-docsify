# @ohos.data.storage

轻量级存储为应用提供key-value键值型的文件数据处理能力，支持应用对数据进行轻量级存储及查询。 数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括数字型、字符串型、布尔型。 > **说明：**> - 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 > - 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.preferences](arkts-data-preferences.md#@ohos.data.preferences).

**起始版本：** 6

**废弃版本：** 9

**替代接口：** preferences

<!--Device-unnamed-declare namespace storage--><!--Device-unnamed-declare namespace storage-End-->

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

## 汇总

### 函数

| 名称 |
| --- |
| [deleteStorage](arkts-arkdata-storage-deletestorage-f.md#deleteStorage) |
| [deleteStorage](arkts-arkdata-storage-deletestorage-f.md#deleteStorage) |
| [deleteStorageSync](arkts-arkdata-storage-deletestoragesync-f.md#deleteStorageSync) |
| [getStorage](arkts-arkdata-storage-getstorage-f.md#getStorage) |
| [getStorage](arkts-arkdata-storage-getstorage-f.md#getStorage) |
| [getStorageSync](arkts-arkdata-storage-getstoragesync-f.md#getStorageSync) |
| [removeStorageFromCache](arkts-arkdata-storage-removestoragefromcache-f.md#removeStorageFromCache) |
| [removeStorageFromCache](arkts-arkdata-storage-removestoragefromcache-f.md#removeStorageFromCache) |
| [removeStorageFromCacheSync](arkts-arkdata-storage-removestoragefromcachesync-f.md#removeStorageFromCacheSync) |

### 接口

| 名称 |
| --- |
| [Storage](arkts-arkdata-storage-storage-i.md) |
| [StorageObserver](arkts-arkdata-storage-storageobserver-i.md) |

### 类型

| 名称 |
| --- |
| [ValueType](arkts-arkdata-storage-valuetype-t.md) |

### 常量

| 名称 |
| --- |
| [MAX_KEY_LENGTH](arkts-arkdata-storage-con.md#MAX_KEY_LENGTH) |
| [MAX_VALUE_LENGTH](arkts-arkdata-storage-con.md#MAX_VALUE_LENGTH) |
