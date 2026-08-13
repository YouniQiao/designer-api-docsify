# postQueryAsUser（系统接口）

## postQueryAsUser

```TypeScript
function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>
```

在指定用户空间中查询的后置处理，用于需要用户认证的关键资产（与[asset.preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser（系统接口）)函数成对出现）。使用Promise异步回调。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>--><!--Device-asset-function postQueryAsUser(userId:number, handle: AssetMap): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| handle | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |

## 示例

```TypeScript
import { asset } from '@kit.AssetStoreKit';

let userId: number = 100;
let handle: asset.AssetMap = new Map();
// 此处传入的new Uint8Array(32)仅作为示例，实际应传入asset.preQueryAsUser执行成功返回的挑战值
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQueryAsUser(userId, handle).then(() => {
  console.info(`Succeeded in post-querying Asset from user space.`);
});
```
