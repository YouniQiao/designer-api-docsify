# getOnlineUpdater (System API)

## Modules to Import

```TypeScript
```

## getOnlineUpdater

```TypeScript
function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater
```

Obtains an **OnlineUpdater** object, which can be used to check for new versions online, download update packages, and install update packages. This API can be used in scenarios such as OTA upgrade (for details, see Upgrading Service Terms) of client applications and online system upgrade. This API can help users obtain system updates in a timely manner, improving upgrade efficiency and user experience. **Overview** This API obtains an **OnlineUpdater** object through the system service interface. The object provides core functions such as checking for new versions, downloading update packages, and installing update packages. **Constraints** - The upgrade package management server deployed by the vendor is required for checking for new versions and downloading update packages.

**Since:** 23

<!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater--><!--Device-update-function getOnlineUpdater(upgradeInfo: UpgradeInfo): Updater-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| upgradeInfo | [UpgradeInfo](arkts-basicservices-update-upgradeinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Updater](arkts-basicservices-update-updater-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
// Define an UpgradeInfo object.
  const upgradeInfo: update.UpgradeInfo = {
    upgradeApp: 'com.ohos.ota.updateclient',  // App package name
    businessType: {
      vendor: update.BusinessVendor.PUBLIC, // Vendor type
      subType: update.BusinessSubType.FIRMWARE // The update type is firmware.
    }
  };  
  // Obtain an OnlineUpdater object.
  let onlineUpdater = update.getOnlineUpdater(upgradeInfo);
```
