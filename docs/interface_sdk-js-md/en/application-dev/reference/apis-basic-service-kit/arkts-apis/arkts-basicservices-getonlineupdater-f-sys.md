# getOnlineUpdater (System API)

## Modules to Import

```TypeScript
import { update } from '@kit.BasicServicesKit';
```

## getOnlineUpdater

```TypeScript
function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater
```

Obtains an **OnlineUpdater** object.

**Since:** 9

<!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater--><!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| upgradeInfo | [UpgradeInfo](arkts-basicservices-upgradeinfo-i-sys.md) | Yes | **OnlineUpdater** object information. |

**Return value:**

| Type | Description |
| --- | --- |
| [Updater](arkts-basicservices-updater-i-sys.md) | **OnlineUpdater** object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

**Example**

```TypeScript
try {
  const upgradeInfo: update.UpgradeInfo = {
    upgradeApp: "com.ohos.ota.updateclient",
    businessType: {
      vendor: update.BusinessVendor.PUBLIC,
      subType: update.BusinessSubType.FIRMWARE
    }
  };
  let updater = update.getOnlineUpdater(upgradeInfo);
} catch(error) {
  console.error(`Fail to get updater error: ${error}`);
}

```

