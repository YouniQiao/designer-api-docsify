# add

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## add

```TypeScript
function add(attributes: AssetMap): Promise<void>
```

新增一条关键资产。使用Promise异步回调。设置[Tag.IS_PERSISTENT](arkts-assetstore-asset-tagtype-e.md)属性时，需要申请ohos.permission.STORE_PERSISTENT_DATA权限，申请方式请参考 [声明权限](../../../security/AccessToken/declare-permissions.md)。

**起始版本：** 11

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attributes | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000003](../errorcode-asset.md#24000003-关键资产已存在) |
| [24000005](../errorcode-asset.md#24000005-锁屏状态不匹配) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000009](../errorcode-asset.md#24000009-算法库操作失败) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000014](../errorcode-asset.md#24000014-文件操作失败) |
| [24000015](../errorcode-asset.md#24000015-获取系统时间失败) |
