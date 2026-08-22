# SystemDefinedAppItem

Represents the data of the home screen icon defined by the system. It is a child class of [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md).

**Inheritance/Implementation:** SystemDefinedAppItem extends [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unifiedDataChannel-class SystemDefinedAppItem--><!--Device-unifiedDataChannel-class SystemDefinedAppItem-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**Examples**

```TypeScript
let appItem = new unifiedDataChannel.SystemDefinedAppItem();
appItem.appId = 'MyAppId';
appItem.appName = 'MyAppName';
appItem.appIconId = 'MyAppIconId';
appItem.appLabelId = 'MyAppLabelId';
appItem.bundleName = 'MyBundleName';
appItem.abilityName = 'MyAbilityName';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
appItem.details = {
    appItemKey1: 123,
    appItemKey2: 'appItemValue',
    appItemKey3: u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(appItem);
```

