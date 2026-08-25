# getInstalledBundleStorageStats

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## getInstalledBundleStorageStats

```TypeScript
function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>
```

Obtains the storage usage of installed applications of a specified user on a device. This API uses a promise to return the result.

> **NOTE：**&gt;
> 1. Only the storage usage of installed applications can be obtained.&gt;
> 2. If **bundleNames** is empty or all bundle names passed are of uninstalled applications, error code 9200012
> will be returned.&gt;
> 3. If some of the applications specified in the **bundleNames** parameter are installed and some are not, the API
> returns normally. For installed applications, their actual storage usage information is returned. For uninstalled
> applications, **0** is returned as their storage usage.&gt;
> 4. This API supports cross-user queries. For example, user 100 can query the storage usage of some applications
> of user 101.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_GET_ALL_BUNDLE_INFO

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleNames | Array & lt;string & gt; | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BundleStorageStats](arkts-mdm-bundlemanager-bundlestoragestats-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
