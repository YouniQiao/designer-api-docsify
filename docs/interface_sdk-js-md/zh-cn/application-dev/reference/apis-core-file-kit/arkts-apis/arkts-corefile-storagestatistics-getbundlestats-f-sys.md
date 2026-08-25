# getBundleStats（系统接口）

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getBundleStats

```TypeScript
function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: number): void
```

异步获取应用存储数据的空间大小（单位为Byte），以callback方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| packageName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md)&gt; | 是 |
| index | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600008 |
| 13900042 |


## getBundleStats

```TypeScript
function getBundleStats(packageName: string, index?: number): Promise<BundleStats>
```

异步获取应用存储数据的空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 9

**需要权限：** ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| packageName | string | 是 |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13600008 |
| 13900042 |
