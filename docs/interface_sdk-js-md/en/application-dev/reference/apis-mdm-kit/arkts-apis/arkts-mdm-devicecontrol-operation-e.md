# Operation

设备操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-deviceControl-enum Operation--><!--Device-deviceControl-enum Operation-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## DISK_ERASURE

```TypeScript
DISK_ERASURE = 0
```

磁盘擦除。接口调用后，设备将立即执行磁盘擦除操作。磁盘擦除完成后，整机设备数据将全部被擦除且无法恢复。企业需要做好应用的安全设计，防止应用被攻击导致企业数据丢失。仅支持PC/2in1设备。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-DISK_ERASURE = 0--><!--Device-Operation-DISK_ERASURE = 0-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## RESET_FACTORY

```TypeScript
RESET_FACTORY = 1
```

设备恢复出厂设置。接口调用后，设备将立即恢复出厂设置。恢复完成后，整机设备数据将全部被擦除且无法恢复。企业需要做好应用的安全设计，防止应用被攻击导致企业数据丢失。已经通过[restrictions.setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy)接口禁用了恢复出厂，需要先解除禁用。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-RESET_FACTORY = 1--><!--Device-Operation-RESET_FACTORY = 1-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## REBOOT

```TypeScript
REBOOT = 2
```

设备重启。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-REBOOT = 2--><!--Device-Operation-REBOOT = 2-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## SHUT_DOWN

```TypeScript
SHUT_DOWN = 3
```

设备关机。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-SHUT_DOWN = 3--><!--Device-Operation-SHUT_DOWN = 3-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## LOCK_SCREEN

```TypeScript
LOCK_SCREEN = 4
```

设备锁屏。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-LOCK_SCREEN = 4--><!--Device-Operation-LOCK_SCREEN = 4-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## LOCK_DEVICE

```TypeScript
LOCK_DEVICE = 5
```

设备锁定。该能力使用后设备屏幕无法使用，按键无响应，仅支持锁屏文案定制，不支持在锁屏界面定制交互功能。在开发过程中，下发设备锁定策略前一定要预留逃生通道，并且确保逃生通道正常。建议开发时保留hdc能力与远程通信能力，通过hdc命令或者远程push能力能触发设备解锁定功能。&lt;br&gt;如果需要实现在屏幕锁定的情况下支持自定义行为的能力，建议使用[applicationManager.setAllowedKioskApps](arkts-mdm-applicationmanager-setallowedkioskapps-f.md#setallowedkioskapps)接口配置支持Kiosk模式，使用[applicationManager.enterKioskMode](../../apis-ability-kit/arkts-apis/arkts-ability-kioskmanager-enterkioskmode-f.md/arkts-ability-kioskmanager-enterkioskmode-f.md#enterkioskmode))接口进入Kiosk模式。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-LOCK_DEVICE = 5--><!--Device-Operation-LOCK_DEVICE = 5-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## UNLOCK_DEVICE

```TypeScript
UNLOCK_DEVICE = 6
```

设备解锁定。接口调用后，设备将被解锁，用户可正常操作设备。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Operation-UNLOCK_DEVICE = 6--><!--Device-Operation-UNLOCK_DEVICE = 6-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

