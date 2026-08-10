# addAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## addAsUser

```TypeScript
function addAsUser(userId: number, attributes: AssetMap): Promise<void>
```

在指定用户空间中新增一条关键资产。使用Promise异步回调。

设置[Tag.IS_PERSISTENT](arkts-assetstore-asset-tagtype-e.md)属性，需申请ohos.permission.STORE_PERSISTENT_DATA权限，申请方式请参考[声明权限](../../../security/AccessToken/declare-permissions.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function addAsUser(userId: number, attributes: AssetMap): Promise<void>--><!--Device-asset-function addAsUser(userId: number, attributes: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。取值范围大于等于100。 |
| attributes | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | 待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 24000014 | The file operation failed. |
| 24000015 | Getting the system time failed. |
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
| 24000003 | The asset already exists. |
| 24000001 | The ASSET service is unavailable. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let userId: number = 100;
let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
asset.addAsUser(userId, attr).then(() => {
  console.info(`Succeeded in adding Asset to user space.`);
});
```

