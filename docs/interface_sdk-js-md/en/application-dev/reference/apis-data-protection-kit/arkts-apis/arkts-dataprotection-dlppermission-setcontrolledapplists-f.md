# setControlledAppLists

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setControlledAppLists

```TypeScript
function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>
```

设置受企业DLP控制的应用程序列表。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.DLP_POLICY_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-dlpPermission-function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>--><!--Device-dlpPermission-function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appLists | Array&lt;string&gt; | Yes | 被管控的应用的appIdentifier列表。 &lt;br&gt;数组最大长度为100，超过最大长度返回19100001错误码。 &lt;br&gt;数组中每个元素为应用的appIdentifier，获取方法参见获取应用的appIdentifier，单个appIdentifier最 大长度为4096字节，超过最大长度返回19100001错误码。 |
| userId | number | No | 为其配置受控应用列表的用户ID。 &lt;br&gt;若参数未指定，则默认使用当前用户。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 19100001 | Invalid parameter value. |
| 19100023 | The specified userId is inconsistent with the current userId. |
| 19100011 | The system ability works abnormally. |
| 201 | Permission denied. |
| 19100024 | The specified userId belongs to a personal space user and cannot be managed. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let appList: Array<string> = ["appId1", "appId2"];
let userId: number = 100;
dlpPermission.setControlledAppLists(appList, userId).then(() => {
  console.info("Successfully set controlled appLists.");
}).catch((error: BusinessError) => {
  console.error(error.message);
}).finally(() => {
  console.info("Completed set controlled appLists operation.");
});
```

