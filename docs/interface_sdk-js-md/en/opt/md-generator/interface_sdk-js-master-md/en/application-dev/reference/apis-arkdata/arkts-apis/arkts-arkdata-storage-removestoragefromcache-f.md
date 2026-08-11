# removeStorageFromCache

## removeStorageFromCache

```TypeScript
function removeStorageFromCache(path: string, callback: AsyncCallback<void>): void
```

Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data operations. Otherwise, data inconsistency will occur. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.removePreferencesFromCache

<!--Device-storage-function removeStorageFromCache(path: string, callback: AsyncCallback<void>): void--><!--Device-storage-function removeStorageFromCache(path: string, callback: AsyncCallback<void>): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## removeStorageFromCache

```TypeScript
function removeStorageFromCache(path: string): Promise<void>
```

Removes the singleton **Storage** instance of a file from the cache. The removed instance cannot be used for data operations. Otherwise, data inconsistency will occur. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ohos.preferences.preferences.removePreferencesFromCache

<!--Device-storage-function removeStorageFromCache(path: string): Promise<void>--><!--Device-storage-function removeStorageFromCache(path: string): Promise<void>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
