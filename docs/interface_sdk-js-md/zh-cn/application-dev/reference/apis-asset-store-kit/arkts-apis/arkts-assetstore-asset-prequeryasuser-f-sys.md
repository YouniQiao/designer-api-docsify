# preQueryAsUser（系统接口）

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## preQueryAsUser

```TypeScript
function preQueryAsUser(userId: number, query: AssetMap): Promise<Uint8Array>
```

在指定用户空间中查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.queryAsUser](arkts-assetstore-asset-queryasuser-f-sys.md#queryasuser)和  
[asset.postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postqueryasuser)接口。使用Promise异步回调。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function preQueryAsUser(userId: number, query: AssetMap): Promise<Uint8Array>--><!--Device-asset-function preQueryAsUser(userId: number, query: AssetMap): Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 用户ID。取值范围大于等于100。 |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 | 关键资产的查询条件，如别名、访问控制属性、自定义数据等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise对象，返回挑战值。 &lt;br&gt;**说明：** 挑战值用于后续用户认证。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000006 | Insufficient memory. |
| 201 | The caller doesn't have the permission. |
| 24000007 | The asset is corrupted. |
| 202 | Non-system applications use system APIs. |
| 24000005 | The screen lock status does not match. |
| 24000002 | The asset is not found. |
| 24000001 | The ASSET service is unavailable. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

## 示例

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let userId: number = 100;
let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
asset.preQueryAsUser(userId, query).then((challenge: Uint8Array) => {
  console.info(`Succeeded in pre-querying Asset from user space.`);
});
```

