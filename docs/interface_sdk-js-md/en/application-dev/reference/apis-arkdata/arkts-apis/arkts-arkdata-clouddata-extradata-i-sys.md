# ExtraData (System API)

Represents the transparently transmitted data, which contains information required for a data change notification.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import cloudData from '@kit.ArkData';
```

## eventId

```TypeScript
eventId: string
```

Event ID. The value **cloud_data_change** indicates cloud data changes.

**Type:** string

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## extraData

```TypeScript
extraData: string
```

Data to be transmitted transparently. **extraData** is a JSON string that must contain the **data** field. The **data** field contains information required for a change notification, including the account ID, application name, database name, database type, and database table name. All the fields cannot be empty.

**Type:** string

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Examples**

```TypeScript
// accountId: ID of the cloud account.
// bundleName: application bundle name.
// containerName: name of the cloud database.
// databaseScopes: type of the cloud database.
// recordTypes: names of the tables in the cloud database.

let extraData: cloudData.ExtraData = {
  eventId: "cloud_data_change",
  extraData: '{"data": "{"accountId": "aaa", "bundleName": "com.bbb.xxx", "containerName": "alias", "databaseScopes": ["private", "shared"], "recordTypes": ["xxx", "yyy", "zzz"]}"}',
}
```
