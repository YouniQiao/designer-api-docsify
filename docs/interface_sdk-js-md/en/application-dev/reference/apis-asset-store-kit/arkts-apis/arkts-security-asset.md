# @ohos.security.asset

/*
 Copyright (c) 2024 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace asset--><!--Device-unnamed-declare namespace asset-End-->

**System capability:** SystemCapability.Security.Asset

## Modules to Import

```TypeScript
import { asset } from 'asset';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [add](arkts-assetstore-asset-add-f.md#add) | Adds an asset. This API uses a promise to return the result. To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#IS_PERSISTENT), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission. |
| [addSync](arkts-assetstore-asset-addsync-f.md#addSync) | Adds an asset. This API returns the result synchronously. To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#IS_PERSISTENT), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission. |
| [batchAdd](arkts-assetstore-asset-batchadd-f.md#batchAdd) | Adds assets in batches based on an attributes array. To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#IS_PERSISTENT), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission. Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) can be added in batches. |
| [batchRemove](arkts-assetstore-asset-batchremove-f.md#batchRemove) | Removes assets in batches based on an alias list. Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) can be removed in batches. |
| [batchUpdate](arkts-assetstore-asset-batchupdate-f.md#batchUpdate) | Updates assets in batches based on an attributes array. Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) can be updated in batches. |
| [postQuery](arkts-assetstore-asset-postquery-f.md#postQuery) | Performs postprocessing for the asset query. This API is used when user authentication is required for the access to an asset. This API must be used with [asset.preQuery](arkts-assetstore-asset-prequery-f.md#preQuery) together. This API uses a promise to return the result. |
| [postQuerySync](arkts-assetstore-asset-postquerysync-f.md#postQuerySync) | Performs postprocessing for the asset query. This API is used when user authentication is required for the access to the asset. This API must be used with [asset.preQuerySync](arkts-assetstore-asset-prequerysync-f.md#preQuerySync) together. This API returns the result synchronously. |
| [preQuery](arkts-assetstore-asset-prequery-f.md#preQuery) | Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset. After the user authentication is successful, call [asset.query](arkts-assetstore-asset-query-f.md#query) and [asset.postQuery](arkts-assetstore-asset-postquery-f.md#postQuery). This API uses a promise to return the result. |
| [preQuerySync](arkts-assetstore-asset-prequerysync-f.md#preQuerySync) | Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset. After the user authentication is successful, call [asset.querySync](arkts-assetstore-asset-querysync-f.md#querySync) and [asset.postQuerySync](arkts-assetstore-asset-postquerysync-f.md#postQuerySync). This API returns the result synchronously. |
| [query](arkts-assetstore-asset-query-f.md#query) | Queries one or more assets. If user authentication is required for the access to the asset, call [asset.preQuery](arkts-assetstore-asset-prequery-f.md#preQuery) before this API and call [asset.postQuery](arkts-assetstore-asset-postquery-f.md#postQuery) after this API. For details about the development procedure, see [Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md). This API uses a promise to return the result. If no asset is found, an exception indicating that no asset is found is thrown instead of returning an empty query result list. |
| [querySync](arkts-assetstore-asset-querysync-f.md#querySync) | Queries one or more assets. If user authentication is required for the access to the asset, call [asset.preQuerySync](arkts-assetstore-asset-prequerysync-f.md#preQuerySync) before this API and call [asset.postQuerySync](arkts-assetstore-asset-postquerysync-f.md#postQuerySync) after this API. For details about the development procedure, see [Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md). This API returns the result synchronously. If no asset is found, an exception indicating that no asset is found is thrown instead of returning an empty query result list. |
| [querySyncResult](arkts-assetstore-asset-querysyncresult-f.md#querySyncResult) | Queries the result of the sync operation. This API uses a promise to return the result. |
| [remove](arkts-assetstore-asset-remove-f.md#remove) | Removes one or more assets. This API uses a promise to return the result. |
| [removeSync](arkts-assetstore-asset-removesync-f.md#removeSync) | Removes one or more assets. This API returns the result synchronously. |
| [update](arkts-assetstore-asset-update-f.md#update) | Updates an asset. This API uses a promise to return the result. |
| [updateSync](arkts-assetstore-asset-updatesync-f.md#updateSync) | Updates an asset. This API returns the result synchronously. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [addAsUser](arkts-assetstore-asset-addasuser-f-sys.md#addAsUser) | Adds an asset in the specified user space. This API uses a promise to return the result. To set [IS_PERSISTENT](arkts-assetstore-asset-tag-e.md#IS_PERSISTENT), the application must have the ohos.permission.STORE_PERSISTENT_DATA permission. |
| [postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postQueryAsUser) | Performs postprocessing for the asset query in the specified user space. This API is used when user authentication is required for the access to an asset. This API must be used with [asset.preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser-(System-API)) together. This API uses a promise to return the result. |
| [preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser) | Performs preprocessing for the asset query in the specified user space. This API is used when user authentication is required for the access to an asset. After the user authentication is successful, call [asset.queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md#queryAsUser-(System-API)) and [asset.postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postQueryAsUser-(System-API)). This API uses a promise to return the result. |
| [queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md#queryAsUser) | Queries one or more assets in the specified user space. If user authentication is required for the access to the asset, call [asset.preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser-(System-API)) before this API and call [asset.postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postQueryAsUser-(System-API)) after this API. For details about the development procedure, see [Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md). This API uses a promise to return the result. |
| [removeAsUser](arkts-assetstore-asset-removeasuser-f-sys.md#removeAsUser) | Removes one or more assets in the specified user space. This API uses a promise to return the result. |
| [updateAsUser](arkts-assetstore-asset-updateasuser-f-sys.md#updateAsUser) | Updates an asset in the specified user space. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BatchErrInfo](arkts-assetstore-asset-batcherrinfo-i.md) | Result object containing error information with a specific index, error code, and message for a single asset. |
| [BatchResult](arkts-assetstore-asset-batchresult-i.md) | Result object containing batch operation,including [batchAdd](arkts-assetstore-asset-batchadd-f.md#batchAdd),[batchUpdate](arkts-assetstore-asset-batchupdate-f.md#batchUpdate),[batchRemove](arkts-assetstore-asset-batchremove-f.md#batchRemove). |
| [SyncResult](arkts-assetstore-asset-syncresult-i.md) | Represents the sync result of an asset. |

### Enums

| Name | Description |
| --- | --- |
| [Accessibility](arkts-assetstore-asset-accessibility-e.md) | Enumerates the types of access control based on the lock screen status. |
| [AuthType](arkts-assetstore-asset-authtype-e.md) | Enumerates the types of user authentication supported by an asset. |
| [ConflictResolution](arkts-assetstore-asset-conflictresolution-e.md) | Enumerates the policies for resolving conflicts (for example, a duplicate alias) when an asset is added. |
| [ErrorCode](arkts-assetstore-asset-errorcode-e.md) | Enumerates the error codes. |
| [OperationType](arkts-assetstore-asset-operationtype-e.md) | Enumerates the types of additional operation to perform. |
| [ReturnType](arkts-assetstore-asset-returntype-e.md) | Enumerates the type of information returned by an asset query operation. |
| [SyncType](arkts-assetstore-asset-synctype-e.md) | Enumerates the sync types supported by an asset. |
| [Tag](arkts-assetstore-asset-tag-e.md) | Enumerate the keys of asset attributes ([AssetMap](arkts-assetstore-asset-assetmap-t.md#AssetMap)), which are in key-value (KV) pairs. |
| [TagType](arkts-assetstore-asset-tagtype-e.md) | Enumerates the asset attribute types. |
| [WrapType](arkts-assetstore-asset-wraptype-e.md) | Enumerates the encrypted import/export types supported by the asset. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AuthType](arkts-assetstore-asset-authtype-e-sys.md) | Enumerates the types of user authentication supported by an asset. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Represents a set of asset attributes in the form of KV pairs. |
| [Value](arkts-assetstore-asset-value-t.md) | Represents the value of each attribute in [AssetMap](arkts-assetstore-asset-assetmap-t.md#AssetMap). |

