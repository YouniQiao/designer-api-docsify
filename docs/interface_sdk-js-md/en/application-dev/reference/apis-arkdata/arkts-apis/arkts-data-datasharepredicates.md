# @ohos.data.dataSharePredicates

DataSharePredicates** provides a filter object to query data in a database by using **DataShare** APIs. It is often used to update, delete, and query data.

The APIs provided by **DataSharePredicates** correspond to the filter criteria of the database. Before using the APIs, you need to have basic database knowledge.

**DataSharePredicates** applies to the following scenario:

- It is used as a search criterion in the media file management service. For details, see  
[FetchOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ in the fetch options of the album management. In this scenario, you do not need to pay attention to the database type.

\_\_\_MD\_COMMENT\_DESC\_USD\_3\_\_\_

- It is used as a search criterion when APIs of the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ and  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ are called. In this scenario, use the corresponding predicate based on the database type.

\_\_\_MD\_COMMENT\_DESC\_USD\_4\_\_\_

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace dataSharePredicates--><!--Device-unnamed-declare namespace dataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

## Summary

### Classes

| Name | Description |
| --- | --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) | Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a  **DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for it. |

