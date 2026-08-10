# Accessibility

枚举，关键资产基于锁屏状态的访问控制类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-asset-enum Accessibility--><!--Device-asset-enum Accessibility-End-->

**System capability:** SystemCapability.Security.Asset

## DEVICE_POWERED_ON

```TypeScript
DEVICE_POWERED_ON = 0
```

开机后可访问。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Accessibility-DEVICE_POWERED_ON = 0--><!--Device-Accessibility-DEVICE_POWERED_ON = 0-End-->

**System capability:** SystemCapability.Security.Asset

## DEVICE_FIRST_UNLOCKED

```TypeScript
DEVICE_FIRST_UNLOCKED = 1
```

首次解锁后可访问

**说明：** 未设置锁屏密码时，等同于开机后可访问。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Accessibility-DEVICE_FIRST_UNLOCKED = 1--><!--Device-Accessibility-DEVICE_FIRST_UNLOCKED = 1-End-->

**System capability:** SystemCapability.Security.Asset

## DEVICE_UNLOCKED

```TypeScript
DEVICE_UNLOCKED = 2
```

解锁状态时可访问

**说明：** 未设置锁屏密码时，等同于开机后可访问。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Accessibility-DEVICE_UNLOCKED = 2--><!--Device-Accessibility-DEVICE_UNLOCKED = 2-End-->

**System capability:** SystemCapability.Security.Asset

