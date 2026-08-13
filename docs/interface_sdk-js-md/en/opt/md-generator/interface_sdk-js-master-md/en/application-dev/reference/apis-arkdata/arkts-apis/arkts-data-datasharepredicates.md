# @ohos.data.dataSharePredicates

**DataSharePredicates** provides a filter object to query data in a database by using **DataShare** APIs. It is often used to update, delete, and query data. The APIs provided by **DataSharePredicates** correspond to the filter criteria of the database. Before using the APIs , you need to have basic database knowledge. **DataSharePredicates** applies to the following scenario: - It is used as a search criterion in the media file management service. For details, see [FetchOptions](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-fetchoptions-i.md#FetchOptions) in the fetch options of the album management. In this scenario, you do not need to pay attention to the database type. &lt;!--Del--&gt; - It is used as a search criterion when APIs of the RDB store and KV store are called. In this scenario, use the corresponding predicate based on the database type. &lt;!--DelEnd--&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dataSharePredicates--><!--Device-unnamed-declare namespace dataSharePredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c.md) |

<!--Del-->
### Classes（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataSharePredicates](arkts-arkdata-datasharepredicates-datasharepredicates-c-sys.md) |
<!--DelEnd-->
