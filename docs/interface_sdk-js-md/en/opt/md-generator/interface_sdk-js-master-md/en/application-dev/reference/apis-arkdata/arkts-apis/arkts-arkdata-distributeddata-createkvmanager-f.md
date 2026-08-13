# createKVManager

## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void
```

Creates a **KVManager** instance to manage KV stores. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** createKVManager

<!--Device-distributedData-function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void--><!--Device-distributedData-function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;KVManager&gt; | Yes |

## Examples

```TypeScript
let kvManager;
try {
    const kvManagerConfig = {
        bundleName : 'com.example.datamanagertest',
        userInfo : {
            userId : '0',
            userType : distributedData.UserType.SAME_USER_ID
        }
    }
    distributedData.createKVManager(kvManagerConfig, function (err, manager) {
        if (err) {
            console.log("Failed to create KVManager: "  + JSON.stringify(err));
            return;
        }
        console.log("Succeeded in creating KVManager");
        kvManager = manager;
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```


## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig): Promise<KVManager>
```

Creates a **KVManager** instance to manage KV stores. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** createKVManager

<!--Device-distributedData-function createKVManager(config: KVManagerConfig): Promise<KVManager>--><!--Device-distributedData-function createKVManager(config: KVManagerConfig): Promise<KVManager>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;KVManager & gt; |

## Examples

```TypeScript
try {
  const kvManagerConfig = {
    bundleName: 'com.example.datamanagertest',
    userInfo: {
      userId: '0',
      userType: distributedData.UserType.SAME_USER_ID
    }
  }
  distributedData.createKVManager(kvManagerConfig).then((manager) => {
    console.log("Succeeded in creating KVManager");
    kvManager = manager;
  }).catch((err) => {
    console.error("Failed to create KVManager: " + JSON.stringify(err));
  });
} catch (e) {
  console.log("An unexpected error occurred. Error:" + e);
}
```
