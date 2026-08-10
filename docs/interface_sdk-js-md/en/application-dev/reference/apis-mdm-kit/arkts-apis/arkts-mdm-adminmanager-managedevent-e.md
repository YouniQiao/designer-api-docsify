# ManagedEvent

可订阅的系统管理事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-adminManager-export enum ManagedEvent--><!--Device-adminManager-export enum ManagedEvent-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_BUNDLE_ADDED

```TypeScript
MANAGED_EVENT_BUNDLE_ADDED = 0
```

应用安装事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_ADDED = 0--><!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_ADDED = 0-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_BUNDLE_REMOVED

```TypeScript
MANAGED_EVENT_BUNDLE_REMOVED = 1
```

应用卸载事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_REMOVED = 1--><!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_REMOVED = 1-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_APP_START

```TypeScript
MANAGED_EVENT_APP_START = 2
```

应用启动事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ManagedEvent-MANAGED_EVENT_APP_START = 2--><!--Device-ManagedEvent-MANAGED_EVENT_APP_START = 2-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_APP_STOP

```TypeScript
MANAGED_EVENT_APP_STOP = 3
```

应用停止事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ManagedEvent-MANAGED_EVENT_APP_STOP = 3--><!--Device-ManagedEvent-MANAGED_EVENT_APP_STOP = 3-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_SYSTEM_UPDATE

```TypeScript
MANAGED_EVENT_SYSTEM_UPDATE = 4
```

系统更新事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ManagedEvent-MANAGED_EVENT_SYSTEM_UPDATE = 4--><!--Device-ManagedEvent-MANAGED_EVENT_SYSTEM_UPDATE = 4-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_ACCOUNT_ADDED

```TypeScript
MANAGED_EVENT_ACCOUNT_ADDED = 5
```

账号新增事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_ADDED = 5--><!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_ADDED = 5-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_ACCOUNT_SWITCHED

```TypeScript
MANAGED_EVENT_ACCOUNT_SWITCHED = 6
```

账号切换事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_SWITCHED = 6--><!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_SWITCHED = 6-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_ACCOUNT_REMOVED

```TypeScript
MANAGED_EVENT_ACCOUNT_REMOVED = 7
```

账号删除事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_REMOVED = 7--><!--Device-ManagedEvent-MANAGED_EVENT_ACCOUNT_REMOVED = 7-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_STARTUP_GUIDE_COMPLETED

```TypeScript
MANAGED_EVENT_STARTUP_GUIDE_COMPLETED = 8
```

开机向导完成事件。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ManagedEvent-MANAGED_EVENT_STARTUP_GUIDE_COMPLETED = 8--><!--Device-ManagedEvent-MANAGED_EVENT_STARTUP_GUIDE_COMPLETED = 8-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_BOOT_COMPLETED

```TypeScript
MANAGED_EVENT_BOOT_COMPLETED = 9
```

设备启动完成事件。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ManagedEvent-MANAGED_EVENT_BOOT_COMPLETED = 9--><!--Device-ManagedEvent-MANAGED_EVENT_BOOT_COMPLETED = 9-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_BUNDLE_UPDATED

```TypeScript
MANAGED_EVENT_BUNDLE_UPDATED = 10
```

应用更新事件。

**起始版本**：26.0.0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_UPDATED = 10--><!--Device-ManagedEvent-MANAGED_EVENT_BUNDLE_UPDATED = 10-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## MANAGED_EVENT_POLICIES_CHANGED

```TypeScript
MANAGED_EVENT_POLICIES_CHANGED = 11
```

策略变更事件。仅支持超级设备管理应用订阅该事件，其他类型设备管理应用订阅该事件时返回9200002错误码。

**起始版本**：26.0.0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ManagedEvent-MANAGED_EVENT_POLICIES_CHANGED = 11--><!--Device-ManagedEvent-MANAGED_EVENT_POLICIES_CHANGED = 11-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

