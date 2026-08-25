# AssetLoader（系统接口）

提供资产上传下载接口的类。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## download

```TypeScript
download(table: string, gid: string, prefix: string, assets: Array<CloudAsset>): Promise<Array<Result<CloudAsset>>>
```

通过该接口实现资产的下载。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| gid | string | 是 |
| prefix | string | 是 |
| assets | Array&lt;[CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Result&lt;[CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md)&gt;&gt;&gt; |

## upload

```TypeScript
upload(table: string, gid: string, assets: Array<CloudAsset>): Promise<Array<Result<CloudAsset>>>
```

通过该接口实现资产的上传。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| gid | string | 是 |
| assets | Array&lt;[CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Result&lt;[CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md)&gt;&gt;&gt; |
