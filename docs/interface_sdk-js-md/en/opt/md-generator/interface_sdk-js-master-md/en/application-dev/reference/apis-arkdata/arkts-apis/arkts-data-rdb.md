# @ohos.data.rdb

The relational database (RDB) manages data based on relational models. With the underlying SQLite database, the RDB provides a complete mechanism for managing local databases. To satisfy different needs in complicated scenarios, the RDB offers a series of methods for performing operations such as adding, deleting, modifying, and querying data, and supports direct execution of SQL statements. The worker threads are not supported. This module provides the following RDB-related functions: - [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md#RdbPredicates): provides APIs for creating predicates. The predicates represent the properties, characteristics, or relationships between data entities in an RDB store and are used to define data operation conditions. - [RdbStore](arkts-arkdata-rdb-rdbstore-i.md#RdbStore): provides APIs for managing data in an RDB store.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [relationalStore](arkts-data-relationalstore.md#@ohos.data.relationalStore)

<!--Device-unnamed-declare namespace rdb--><!--Device-unnamed-declare namespace rdb-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [deleteRdbStore](arkts-arkdata-rdb-deleterdbstore-f.md#deleteRdbStore) |
| [deleteRdbStore](arkts-arkdata-rdb-deleterdbstore-f.md#deleteRdbStore) |
| [getRdbStore](arkts-arkdata-rdb-getrdbstore-f.md#getRdbStore) |
| [getRdbStore](arkts-arkdata-rdb-getrdbstore-f.md#getRdbStore) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RdbStore](arkts-arkdata-rdb-rdbstore-i.md) |
| [StoreConfig](arkts-arkdata-rdb-storeconfig-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SubscribeType](arkts-arkdata-rdb-subscribetype-e.md) |
| [SyncMode](arkts-arkdata-rdb-syncmode-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ResultSet](arkts-arkdata-rdb-resultset-t.md) |
| [ValueType](arkts-arkdata-rdb-valuetype-t.md) |
| [ValuesBucket](arkts-arkdata-rdb-valuesbucket-t.md) |
