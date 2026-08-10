# createKVManager

## createKVManager

```TypeScript
function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void
```

创建一个KVManager对象实例，用于管理数据库对象，使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore#createKVManager

<!--Device-distributedData-function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void--><!--Device-distributedData-function createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | Yes | 提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;KVManager&gt; | Yes | 回调函数。返回创建的KVManager对象实例。 |

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

创建一个KVManager对象实例，用于管理数据库对象，使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore#createKVManager

<!--Device-distributedData-function createKVManager(config: KVManagerConfig): Promise<KVManager>--><!--Device-distributedData-function createKVManager(config: KVManagerConfig): Promise<KVManager>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [KVManagerConfig](arkts-arkdata-distributedkvstore-kvmanagerconfig-i.md) | Yes | 提供KVManager实例的配置信息，包括调用方的包名和用户信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KVManager&gt; | Promise对象。返回创建的KVManager对象实例。 |

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

