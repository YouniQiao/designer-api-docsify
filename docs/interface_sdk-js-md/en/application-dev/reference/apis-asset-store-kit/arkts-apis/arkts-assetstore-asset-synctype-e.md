# SyncType

枚举，关键资产支持的同步类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-asset-enum SyncType--><!--Device-asset-enum SyncType-End-->

**System capability:** SystemCapability.Security.Asset

## NEVER

```TypeScript
NEVER = 0
```

不允许同步关键资产。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SyncType-NEVER = 0--><!--Device-SyncType-NEVER = 0-End-->

**System capability:** SystemCapability.Security.Asset

## THIS_DEVICE

```TypeScript
THIS_DEVICE = 1 << 0
```

只在本设备进行同步，如仅在本设备还原的备份场景。

**说明：** 本字段是能力预埋，当前不支持。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SyncType-THIS_DEVICE = 1 << 0--><!--Device-SyncType-THIS_DEVICE = 1 << 0-End-->

**System capability:** SystemCapability.Security.Asset

## TRUSTED_DEVICE

```TypeScript
TRUSTED_DEVICE = 1 << 1
```

只在可信设备间进行同步，如克隆场景。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SyncType-TRUSTED_DEVICE = 1 << 1--><!--Device-SyncType-TRUSTED_DEVICE = 1 << 1-End-->

**System capability:** SystemCapability.Security.Asset

## TRUSTED_ACCOUNT

```TypeScript
TRUSTED_ACCOUNT = 1 << 2
```

只在登录可信账号的设备间进行同步，如云同步场景。

**说明：** 本字段是能力预埋，当前不支持。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-SyncType-TRUSTED_ACCOUNT = 1 << 2--><!--Device-SyncType-TRUSTED_ACCOUNT = 1 << 2-End-->

**System capability:** SystemCapability.Security.Asset

