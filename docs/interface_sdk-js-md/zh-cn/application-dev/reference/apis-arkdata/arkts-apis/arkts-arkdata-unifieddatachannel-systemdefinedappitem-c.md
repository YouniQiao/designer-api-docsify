# SystemDefinedAppItem

系统定义的桌面图标类型数据，是[SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)的子类。

**继承/实现关系：** SystemDefinedAppItem extends [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unifiedDataChannel-class SystemDefinedAppItem--><!--Device-unifiedDataChannel-class SystemDefinedAppItem-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

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
  "appItemKey1": 123,
  "appItemKey2": 'appItemValue',
  "appItemKey3": u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(appItem);
```

