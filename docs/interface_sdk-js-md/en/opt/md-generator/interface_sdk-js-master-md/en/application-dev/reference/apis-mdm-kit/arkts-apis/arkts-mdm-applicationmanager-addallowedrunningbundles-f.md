# addAllowedRunningBundles

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## addAllowedRunningBundles

```TypeScript
function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void
```

Adds applications to the application running trustlist. Only applications in the trustlist are allowed to run under the specified user. > **NOTE：**> > 1. Most APIs provided by MDM Kit are available only to MDM applications. When using this API, add the MDM > application to the application running trustlist. Otherwise, the MDM application will be prohibited from running, > blocking the API call. For details about whether the API is open only to MDM applications, see the module > description. > > 2. If the application running blocklist is not empty, this API cannot be used to add applications to the running > trustlist. Otherwise, the error code 9200010 is reported. APIs related to the application running blocklist > include [addDisallowedRunningBundlesSync](arkts-mdm-applicationmanager-adddisallowedrunningbundlessync-f.md#addDisallowedRunningBundlesSync), > [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)), > [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)), and > [addDisallowedRunningBundles](arkts-mdm-applicationmanager-adddisallowedrunningbundles-f-sys.md#addDisallowedRunningBundles-(System-API)). > > 3. This API only takes effect for third-party applications. System applications are not subject to this list and > are allowed to run by default.

**Since:** 21

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void--><!--Device-applicationManager-function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| appIdentifiers | Array & lt;string & gt; | Yes |
| accountId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace it as required.
let appIdentifiers: Array<string> = ['0123456789123456789'];

try {
  applicationManager.addAllowedRunningBundles(wantTemp, appIdentifiers, 100);
  console.info('Succeeded in adding allowed running bundles.');
} catch (err) {
  console.error(`Failed to add allowed running bundles. Code is ${err.code}, message is ${err.message}`);
}
```
