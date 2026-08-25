# createAssetLoaderStub (System API)

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## createAssetLoaderStub

```TypeScript
function createAssetLoaderStub(instance: AssetLoader): Promise<rpc.RemoteObject>
```

Creates a RemoteObject instance based on an AssetLoader instance. The system uses this object to call the APIs of the AssetLoader instance. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instance | [AssetLoader](arkts-arkdata-cloudextension-assetloader-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;rpc.RemoteObject & gt; |
