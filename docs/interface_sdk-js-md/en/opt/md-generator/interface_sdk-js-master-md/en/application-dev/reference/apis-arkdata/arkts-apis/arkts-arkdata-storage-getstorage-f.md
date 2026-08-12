# getStorage

## getStorage

```TypeScript
function getStorage(path: string, callback: AsyncCallback<Storage>): void
```

Reads the specified file and loads its data to the **Storage** instance for data operations. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getPreferences](ohos.preferences.preferences.getPreferences)

<!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void--><!--Device-storage-function getStorage(path: string, callback: AsyncCallback<Storage>): void-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Storage&gt; | Yes |


## getStorage

```TypeScript
function getStorage(path: string): Promise<Storage>
```

Reads the specified file and loads its data to the **Storage** instance for data operations. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [getPreferences](ohos.preferences.preferences.getPreferences)

<!--Device-storage-function getStorage(path: string): Promise<Storage>--><!--Device-storage-function getStorage(path: string): Promise<Storage>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Storage & gt; |
