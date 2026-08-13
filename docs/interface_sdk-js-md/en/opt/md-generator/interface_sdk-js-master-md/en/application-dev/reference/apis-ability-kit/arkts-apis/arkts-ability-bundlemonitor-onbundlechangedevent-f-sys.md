# on_BundleChangedEvent (System API)

## Modules to Import

```TypeScript
import { bundleMonitor } from '@kit.AbilityKit';
```

## on_BundleChangedEvent

```TypeScript
function on(type: BundleChangedEvent, callback: Callback<BundleChangedInfo>): void
```

Register to monitor the installation status

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.LISTEN_BUNDLE_CHANGE

<!--Device-bundleMonitor-function on(type: BundleChangedEvent, callback: Callback<BundleChangedInfo>): void--><!--Device-bundleMonitor-function on(type: BundleChangedEvent, callback: Callback<BundleChangedInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BundleChangedEvent](arkts-ability-bundlemonitor-bundlechangedevent-t-sys.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BundleChangedInfo](arkts-ability-bundlemonitor-bundlechangedinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleMonitor } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackFun = (bundleChangeInfo: bundleMonitor.BundleChangedInfo) => {
  console.info(`bundleName : ${bundleChangeInfo.bundleName} userId : ${bundleChangeInfo.userId}`);
};
try {
  bundleMonitor.on('add', callbackFun);
} catch (errData) {
  let message = (errData as BusinessError).message;
  let errCode = (errData as BusinessError).code;
  console.error(`errData is errCode:${errCode}  message:${message}`);
}
```
